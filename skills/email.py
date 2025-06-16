# skills/email.py
import smtplib
from email.message import EmailMessage
from voice.tts import speak
from voice.stt import listen
# Hardcoded contact list (add more as needed)
contacts = {
    "atharv": "atharvmulik93@gmail.com",
    "test": "test@example.com"
}
def send_email():
    try:
        speak("Who do you want to send the email to?")
        name = listen().lower()
        if name not in contacts:
            speak(f"Sorry, I don't have an email for {name}.")
            return
        to_email = contacts[name]
        speak("What is the subject?")
        subject = listen()
        speak("What is the message?")
        content = listen()
        # Email Setup
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = "atharvmulik93@gmail.com"
        msg["To"] = to_email
        msg.set_content(content)
        # Login & Send (Use Gmail App Password)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("your_email@gmail.com", "123456789")
            smtp.send_message(msg)
        speak("Email has been sent successfully.")
    except Exception as e:
        print("Error:", e)
        speak("Sorry, I was not able to send the email.")
