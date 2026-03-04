import re
_ws=re.compile(r"\s+")

def normalize_text(t:str)->str:
    return _ws.sub(' ',t).strip()
