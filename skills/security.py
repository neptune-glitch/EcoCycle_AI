"""
Security agent tool — input filtering with tracing and least-privilege scope.


"""

import re
import logging
from datetime import datetime

logging.basicConfig(
    filename="security_trace.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

# Each rule maps a category -> compiled regex patterns (word-boundary safe)
THREAT_PATTERNS = {
    "prompt_injection": [
        r"\bignore (all|previous|prior) instructions\b",
        r"\bignore the (system|above) prompt\b",
        r"\bdisregard (your|the) (rules|instructions)\b",
        r"\byou are now\b",
        r"\bact as (if|though)\b",
    ],
    "credential_exfiltration": [
        r"\bapi[_ -]?key\b",
        r"\bpassword\b",
        r"\bsecret[_ -]?key\b",
        r"\baccess[_ -]?token\b",
    ],
    "jailbreak_attempt": [
        r"\bsystem prompt\b",
        r"\bdeveloper mode\b",
        r"\bbypass (safety|restrictions|filters)\b",
        r"\bjailbreak\b",
    ],
}


def security_check(user_input: str) -> str:
    """
    Inspect user input for prompt injection, credential exfiltration,
    or jailbreak attempts before it reaches the agent's reasoning step.

    Returns "SAFE" or "BLOCKED: <category>" and writes a trace log
    entry for every check performed (both safe and blocked), so the
    decision is auditable.
    """
    text = user_input.lower()

    for category, patterns in THREAT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text):
                logging.info(
                    f"BLOCKED | category={category} | pattern={pattern} | input={user_input[:200]}"
                )
                return f"BLOCKED: {category}"

    logging.info(f"SAFE | input={user_input[:200]}")
    return "SAFE"