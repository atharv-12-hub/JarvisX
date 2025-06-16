import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from voice.stt import listen
from voice.tts import speak
from skills.wiki import search_wikipedia
from skills.weather import get_weather
from skills.email import send_email
from skills.translator import translate_text
from skills.gpt import ask_gpt
from skills.system_control import execute_command


# GUI setup
root = tk.Tk()
root.title("Jarvis - AI Assistant")
root.geometry("700x550")
root.configure(bg="#1e1e1e")

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 12), bg="black", fg="lime", padx=10, pady=10)
output_box.pack(padx=10, pady=20, fill=tk.BOTH, expand=True)
output_box.insert(tk.END, "✅ Click 'Start Jarvis' to begin.\n")
output_box.config(state='disabled')


def log_to_gui(text):
    output_box.config(state='normal')
    output_box.insert(tk.END, f"{text}\n")
    output_box.yview(tk.END)
    output_box.config(state='disabled')


def gui_speak(text):
    speak(text)
    log_to_gui(f"🤖 Jarvis: {text}")


def jarvis_main():
    gui_speak("Hello, I am Jarvis, your personal assistant. How can I help you today?")
    while True:
        command = listen()
        log_to_gui(f"🎤 You: {command}")

        if "exit" in command or "stop" in command:
            gui_speak("Goodbye Atharv! See you soon.")
            break

        elif "your name" in command:
            gui_speak("I am Jarvis, your AI assistant.")

        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            gui_speak(f"The current time is {current_time}.")

        elif "weather" in command:
            gui_speak("Which city?")
            city = listen()
            log_to_gui(f"🎤 You: {city}")
            get_weather(city)

        elif "wikipedia" in command or "wiki" in command or "pedia" in command:
            gui_speak("What should I search on Wikipedia?")
            query = listen()
            log_to_gui(f"🎤 You: {query}")
            result = search_wikipedia(query)
            gui_speak(result)

        elif "email" in command or "send mail" in command:
            gui_speak("To whom should I send the email?")
            recipient = listen()
            gui_speak("What is the subject?")
            subject = listen()
            gui_speak("What is the message?")
            message = listen()
            send_email(recipient, subject, message)

        elif "translate" in command:
            gui_speak("What text do you want to translate?")
            text = listen()
            gui_speak("To which language?")
            language = listen()
            result = translate_text(text, language)
            gui_speak(result)

        elif "open" in command or "shutdown" in command or "restart" in command:
            execute_command(command)

        elif "chat" in command or "gpt" in command:
            gui_speak("What do you want to ask?")
            prompt = listen()
            response = ask_gpt(prompt)
            gui_speak(response)

        else:
            gui_speak("I'm sorry, I didn't understand that. Please try again.")


# Buttons
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

def start_jarvis():
    Thread(target=jarvis_main).start()

start_btn = tk.Button(btn_frame, text="▶ Start Jarvis", command=start_jarvis, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=20)
start_btn.pack(side=tk.LEFT, padx=10)

exit_btn = tk.Button(btn_frame, text="❌ Exit", command=root.destroy, bg="#f44336", fg="white", font=("Arial", 12, "bold"), width=20)
exit_btn.pack(side=tk.LEFT, padx=10)

# Run the GUI
root.mainloop()
