```markdown
# 🌍 Migrants Rights Guidance Platform

A privacy-focused, local Retrieval-Augmented Generation (RAG) system that provides accurate answers about migrants' rights and asylum procedures using official legal documents as the knowledge source. The entire system runs on your laptop using open-source tools—no cloud APIs, no data leaks.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## ✨ Features

- 🔒 **100% Local & Private**: All documents, embeddings, and LLM inference run entirely on your machine
- 📚 **Multi-Document Support**: Index multiple legal PDFs simultaneously (Dublin Regulation, national guidelines, etc.)
- 🎯 **Domain-Specific**: Fine-tuned prompts for legal and migration-specific queries
- 🔄 **Complete RAG Pipeline**: From PDF ingestion to context-aware answer generation
- 💬 **Dual Interface**: CLI for quick queries, Streamlit web UI for interactive sessions
- 📖 **Source Attribution**: Track which document each answer comes from

## 🏗️ Architecture

### Indexing Pipeline (Offline)
```
PDFs → Text Extraction → Chunking → Embeddings → Vector Store
```

1. Load PDFs from `data/` directory
2. Extract and split text into overlapping chunks
3. Generate embeddings using Sentence-Transformers
4. Store in persistent ChromaDB collection

### Query Pipeline (Online)
```
Question → Embedding → Similarity Search → Context Retrieval → LLM Generation → Answer
```

1. Embed user question with same model
2. Retrieve top-k most relevant chunks
3. Build legal-focused prompt with retrieved context
4. Generate grounded answer via Llama 3
5. Return answer with source attribution

## 📋 Prerequisites

- Python 3.8 or higher
- 8GB+ RAM recommended
- Ollama installed on your system

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/migrants-rights-guidance-platform.git
cd migrants-rights-guidance-platform
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv .venv

# Activate on macOS/Linux
source .venv/bin/activate

# Activate on Windows
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```txt
langchain>=0.1.0
langchain-community>=0.0.10
chromadb>=0.4.0
sentence-transformers>=2.2.0
pypdf>=3.17.0
streamlit>=1.29.0
ollama>=0.1.0
```

### 4. Install Ollama and Download Model

```bash
# Install Ollama from https://ollama.ai

# Pull Llama 3 model
ollama pull llama3

# Verify installation
ollama run llama3
```

### 5. Add Your Documents

Place your legal PDFs in the `data/` directory:

```
data/
├── DUBLIN_REGULATIONS.pdf
├── asylum_procedures_guide.pdf
└── migrants_rights_handbook.pdf
```

### 6. Index Your Documents

```bash
python index_pdfs.py
```

This creates the vector database in `db/` directory (one-time setup, re-run when PDFs change).

## 💻 Usage

### Command Line Interface

```bash
python query_cli.py
```

**Example:**
```
Your question (or 'exit'): Who determines which country handles my asylum application?

Answer:
Under the Dublin Regulation, the responsibility for examining an asylum 
application is determined by a hierarchy of criteria. The primary factors 
include family unity, recent visa or residence permits, and irregular entry 
points. The country where you first entered the EU or where your fingerprints 
were taken is often responsible.

Source: DUBLIN_REGULATIONS.pdf

Your question (or 'exit'): 
```

### Web Interface

```bash
streamlit run app.py
```

Open your browser to `http://localhost:8501`

The web UI provides:
- Chat-style conversation interface
- Conversation history within session
- Visual source attribution
- Easy copy/paste of answers

## 📂 Project Structure

```
.
├── app.py                 # Streamlit web interface
├── index_pdfs.py          # Document indexing script
├── query_cli.py           # CLI query interface
├── dublin_rag.py          # Core RAG logic and utilities
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── data/                  # Input PDFs (not tracked in git)
│   ├── DUBLIN_REGULATIONS.pdf
│   └── other_documents.pdf
└── db/                    # ChromaDB storage (generated)
    └── chroma.sqlite3
```

## 🔍 Example Questions

Try asking questions like:

- "Which country is responsible for examining my asylum application under the Dublin rules?"
- "What happens if my fingerprints were taken in another EU country?"
- "How are family members treated in the Dublin procedure?"
- "Are there special rules for unaccompanied minors?"
- "Can I appeal a Dublin transfer decision?"
- "What are my rights during the Dublin procedure?"

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **LLM** | Llama 3 (via Ollama) |
| **Orchestration** | LangChain |
| **Vector Database** | ChromaDB |
| **Embeddings** | Sentence-Transformers (all-MiniLM-L6-v2) |
| **PDF Processing** | PyPDF / LangChain PyPDFLoader |
| **Web UI** | Streamlit |
| **CLI** | Python argparse |

## 🔧 Configuration

You can customize the RAG system by modifying parameters in `dublin_rag.py`:

```python
# Embedding model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Chunk settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval settings
TOP_K = 5

# LLM settings
MODEL_NAME = "llama3"
TEMPERATURE = 0.1
```

## 🐛 Troubleshooting

### Ollama Connection Issues
```bash
# Check if Ollama is running
ollama list

# Restart Ollama service
ollama serve
```

### ChromaDB Errors
```bash
# Clear and rebuild the database
rm -rf db/
python index_pdfs.py
```

### Memory Issues
- Reduce `CHUNK_SIZE` in configuration
- Use a smaller embedding model
- Reduce `TOP_K` retrieval parameter

## 🌱 Future Enhancements

- [ ] Multilingual support (German, French, Arabic)
- [ ] Article-level citations with PDF page numbers
- [ ] Extend to broader EU and national migration law
- [ ] Authentication for NGOs and caseworkers
- [ ] Conversation memory and follow-up questions
- [ ] Export chat history to PDF
- [ ] Integration with official government databases
- [ ] Mobile-responsive web interface

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Areas for Contribution
- Improving prompt engineering for better legal responses
- Adding more document collections and sources
- Enhancing UI/UX design
- Adding evaluation metrics for answer quality
- Writing tests and documentation
- Translating interface to multiple languages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Legal Disclaimer

This tool is for informational purposes only and does not constitute legal advice. Users should consult with qualified legal professionals for specific legal guidance regarding asylum and migration matters.

## 🙏 Acknowledgments

- Built with [LangChain](https://github.com/langchain-ai/langchain)
- Powered by [Ollama](https://ollama.ai) and [Llama 3](https://ai.meta.com/llama/)
- Vector storage by [ChromaDB](https://www.trychroma.com/)
- Embeddings from [Sentence-Transformers](https://www.sbert.net/)

## 📧 Contact

For questions, suggestions, or collaboration opportunities, please open an issue or reach out via sher29.dev@gmail.com.

---

**⭐ If you find this project helpful, please consider giving it a star!**
```

Just copy everything above and paste it directly into your GitHub README.md file. The formatting will render perfectly on GitHub!
