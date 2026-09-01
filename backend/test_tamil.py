import asyncio
import edge_tts

async def amain():
    # Test Tamil voice file generation
    tamil_text = "வணக்கம், நான் உங்கள் மெய்நிகர் பேராசிரியர். இன்று நாம் பைதான் பற்றி படிக்கப்போகிறோம்."
    communicate = edge_tts.Communicate(tamil_text, "ta-IN-ValluvarNeural")
    await communicate.save("test_tamil.mp3")
    print("Tamil audio saved successfully!")

if __name__ == "__main__":
    asyncio.run(amain())
