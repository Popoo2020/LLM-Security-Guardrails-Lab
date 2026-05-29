# Security Policy

## Purpose

This repository is an educational AI-security lab for deterministic prompt-risk inspection, sensitive-value redaction examples and guardrail testing.

## Supported use

Use this project only for:

- educational review,
- authorised AI-security testing,
- portfolio evaluation,
- local demonstrations,
- controlled internal experiments.

It is not a production LLM firewall, DLP system or complete model-safety platform.

## Security posture

The project is designed around transparent, testable controls:

- pattern-based prompt-risk inspection,
- simple sensitive-value redaction examples,
- deterministic pytest coverage,
- explicit limitations in documentation.

## Reporting security issues

If you find a security-relevant issue, open a GitHub issue with:

1. the affected file or behaviour,
2. why the behaviour could create risk,
3. a minimal reproduction case,
4. whether the issue affects tests, documentation or runtime logic.

Do not include real credentials, private prompts, personal data or sensitive third-party information.

## Known limitations

- Pattern-based detection will not catch all attack variants.
- This is not a production-grade security control.
- Redaction examples are intentionally scoped and do not replace enterprise DLP.
- The lab currently focuses on input inspection and baseline sanitisation only.
