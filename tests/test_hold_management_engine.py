from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hold_management_engine import classify_row, run_engine


def test_missing_po_routes_to_account_management():
    row = pd.Series({
        "hold_reason": "Purchase order missing",
        "po_status": "Missing",
        "service_status": "Ready",
        "credit_status": "Clear",
        "contract_status": "Active",
        "hold_date": pd.Timestamp("2026-07-01"),
        "order_value": 10000,
    })
    result = classify_row(row, pd.Timestamp("2026-08-01"))
    assert result["hold_category"] == "Commercial Documentation"
    assert result["owner_team"] == "Account Management"


def test_engine_produces_one_result_per_case(tmp_path):
    output = tmp_path / "result.csv"
    result = run_engine(ROOT / "data" / "sample_billing_holds.csv", output)
    assert len(result) == 12
    assert result["case_id"].is_unique
    assert output.exists()


def test_all_cases_have_explainable_outputs(tmp_path):
    result = run_engine(
        ROOT / "data" / "sample_billing_holds.csv",
        tmp_path / "result.csv",
    )
    required = ["hold_category", "owner_team", "recommended_action", "priority", "decision_reason"]
    assert result[required].notna().all().all()
