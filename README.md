# Credito Bancario - Credit Risk Analysis

This repository contains the original Taiwan credit analysis notebook and a new lightweight Python profiling layer under `src/credit_risk/`.

## What this PR changes

The notebook remains the source of the full exploratory analysis. The Python code added here does not train a credit-risk model. It provides:

- local CSV/Excel ingestion with explicit errors;
- normalized column names;
- missing-value and numeric profiling outputs;
- duplicate-row metrics;
- an optional `default_rate_summary.csv` when a known default target column is present;
- tests for ingestion and profiling behavior.

## Structure

```text
.
├── CréditoBancário.ipynb
├── data/
├── images/
├── notebooks/
├── src/credit_risk/
├── tests/
├── requirements.txt
└── README.md
```

## Dataset requirement

The expected local input is `data/raw/credit_card_clients.csv`. That file is not committed. Without it, the pipeline cannot be executed end to end.

## How to run when the dataset is available

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
python -m credit_risk.pipeline --input data/raw/credit_card_clients.csv --output data/processed
```

## Outputs

Always generated when the input file exists:

- `data/processed/missing_summary.csv`
- `data/processed/numeric_summary.csv`
- `data/processed/dataset_metrics.json`

Generated only when a known default target column exists:

- `data/processed/default_rate_summary.csv`

## Current limitations

- Predictive modeling still lives in future work; it is not implemented in this PR.
- Dataset source, schema and target definition need stronger documentation.
- The README avoids claiming banking production readiness or model performance that has not been validated.
