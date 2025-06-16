# skills/notes.py

from datetime import datetime
from voice.tts import speak

def take_note(note_text):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("data/notes.txt", "a") as f:
            f.write(f"[{timestamp}] {note_text}\n")
        speak("I’ve saved your note.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't save the note.")
