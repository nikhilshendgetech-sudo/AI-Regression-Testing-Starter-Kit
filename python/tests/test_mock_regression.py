import csv
from pathlib import Path
import pytest

DATASET = Path(__file__).parents[2] / "datasets" / "ai_regression_tests.csv"

def load_cases():
    with DATASET.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

@pytest.mark.parametrize("case", load_cases(), ids=lambda c: c["test_id"])
def test_mock_regression_case_has_usable_expectation(case):
    # Free MVP demo: validates that every regression case has enough
    # information to be executed against a real model later.
    assert len(case["user_input"]) >= 10
    assert len(case["expected_behavior"]) >= 20
    assert len(case["evaluation_criteria"]) >= 20
