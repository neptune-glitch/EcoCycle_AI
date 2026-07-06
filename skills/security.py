def security_check(user_input: str) -> str:
    """
    Basic security filter.
    """

    blocked = [
        "ignore previous",
        "system prompt",
        "api key",
        "password",
        "secret",
        "hack",
        "bypass",
    ]

    text = user_input.lower()

    for word in blocked:
        if word in text:
            return "BLOCKED"

    return "SAFE"