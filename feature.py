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
    
    
    elif "feature" or "what can you do" in query:
        speak("Blue is always there to help you here is the list of what I can do")
        print("Blue is always there to help you here is the list of what I can do")
        speak("Open a web page for example open google,youtube")
        print("Open a web page for example open google,youtube")
        speak("Open application for example open vs Code or netbeans")
        print("Open application for example open vs Code or netbeans")
        speak("Tells the weather")
        print("Tells the weather")
        speak("Tells the current date and time")
        print("Tells the current date and time")
        speak("Set an alarm")
        print("Set an alarm")
        speak("Tells you news for today")
        print("Tells you news for today")
        speak("Tells you the current location")
        print("Tells you the current location")
        speak("I am still under development soon I will be able to do other things too")
           


        

