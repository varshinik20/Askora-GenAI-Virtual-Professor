from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import os

from genai_engine import generate_explanation
from tts import text_to_speech

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()
    user_text = data.get("text", "").strip()

    if not user_text:
        return jsonify({"text": "Please enter a topic.", "audio": ""})

    ai_text = generate_explanation(user_text)

    audio_file = text_to_speech(ai_text)

    return jsonify({
        "text": ai_text,
        "audio": f"/audio/{audio_file}"
    })


@app.route("/audio/<filename>")
def serve_audio(filename):
    return send_from_directory("static/audio", filename)


if __name__ == "__main__":
    app.run(debug=True)