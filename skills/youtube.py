import pywhatkit
from voice.tts import speak

def play_youtube(video_name):
    speak(f"Playing {video_name} on YouTube...")
    pywhatkit.playonyt(video_name)
