import os
import uuid
import edge_tts
import asyncio
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS

from genai_engine import generate_explanation

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Ensure audio folder exists
AUDIO_DIR = os.path.join("static", "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

# 🧹 Clean OLD audio files on startup
try:
    for f in os.listdir(AUDIO_DIR):
        if f.endswith(".mp3"):
            os.remove(os.path.join(AUDIO_DIR, f))
    print("Cleanup successful.")
except Exception as e:
    print("Cleanup Error:", e)

# Verified Voice Mapping
VOICE_MAP = {
    "english": "en-US-EmmaMultilingualNeural",
    "tamil": "ta-IN-PallaviNeural",
    "hindi": "hi-IN-SwaraNeural"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
async def ask():
    data = request.get_json()
    language = data.get("language", "english").lower()
    user_text = data.get("text", "").strip()

    if not user_text:
        return jsonify({"text": "Please enter a topic."})

    try:
        # Step 1: AI response (Groq is very fast)
        ai_text = generate_explanation(user_text, language)

        # Step 2: Audio generation (Fast via edge-tts save)
        voice = VOICE_MAP.get(language, "en-US-EmmaMultilingualNeural")
        filename = f"{uuid.uuid4().hex}.mp3"
        filepath = os.path.join(AUDIO_DIR, filename)

        # Use Communicate for high-speed file generation
        communicate = edge_tts.Communicate(ai_text, voice)
        await communicate.save(filepath)

        # Step 3: Return BOTH text and audio URL
        return jsonify({
            "text": ai_text,
            "audio": f"/audio/{filename}"
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"text": f"System Error: {e}"}), 500

@app.route("/audio/<filename>")
def serve_audio(filename):
    return send_from_directory(AUDIO_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)