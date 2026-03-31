from langdetect import detect
from deep_translator import GoogleTranslator

def detect_lang(text):
    try:
        if len(text.strip()) < 5:
            return "en"
        return detect(text)
    except:
        return "en"

def translate_to_en(text, lang):
    try:
        if lang == "en":
            return text
        return GoogleTranslator(source=lang, target="en").translate(text)
    except:
        return text

def translate_back(text, lang):
    try:
        if lang == "en":
            return text
        return GoogleTranslator(source="en", target=lang).translate(text)
    except:
        return text