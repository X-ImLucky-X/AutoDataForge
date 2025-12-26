# src/utils/dataset_writer.py

import json
from pathlib import Path


def write_jsonl(samples: list[dict], output_path: str | Path) -> None:
    """
    Write training samples to a JSONL file.

    Args:
        samples (list[dict]): List of training samples.
        output_path (str or Path): Destination file path.

    Returns:
        None
    """
    if not samples:
        return

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as f:
        for sample in samples:
            f.write(json.dumps(sample, ensure_ascii=False) + "\n")
