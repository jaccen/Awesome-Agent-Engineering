"""Revalidate all historical arXiv discovery candidates; no admission on failed checks."""
import json,re,time,urllib.request,urllib.parse,xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
rows={}
for base in ['reports/daily-updates','reports/arxiv-daily']:
 for p in (ROOT/base).rglob('*.json'):
  try:d=json.loads(p.read_text(encoding='utf-8-sig'))
  except (ValueError,OSError):continue
  if isinstance(d,dict):
   for r in d.get('papers',[]):
    if isinstance(r,dict) and re.fullmatch(r'\d{4}\.\d{4,5}',str(r.get('id',''))):rows[r['id']]=r
known=set()
for name in ['papers','methods']:
 for r in json.loads((ROOT/f'data/{name}.json').read_text(encoding='utf-8-sig'))[name]:known.add(re.sub(r'v\d+$','',str(r.get('arxiv_id') or '').split('/abs/')[-1]))
results=[];pending=[r for aid,r in sorted(rows.items()) if aid not in known]
ns={'a':'http://www.w3.org/2005/Atom'}
for i in range(0,len(pending),50):
 batch=pending[i:i+50];url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'id_list':','.join(r['id'] for r in batch),'max_results':50});official={};error=None
 for attempt in range(2):
  try:
   req=urllib.request.Request(url,headers={'User-Agent':'Awesome-Agent-Engineering-candidate-review/1.0'})
   with urllib.request.urlopen(req,timeout=25) as f:root=ET.fromstring(f.read())
   for e in root.findall('a:entry',ns):
    aid=re.sub(r'v\d+$','',e.findtext('a:id','',ns).split('/abs/')[-1]);official[aid]={'title':' '.join(e.findtext('a:title','',ns).split()),'abstract':' '.join(e.findtext('a:summary','',ns).split()),'published':e.findtext('a:published','',ns)[:10]}
   error=None;break
  except Exception as exc:error=str(exc);time.sleep(4)
 for r in batch:
  o=official.get(r['id']);status='unverified';reason=error or 'Identifier missing from official response'
  if o:
   if re.sub(r'\W','',o['title']).casefold()!=re.sub(r'\W','',r['title']).casefold():reason='Title mismatch'
   elif not o['published'] or o['published']>'2026-11-18':reason='Invalid publication date'
   elif re.search(r'\b(agent|agents|agentic|multi-agent|vision-language-action|tool.use|tool.calling)\b',o['title'],re.I):status='verified-in-scope';reason='Official identifier, title and publication date matched; explicit agent topic in title'
   else:status='needs-scope-review';reason='Metadata verified; title alone insufficient to establish Agent scope'
  results.append({'id':r['id'],'status':status,'reason':reason,'source':'https://arxiv.org/abs/'+r['id'],'metadata':o,'checked_at':datetime.now(timezone.utc).isoformat()})
 out=ROOT/'reports/daily-updates/2026-11-18-candidate-review.json';out.write_text(json.dumps({'total_discovered':len(rows),'already_known':len(rows)-len(pending),'reviewed':len(results),'total_pending':len(pending),'results':results},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n');print(f'Reviewed {len(results)}/{len(pending)}',flush=True);time.sleep(3)
