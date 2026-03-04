import json
from pathlib import Path
from unitmix_extractor import extract_unit_mix

def test_smoke():
    row = json.loads(Path("data/sample_inputs.jsonl").read_text(encoding="utf-8").splitlines()[0])
    pred = extract_unit_mix(row["text"])
    assert pred["total_units"] is not None
