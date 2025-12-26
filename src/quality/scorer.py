# src/quality/scorer.py

def score_summary(document: str, summary: str) -> float:
    """
    Score the quality of a summary based on simple heuristics.

    Args:
        document (str): Original document text.
        summary (str): Generated summary.

    Returns:
        float: Quality score between 0 and 1.
    """
    if not document or not summary:
        return 0.0

    doc_len = len(document.split())
    sum_len = len(summary.split())

    # 1. Presence score
    presence_score = 1.0 if sum_len > 0 else 0.0

    # 2. Length sanity score
    if sum_len < 10:
        length_score = 0.2
    elif sum_len > doc_len:
        length_score = 0.2
    else:
        length_score = 1.0

    # 3. Compression score
    compression_ratio = sum_len / max(doc_len, 1)
    compression_score = 1.0 - compression_ratio
    compression_score = max(0.0, min(1.0, compression_score))

    # Final score
    final_score = (presence_score + length_score + compression_score) / 3

    return round(final_score, 3)
