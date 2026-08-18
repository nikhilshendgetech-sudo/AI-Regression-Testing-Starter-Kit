# Quick Start — AI Regression Testing Starter Kit

## What this free kit is
A practical starter resource for QA Engineers and SDETs who want to design
repeatable regression tests for AI/LLM applications.

## 1. Review the dataset
Open `datasets/ai_regression_tests.csv`. Each row contains a realistic scenario,
context, expected behavior, evaluation criteria, and severity.

## 2. Use the scorecard
Open `templates/evaluation_scorecard.xlsx`.
Score Accuracy, Relevance, Groundedness, Safety, and Consistency from 0–2.
The default pass threshold is 8/10.

## 3. Run the Python starter checks
From the project root:
```bash
python -m venv .venv
# Activate .venv using your OS-specific command
pip install -r python/requirements.txt
pytest python/tests -v
```

The free MVP does not include a paid API key. Connect your own model/API in
`python/run_real_evaluation.py` for real model execution.

## 4. Try the Promptfoo example
Install Promptfoo and follow `promptfoo/README.md`.
Never commit API keys.

## 5. Run CI
Push the repository to GitHub. The included workflow validates the dataset and
generates a pytest HTML artifact.

## Recommended real-world workflow
Prompt/model change → run fixed evaluation dataset → score outputs →
compare with baseline → review failures → decide pass/fail → release.

## Scope
This is a starter framework, not a complete AI safety or production validation system.
Security, privacy, compliance, and high-risk AI applications require additional controls
and expert review.
