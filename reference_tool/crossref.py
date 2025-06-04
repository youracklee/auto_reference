import json
from typing import List, Dict
from urllib.parse import urlencode
from urllib.request import urlopen, Request


def search(query: str, rows: int = 5) -> List[Dict[str, str]]:
    params = urlencode({'query': query, 'rows': rows})
    url = f'https://api.crossref.org/works?{params}'
    req = Request(url, headers={'User-Agent': 'reference-tool/0.1'})
    with urlopen(req) as resp:
        data = json.load(resp)
    results = []
    for item in data.get('message', {}).get('items', []):
        title = item.get('title', [''])[0]
        doi = item.get('DOI')
        if doi:
            results.append({'title': title, 'doi': doi})
    return results
