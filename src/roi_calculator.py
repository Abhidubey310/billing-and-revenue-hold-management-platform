"""Illustrative ROI calculator for the synthetic billing-hold portfolio project.

All figures are assumptions supplied in data/roi_assumptions.csv. The output is
for portfolio demonstration only and must not be presented as measured savings.
"""

from pathlib import Path
import pandas as pd


def load_assumptions(path: Path) -> dict[str, float]:
    df = pd.read_csv(path)
    required = {"metric", "value"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    return dict(zip(df["metric"], pd.to_numeric(df["value"], errors="raise")))


def calculate_roi(a: dict[str, float]) -> pd.DataFrame:
    annual_cases = a["monthly_hold_cases"] * a["working_months_per_year"]

    manual_hours = annual_cases * a["manual_minutes_per_case"] / 60
    assisted_hours = annual_cases * a["assisted_minutes_per_case"] / 60
    direct_hours_saved = manual_hours - assisted_hours

    rework_hours_before = (
        annual_cases * a["error_rework_rate_before"] * a["rework_minutes_per_case"] / 60
    )
    rework_hours_after = (
        annual_cases * a["error_rework_rate_after"] * a["rework_minutes_per_case"] / 60
    )
    rework_hours_saved = rework_hours_before - rework_hours_after

    total_hours_saved = direct_hours_saved + rework_hours_saved
    annual_gross_benefit = total_hours_saved * a["loaded_hourly_cost"]
    annual_net_benefit = annual_gross_benefit - a["annual_support_cost"]

    first_year_cost = a["one_time_build_cost"] + a["annual_support_cost"]
    first_year_roi_pct = (
        (annual_gross_benefit - first_year_cost) / first_year_cost * 100
        if first_year_cost else 0
    )
    payback_months = (
        a["one_time_build_cost"] / (annual_net_benefit / 12)
        if annual_net_benefit > 0 else float("inf")
    )

    metrics = [
        ("Annual cases reviewed", annual_cases, "cases"),
        ("Manual effort before", manual_hours, "hours"),
        ("Effort after automation", assisted_hours, "hours"),
        ("Direct processing hours saved", direct_hours_saved, "hours"),
        ("Rework hours saved", rework_hours_saved, "hours"),
        ("Total annual hours saved", total_hours_saved, "hours"),
        ("Capacity equivalent", total_hours_saved / 1820, "FTE"),
        ("Annual gross benefit", annual_gross_benefit, "GBP"),
        ("Annual net benefit", annual_net_benefit, "GBP"),
        ("First-year ROI", first_year_roi_pct, "%"),
        ("Estimated payback period", payback_months, "months"),
    ]

    return pd.DataFrame(metrics, columns=["metric", "value", "unit"])


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    assumptions = load_assumptions(root / "data" / "roi_assumptions.csv")
    result = calculate_roi(assumptions)
    output = root / "outputs" / "example_roi_summary.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output, index=False)
    print(result.to_string(index=False))


if __name__ == "__main__":
    main()
