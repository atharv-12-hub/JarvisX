# main.py

from voice.stt import listen
from voice.tts import speak
from skills.weather import get_weather
from skills.wiki import search_wikipedia 
from datetime import datetime
from skills.youtube import play_youtube
from skills.notes import take_note
from skills.email import send_email
from skills.gpt import ask_gpt
from skills.system_control import open_app
from skills.translator import translate_text
import pywhatkit








def greet_user():
    speak("Hello, I am Jarvis, your personal assistant. How can I help you today?")

def main():
    greet_user()

    while True:
        query = listen().lower()

        if "exit" in query or "stop" in query:
            speak("Goodbye Atharv! See you soon.")
            break

        elif "your name" in query:
            speak("I am Jarvis, your AI assistant.")

        elif "time" in query:
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")

        elif "weather" in query:
            speak("Which city?")
            city = listen().lower()
            get_weather(city)

        elif "wikipedia" in query or "wiki" in query or "pedia" in query:
            speak("What should I search on Wikipedia?")
            topic = listen()
            search_wikipedia(topic)
        elif "youtube" in query or "play" in query:
            speak("What should I play on YouTube?")
            video = listen()
            play_youtube(video)
        elif "note" in query or "remember" in query:
            speak("What should I note down?")
            note = listen()
            take_note(note)
        elif "send email" in query or "email" in query:
            from skills.email import send_email
            send_email()
        elif "chatgpt" in query or "ai" in query or "gpt" in query:
            speak("What do you want to ask ChatGPT?")
            user_query = listen()
            ask_gpt(user_query)
        elif "open" in query:
            app = query.replace("open", "").strip()
            open_app(app)
        elif "translate" in query:
            speak("What sentence should I translate?")
            sentence = listen()

            speak("Which language should I translate it to?")
            lang = listen().lower()

            # Language code mapping
            language_codes = {
                "hindi": "hi",
                "marathi": "mr",
                "french": "fr",
                "german": "de",
                "spanish": "es",
                "japanese": "ja"
            }

            lang_code = language_codes.get(lang, "en")
            translate_text(sentence, lang_code)
        elif "youtube" in query or "play" in query:
            speak("What should I play on YouTube?")
            yt_query = listen()
            speak(f"Playing {yt_query} on YouTube.")
            pywhatkit.playonyt(yt_query)

        else:
            speak("I'm sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()
