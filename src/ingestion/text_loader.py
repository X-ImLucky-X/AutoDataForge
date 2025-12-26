# src/ingestion/text_loader.py

from pathlib import Path


def load_text_file(file_path: str | Path) -> str:
    """
    Load a .txt file and return its contents as a string.

    Args:
        file_path (str or Path): Path to the text file.

    Returns:
        str: File contents as a single string.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a .txt file.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".txt":
        raise ValueError(f"Unsupported file type: {path.suffix}")

    with path.open("r", encoding="utf-8") as f:
        return f.read()
