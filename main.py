import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from chatbot.llm import chat
from chatbot.translate import detect_lang, translate_to_en, translate_back
from chatbot.memory import load_memory, save_memory

app = FastAPI()

# Serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load memory
messages = load_memory()

# System prompt
SYSTEM = {
    "role": "system",
    "content": "Always reply in the same language as the user. Default to English if unclear."
}

# Ensure system message exists once
if not messages or messages[0]["role"] != "system":
    messages.insert(0, SYSTEM)


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/chat")
def chat_api(user_input: str):
    global messages

    try:
        print("✅ USER INPUT:", user_input)

        # Detect language
        lang = detect_lang(user_input)
        print("🌍 DETECTED LANG:", lang)

        # Translate to English
        text_en = translate_to_en(user_input, lang)
        print("🔤 TRANSLATED:", text_en)

        # Add user message
        messages.append({"role": "user", "content": text_en})

        # 🔥 LIMIT MEMORY HERE
        messages = messages[-10:]

        # Get AI response
        reply = chat(messages)
        print("🤖 RAW REPLY:", reply)

        # Save response
        messages.append({"role": "assistant", "content": reply})
        save_memory(messages)

        # Translate back if needed
        final = reply if lang == "en" else translate_back(reply, lang)

        print("✅ FINAL:", final)

        return {"response": final}

    except Exception as e:
        print("🔥 ERROR:", e)
        return {"response": "❌ Server error. Please try again."}