import asyncio
import edge_tts

async def list_voices():
    voices = await edge_tts.VoicesManager.create()
    target_langs = ["en-US", "ta-IN", "hi-IN"]
    for voice in voices.voices:
        short_name = voice["ShortName"]
        gender = voice["Gender"]
        if any(lang in short_name for lang in target_langs):
            print(f"{short_name}|{gender}")

if __name__ == "__main__":
    asyncio.run(list_voices())
