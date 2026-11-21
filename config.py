model= "gemini-3.8-flash"
language=["English", "Hindi", "Hinglish"]
level=["Beginner", "Intermediate", "Advanced"]


NOTE_SCHEMA = {
"key_terms": {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "term": {"type": "string"},
            "definition": {"type": "string"}
        },
        "required": ["term", "definition"]
    }
}
}

NOTE_PROMPT = """
I have send a youtube video lecture link 
consider following instructions to generate notes from the video lecture:
Use both what is said and what is shown (slides, code, whiteboard)
• Split the video into chapters in time order, with the real start time as MM:SS or HH:MM:SS
• Write 3–6 short key points per chapter
• List key terms with a one-line definition
• Write for a {level} audience in {language}
• Include only what is in the video"""