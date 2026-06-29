# Credito Bancario - Credit Risk Analysis

Professional Python project for exploratory credit-risk analysis. The original notebook is preserved and reusable project code now lives in `src/credit_risk/`.

## Staff Data Engineer assessment

This repository is valuable for fintech and banking interviews because it works with customer behavior, payment history and risk signals. The main gap was that all logic lived in a notebook with local/Drive paths and no reproducible project structure.

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

## How to run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
python -m credit_risk.pipeline --input data/raw/credit_card_clients.csv --output data/processed
```

## Pipeline capabilities

- CSV/Excel ingestion with clear errors.
- Column-name normalization.
- Missing-value summary.
- Numeric profiling.
- Duplicate-row metrics.
- Artifact generation in `data/processed/`.

## Current limitations

- The dataset is not committed and must be provided locally.
- Predictive modeling should be extracted from the notebook in a later PR.
- Expected schema and target definitions should be formalized.
- A final executive risk summary should be generated automatically.
