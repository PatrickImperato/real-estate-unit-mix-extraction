import json
from pathlib import Path
import typer
from unitmix_extractor import extract_unit_mix

app = typer.Typer(add_completion=False)

@app.command()
def run(input_path: Path, output_path: Path = Path("predictions.jsonl")):
    rows=[json.loads(l) for l in input_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    with output_path.open("w", encoding="utf-8") as f:
        for r in rows:
            pred = extract_unit_mix(r["text"])
            f.write(json.dumps({"id": r["id"], **pred}, ensure_ascii=False) + "\n")
    typer.echo(f"Wrote {len(rows)} predictions to {output_path}")

if __name__ == "__main__":
    app()
