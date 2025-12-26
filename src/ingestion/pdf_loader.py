# src/ingestion/pdf_loader.py

from pathlib import Path
import fitz  # PyMuPDF


def load_pdf_file(file_path: str | Path) -> str:
    """
    Load a PDF file and extract its text content.

    Args:
        file_path (str or Path): Path to the PDF file.

    Returns:
        str: Extracted text as a single string.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a PDF.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Unsupported file type: {path.suffix}")

    text_chunks = []

    with fitz.open(path) as doc:
        for page in doc:
            page_text = page.get_text()
            if page_text:
                text_chunks.append(page_text)

    return "\n".join(text_chunks)
