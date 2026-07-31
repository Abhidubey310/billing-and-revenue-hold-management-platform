"""Synthetic billing and revenue hold management engine."""

from __future__ import annotations

from pathlib import Path
import sys
import pandas as pd

REQUIRED_COLUMNS = {
    "case_id", "customer_name", "order_reference", "hold_date", "order_value",
    "hold_reason", "po_status", "service_status", "credit_status",
    "contract_status", "customer_response", "last_update_date",
}


def validate_input(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    if df.empty:
        raise ValueError("Input file contains no hold records.")
    if df["case_id"].isna().any() or df["order_reference"].isna().any():
        raise ValueError("Case ID and order reference must not be blank.")


def classify_row(row: pd.Series, as_of_date: pd.Timestamp) -> pd.Series:
    reason = str(row["hold_reason"]).strip().lower()
    age_days = int((as_of_date - row["hold_date"]).days)
    value = float(row["order_value"])

    if row["po_status"].upper() == "MISSING" or "purchase order" in reason:
        category, owner, action = "Commercial Documentation", "Account Management", "Obtain valid purchase order"
    elif row["service_status"].upper() == "NOT READY" or "service activation" in reason:
        category, owner, action = "Service Readiness", "Delivery Operations", "Confirm service readiness and activation date"
    elif row["credit_status"].upper() in {"REVIEW", "BLOCKED"} or "credit" in reason:
        category, owner, action = "Credit Control", "Credit Team", "Complete credit review before release"
    elif row["contract_status"].upper() == "REVIEW" or "contract" in reason:
        category, owner, action = "Contract Review", "Commercial Operations", "Resolve contract or pricing clarification"
    elif "duplicate" in reason:
        category, owner, action = "Potential Duplicate", "Billing Operations", "Validate duplicate and cancel or release"
    elif "customer confirmation" in reason:
        category, owner, action = "Customer Dependency", "Account Management", "Obtain customer confirmation"
    elif "data quality" in reason:
        category, owner, action = "Data Quality", "Revenue Operations", "Correct source data and revalidate"
    else:
        category, owner, action = "Unclassified Exception", "Billing Operations", "Perform manual review and confirm valid hold reason"

    if age_days >= 120 or value >= 75000:
        priority = "Critical"
    elif age_days >= 60 or value >= 40000:
        priority = "High"
    elif age_days >= 30 or value >= 15000:
        priority = "Medium"
    else:
        priority = "Low"

    explanation = f"{category}; {age_days} days on hold; value {value:,.0f}"
    return pd.Series({
        "hold_category": category,
        "owner_team": owner,
        "recommended_action": action,
        "age_days": age_days,
        "priority": priority,
        "decision_reason": explanation,
    })


def run_engine(input_path: Path, output_path: Path, as_of_date: str = "2026-08-01") -> pd.DataFrame:
    df = pd.read_csv(input_path)
    validate_input(df)
    df["hold_date"] = pd.to_datetime(df["hold_date"], errors="raise")
    df["last_update_date"] = pd.to_datetime(df["last_update_date"], errors="raise")
    df["order_value"] = pd.to_numeric(df["order_value"], errors="raise")

    assessment = df.apply(classify_row, axis=1, as_of_date=pd.Timestamp(as_of_date))
    result = pd.concat([df, assessment], axis=1)
    rank = {"Critical": 1, "High": 2, "Medium": 3, "Low": 4}
    result["_rank"] = result["priority"].map(rank)
    result = result.sort_values(["_rank", "order_value"], ascending=[True, False]).drop(columns="_rank")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output_path, index=False)
    return result


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        result = run_engine(
            root / "data" / "sample_billing_holds.csv",
            root / "outputs" / "example_hold_recommendations.csv",
        )
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Processed {len(result)} hold cases with total value {result['order_value'].sum():,.0f}.")
    print(result[["case_id", "hold_category", "owner_team", "priority"]].to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
