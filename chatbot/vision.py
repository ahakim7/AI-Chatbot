from openai import OpenAI
import os
import base64

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_image(path, question=None):
    with open(path, "rb") as f:
        base64_image = base64.b64encode(f.read()).decode("utf-8")

    image_url = f"data:image/jpeg;base64,{base64_image}"

    prompt = question if question else "Describe this image and extract any visible text."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": image_url}
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content