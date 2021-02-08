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
    

        
      
    elif "current" or "now" in query:
        #geojs website
        
        raa = requests.get('https://get.geojs.io/')
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        
        ipAdd = ip_request.json()['ip']
        print(ipAdd)
        
        url1 = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
        geo_request = requests.get(url1)
        geo_data = geo_request.json()
        
        #print(geo_data)
        speak("Your current contry location is")
        print(geo_data['country'])
        speak(geo_data['country'])
        
        speak("Your current city location is")
        print(geo_data['city'])
        speak(geo_data['city'])
        
        speak("Your current region location is")
        print(geo_data['region'])
        speak(geo_data['region'])
        
        speak("Your current location latitude is")
        print(geo_data['latitude'])
        speak(geo_data['latitude'])
        
        speak("Your current location longitude is")
        print(geo_data['longitude'])
        speak(geo_data['longitude'])

        speak("Your current location timezone is")
        print(geo_data['timezone'])
        speak(geo_data['timezone'])
