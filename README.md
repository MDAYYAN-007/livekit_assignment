# PitchSense – AI Startup Pitch Mentor

PitchSense is a memory-driven AI mentor that helps founders refine and evaluate their startup pitches.

It uses:

* Retrieval-Augmented Generation (RAG)
* Persistent session memory
* Groq-hosted LLaMA model
* FAISS vector search
* PDF export tool
* Optional LiveKit real-time deployment

The system behaves like a structured startup accelerator mentor instead of a generic chatbot.

---

## Features

* Stateful pitch refinement (remembers previous context)
* Stage-based mentoring (discovery → strategy → evaluation)
* RAG-based grounding using pitch framework PDFs
* Structured JSON output control
* Export pitch evaluation as downloadable PDF
* Can run in CLI mode or LiveKit agent mode

---

## Tech Stack

* Python
* LangChain
* Groq (LLaMA 3.3 70B)
* FAISS (vector similarity search)
* HuggingFace Sentence Transformers
* ReportLab (PDF generation)
* LiveKit (real-time agent)

---

# Setup Instructions

## 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

## 2. Install Dependencies

```bash
pip install \
langchain \
langchain-groq \
langchain-community \
langchain-text-splitters \
langchain-huggingface \
sentence-transformers \
faiss-cpu \
reportlab \
livekit-agents \
livekit \
groq
```

---

## 3. Build the Vector Index (Important)

Place your pitch framework PDFs inside:

```
data/pitch_docs/
```

Then run:

```bash
python retrieval/build_index.py
```

This will:

* Load PDFs
* Chunk documents
* Create embeddings
* Build FAISS index
* Save it locally

You only need to do this once (unless you change PDFs).

---

# How to Run

You can run this project in two ways.

---

# Option 1 – CLI Mode (Recommended for Testing)

Run:

```bash
python cli_chat.py
```

You can now interact in the terminal:

```
You: I am building a SaaS for grocery stores...
```

Type:

```
exit
```

to stop.

This mode:

* Uses memory
* Uses RAG
* Can generate PDF reports
* Runs fully locally

---

# Option 2 – LiveKit Agent Mode (Real-Time)

This deploys PitchSense as a LiveKit agent.

## Step 1 – Add LiveKit Credentials

Edit `generate_token.py`:

```python
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
```

---

## Step 2 – Start Worker

```bash
python agent.py start
```

---

## Step 3 – Generate Token

```bash
python generate_token.py
```

Copy the generated JWT token.

---

## Step 4 – Join Room

Use the token in a LiveKit frontend or UI.

Agent name must match:

```
pitchsense-agent
```

Now the AI mentor will respond in real-time.

---

# Project Structure

```
core/               → Engine + Prompt logic
memory/             → Session persistence (JSON)
retrieval/          → RAG + FAISS index
tools/              → PDF export tool
cli_chat.py         → Terminal interface
agent.py            → LiveKit deployment
generate_token.py   → LiveKit token generator
```

---

# How It Works Internally

1. User sends message
2. Memory is loaded
3. Relevant framework content retrieved via FAISS
4. Prompt constructed
5. Groq LLaMA model called
6. Structured JSON returned
7. Memory updated
8. Optional PDF generated

---

# Notes

* First run may consume high memory due to embedding model loading.
* If running LiveKit mode on low RAM, reduce worker processes.
* Keep embedding model consistent when rebuilding index.

---

# Why This Project?

This project was built to explore:

* Structured AI systems
* Memory-driven agents
* RAG architecture
* Tool calling
* Real-time AI deployment

It is more than a simple chatbot, it behaves like a guided startup mentor.

---
