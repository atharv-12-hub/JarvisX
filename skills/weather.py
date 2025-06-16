import requests
from voice.tts import speak

API_KEY = "fa2d75b8a915a87a52f8aa809c163a8e"  # Replace with your valid key

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Debug print in terminal
        print("API response:", data)

        if "main" in data:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            speak(f"The weather in {city} is {condition} with a temperature of {temp}°C.")
        else:
            error_message = data.get("message", "unknown error")
            speak(f"Sorry, I couldn't find weather for {city}. Reason: {error_message}")
    except Exception as e:
        speak("Something went wrong while fetching the weather.")
        print("Error:", e)
