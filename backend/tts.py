from gtts import gTTS
import os
import time


def text_to_speech(text):

    filename = f"output_{int(time.time())}.mp3"

    audio_folder = os.path.join("static", "audio")

    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)

    file_path = os.path.join(audio_folder, filename)

    tts = gTTS(text=text, lang="en", tld="co.in")
    tts.save(file_path)

    return filename