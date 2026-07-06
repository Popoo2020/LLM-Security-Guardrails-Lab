# Threat Model

## Scope

This threat model covers the educational guardrails lab, including deterministic prompt-risk inspection, sensitive-value redaction examples, tests and CI validation. It does not cover production LLM traffic, enterprise DLP or real customer prompts.

## Assets

- User-provided prompts and sample inputs.
- Sensitive-value redaction patterns.
- Prompt-risk inspection logic.
- Test fixtures and expected classifications.
- CI workflows and dependency manifests.

## Trust boundaries

1. User or fixture input to prompt-risk inspection.
2. Raw text to redacted/sanitised output.
3. Classification output to downstream consumer decisions.
4. Repository changes to CI and security checks.

## Primary risks and controls

| Risk | Impact | Existing control | Additional note |
|---|---|---|---|
| Prompt injection bypass | Unsafe text not detected | Deterministic pattern checks and tests | Pattern matching is not a full model-safety system. |
| Sensitive value leakage | Secrets or personal data remain in output | Redaction examples and tests | Do not use real secrets in fixtures. |
| False assurance | Users overtrust a demo guardrail | SECURITY.md states limitations | Keep README and reports explicit about scope. |
| Regression in guardrail logic | Known unsafe patterns stop being detected | pytest and CI validation | Add fixtures for every new bypass class. |
| Dependency or CI regression | Broken validation pipeline | ruff, pytest, Bandit, pip-audit and CodeQL | Keep checks required before merging. |

## Security invariants

- Test fixtures must not contain real secrets, personal data or private prompts.
- Redaction examples must preserve safety over completeness claims.
- Guardrail outputs must not be represented as production-grade guarantees.
- CI must validate prompt-risk and redaction behaviour before changes are accepted.

## Out of scope

- Production LLM firewalling.
- Enterprise DLP replacement.
- Live model jailbreak evaluation.
- Real customer prompt processing.
