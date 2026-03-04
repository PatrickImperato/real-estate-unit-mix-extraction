import re
from typing import List, Tuple
Span = Tuple[str,str]

_re_total_units = re.compile(r"\b(\d+)\s*(?:unit|units|plex)\b", re.I)
_re_group = re.compile(
    r"\b(\d+)\s*(?:unit|units)\b[^\d]{0,40}?(\d+)\s*(?:bed|beds|br|bedroom|bedrooms)\b[^\d]{0,40}?(\d+(?:\.5)?)\s*(?:bath|baths|ba|bathroom|bathrooms)\b",
    re.I
)

def predict_spans(text: str) -> List[Span]:
    spans: List[Span] = []
    m = _re_total_units.search(text)
    if m:
        spans.append((m.group(0), "TOTUNIT"))
    for g in _re_group.finditer(text):
        spans.append((g.group(1) + " units", "DETUNIT"))
        spans.append((g.group(2) + " bed", "DETBED"))
        spans.append((g.group(3) + " bath", "DETBATH"))
    return spans
