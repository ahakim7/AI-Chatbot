from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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