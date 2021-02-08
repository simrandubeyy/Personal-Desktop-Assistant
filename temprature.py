import pyttsx3
import datetime#inbuilt
import speech_recognition as sr
import wikipedia
import webbrowser#inbuilt
import os#inbuilt
import smtplib#inbuilt
#import time#inbuilt 
import requests
from bs4 import BeautifulSoup
from random import randint
import secrets
from playsound import playsound
import pyowm 
import speedtest

#start
x = 'hello simran, how are you?'

def speak(t):
    engine = pyttsx3.init()
    s =engine.getProperty('voices')
    engine.setProperty('rate',160)#rate at which it will speak
    engine.setProperty('voice',s[0].id)#male or female voice
    engine.say(t)
    engine.runAndWait()
    
speak(x)



#greatings
def wishme():
    #greats you 
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
    
    speak("I am Blue. Please tell me how may I help you?")
    
    


#will listen to the voice and return what you said    
def takeCommand(ask=False):
    #takes mocrophone input from the user and returns string output
    
    r= sr.Recognizer()#this class will help to recognize
    with sr.Microphone() as source:
        if ask:
            print(ask)
        print("Listening...")
        r.pause_threshold = 1 #seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source) 
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')#recognize_google enginne used (there are various other engine available too)
        print(f"User said: {query}\n")#f string used 
        
    except Exception as e:
        print(e)
        
        print("Say that again please")
        
        return "None"#Just a string None
    return query
    


    
    elif "weather" or "temprature" in query: 
        #https://home.openweathermap.org/api_keys
        speak("Blue is here to give you temprature update")
        
        owm = pyowm.OWM('e27d8164b3234c34502aa9a41d68040e')
        
        speak("Tell me the location please")
        
        place1 = takeCommand("Tell me the location please")
        location1 = owm.weather_at_place(place1)
        weather = location1.get_weather()
        #print(weather)
        
        temp = weather.get_temperature('celsius')
        humidity = weather.get_humidity()
       
        
        print(temp)
        speak("Here is the current temprature")
        speak(temp)
        print(humidity)
        speak("Here is the current humidity level")
        speak(humidity)
       
        #print(humidity)
       # for key,value in temp.items():
           # print(key,value)


