# src/cleaning/pii_removal.py

import re


def mask_pii(text: str) -> str:
    """
    Mask basic PII such as email addresses and phone numbers.

    Args:
        text (str): Input text.

    Returns:
        str: Text with PII masked.
    """
    if not text:
        return ""

    # Mask email addresses
    text = re.sub(
        r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
        "[EMAIL]",
        text
    )

    # Mask phone numbers (simple patterns)
    text = re.sub(
        r"\b\d{10}\b",
        "[PHONE]",
        text
    )

    return text
