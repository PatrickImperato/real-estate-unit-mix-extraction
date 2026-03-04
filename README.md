# Real estate unit mix extraction

Extract structured unit mix from messy listing descriptions.

This repository targets recruiters and hiring managers.

It highlights product thinking, dataset design, and evaluation.

It intentionally omits a full production system.

## What this project solves

Real estate listings often describe unit mix inside free text.

Agents use inconsistent formats.

You want structured numbers for analysis.

## Inputs and outputs

Input

• One listing description as plain text

Output

• total_units
• unit_mix with count, beds, baths

Example output

```json
{
  "total_units": 4,
  "unit_mix": [
    {"count": 2, "beds": 1, "baths": 1},
    {"count": 2, "beds": 2, "baths": 1}
  ]
}
```

## Quickstart

Requirements

• Python 3.10+

Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install pytest
```

Run the pipeline on sample inputs

```bash
python cli.py run data/sample_inputs.jsonl predictions.jsonl
```

Evaluate on sample labels

```bash
python unitmix_eval/evaluate.py --inputs data/sample_inputs.jsonl --labels data/sample_labels.jsonl
```

Run tests

```bash
pytest
```

## Pipeline design

High level flow

• Text normalization
• Entity extraction
• Grouping and pairing
• Numeric normalization
• Structured output

The repo ships a safe NER stub.

It mimics a trained model without shipping weights.

To plug in a real spaCy model, replace unitmix_extractor ner_stub.py.

## Documentation

• docs/problem_definition.md
• docs/output_schema.md
• docs/data_labeling_guide.md
• docs/modeling_approach.md
• docs/training_process.md
• docs/evaluation_plan.md
• docs/error_analysis.md
• docs/whats_omitted_and_why.md

## Rent pricing step

The product calls a rent pricing step after unit mix extraction.

This repo treats it as a black box.

See unitmix_extractor rent_estimator_stub.py.

## What is intentionally omitted

• Deployed app
• Hosting details
• Keys and secrets
• Production dataset
• Production scraper
• Production model artifacts
