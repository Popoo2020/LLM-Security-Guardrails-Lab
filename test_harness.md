# Test Harness

This lab provides a simple test harness to evaluate prompt injection
countermeasures.  The current implementation is intentionally minimal and
serves as a foundation for building more comprehensive tests.

## Running Tests

Tests are written with [`pytest`](https://docs.pytest.org/).  To run the
existing tests:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt  # ensure pytest is installed
pytest -q tests/test_prompt_injection.py
```

The test file imports a `sanitize_prompt` function from your application
code.  It feeds crafted inputs containing potential injection patterns and
asserts that the sanitisation logic neutralises them appropriately.

## Understanding the Harness

The provided `sanitize_prompt` example performs a very naive sanitisation
by replacing occurrences of `"--"`, `";"` and other shell‑related tokens.
The test cases demonstrate both benign and malicious prompts.  When
expanding the harness:

1. **Enumerate attack categories** – Represent different injection
   techniques such as overriding system prompts, retrieving sensitive
   documents or causing code execution.
2. **Define expected behaviour** – Decide whether the guardrail should
   block, sanitise or allow the given input.  Write assertions reflecting
   these expectations.
3. **Test edge cases** – Consider ambiguous inputs and ensure that the
   sanitiser doesn’t over‑sanitise (leading to loss of functionality) or
   under‑sanitise (allowing an attack).
4. **Measure effectiveness** – In future versions, incorporate metrics for
   false positives/negatives and performance impact.

## Expanding the Harness

The lab aims to cover additional guardrail categories:

* **Retrieval poisoning tests** – Provide malicious documents and verify
  that retrieval filtering removes or annotates them appropriately.
* **Output filtering tests** – Generate responses from the model and assert
  that redaction pipelines remove sensitive information and enforce
  allow/deny lists.
* **Eval rubric** – Develop a rubric to score guardrail performance across
  scenarios.  This could include metrics like detection rate, false
  positive rate and latency overhead.

Feel free to open issues or pull requests to contribute new test cases and
enhancements to the harness.
