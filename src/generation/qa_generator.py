# src/generation/qa_generator.py

def generate_qa_pairs(llm, text: str, num_pairs: int = 3) -> list[dict]:
    """
    Generate question-answer pairs from cleaned text using an LLM.

    Args:
        llm: Callable LLM interface
        text (str): Cleaned input text
        num_pairs (int): Number of Q/A pairs to generate

    Returns:
        list[dict]: List of {"question": ..., "answer": ...}
    """
    if not text:
        return []

    prompt = (
        f"Generate exactly {num_pairs} high-quality question-answer pairs "
        "from the text below. The questions should be clear and useful for a chatbot. "
        "Return the output in the following format:\n\n"
        "Q: <question>\nA: <answer>\n\n"
        "TEXT:\n"
        f"{text}"
    )

    response = llm(prompt)

    if not response:
        return []

    qa_pairs = []
    current_q = None

    for line in response.splitlines():
        line = line.strip()
        if line.startswith("Q:"):
            current_q = line[2:].strip()
        elif line.startswith("A:") and current_q:
            qa_pairs.append({
                "question": current_q,
                "answer": line[2:].strip()
            })
            current_q = None

    return qa_pairs
