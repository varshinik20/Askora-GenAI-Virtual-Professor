import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY not found")

client = Groq(api_key=api_key)


from language_module import LanguageModule

def generate_explanation(user_input, language="english"):

    system_prompt = LanguageModule.get_system_prompt(language)
    
    prompt = f"""
Explain the following topic:
{user_input}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt + " Always finalize your explanation and do not stop in the middle of a sentence."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=1500
    )

    return response.choices[0].message.content.strip()