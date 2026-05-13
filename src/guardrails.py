"""Minimal defensive guardrail helpers for LLM input experiments.

This module is intentionally small and transparent.  It does not claim to
solve prompt injection comprehensively; instead, it provides a deterministic
baseline that can be unit-tested and extended as the lab matures.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class GuardrailDecision:
    """Result object for simple prompt-risk inspection."""

    blocked: bool
    reasons: tuple[str, ...]
    sanitized_prompt: str


_SUSPICIOUS_PATTERNS: dict[str, re.Pattern[str]] = {
    "instruction_override": re.compile(r"\b(ignore|disregard|override)\b.{0,40}\b(instructions?|system prompt|previous)\b", re.IGNORECASE),
    "secret_request": re.compile(r"\b(reveal|show|print|exfiltrate)\b.{0,40}\b(secret|api key|token|password|system prompt)\b", re.IGNORECASE),
    "tool_abuse": re.compile(r"\b(run|execute|call)\b.{0,40}\b(shell|bash|powershell|tool)\b", re.IGNORECASE),
}

_REDACTION_RULES: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"(?i)api[_ -]?key\s*[:=]\s*\S+"), "API_KEY=[REDACTED]"),
    (re.compile(r"(?i)password\s*[:=]\s*\S+"), "PASSWORD=[REDACTED]"),
    (re.compile(r"(?i)bearer\s+[A-Za-z0-9._\-]+"), "Bearer [REDACTED]"),
)


def sanitize_prompt(prompt: str) -> str:
    """Apply conservative text redactions to potentially sensitive prompt data."""
    if not isinstance(prompt, str):
        raise TypeError("prompt must be a string")

    sanitized = prompt.strip()
    for pattern, replacement in _REDACTION_RULES:
        sanitized = pattern.sub(replacement, sanitized)
    return sanitized


def inspect_prompt(prompt: str) -> GuardrailDecision:
    """Inspect a prompt for simple prompt-injection indicators.

    The function returns both a sanitized prompt and a compact reason list so
    that tests and future evaluation harnesses can reason about behaviour.
    """
    sanitized = sanitize_prompt(prompt)
    reasons: list[str] = []
    for reason, pattern in _SUSPICIOUS_PATTERNS.items():
        if pattern.search(sanitized):
            reasons.append(reason)
    return GuardrailDecision(
        blocked=bool(reasons),
        reasons=tuple(reasons),
        sanitized_prompt=sanitized,
    )


def batch_inspect(prompts: Iterable[str]) -> list[GuardrailDecision]:
    """Inspect multiple prompts and return deterministic guardrail decisions."""
    return [inspect_prompt(prompt) for prompt in prompts]
