from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables (safe even if already loaded in main.py)
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Optional safety check
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found. Check your .env file.")

# Initialize client
client = OpenAI(api_key=api_key)
print("API KEY LOADED:", os.getenv("OPENAI_API_KEY"))


def chat(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )

    text = response.choices[0].message.content

    if not text:
        return "Sorry, I couldn't generate a response."

    return text.strip()