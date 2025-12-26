
# 🚀 AutoDataForge  
**AI-Powered Training Data Preparation System**

AutoDataForge is a modular, end-to-end AI system that transforms raw documents into **high-quality, model-ready training datasets** for tasks such as **text summarization** and **chatbot development**.

---

## 📌 Problem Statement

Training modern AI models requires **large amounts of clean, structured data**. Real-world data is unstructured, noisy, and often contains sensitive information—unsuitable for direct training.

**AutoDataForge solves this** by automating the pipeline from raw text to validated datasets.

---

## 🎯 Features

✔ Ingests `.txt` and `.pdf` documents  
✔ Cleans and normalizes text deterministically  
✔ Masks PII (emails, phone numbers)  
✔ Generates summaries via LLM  
✔ Scores and filters outputs  
✔ Exports training-ready JSONL datasets  

---

## 🧠 Architecture

```
Raw Document → Ingestion → Cleaning → PII Masking → 
LLM Generation → Quality Scoring → JSONL Dataset
```

---

## 📂 Project Structure

```
AutoDataForge/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── ingestion/
│   ├── cleaning/
│   ├── generation/
│   ├── quality/
│   └── pipeline.py
├── requirements.txt
└── README.md
```

---

## 📤 Output Format

Produces **JSON Lines** for LLM training:

```json
{
    "document": "cleaned text...",
    "summary": "generated summary..."
}
```

---

## 🛠️ Tech Stack

- Python 3.11
- PyMuPDF (PDF processing)
- LLM integration (OpenAI, local models)
- JSONL format

---

## 🔑 Key Highlights

- Clean separation of concerns
- Deterministic preprocessing
- Quality gating for AI outputs
- Privacy-aware design
- Production-ready architecture
