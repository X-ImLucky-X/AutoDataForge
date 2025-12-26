# src/cleaning/text_cleaner.py

import re


def clean_text(text: str) -> str:
    """
    Normalize raw text by removing noise and standardizing format.

    Args:
        text (str): Raw input text.

    Returns:
        str: Cleaned and normalized text.
    """
    if not text:
        return ""

    # Convert to lowercase for consistency
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Replace multiple whitespace with single space
    text = re.sub(r"\s+", " ", text)

    # Remove excessive special characters (keep punctuation)
    text = re.sub(r"[^\w\s.,!?]", "", text)

    return text.strip()
