import wikipedia
from voice.tts import speak

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia, {summary}")
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Your query is too broad. Can you be more specific?")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find anything on Wikipedia for that.")
