"""Extension point for a real model/API evaluation.

Replace call_model() with your provider/API call, then implement
evaluate_response() using deterministic checks or an evaluator model.
The free kit intentionally ships without API keys or paid API calls.
"""

import csv
from pathlib import Path

DATASET = Path(__file__).parents[1] / "datasets" / "ai_regression_tests.csv"

def call_model(user_input: str, context: str) -> str:
    raise NotImplementedError(
        "Connect your chosen LLM/API here. No API key is bundled with this product."
    )

def evaluate_response(case, response: str) -> dict:
    # Starter heuristic. Production evaluation should use stronger
    # semantic/LLM-as-judge checks and application-specific thresholds.
    return {
        "test_id": case["test_id"],
        "status": "NOT_IMPLEMENTED",
        "response": response,
        "notes": "Implement provider-specific evaluation logic."
    }

if __name__ == "__main__":
    with DATASET.open(newline="", encoding="utf-8") as f:
        cases = list(csv.DictReader(f))
    print(f"Loaded {len(cases)} AI regression cases.")
    print("Next step: connect your model/API in call_model().")
