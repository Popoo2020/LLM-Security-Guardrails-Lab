# Threat Model

This document outlines the threat model for the LLM Security Guardrails Lab. It identifies assets, potential threats and mitigations related to large language model (LLM) applications.

## Assets

* **User Data:** Messages, prompts and personal context provided by users.
* **Model Integrity:** The correctness and reliability of the LLM outputs.
* **System Infrastructure:** Servers, storage and networking components hosting the LLM service.

## Threats

1. **Prompt Injection:** Attackers craft malicious inputs to manipulate the LLM into revealing secrets, executing unwanted actions or bypassing safety filters.
2. **Data Leakage:** Sensitive data or personally identifiable information (PII) may be inadvertently included in training or inference responses.
3. **Model Abuse:** The LLM could be used to generate harmful content, misinformation or spam if guardrails are not enforced.
4. **Retrieval Poisoning:** Malicious actors insert poisoned documents into the retrieval store to influence LLM outputs.
5. **Denial of Service:** Flooding the service with requests to degrade performance or disrupt availability.

## Mitigations

* **Input Sanitization:** Strip or escape special tokens, scripts and patterns commonly used in prompt injection attacks. Implement a sanitization layer to redact emails, IP addresses and secrets.
* **Rate Limiting & Authentication:** Apply per‑user rate limits and require authentication to prevent abuse and DoS attacks.
* **Content Filtering:** Use classifiers to detect and block toxic or disallowed content before and after LLM generation.
* **Monitoring & Logging:** Record requests and responses with correlation identifiers to enable incident triage and forensic analysis.
* **Data Governance:** Ensure training data is sanitized and implement policies for deletion or anonymization of user data.
* **Retrieval Integrity Checks:** Validate the integrity and source of documents added to the vector store to mitigate poisoning.