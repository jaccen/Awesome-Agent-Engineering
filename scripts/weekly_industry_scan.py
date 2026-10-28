#!/usr/bin/env python3
"""Weekly industry trend scan for Agent ecosystem.

Scans GitHub trending (LLM/agent repos), HuggingFace trending models, and
generates a weekly trend report. Candidates need review before admission.

Exit 0: complete, no new candidates; 10: candidates found.
"""
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ── GitHub: search trending agent repos via Search API ──────────────────────
GH_API = 'https://api.github.com/search/repositories'


def gh_search(query, sort='stars', per_page=30, fetcher=None):
    fetcher = fetcher or urllib.request.urlopen
    params = {'q': query, 'sort': sort, 'order': 'desc', 'per_page': str(per_page)}
    url = GH_API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'Awesome-Agent-Engineering-scan/1.0',
    })
    with fetcher(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return data.get('items', [])


def scan_github_agent_repos(since_days=7, fetcher=None):
    """Find recently-starred agent-related repos."""
    since = (datetime.now(timezone.utc) - timedelta(days=since_days)).strftime('%Y-%m-%d')
    queries = [
        f'agent LLM pushed:>{since} stars:>50',
        f'multi-agent framework pushed:>{since} stars:>100',
        f'coding agent pushed:>{since} stars:>50',
        f'web agent browser pushed:>{since} stars:>50',
        f'rag agent pushed:>{since} stars:>50',
        f'agent benchmark pushed:>{since} stars:>30',
        f'mcp server pushed:>{since} stars:>30',
    ]
    all_repos = {}
    for q in queries:
        try:
            items = gh_search(q, fetcher=fetcher)
            for item in items:
                all_repos[item['full_name']] = {
                    'name': item['full_name'],
                    'url': item['html_url'],
                    'stars': item['stargazers_count'],
                    'description': (item['description'] or '')[:200],
                    'language': item.get('language') or '',
                    'pushed_at': item['pushed_at'][:10],
                    'topics': item.get('topics', [])[:8],
                }
        except Exception as exc:
            print(f'  [WARN] GitHub query failed: {q[:50]}... — {exc}')
        time.sleep(2)  # GitHub rate limit: 10 req/min for search
    return sorted(all_repos.values(), key=lambda r: r['stars'], reverse=True)


# ── HuggingFace: trending models via API ────────────────────────────────────
HF_API = 'https://huggingface.co/api/models'


def scan_hf_trending(fetcher=None):
    fetcher = fetcher or urllib.request.urlopen
    params = {'sort': 'likes7d', 'direction': '-1', 'limit': '30',
              'filter': 'agent,tool-use,function-calling,vla,rag,reasoning'}
    url = HF_API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': 'Awesome-Agent-Engineering-scan/1.0'})
    try:
        with fetcher(req, timeout=30) as resp:
            models = json.loads(resp.read())
        out = []
        for m in models:
            out.append({
                'model_id': m.get('id', ''),
                'url': f"https://huggingface.co/{m.get('id', '')}",
                'likes': m.get('likes', 0),
                'downloads': m.get('downloads', 0),
                'tags': [t for t in m.get('tags', []) if not t.startswith('_')][:8],
            })
        return out
    except Exception as exc:
        print(f'  [WARN] HuggingFace scan failed: {exc}')
        return []


def main():
    report_date = datetime.now(timezone.utc).date().isoformat()
    output_dir = ROOT / 'reports/weekly-trending'
    output_dir.mkdir(parents=True, exist_ok=True)

    print('[1/2] Scanning GitHub trending agent repos...')
    gh_repos = scan_github_agent_repos(since_days=7)
    print(f'  Found {len(gh_repos)} trending repos')

    print('[2/2] Scanning HuggingFace trending models...')
    hf_models = scan_hf_trending()
    print(f'  Found {len(hf_models)} trending models')

    report = {
        'date': report_date,
        'retrieved_at': datetime.now(timezone.utc).isoformat(),
        'github_repos_count': len(gh_repos),
        'hf_models_count': len(hf_models),
        'github_repos': gh_repos[:50],
        'hf_models': hf_models[:30],
        'note': 'Weekly trend candidates for frameworks and startups KBs. Review before admission.',
    }

    # Write JSON
    (output_dir / 'latest.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    # Write Markdown report
    lines = [
        f"# Weekly Industry Trend Report — {report_date}", '',
        f'**GitHub trending repos:** {len(gh_repos)} | **HuggingFace trending models:** {len(hf_models)}',
        '',
        'Candidates need review before admission to frameworks.json / startups.json.', '',
        '## GitHub Trending Agent Repos (Top 50 by stars)', '',
        '| Repo | Stars | Description | Language |',
        '|------|-------|-------------|----------|',
    ]
    for r in gh_repos[:50]:
        desc = r['description'].replace('|', '\\|')[:80]
        lines.append(f"| [{r['name']}]({r['url']}) | {r['stars']} | {desc} | {r['language']} |")
    lines += ['', '## HuggingFace Trending Models (Top 30 by weekly likes)', '',
              '| Model | Likes | Downloads | Tags |',
              '|-------|-------|-----------|------|']
    for m in hf_models[:30]:
        tags = ', '.join(m['tags'][:4])
        lines.append(f"| [{m['model_id']}]({m['url']}) | {m['likes']} | {m['downloads']} | {tags} |")
    lines.append('')

    (output_dir / (report_date + '.md')).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'\n[COMPLETE] Report saved to {output_dir}/{report_date}.md')
    has_candidates = len(gh_repos) > 0 or len(hf_models) > 0
    return 10 if has_candidates else 0


if __name__ == '__main__':
    raise SystemExit(main())
