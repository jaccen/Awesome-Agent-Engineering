#!/usr/bin/env python3
"""Daily arXiv Agent-paper discovery. Candidates need review before admission.

Exit 0: complete, no new candidates; 10: complete, candidates found;
2: incomplete/unavailable (never silently report a successful empty search).
"""
import argparse
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NS = {'a': 'http://www.w3.org/2005/Atom', 'o': 'http://a9.com/-/spec/opensearch/1.1/'}
API = 'https://export.arxiv.org/api/query?'


def fetch(url, retries=2):
    last_error = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'Awesome-Agent-Engineering-scan/1.0'})
            with urllib.request.urlopen(request, timeout=30) as response:
                feed = ET.fromstring(response.read())
            if feed.tag != '{http://www.w3.org/2005/Atom}feed':
                raise ValueError('Not an Atom feed')
            return feed
        except (OSError, ET.ParseError, ValueError) as exc:
            last_error = exc
            if attempt + 1 < retries:
                time.sleep(4)
    raise OSError(f'{type(last_error).__name__}: {last_error}')


def parse_entries(feed):
    out = []
    for entry in feed.findall('a:entry', NS):
        aid = re.sub(r'v\d+$', '', entry.findtext('a:id', '', NS).rsplit('/abs/', 1)[-1])
        if not re.fullmatch(r'\d{4}\.\d{4,5}', aid):
            raise ValueError('arXiv returned an error or unrecognized identifier')
        authors = [a.findtext('a:name', '', NS) for a in entry.findall('a:author', NS)]
        out.append({
            'id': aid,
            'title': ' '.join(entry.findtext('a:title', '', NS).split()),
            'abstract': ' '.join(entry.findtext('a:summary', '', NS).split()),
            'published': entry.findtext('a:published', '', NS)[:10],
            'authors': authors[:8],
            'categories': [item.get('term', '') for item in entry.findall('a:category', NS)],
        })
    for row in out:
        row['primary'] = row['categories'][0] if row['categories'] else ''
    return out


# Agent-relevant keyword families for filtering (paper must match at least one)
AGENT_KEYWORDS = [
    'agent', 'agents', 'agentic', 'autonomous agent', 'multi-agent', 'multiagent',
    'tool use', 'tool-use', 'tool learning', 'function calling', 'tool calling',
    'llm agent', 'llm-based agent', 'language agent', 'planning agent',
    'web agent', 'gui agent', 'computer use', 'computer-use',
    'code agent', 'software agent', 'swe-bench', 'coding agent',
    'embodied agent', 'robot agent', 'vla', 'vision-language-action',
    'world model', 'agent benchmark', 'agent framework', 'agent eval',
    'rag agent', 'retrieval-augmented agent', 'memory agent',
    'agent safety', 'agent alignment', 'agent monitor',
    'mcp', 'model context protocol', 'a2a protocol',
    'react', 'reflexion', 'autogpt', 'metagpt', 'autogen',
]


def is_agent_paper(row):
    text = (row['title'] + ' ' + row['abstract']).casefold()
    return any(kw in text for kw in AGENT_KEYWORDS)


# Query families — precise phrases, valid arXiv boolean grouping.
# arXiv AND binds tighter than OR, so OR groups must be fully parenthesized.
def build_queries(since, until):
    return [
        # Tool use (proven to work)
        f'all:"tool use" AND (all:llm OR all:agent) AND submittedDate:[{since} TO {until}]',
        # Web/GUI agents
        f'(ti:"web agent" OR ti:"gui agent") AND submittedDate:[{since} TO {until}]',
        # Code agents
        f'(ti:"coding agent" OR ti:"code agent" OR ti:"software agent") AND submittedDate:[{since} TO {until}]',
        # Multi-agent + LLM
        f'all:"multi-agent" AND (all:llm OR all:"language model") AND submittedDate:[{since} TO {until}]',
        # VLA / embodied agent
        f'(all:"vision-language-action" OR all:"embodied agent") AND submittedDate:[{since} TO {until}]',
        # World models for agents
        f'all:"world model" AND (all:agent OR all:embodied) AND submittedDate:[{since} TO {until}]',
        # Agent benchmarks/safety
        f'(ti:"agent benchmark" OR ti:"agent safety") AND submittedDate:[{since} TO {until}]',
        # RAG agents
        f'(all:"rag agent" OR all:"retrieval-augmented agent") AND submittedDate:[{since} TO {until}]',
    ]


def scan(queries, known, fetcher=fetch, delay=2.5, max_pages=5):
    found, query_results = {}, []
    for query in queries:
        query_result = {'query': query, 'status': 'complete', 'pages': 0, 'fetched': 0}
        try:
            for page in range(max_pages):
                params = {'search_query': query, 'sortBy': 'submittedDate', 'sortOrder': 'descending',
                          'start': page * 100, 'max_results': 100}
                feed = fetcher(API + urllib.parse.urlencode(params))
                entries = parse_entries(feed)
                total_text = feed.findtext('o:totalResults', None, NS)
                if total_text is None or not total_text.isdigit():
                    raise ValueError('Missing/invalid totalResults; completeness cannot be established')
                total = int(total_text)
                query_result['pages'] += 1
                query_result['fetched'] += len(entries)
                for row in entries:
                    if is_agent_paper(row) and row['id'] not in known:
                        if row['id'] not in found:
                            found[row['id']] = row
                if query_result['fetched'] >= total:
                    break
                if not entries:
                    raise ValueError('Empty page before totalResults reached')
                if page + 1 == max_pages:
                    raise ValueError('Pagination cap reached; search incomplete')
                time.sleep(delay)
        except (OSError, ValueError, ET.ParseError) as exc:
            query_result.update(status='failed', error=str(exc))
        query_results.append(query_result)
        time.sleep(delay)
    return sorted(found.values(), key=lambda row: (row['published'], row['id']), reverse=True), query_results


def categorize_candidate(row):
    """Lightly categorize a candidate for the report."""
    text = (row['title'] + ' ' + row['abstract']).casefold()
    cats = []
    checks = [
        ('Multi-Agent', 'multi-agent'), ('Tool Use', 'tool use'), ('Web/GUI', 'web agent'),
        ('Code', 'code agent'), ('Embodied', 'embodied'), ('World Model', 'world model'),
        ('RAG', 'rag'), ('Planning', 'planning'), ('Memory', 'memory'),
        ('Safety', 'safety'), ('Benchmark', 'benchmark'), ('Framework', 'framework'),
    ]
    for label, kw in checks:
        if kw in text:
            cats.append(label)
    return cats or ['General']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('days', nargs='?', type=int, default=3)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'reports/arxiv-daily')
    args = parser.parse_args()
    if args.days < 1 or args.days > 365:
        parser.error('days must be between 1 and 365')
    now = datetime.now(timezone.utc)
    since = (now - timedelta(days=args.days)).strftime('%Y%m%d%H%M')
    until = now.strftime('%Y%m%d%H%M')
    queries = build_queries(since, until)
    data = json.loads((ROOT / 'data/methods.json').read_text(encoding='utf-8'))
    known = {re.sub(r'v\d+$', '', row['arxiv_id']) for row in data['methods'] if row.get('arxiv_id')}
    papers, searches = scan(queries, known)
    complete = all(item['status'] == 'complete' for item in searches)
    for p in papers:
        p['suggested_categories'] = categorize_candidate(p)
    report = {
        'date': now.date().isoformat(), 'retrieved_at': now.isoformat(),
        'status': 'complete' if complete else 'incomplete', 'window_days': args.days,
        'known_arxiv_ids': len(known), 'count': len(papers),
        'queries_run': len(queries), 'queries': searches, 'papers': papers,
        'note': 'Discovery candidates, not admitted or fully verified methods.',
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if not complete:
        destination = args.output_dir / (now.strftime('attempt-%Y%m%dT%H%M%SZ') + '.json')
        destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print('[INCONCLUSIVE] Search incomplete; previous latest.json preserved. Details:', destination)
        return 2
    (args.output_dir / 'latest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        f"# arXiv Agent-paper discovery — {report['date']}", '',
        f'UTC window: {since} to {until}; {len(queries)} queries, complete pagination.',
        f'{len(papers)} candidates after deduplication against {len(known)} known arXiv IDs.', '',
        'Candidates need primary-source and scope review before admission.', '',
    ]
    for row in papers:
        cats = ', '.join(row['suggested_categories'])
        lines.append(f"- [{row['title']}](https://arxiv.org/abs/{row['id']}) — {row['published']} ({cats})")
    (args.output_dir / (report['date'] + '.md')).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'[COMPLETE] {len(papers)} discovery candidates from {len(queries)} queries')
    return 10 if papers else 0


if __name__ == '__main__':
    raise SystemExit(main())
