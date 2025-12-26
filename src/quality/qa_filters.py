# src/quality/qa_filters.py

from src.quality.qa_scorer import score_qa_pair
from src.config import QUALITY_THRESHOLD


def is_valid_qa(question: str, answer: str) -> bool:
    return score_qa_pair(question, answer) >= QUALITY_THRESHOLD
