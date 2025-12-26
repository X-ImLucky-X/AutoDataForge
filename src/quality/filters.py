# src/quality/filters.py

from src.quality.scorer import score_summary
from src.config import QUALITY_THRESHOLD


def is_valid_summary(document: str, summary: str) -> bool:
    """
    Determine whether a summary meets the quality threshold.

    Args:
        document (str): Original document text.
        summary (str): Generated summary.

    Returns:
        bool: True if summary is valid, False otherwise.
    """
    score = score_summary(document, summary)
    return score >= QUALITY_THRESHOLD
