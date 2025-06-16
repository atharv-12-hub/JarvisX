# voice/stt.py

import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"🗣 You said: {query}")
        return query
    except sr.UnknownValueError:
        print("❌ Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("❌ Speech service is down.")
        return ""
