# 🤖 Multimodal AI Chatbot

A full-stack **multimodal AI chatbot** built with FastAPI that supports **text, voice, and image interactions**. This project integrates advanced AI capabilities including speech recognition, text-to-speech, image understanding, multilingual translation, and conversational memory.

---

## 🚀 Features

* 💬 **Conversational AI** – Natural language responses using OpenAI LLM
* 🎤 **Speech-to-Text** – Convert voice input into text (Whisper)
* 🔊 **Text-to-Speech** – AI-generated voice responses
* 🖼️ **Image Understanding** – Upload images and ask questions about them
* 🌍 **Multilingual Support** – English, Bengali, Finnish (auto-detection + translation)
* 🧠 **Conversation Memory** – Stores and recalls chat history
* ⚡ **FastAPI Backend** – High-performance API system
* 🌐 **Web Interface** – Interactive frontend (HTML/CSS/JS)

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python)
* **AI Models:** OpenAI API (GPT-4o-mini)
* **Speech:** Whisper (STT), TTS engine
* **Translation:** Custom translation module
* **Frontend:** HTML, CSS, JavaScript
* **Other:** dotenv, file handling, REST APIs

---

## 📂 Project Structure

```
Chatbot/
│── chatbot/
│   ├── llm.py
│   ├── speech.py
│   ├── translate.py
│   ├── vision.py
│   ├── memory.py
│
│── static/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│
│── main.py
│── .env (not included)
│── .gitignore
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/ahakim7/AI-Chatbot.git
cd AI-Chatbot
```

---

### 2️⃣ Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate   (Windows)
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Set environment variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the application

```
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🎮 How to Use

* 💬 Type messages to chat with the AI
* 🎤 Use voice input for speech interaction
* 🖼️ Upload images and ask questions
* 🌍 Chat in multiple languages

---

## 🔐 Security

* API keys are stored securely using `.env`
* `.env` is excluded from version control via `.gitignore`

---

## 🎯 Future Improvements

* 🌍 Deploy to cloud (Render / Railway)
* ⚡ Streaming responses (real-time typing)
* 🧠 Vector database (RAG memory)
* 🎨 Modern frontend (React)
* 📱 Mobile-friendly UI

---

## 👨‍💻 Author

**Mohammad Azijul Hakim**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
