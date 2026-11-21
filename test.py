from gemini_client import get_client
from config import model

print("yes")
client = get_client()
if client is None:
    print("API key missing. Add GEMINI_API_KEY to your .env file.")
else:
    interaction = client.interactions.create(
        model=model,
        input=[
            {"type": "video", "uri": "https://youtu.be/jWhQweWdLF4?si=zpUkPdhAKUVa_EWM"},
            {"type": "text", "text": "Please summarize the video in 3 sentences."},
        ],
    )
    print(interaction.output_text)
    print("done")