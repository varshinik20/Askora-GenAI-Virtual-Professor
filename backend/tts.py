from gtts import gTTS
import os
import time

def text_to_speech(text):
    filename = f"output_{int(time.time())}.mp3"

    audio_folder = os.path.join(os.getcwd(), "static", "audio")

    # Create folder if not exists
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)

    path = os.path.join(audio_folder, filename)

    tts = gTTS(
        text=text,
        lang="en",
        tld="co.in"
    )

    tts.save(path)

    return filename
