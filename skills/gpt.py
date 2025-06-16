import openai
from voice.tts import speak

# Paste your OpenAI API key here
openai.api_key = "your_openai_api_key_here"

def ask_gpt(prompt):
    try:
        speak("Let me think...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can upgrade to gpt-4 if allowed
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content
        speak(answer)
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't connect to ChatGPT.")
