from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import shutil

from chatbot.llm import chat
from chatbot.translate import detect_lang, translate_to_en, translate_back
from chatbot.memory import load_memory, save_memory
from chatbot.speech import speech_to_text, text_to_speech
from chatbot.vision import analyze_image

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/audio", StaticFiles(directory="."), name="audio")

messages = load_memory()

SYSTEM = {
    "role": "system",
    "content": "Always reply in the same language as the user."
}

@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/chat")
def chat_api(user_input: str):
    global messages

    lang = detect_lang(user_input)
    text_en = translate_to_en(user_input, lang)

    messages.append({"role": "user", "content": text_en})
    reply = chat(messages)

    messages.append({"role": "assistant", "content": reply})
    save_memory(messages)

    final = reply if lang == "en" else translate_back(reply, lang)

    return {"response": final}


@app.post("/image-upload")
async def image_upload(file: UploadFile = File(None), question: str = Form("")):
    if not file:
        return {"response": "No image provided."}

    path = "uploaded.jpg"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_image(path, question)
    return {"response": result}


@app.post("/audio")
async def audio_api(file: UploadFile = File(...)):
    try:
        with open("audio.wav", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("Audio saved")

        # 🎤 Speech → Text
        text = speech_to_text("audio.wav")
        print("Transcribed:", text)

        if not text or text.strip() == "":
            return {
                "user_text": "",
                "response_text": "❌ No speech detected",
                "audio_file": ""
            }

        lang = detect_lang(text)
        text_en = translate_to_en(text, lang)

        global messages
        messages.append({"role": "user", "content": text_en})

        # 🤖 AI
        reply = chat(messages)
        print("AI reply:", reply)

        messages.append({"role": "assistant", "content": reply})
        save_memory(messages)

        final = reply if lang == "en" else translate_back(reply, lang)

        # 🔊 TTS
        try:
            audio_path = text_to_speech(final, lang)
            print("Audio file:", audio_path)
            audio_url = f"/audio/{audio_path}"
        except Exception as e:
            print("TTS error:", e)
            audio_url = ""

        return {
            "user_text": text,
            "response_text": final,
            "audio_file": audio_url
        }

    except Exception as e:
        print("🔥 FULL ERROR:", e)
        return {
            "user_text": "",
            "response_text": "❌ Voice processing failed",
            "audio_file": ""
        }