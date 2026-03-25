# 🔍 Research Assistant Agent

An intelligent AI-powered research assistant built using LangChain that can search the web, read PDFs, and perform calculations to answer complex queries.

---

## 🚀 Features

* 🌐 **Web Search Tool** – Fetches real-time information using DuckDuckGo
* 📄 **PDF Reader** – Extracts and summarizes content from PDF files
* 🧮 **Calculator Tool** – Performs basic mathematical computations
* 🤖 **Agent-Based Reasoning** – Uses LangChain agents to decide which tool to use
* 💬 **Interactive CLI** – Ask questions in real-time

---

## 🛠️ Tech Stack

* Python
* LangChain
* OpenAI API
* DuckDuckGo Search
* PyPDFLoader

---

## 📂 Project Structure

```
ResearchAssistantAgent/
│── ResearchAssistant.py   # Main agent script
│── .env                   # API keys (not pushed)
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Dhiti-Wadhwa/ResearchAssistantAgent.git
cd ResearchAssistantAgent
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python ResearchAssistant.py
```

---

## 💡 Example Usage

```
Ask something: What is Formula Student?
Ask something: Summarize this PDF (provide file path)
Ask something: 25 * 67
```

---

## 🧠 How It Works

The agent uses LangChain’s `create_agent` to:

1. Understand the user query
2. Decide which tool to use
3. Execute the tool
4. Return the final answer

---

## 🚧 Future Improvements

* Add memory for conversation context
* Integrate advanced search APIs (SerpAPI, Tavily)
* Build a web interface (Streamlit / React)
* Add document-based Q&A with embeddings

---

## 🙌 Acknowledgements

* LangChain
* OpenAI
* DuckDuckGo

---

## 📌 Author

**Dhiti Wadhwa**
**Daksh Mishra**
**Dishita Runwal**

---
# ResearchAssistantAgent
