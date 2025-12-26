# src/quality/qa_scorer.py

def score_qa_pair(question: str, answer: str) -> float:
    """
    Score a Q/A pair using simple heuristics.

    Returns:
        float: score between 0 and 1
    """
    if not question or not answer:
        return 0.0

    q_len = len(question.split())
    a_len = len(answer.split())

    if q_len < 3 or a_len < 5:
        return 0.3

    if question.lower() == answer.lower():
        return 0.0

    return 0.8
