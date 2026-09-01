import asyncio
import edge_tts

async def amain():
    communicate = edge_tts.Communicate("Hello world.", "en-US-AndrewMultilingualNeural")
    count = 0
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            count += len(chunk["data"])
    print(f"Successfully streamed {count} bytes of audio.")

if __name__ == "__main__":
    asyncio.run(amain())
