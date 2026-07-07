# ♻️ EcoCycle AI

> An AI-powered waste identification and recycling assistant built using **Google Gemini**, **ChromaDB (RAG)**, and **Streamlit**.

---

## 🌍 Overview

EcoCycle AI helps users identify waste items from an image and provides recycling guidance, material information, reuse ideas, and compostability details.

Instead of relying only on an AI model, EcoCycle AI uses **Retrieval-Augmented Generation (RAG)** with **ChromaDB** to retrieve accurate recycling knowledge before generating a response.

---

## ✨ Features

- 📷 Upload an image of a waste item
- 🤖 AI-powered image identification using Gemini Vision
- 📚 RAG-based recycling knowledge retrieval
- ♻️ Material identification
- ✅ Recycling status
- 🌱 Compostability information
- 💡 Creative reuse ideas
- 🎨 Modern Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini 2.5 Flash
- Gemini Embeddings
- ChromaDB
- Pandas
- Pillow
- python-dotenv

---

## 🏗️ Architecture

```
          User
            │
            ▼
     Streamlit UI
            │
            ▼
   Gemini Vision Model
            │
            ▼
    Waste Item Detected
            │
            ▼
 Gemini Embedding Model
            │
            ▼
        ChromaDB
            │
            ▼
 Recycling Knowledge
            │
            ▼
      Final Response
```

---

## 📂 Project Structure

```
EcoCycle_AI/
│
├── agents/
├── chroma_db/
├── data/
│   └── waste_knowledge.csv
│
├── images/
├── skills/
│   ├── identify.py
│   ├── retrieve.py
│   └── advise.py
│
├── streamlit_app.py
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/neptune-glitch/EcoCycle_AI.git
cd EcoCycle_AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the application

```bash
streamlit run streamlit_app.py
```

---

## 📸 How It Works

1. Upload an image of a waste item.
2. Gemini Vision identifies the object.
3. Gemini Embeddings convert the detected item into a vector.
4. ChromaDB retrieves the most relevant recycling knowledge.
5. EcoCycle AI displays:
   - Material
   - Recycling status
   - Compostability
   - Reuse ideas
   - Eco-friendly guidance

---

## 📚 Knowledge Base

Current supported items include:

- Plastic Bottle
- Glass Bottle
- Plastic Bag
- Banana Peel
- Tin Can
- Aluminum Can
- Cardboard
- Newspaper
- Coffee Grounds
- Egg Shell

The knowledge base can easily be expanded by updating the CSV dataset.

---

## 🔒 Security

API keys are stored securely using a `.env` file and are excluded from version control using `.gitignore`.

---

## 🌱 Future Improvements

- Live camera detection
- More waste categories
- Nearby recycling center recommendations
- Barcode scanning
- Multi-language support
- Carbon footprint estimation

---

## 📸 Screenshots

### Home Page

> <img width="1920" height="1080" alt="Screenshot (87)" src="https://github.com/user-attachments/assets/8c96b4bf-2d1a-431e-abc2-e877d8bb4623" />


### Detection Result

> <img width="1920" height="1080" alt="Screenshot (88)" src="https://github.com/user-attachments/assets/33620ee9-0675-4015-90d0-ae49bc416834" />
> <img width="1920" height="1080" alt="Screenshot (88)" src="https://github.com/user-attachments/assets/c3600551-13b7-453d-842b-adffe79c852f" />
> <img width="1920" height="1080" alt="Screenshot (89)" src="https://github.com/user-attachments/assets/75821c5e-f75b-4f2b-98d7-2d05bf668a1e" />





---

## 🌐 Live Demo

> **https://eccmsxsjdw8any4nekytyi.streamlit.app/**
---


## 🎥 Demo Video

> **https://youtu.be/GqJlkBbJzx8** 

---



## 👩‍💻 Author

**Bharti Pathak**

Built with ❤️ using Google Gemini, ChromaDB, and Streamlit.

---

## 📄 License

This project is licensed under the MIT License.
