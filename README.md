# 📄 Legal Policy Document Analyzer — Enterprise RAG Backend

This project is a **production-style Retrieval-Augmented Generation (RAG) backend** designed to make legal and policy documents easier to explore and understand. Instead of sending entire documents to an AI model, the system retrieves only the most relevant sections and generates grounded answers with clear source citations.

The goal of this project is to demonstrate how **enterprise AI backends** are actually built — focusing on privacy, explainability, and clean backend architecture rather than just basic chatbot functionality.

---

# 🚀 What This Project Does

Working with long policy documents can be slow and confusing. This backend solves that by allowing users to:

* 📂 Upload legal or policy PDF files
* 🤖 Ask natural-language questions about the content
* 🔎 Get answers grounded in real document context
* 📑 See page-level citations for transparency
* 🔐 Keep all AI processing local using Ollama (no external APIs)

Instead of hallucinating answers, the system retrieves relevant document chunks first and uses them to guide the AI response.

---

# 🏗️ How It Works (High-Level Architecture)

```
FastAPI API Layer
        ↓
RAG Service Layer
        ↓
Retriever (FAISS Vector Store)
        ↓
Grounded Prompt Chain
        ↓
Local LLM (Ollama)
```

**Flow explained simply:**

1. A user uploads a PDF policy.
2. The document is split into smaller chunks and converted into embeddings.
3. When a question is asked, only relevant chunks are retrieved.
4. These chunks are passed into a grounded prompt.
5. The local LLM generates a contextual, explainable answer.

---

# 🛠️ Tech Stack

## Backend

* FastAPI
* Python

## AI / RAG Layer

* LangChain
* Ollama (llama3 — local LLM)
* FAISS Vector Database

## DevOps / Deployment

* Docker
* Docker Compose

This stack reflects a **real-world enterprise AI backend**, not just a prototype script.

---

# 📁 Project Structure

```
app/
 ├── api/            # FastAPI routes (upload + ask endpoints)
 ├── services/       # Business logic & RAG orchestration
 ├── rag/            # Loader, splitter, retriever, prompt chain
 ├── models/         # LLM + embedding adapters
main.py
Dockerfile
docker-compose.yml
```

The folder structure separates concerns clearly, making the project easier to scale or extend later.

---

# ⚙️ Getting Started

## ✅ Requirements

Before running the project, make sure you have:

* Docker Desktop installed
* Ollama installed locally

Start Ollama:

```
ollama serve
```

---

# 🐳 Running with Docker (Recommended)

Start everything with one command:

```
docker compose up --build
```

Once running, open:

```
http://localhost:8000/docs
```

This opens the interactive FastAPI Swagger UI where you can test endpoints.

---

# 📂 Uploading a Policy Document

Endpoint:

```
POST /upload-policy
```

Upload any `.pdf` file containing legal or policy content.
The backend will automatically process and index the document for semantic search.

---

# ❓ Asking Questions

Endpoint:

```
POST /ask-policy
```

Example:

```
What happens if someone violates the policy?
```

Response format:

* `answer` → AI-generated grounded response
* `sources` → Page numbers used for the answer

This makes responses explainable instead of opaque.

---

# 🔐 Privacy & Security Design

This project follows a **privacy-first AI architecture**, which is especially important for legal documents:

* ✅ Runs entirely on a local LLM (Ollama)
* ✅ No external API calls or data sharing
* ✅ Only retrieved document chunks are sent to the model
* ✅ Environment variables for configuration
* ✅ Sensitive files excluded via `.gitignore` and `.dockerignore`
* ✅ Prompt grounding to reduce hallucinations and injection risks

---

# 🧪 Running Without Docker (Local Development)

If you prefer running locally:

Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start the server:

```
uvicorn main:app --reload
```

---

# 📦 Useful Docker Commands

Start containers:

```
docker compose up -d
```

Stop containers:

```
docker compose down
```

Rebuild after code changes:

```
docker compose up --build
```

---

# 🌱 Future Improvements

Some planned enhancements:

* Streaming LLM responses
* Persistent vector storage
* Multi-document indexing
* Authentication & access control
* Non-root Docker security hardening

---

# 👨‍💻 Why This Project Exists

Most tutorials stop at simple chatbots. This project goes further by showing how to design a **realistic AI backend** with:

* Proper RAG architecture
* Clean service-layer separation
* Privacy-focused AI workflows
* Containerized deployment

It’s built to reflect how enterprise AI systems are structured behind the scenes — making it both a learning project and a strong portfolio piece.
