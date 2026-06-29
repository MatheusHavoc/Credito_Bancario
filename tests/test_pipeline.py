from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from credit_risk.pipeline import load_dataset, missing_summary, run_pipeline


def test_load_dataset_normalizes_columns(tmp_path):
    dataset = tmp_path / "sample.csv"
    pd.DataFrame({"Credit Limit": [100, None], "Default": [0, 1]}).to_csv(
        dataset, index=False
    )
    df = load_dataset(dataset)
    assert list(df.columns) == ["credit_limit", "default"]


def test_missing_summary_counts_nulls():
    summary = missing_summary(pd.DataFrame({"a": [1, None]}))
    assert summary.loc[0, "missing_count"] == 1


def test_run_pipeline_writes_outputs(tmp_path):
    dataset = tmp_path / "sample.csv"
    output = tmp_path / "processed"
    pd.DataFrame({"limit": [1, 2], "default": [0, 1]}).to_csv(dataset, index=False)
    result = run_pipeline(dataset, output)
    assert result["rows"] == 2
    assert (output / "dataset_metrics.json").exists()
