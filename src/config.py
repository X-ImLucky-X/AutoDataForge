# src/config.py

from pathlib import Path

# -------------------------
# Base Project Paths
# -------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
CLEANED_DATA_DIR = DATA_DIR / "cleaned"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# -------------------------
# Generation Settings
# -------------------------

# Number of QA pairs to generate per document
NUM_QA_PAIRS = 3

# -------------------------
# Quality Control Settings
# -------------------------

# Minimum acceptable quality score (0 to 1)
QUALITY_THRESHOLD = 0.5
