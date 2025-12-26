# src/pipeline.py

from pathlib import Path

from src.ingestion.text_loader import load_text_file
from src.ingestion.pdf_loader import load_pdf_file
from src.cleaning.text_cleaner import clean_text
from src.cleaning.pii_removal import mask_pii
from src.generation.summarizer import generate_summary
from src.quality.filters import is_valid_summary
from src.generation.qa_generator import generate_qa_pairs
from src.quality.qa_filters import is_valid_qa



def run_pipeline(file_path: str | Path, llm) -> list[dict]:
    """
    Run the full data preparation pipeline on a single input file.

    Args:
        file_path (str or Path): Path to input file (.txt or .pdf)
        llm: Callable language model interface

    Returns:
        list[dict]: List of validated training samples
    """
    path = Path(file_path)

    # -------- Ingestion --------
    if path.suffix.lower() == ".txt":
        raw_text = load_text_file(path)
    elif path.suffix.lower() == ".pdf":
        raw_text = load_pdf_file(path)
    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")

    # -------- Cleaning --------
    cleaned_text = clean_text(raw_text)
    cleaned_text = mask_pii(cleaned_text)

    # -------- Generation --------
    summary = generate_summary(llm, cleaned_text)
    qa_pairs = generate_qa_pairs(llm, cleaned_text)


    # -------- Quality Control --------
    samples = []

    # Summary sample
    if is_valid_summary(cleaned_text, summary):
        samples.append({
            "type": "summary",
            "document": cleaned_text,
            "summary": summary
    })

    # Q/A samples
    for qa in qa_pairs:
        if is_valid_qa(qa["question"], qa["answer"]):
            samples.append({
                "type": "qa",
                "question": qa["question"],
            "answer": qa["answer"]
        })


    return samples
