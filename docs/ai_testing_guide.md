# Practical AI Regression Testing Guide

## Why regression testing is different for AI
Traditional software often has deterministic assertions. LLM applications can produce
variable natural-language outputs, so evaluation should focus on observable behavior,
grounding, safety, and task-specific quality.

## Recommended regression loop
1. Capture representative production/use-case inputs.
2. Build a versioned evaluation dataset.
3. Define expected behavior and evaluation criteria.
4. Establish a baseline.
5. Change the prompt/model/retrieval configuration.
6. Re-run the same dataset.
7. Compare scores and investigate failures.
8. Apply release thresholds and human review where required.

## Suggested dimensions
- Correctness / task success
- Relevance
- Groundedness
- Consistency
- Safety / privacy
- Refusal behavior
- Scope adherence

## Regression principle
Do not rely on a single pass/fail assertion for every natural-language response.
Combine deterministic checks, rubric-based evaluation, representative datasets,
and human review for important or ambiguous cases.

## Baseline
Store the previous approved evaluation results. A regression is any unacceptable
degradation against the defined threshold, not simply a different wording.

## Security
Prompt injection and sensitive-data scenarios should be treated as security tests.
Passing a numeric score does not automatically prove an application is secure.
