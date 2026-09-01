import asyncio
import edge_tts

async def amain():
    communicate = edge_tts.Communicate("Hello world, this is a test of the Virtual Professor's voice engine.", "en-US-AndrewMultilingualNeural")
    await communicate.save("test_audio.mp3")
    print("Test audio saved successfully!")

if __name__ == "__main__":
    try:
        asyncio.run(amain())
    except Exception as e:
        print(f"Error generating audio: {e}")
