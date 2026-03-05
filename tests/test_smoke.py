import json
from pathlib import Path
from unitmix_extractor import extract_unit_mix


def test_smoke():

    lines = Path("data/sample_inputs.jsonl").read_text(encoding="utf-8").splitlines()

    assert len(lines) > 0

    row = json.loads(lines[0])

    pred = extract_unit_mix(row["text"])

    assert isinstance(pred, dict)

    assert "total_units" in pred

    assert "unit_mix" in pred
