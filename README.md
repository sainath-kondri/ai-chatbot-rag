# 🤖 AI Chatbot with RAG (Retrieval-Augmented Generation)

A powerful AI chatbot that lets you **chat with your own PDF documents** using state-of-the-art NLP techniques. Upload any PDF and ask questions — the AI retrieves the most relevant context and generates accurate answers.

---

## 🚀 Live Demo

> Upload a PDF → Ask a question → Get instant AI-powered answers!

---

## 🧠 How It Works

```
PDF Documents
     ↓
Text Extraction (PyPDF2)
     ↓
Text Chunking (LangChain)
     ↓
Embeddings (HuggingFace - all-MiniLM-L6-v2)
     ↓
Vector Store (FAISS)
     ↓
User Query → Semantic Search → Relevant Chunks
     ↓
LLM (Groq - LLaMA 3) → Answer
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| 🤖 LLM | Groq API (LLaMA 3 8B) |
| 🦜 Framework | LangChain |
| 📦 Vector Store | FAISS |
| 🔤 Embeddings | HuggingFace (all-MiniLM-L6-v2) |
| 📄 PDF Parsing | PyPDF2 |
| 🌐 UI | Streamlit |
| 🐍 Language | Python 3.10+ |

---

## ✨ Features

- 📄 Upload **multiple PDF documents** at once
- 💬 **Conversational memory** — remembers previous questions
- ⚡ **Fast responses** powered by Groq's ultra-fast inference
- 🔍 **Semantic search** — finds the most relevant context
- 🎨 **Clean UI** built with Streamlit

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/sainath-kondri/ai-chatbot-rag.git
cd ai-chatbot-rag
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free Groq API key at: https://console.groq.com

### 4. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
ai-chatbot-rag/
│
├── app.py              # Main Streamlit application
├── rag_pipeline.py     # RAG logic (embeddings, vector store, LLM chain)
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed to GitHub)
├── .gitignore          # Ignores .env and other sensitive files
└── README.md           # Project documentation
```

---

## 📸 Screenshots

> Chat interface with PDF upload and AI responses

---

## 🎯 Use Cases

- 📚 Chat with research papers
- 📋 Query legal documents
- 📖 Understand textbooks
- 💼 Analyze business reports

---

## 👨‍💻 Author

**Sainath Kondri**
- 🌐 [Portfolio](https://sainath-kondri.github.io)
- 💼 [LinkedIn](https://www.linkedin.com/in/sainath-kondri-45287226a)
- 🐙 [GitHub](https://github.com/sainath-kondri)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
