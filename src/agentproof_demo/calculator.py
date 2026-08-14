def classify_number(value: int) -> str:
    """Return a stable category for a signed integer."""
    if value < 0:
        return "negative"
    if value == 0:
        return "zero"
    return "positive"
