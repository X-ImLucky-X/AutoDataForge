# src/generation/summarizer.py

def generate_summary(llm, text: str) -> str:
    """
    Generate a concise summary from cleaned text using an LLM.

    Args:
        llm: A callable LLM interface that accepts a prompt and returns text.
        text (str): Cleaned input text.

    Returns:
        str: Generated summary.
    """
    if not text:
        return ""

    prompt = (
        "Summarize the following text in 3 to 5 clear, factual sentences. "
        "Do not add opinions or new information.\n\n"
        f"{text}"
    )

    summary = llm(prompt)

    if not summary:
        return ""

    return summary.strip()
