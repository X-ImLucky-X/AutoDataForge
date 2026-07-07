# 🚀 AutoDataForge

> **AI-Powered Training Data Preparation System**

AutoDataForge is an end-to-end AI data engineering pipeline that transforms raw, unstructured documents into **clean, privacy-safe, high-quality training datasets** for Large Language Models (LLMs) and other NLP applications.

Designed with a modular architecture, the system automates every stage of dataset preparation—from document ingestion and text cleaning to AI-powered summarization and quality validation—producing model-ready **JSONL** datasets.

---

## ✨ Features

- 📄 Ingests both **TXT** and **PDF** documents
- 🧹 Cleans and normalizes raw text
- 🔒 Automatically masks Personally Identifiable Information (PII)
  - Email addresses
  - Phone numbers
- 🤖 Generates summaries using Large Language Models
- 📊 Scores and filters low-quality outputs
- 📦 Exports training-ready **JSONL** datasets
- 🏗️ Modular, extensible pipeline architecture

---

## 🧠 System Architecture

```text
          Raw Documents
         (.txt / .pdf)
                │
                ▼
        Document Ingestion
                │
                ▼
      Text Cleaning & Parsing
                │
                ▼
         PII Detection & Masking
                │
                ▼
       LLM Summary Generation
                │
                ▼
      Quality Evaluation & Filtering
                │
                ▼
      Training Dataset (JSONL)
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.11** | Core programming language |
| **PyMuPDF** | PDF parsing and extraction |
| **Regex** | Text cleaning & PII detection |
| **OpenAI / Local LLMs** | Summary generation |
| **JSONL** | Dataset export format |

---

## 📂 Project Structure

```text
AutoDataForge/
│
├── data/
│   ├── raw/                 # Input documents
│   └── processed/           # Generated datasets
│
├── src/
│   ├── ingestion/           # Document loading
│   ├── cleaning/            # Text normalization
│   ├── generation/          # LLM summarization
│   ├── quality/             # Quality scoring
│   └── pipeline.py          # Main orchestration pipeline
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/X-ImLucky-X/AutoDataForge.git
```

### 2. Navigate to the project

```bash
cd AutoDataForge
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Place your input documents inside:

```text
data/raw/
```

Run the pipeline:

```bash
python src/pipeline.py
```

Processed datasets will be generated inside:

```text
data/processed/
```

---

## 📤 Output Format

The pipeline exports datasets in **JSON Lines (JSONL)** format, making them suitable for LLM fine-tuning and other NLP workflows.

Example:

```json
{
    "document": "Cleaned document text...",
    "summary": "Generated summary..."
}
```

Each line represents one training sample.

---

## 🔑 Pipeline Workflow

1. 📥 Read raw documents
2. 🧹 Normalize and clean extracted text
3. 🔒 Detect and mask sensitive information
4. 🤖 Generate summaries using an LLM
5. 📈 Evaluate output quality
6. 💾 Export validated examples as JSONL

---

## 🎯 Use Cases

- LLM Fine-tuning
- Text Summarization
- Retrieval-Augmented Generation (RAG)
- Dataset Curation
- AI Data Engineering
- NLP Research
- Chatbot Training

---

## 🌟 Key Highlights

- Modular architecture for easy extension
- Deterministic preprocessing pipeline
- Privacy-aware dataset generation
- Quality gating for AI-generated outputs
- Production-ready project structure
- Easily adaptable to different LLM providers

---

## 🔮 Future Improvements

- Multi-language support
- OCR for scanned PDFs
- Named Entity Recognition (NER)
- Duplicate document detection
- Human-in-the-loop review
- Web dashboard for pipeline monitoring
- Batch processing with parallel execution
- Support for additional output formats (CSV, Parquet)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐** on GitHub.

Your support helps improve the project and makes it easier for others to discover.
