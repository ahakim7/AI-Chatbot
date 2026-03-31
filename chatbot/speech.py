import whisper
from gtts import gTTS

model = whisper.load_model("base")

def speech_to_text(path):
    result = model.transcribe(path)
    return result["text"]

def text_to_speech(text, lang="en"):
    file = "response.mp3"  # MUST be mp3
    tts = gTTS(text=text, lang=lang)
    tts.save(file)
    return file