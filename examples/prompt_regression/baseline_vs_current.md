# Prompt Regression Example

## Scenario

A customer-support prompt is changed to make responses shorter.

### Baseline requirement

Question:

Can I return an unused product after 20 days?

Approved policy:

Unused products can be returned within 30 days of delivery, provided the product is in original condition.

### Baseline output

Yes. An unused product can be returned after 20 days because it is within the 30-day return window, provided it remains in its original condition.

### Current output after prompt change

Returns are available within 14 days.

## Regression Result

**FAIL**

The current response changed the approved return window from 30 days to 14 days.

## Key Principle

Regression testing should compare required behavior, not exact wording.

## Recommended workflow

1. Store an approved baseline.
2. Change prompt/model/retrieval configuration.
3. Re-run the same dataset.
4. Evaluate current output against the same criteria.
5. Compare baseline and current results.
6. Investigate failures before release.