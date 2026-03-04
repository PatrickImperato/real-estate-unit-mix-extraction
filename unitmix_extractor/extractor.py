from .preprocessing import normalize_text
from .ner_stub import predict_spans
from .postprocess import build

def extract_unit_mix(text: str):
    clean = normalize_text(text)
    spans = predict_spans(clean)
    out = build(spans)
    out["debug"] = {"spans": spans}
    return out
