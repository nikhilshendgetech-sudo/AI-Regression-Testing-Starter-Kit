import csv
from pathlib import Path

import pytest


DATASET = Path(__file__).parents[2] / "datasets" / "ai_regression_tests.csv"


def load_cases():
    with DATASET.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def case_id(case):
    return (
        f'{case["test_id"]} - '
        f'{case["category"]} - '
        f'{case["application"]}'
    )


@pytest.mark.parametrize("case", load_cases(), ids=case_id)
def test_regression_case_has_usable_expectation(case):
    """
    MVP regression validation.

    Validates that every AI regression case contains enough
    information to be executed against a real AI/LLM system.
    """
    assert len(case["user_input"]) >= 10
    assert len(case["expected_behavior"]) >= 20
    assert len(case["evaluation_criteria"]) >= 20