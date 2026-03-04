import json
from pathlib import Path
from unitmix_extractor import extract_unit_mix
from unitmix_eval.metrics import score_one

def load_jsonl(p: Path):
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            yield json.loads(line)

def main(inputs_path: Path, labels_path: Path):
    inputs = {r["id"]: r for r in load_jsonl(inputs_path)}
    labels = {r["id"]: r for r in load_jsonl(labels_path)}
    scores=[]
    for _id,gold in labels.items():
        pred = extract_unit_mix(inputs[_id]["text"])
        scores.append(score_one(gold, pred))
    n=max(1,len(scores))
    return {
        "n": len(scores),
        "total_exact_rate": sum(s["total_exact"] for s in scores)/n,
        "mix_exact_rate": sum(s["mix_exact"] for s in scores)/n,
        "avg_mix_overlap_rate": sum(s["mix_overlap_rate"] for s in scores)/n
    }

if __name__ == "__main__":
    import argparse
    a=argparse.ArgumentParser()
    a.add_argument("--inputs", required=True)
    a.add_argument("--labels", required=True)
    args=a.parse_args()
    print(json.dumps(main(Path(args.inputs), Path(args.labels)), indent=2))
