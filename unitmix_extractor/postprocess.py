import re
from typing import List, Dict, Any, Optional

_num = re.compile(r"(\d+(?:\.5)?)")

def _to_int(x:str)->Optional[int]:
    m=_num.search(x)
    return int(float(m.group(1))) if m else None

def _to_float(x:str)->Optional[float]:
    m=_num.search(x)
    return float(m.group(1)) if m else None

def build(spans: List[tuple[str,str]])->Dict[str,Any]:
    total=None
    for t,l in spans:
        if l=="TOTUNIT":
            total=_to_int(t)
            break
    mix=[]
    i=0
    while i < len(spans):
        t,l=spans[i]
        if l!="DETUNIT":
            i+=1
            continue
        count=_to_int(t)
        beds=_to_int(spans[i+1][0]) if i+1 < len(spans) and spans[i+1][1]=="DETBED" else None
        baths=_to_float(spans[i+2][0]) if i+2 < len(spans) and spans[i+2][1]=="DETBATH" else None
        if count is not None and beds is not None and baths is not None:
            baths_out = int(baths) if baths.is_integer() else baths
            mix.append({"count":count,"beds":beds,"baths":baths_out})
            i+=3
        else:
            i+=1
    if total is None and mix:
        total=sum(u["count"] for u in mix)
    return {"total_units": total, "unit_mix": mix}
