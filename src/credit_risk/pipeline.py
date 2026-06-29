from __future__ import annotations

import argparse
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

import pandas as pd

LOGGER = logging.getLogger(__name__)


class DataValidationError(ValueError):
    """Raised when an input dataset does not match the expected contract."""


@dataclass(frozen=True)
class ProjectConfig:
    """Runtime configuration for the credit-risk profiling pipeline."""

    project_name: str
    default_dataset: str
    possible_target_columns: tuple[str, ...] = (
        "default_payment_next_month",
        "default.payment.next.month",
        "default",
    )


CONFIG = ProjectConfig("Credit risk analysis", "credit_card_clients.csv")


def normalize_column_name(column: object) -> str:
    """Return a normalized column name."""
    return (
        str(column)
        .strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace(".", "_")
    )


def load_dataset(
    path: str | Path, required_columns: Sequence[str] = ()
) -> pd.DataFrame:
    """Load CSV or Excel data with validation and normalized column names."""
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")
    LOGGER.info("Loading dataset from %s", dataset_path)
    suffix = dataset_path.suffix.lower()
    if suffix == ".csv":
        df = pd.read_csv(dataset_path)
    elif suffix in {".xlsx", ".xls"}:
        df = pd.read_excel(dataset_path)
    else:
        raise DataValidationError(f"Unsupported file format: {suffix}")
    df = df.copy()
    df.columns = [normalize_column_name(column) for column in df.columns]
    missing = sorted(set(required_columns) - set(df.columns))
    if missing:
        raise DataValidationError(f"Missing required columns: {missing}")
    return df


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return missing-value metrics by column."""
    total_rows = len(df)
    summary = pd.DataFrame(
        {"column": df.columns, "missing_count": df.isna().sum().values}
    )
    summary["missing_pct"] = (
        0.0 if total_rows == 0 else summary["missing_count"] / total_rows
    )
    return summary.sort_values(
        ["missing_count", "column"], ascending=[False, True]
    ).reset_index(drop=True)


def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return numeric descriptive statistics."""
    numeric_df = df.select_dtypes(include="number")
    return (
        pd.DataFrame()
        if numeric_df.empty
        else numeric_df.describe().transpose().reset_index(names="column")
    )


def default_rate_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return default-rate summary when a known default target column is available."""
    target_column = next(
        (column for column in CONFIG.possible_target_columns if column in df.columns),
        None,
    )
    if target_column is None:
        LOGGER.info(
            "Skipping default-rate summary; no known default target column was found"
        )
        return pd.DataFrame()
    return pd.DataFrame(
        {
            "metric": ["records", "default_rate"],
            "value": [int(len(df)), float(df[target_column].mean())],
        }
    )


def run_pipeline(
    input_path: str | Path, output_dir: str | Path = "data/processed"
) -> dict[str, Any]:
    """Run local profiling and optional credit-default summaries for an available dataset."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    df = load_dataset(input_path)
    missing_summary(df).to_csv(output_path / "missing_summary.csv", index=False)
    numeric_summary(df).to_csv(output_path / "numeric_summary.csv", index=False)
    default_summary = default_rate_summary(df)
    if not default_summary.empty:
        default_summary.to_csv(output_path / "default_rate_summary.csv", index=False)
    metrics = {"row_count": int(len(df)), "duplicate_rows": int(df.duplicated().sum())}
    (output_path / "dataset_metrics.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8"
    )
    LOGGER.info("Pipeline completed for %s", CONFIG.project_name)
    return {
        "rows": metrics["row_count"],
        "duplicate_rows": metrics["duplicate_rows"],
        "outputs": str(output_path),
    }


def main(argv: Sequence[str] | None = None) -> int:
    """Command-line entrypoint."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    parser = argparse.ArgumentParser(description=CONFIG.project_name)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="data/processed")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(run_pipeline(args.input, args.output), indent=2))
    except Exception:
        LOGGER.exception("Pipeline failed")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
