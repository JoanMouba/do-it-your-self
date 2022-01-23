#  @uthor: Dr.-Ing. Joan MOUBA, joan.mouba@gmail.com
# Project: Building my own personal assistant with Python

# Standard library modules
import time
from datetime import datetime
from typing import Any
# Speech recognition and synthesis modules
import pyttsx3
import speech_recognition as sr
# Web scraping modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# Information scraping on Wikipedia modules
import wikipedia
# Jokes module
import pyjokes
# multimedia modules
from playsound import playsound
import pywhatkit

recognizer = sr.Recognizer()
microphone = sr.Microphone()

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
speaker.setProperty("rate", 140)
speaker.setProperty("volume", 0.9)  # volume 0-1

chrome_options = Options()
chrome_options.headless = True
chrome_driver_path = "./chromedriver.exe"
chrome_driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(
    service=chrome_driver_service,
    options=chrome_options
)

def speak(text: str, speaker: pyttsx3.engine):
    speaker.say(text)
    speaker.runAndWait()

def get_weather(city: str, driver: Any) -> str:
    try:
        weather_station = "https://www.weather-forecast.com/locations/" \
                          + city \
                          + "/forecasts/latest"
        driver.get(weather_station)
        allow_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        allow_cookies.click()
        weather = driver.find_element(By.XPATH, '/html/body/main/section[2]/div/div[2]/div[2]')
        weather_forecast = weather.text
        return weather_forecast
    except:
        pass

intro_text = """Hello, Hello I am Alexa, your personal assistant.
I can tell the weather of the cities of the world, give the time, search Wikipedia, make jokes, play sound and videos!  """
speak(intro_text, speaker)

recognized_text: str = ""
while True:
    time.sleep(1)
    conversational_text = "What do you want me to do ?"
    weather_forecast_text = ""
    try:
        with microphone as mic:
            print(conversational_text)
            speak(conversational_text, speaker)
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            listened_audio = recognizer.listen(mic, phrase_time_limit=10)
            print("stop speaking, let me think")
            time.sleep(1)

            recognized_text = recognizer.recognize_google(listened_audio)
            recognized_text = recognized_text.lower()
            print(f"I heard:  {recognized_text}!")
            speak("I heard: " + recognized_text, speaker)
            time.sleep(2)
            if "go" in recognized_text and "sleep" in recognized_text:
                break
            elif "weather" in recognized_text or "waver" in recognized_text or "waiver" in recognized_text:
                _, *city = recognized_text.split()
                if city is None:
                    break
                city = " ".join(city)
                weather_forecast_text = get_weather(city, driver)
                speak(weather_forecast_text, speaker)
            elif ("wikipedia" in recognized_text) or ("wikipage" in recognized_text):
                _, *wiki_interest = recognized_text.split()
                if wiki_interest is None:
                    break
                wiki_interest = " ".join(wiki_interest)
                speak(wikipedia.summary(wiki_interest, sentences=3), speaker)
            elif ("what" in recognized_text) and ("time" in recognized_text):
                current_time = datetime.now().strftime('%I%M %p')
                speak("Current time is : " + current_time, speaker)
            elif  ("make" in recognized_text) and ("joke" in recognized_text):
                speak(pyjokes.get_joke(language='en', category='neutral'), speaker)
            if ("play" in recognized_text) and ("music" in recognized_text):
                playsound("music/Powerful-Emotional-Trailer.mp3")
            elif ("play" in recognized_text) and ("video" in recognized_text):
                pywhatkit.playonyt("https://www.youtube.com/watch?v=7d_MEZEHyE8")
            else:
                repeat_please_text = "Sorry, I did not understand your command!"
                print(repeat_please_text)
                speak(repeat_please_text, speaker)

    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
print("Step 5 of our Personal Assistant with Python, Done!")
