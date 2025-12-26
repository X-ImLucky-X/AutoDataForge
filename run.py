# run.py
"""Entry point to execute the AutoDataForge pipeline on all files in data/raw.
Includes diagnostic output when samples are filtered out by quality control.
"""
import pathlib
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from src.pipeline import run_pipeline
from src.llm_groq import real_llm
from src.quality.scorer import score_summary
from src.cleaning.text_cleaner import clean_text
from src.cleaning.pii_removal import mask_pii
from src.generation.summarizer import generate_summary
from src.utils.dataset_writer import write_jsonl

OUTPUT_FILE = "data/processed/summarization_dataset.jsonl"

def process_file(file_path):
    print(f"\n>>> Processing: {file_path.name}")
    try:
        samples = run_pipeline(file_path, real_llm)

        if samples:
            write_jsonl(samples, OUTPUT_FILE)

            for i, s in enumerate(samples, 1):
                print(f"  [PASSED] Sample {i}")
                if s.get("type") == "summary":
                    print(f"  Summary: {s['summary']}")
                elif s.get("type") == "qa":
                    print(f"  Q: {s['question']}")
                    print(f"  A: {s['answer']}")

        else:
            print("  [FILTERED] No valid samples generated.")
            with open(file_path, "r", encoding="utf-8") as f:
                raw = f.read()
            cleaned = mask_pii(clean_text(raw))
            sum_text = generate_summary(real_llm, cleaned)
            score = score_summary(cleaned, sum_text)
            print(f"  Debug Score: {score:.3f} (Threshold: 0.5)")
            print(f"  Generated Summary: {sum_text}")

    except Exception as e:
        print(f"  [ERROR] {e}")


def main():
    project_root = pathlib.Path(__file__).resolve().parent
    raw_dir = project_root / "data" / "raw"
    
    if not raw_dir.exists():
        print(f"Error: Directory {raw_dir} not found.")
        return

    files = list(raw_dir.glob("*.txt")) + list(raw_dir.glob("*.pdf"))
    
    if not files:
        print(f"No .txt or .pdf files found in {raw_dir}")
        return

    print(f"Found {len(files)} file(s). Running pipeline...")
    for f in files:
        process_file(f)

if __name__ == "__main__":
    main()
