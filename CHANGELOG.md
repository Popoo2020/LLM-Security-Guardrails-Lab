# Changelog

All important changes to **LLM‑Security‑Guardrails‑Lab** are documented here
using the [Keep a Changelog](https://keepachangelog.com/) format and
[Semantic Versioning](https://semver.org/).

## [0.1.0] – 2026‑03‑01

### Added

* **Threat model:** Added `docs/threat_model.md` describing the lab’s
  assets, threat agents (prompt injection, data exfiltration, model
  exploitation, etc.) and high‑level mitigations.
* **Prompt injection harness:** Added `tests/test_prompt_injection.py` with a
  simple `sanitize_prompt` function and test cases demonstrating how to
  detect and neutralise malicious instructions.
* **Attack surface & test harness documentation:** Added `docs/attack_surface.md`
  to enumerate potential attack vectors in LLM‑enabled applications and
  `docs/test_harness.md` to explain how to run tests and interpret results.
* **Repository standards:** Added open‑source hygiene files such as
  LICENSE, SECURITY policy, CODE_OF_CONDUCT, CONTRIBUTING guide and
  CODEOWNERS file.
* **Initial release:** Published version `v0.1.0` to mark the first set of
  deliverables and enable community collaboration.
