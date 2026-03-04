# Real Estate Unit Mix Extraction

Extract structured unit mix data from unstructured apartment listing descriptions.

This project demonstrates an applied NLP system that converts messy real estate listing text into structured data that can be used for financial modeling, underwriting, and portfolio analysis.

The repository focuses on the design of the NLP extraction system, including problem framing, dataset design, labeling strategy, modeling approach, and evaluation methodology.

The production system includes additional components that are intentionally not included here.

---

## Table of Contents

• [Problem](#problem)  
• [Example](#example)  
• [System Overview](#system-overview)  
• [Modeling Approach](#modeling-approach)  
• [Dataset and Labeling](#dataset-and-labeling)  
• [Evaluation](#evaluation)  
• [Repository Structure](#repository-structure)  
• [Running the Example Pipeline](#running-the-example-pipeline)  
• [Documentation](#documentation)  
• [What Is Intentionally Omitted](#what-is-intentionally-omitted)

---

## Problem

Apartment building listings frequently describe the **unit mix** inside free form text written by listing agents.

Examples of listing descriptions may include phrases like:

20 one bedroom 1 bathrooms  
five two bedroom with one and half bath

In many cases the unit mix is embedded inside longer paragraphs describing the property.

Because there is no standardized format, extracting reliable unit mix data from listings at scale becomes difficult.

However, structured unit mix data is critical for many real estate workflows, including:

• rent estimation  
• underwriting models  
• automated financial projections  
• portfolio analysis

This project focuses on building an NLP pipeline that converts messy listing descriptions into structured unit mix data.

Back to top → [Table of Contents](#table-of-contents)

---

## Example

Input text

Four total units. Two units are 1 bedroom 1 bath. Two units are 2 bedroom 1 bath.

Structured output

```json
{
  "total_units": 4,
  "unit_mix": [
    { "count": 2, "beds": 1, "baths": 1 },
    { "count": 2, "beds": 2, "baths": 1 }
  ]
}
```

Back to top → [Table of Contents](#table-of-contents)

---

## System Overview

The overall system converts raw listing text into structured data that can be used by downstream models.

High level flow

Listing description text  
→ NLP entity extraction  
→ span grouping and normalization  
→ structured unit mix JSON  
→ rent estimation step  
→ downstream financial modeling

This repository focuses specifically on the **information extraction layer**.

The rent estimation step is represented with a stub interface to illustrate how the extraction output connects to downstream models.

Back to top → [Table of Contents](#table-of-contents)

---

## Modeling Approach

The core extraction approach uses **Named Entity Recognition**.

Primary approach

• spaCy NER for entity extraction

Additional experiments

• lightweight BERT fine tuning experiments

Training approach

• manually labeled training examples  
• domain specific labeling schema  
• iterative dataset refinement through error analysis

The goal was **practical extraction accuracy** for underwriting workflows rather than perfect extraction on every listing.

Back to top → [Table of Contents](#table-of-contents)

---

## Dataset and Labeling

The extraction task requires a domain specific labeling schema.

Primary entity labels

• TOTUNIT  
• DETUNIT  
• TOTBED  
• DETBED  
• TOTBATH  
• DETBATH

Annotation tool

Doccano sequence labeling.

Design goals for the labeling schema

• simple enough for fast annotation  
• expressive enough to reconstruct the unit mix deterministically  
• flexible across inconsistent listing formats

Example dataset files included in the repository

• [Sample Inputs](data/sample_inputs.jsonl)  
• [Sample Labels](data/sample_labels.jsonl)

Back to top → [Table of Contents](#table-of-contents)

---

## Evaluation

Evaluation focuses on **structured output quality** rather than token level NER metrics.

Metrics included

• total unit count exact match  
• unit mix exact match  
• unit mix overlap score

This allows evaluation of the **full extraction pipeline**, not just the NER model.

Evaluation script

• [Evaluation Script](unitmix_eval/evaluate.py)

Back to top → [Table of Contents](#table-of-contents)

---

## Repository Structure

Key folders

**data**  
Sample input listings and synthetic labels

**docs**  
Design documentation and methodology

**unitmix_extractor**  
Core extraction pipeline

**unitmix_eval**  
Evaluation harness and scoring metrics

**tests**  
Basic smoke tests for pipeline validation

Back to top → [Table of Contents](#table-of-contents)

---

## Running the Example Pipeline

Create environment

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .
pip install pytest
```

Run extraction on sample data

```bash
python cli.py data/sample_inputs.jsonl
```

Evaluate predictions

```bash
python unitmix_eval/evaluate.py --inputs data/sample_inputs.jsonl --labels data/sample_labels.jsonl
```

Run tests

```bash
python -m pytest -q tests
```

Back to top → [Table of Contents](#table-of-contents)

---

## Documentation

Additional design documentation

• [Problem Definition](docs/problem_definition.md)  
• [Output Schema](docs/output_schema.md)  
• [Dataset and Labeling Guide](docs/data_labeling_guide.md)  
• [Modeling Approach](docs/modeling_approach.md)  
• [Training Process](docs/training_process.md)  
• [Evaluation Plan](docs/evaluation_plan.md)  
• [Error Analysis](docs/error_analysis.md)  
• [What Is Omitted And Why](docs/whats_omitted_and_why.md)

Back to top → [Table of Contents](#table-of-contents)

---

## What Is Intentionally Omitted

The production system includes additional components that are not included in this repository.

These include

• deployed web application  
• infrastructure and hosting configuration  
• production scraping pipelines  
• full training datasets  
• trained model artifacts  
• external rent estimation providers

These components are excluded to keep the repository safe to share while still demonstrating the design and implementation approach.
