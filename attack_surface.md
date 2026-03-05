# Attack Surface

This document catalogues the key entry points and potential abuses in
applications that integrate large language models (LLMs).  Understanding the
attack surface helps prioritise defensive measures and informs threat
mitigation strategies.

## Entry Points

### Prompt Input

Users supply prompts directly to the LLM or through an application interface.
Attackers can craft inputs containing hidden instructions, malicious code or
social‑engineering content.  For example, prompt injection attacks attempt
to override system prompts or extract sensitive data from the model’s
context.

### Retrieval Sources

Many LLM applications use retrieval‑augmented generation (RAG) to fetch
context from external knowledge bases.  These sources may be untrusted or
subject to poisoning.  An attacker could insert malicious documents into
the knowledge base, causing the LLM to produce harmful or misleading
responses.

### Output Channels

Generated content may be displayed directly to users, stored in logs or
forwarded to downstream systems.  Attackers may attempt to exfiltrate
secrets, inject malicious links or include content that triggers client‑side
scripts.

### Model Configuration & Plugins

Integrations with external plugins (e.g. code execution, web browsing) expand
the attack surface.  Misconfigured plugins may allow arbitrary command
execution or access to sensitive resources.

## Potential Abuses

* **Prompt Injection:** Crafting inputs that persuade the model to reveal
  hidden instructions, secrets or to perform actions outside its intended
  scope.
* **Retrieval Poisoning:** Inserting malicious data into a knowledge base
  so that the model learns or retrieves harmful content.
* **Data Exfiltration:** Using the model to extract proprietary or
  confidential information from memory, logs or context windows.
* **Jailbreaking/Bypassing Restrictions:** Exploiting weaknesses in
  guardrails to circumvent content filters and produce disallowed outputs.
* **Malicious Output:** Causing the model to generate phishing content,
  offensive language or malware instructions that may be executed by
  downstream systems.

## Mitigations

* **Sanitisation:** Implement input pre‑processing to strip or neutralise
  potentially harmful tokens, patterns or instructions.
* **Retrieval Filtering:** Validate and curate knowledge bases.  Apply
  adversarial filtering or trust scores to retrieved documents before
  supplying them to the model.
* **Output Filtering:** Apply allow/deny lists and pattern matching to
  generated responses.  Summarise or redact sensitive information.
* **Access Controls:** Limit plugin capabilities and require explicit
  authorization for actions that affect external systems.
* **Monitoring & Logging:** Record inputs and outputs for forensic
  analysis.  Use rate limiting to detect anomalous interaction patterns.

This is a living document; feel free to contribute additional attack
scenarios and defences as research evolves.
