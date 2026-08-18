import csv
from pathlib import Path

DATASET = Path(__file__).parents[2] / "datasets" / "ai_regression_tests.csv"

def load_cases():
    with DATASET.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def test_dataset_has_expected_cases():
    cases = load_cases()
    assert len(cases) == 10
    assert len({c["test_id"] for c in cases}) == 10

def test_required_fields_are_present():
    cases = load_cases()
    required = {
        "test_id", "category", "application", "user_input", "context",
        "expected_behavior", "evaluation_criteria", "severity"
    }
    for case in cases:
        assert required.issubset(case.keys())
        assert all(case[field].strip() for field in required)

def test_severity_values_are_valid():
    valid = {"Low", "Medium", "High", "Critical"}
    for case in load_cases():
        assert case["severity"] in valid
