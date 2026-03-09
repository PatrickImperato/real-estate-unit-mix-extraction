# Modeling Approach

This project treats unit mix extraction as a structured information extraction problem.

## Goal

Convert messy apartment listing text into normalized unit mix data that can be used in downstream underwriting and portfolio analysis workflows.

## Approach

The extraction pipeline uses two stages.

### Stage 1

Named entity recognition identifies candidate spans such as:

1. unit count
2. bedroom count
3. bathroom count

### Stage 2

Post processing logic groups those spans into normalized unit types and validates them against simple structural rules.

## Why this approach

This design balances three goals:

1. interpretability
2. controllable output structure
3. practical use in downstream financial workflows

## Production note

This public repository ships a safe stub model so the project can run without exposing production artifacts or proprietary data.

The intent is to demonstrate problem framing, pipeline design, and evaluation methodology.
