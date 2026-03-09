# Output Schema

The extraction pipeline produces structured unit mix records.

Each output record is designed to support downstream underwriting and portfolio analysis.

## Core fields

**unit_type**  
Normalized unit label such as studio, one bedroom, or two bedroom.

**bedrooms**  
Numeric bedroom count.

**bathrooms**  
Numeric bathroom count when available.

**unit_count**  
Number of units matching the extracted type.

**source_text**  
Original listing fragment associated with the extracted data.

**confidence**  
Estimated confidence score for the extracted record.

## Why this matters

A clear schema makes the output easier to validate, compare, and integrate into underwriting workflows.
