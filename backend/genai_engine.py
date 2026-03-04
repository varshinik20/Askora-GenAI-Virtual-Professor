import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("❌ GROQ_API_KEY not found")

client = Groq(api_key=api_key)

def generate_explanation(user_input: str) -> str:
    prompt = f"""
You are a friendly college professor.

Explain the topic clearly, step-by-step, with examples.
Do not cut off mid-sentence.

Topic:
{user_input}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ FIXED MODEL
        messages=[
            {"role": "system", "content": "You are a helpful virtual professor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=700
    )

    return response.choices[0].message.content.strip()