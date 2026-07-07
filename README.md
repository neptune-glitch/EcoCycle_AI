# ♻️ EcoCycle AI

> An AI agent for waste identification and reuse-hack generation, built using **Google ADK**, **Gemini 2.5 Flash**, **ChromaDB (RAG)**, and **Streamlit**.

---

## 🌍 Overview

EcoCycle AI helps users identify waste items from a photo and generates an AI-written recycling and reuse plan — material type, recyclability, compostability, and creative reuse ideas.

Instead of a single model call, EcoCycle AI is built as an **agent pipeline**: an image-identification step, a **Retrieval-Augmented Generation (RAG)** step grounded in a ChromaDB knowledge base, a **security check** step, and a final generation step — orchestrated with **Google's Agent Development Kit (ADK)**.

---

## ✨ Features

- 📷 Upload an image of a waste item
- 🤖 AI-powered image identification using Gemini Vision
- 📚 RAG-based recycling knowledge retrieval (grounded, not hallucinated)
- 🔒 Security-agent input filtering (prompt injection / credential exfiltration defense, with tracing)
- ♻️ Material identification
- ✅ Recycling status
- 🌱 Compostability information
- 💡 AI-generated creative reuse ideas
- 🎨 Modern Streamlit interface, deployed live

---

## 🛠️ Tech Stack

- Python
- Streamlit
- **Google ADK** (Agent Development Kit)
- Google Gemini 2.5 Flash (vision + generation)
- Gemini Embeddings
- ChromaDB
- Pandas
- Pillow
- python-dotenv

---

## 🏗️ Architecture
