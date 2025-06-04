import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import json
import urllib.request
import reference_tool.crossref
from reference_tool.crossref import search

class DummyResponse:
    def __init__(self, payload: str):
        self.payload = payload.encode()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    def read(self):
        return self.payload

def test_search(monkeypatch):
    payload = json.dumps({
        "message": {"items": [{"title": ["A Title"], "DOI": "10.1/abc"}]}
    })
    monkeypatch.setattr(reference_tool.crossref, 'urlopen', lambda req: DummyResponse(payload))
    results = search("example", rows=1)
    assert results == [{"title": "A Title", "doi": "10.1/abc"}]
