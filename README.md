# 🤖 Multimodal AI Chatbot (Live)

🚀 **Live Demo:**
https://ai-chatbot-ney5.onrender.com/

---

## 📌 Overview

This is a **full-stack AI chatbot** deployed on the cloud, capable of handling natural conversations with multilingual support and contextual memory.

The project demonstrates real-world AI integration, backend development, and deployment practices.

---

## 🚀 Features

* 💬 Conversational AI using OpenAI (GPT-4o-mini)
* 🌍 Multilingual support (English, Bengali, Finnish)
* 🧠 Context-aware chat with memory optimization
* ⚡ FastAPI backend
* 🌐 Live deployment on Render
* 🔐 Secure API key handling using environment variables

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python)
* **AI Model:** OpenAI API
* **Frontend:** HTML, CSS, JavaScript
* **Deployment:** Render
* **Other:** dotenv, langdetect, deep-translator

---

## 📂 Project Structure

```
Chatbot/
│── chatbot/
│   ├── llm.py
│   ├── translate.py
│   ├── memory.py
│
│── static/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│
│── main.py
│── requirements.txt
│── .gitignore
│── README.md
```

---

## ⚙️ Setup (Local)

### 1. Clone the repo

```
git clone https://github.com/ahakim7/AI-Chatbot.git
cd AI-Chatbot
```

---

### 2. Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Add environment variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5. Run the app

```
uvicorn main:app --reload
```

---

## 🌍 Deployment

This project is deployed on Render using:

* Build Command:

```
pip install -r requirements.txt
```

* Start Command:

```
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## 🔐 Security

* API keys are stored securely using environment variables
* `.env` is excluded via `.gitignore`

---

## 🎯 Key Learnings

* Handling API authentication errors
* Debugging backend systems
* Managing dependencies for cloud deployment
* Optimizing chatbot memory and performance

---

## 🚀 Future Improvements

* 🎤 Voice interaction (cloud-compatible)
* 🖼️ Image understanding (optimized deployment)
* ⚡ Streaming responses (real-time typing)
* 🎨 Improved UI/UX

---

## 👨‍💻 Author

**Mohammad Azijul Hakim**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
