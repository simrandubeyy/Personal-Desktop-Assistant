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
    
 

if __name__ =="__main__":
    
    
    wishme()
        
   # while True:
    if 1:
        query = takeCommand().lower()
        #logic for execting task based on query
        
    #Browser search
    if "wikipedia" in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia","")#replacing wikipedia from query and making it blank
        results1 = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results1)
        speak(results1)
        
    elif  "youtube" in query:
        webbrowser.open("youtube.com")
    
    elif  "google" in query:
        webbrowser.open("google.com")
        
    elif  "stackoverflow" in query:
        webbrowser.open("stackoverflow.com")
        
    elif  "gmail" in query:
        webbrowser.open("gmail.com")
     
       
    #open .exe file    
    elif "visual code" in query:
        codePath="C:\\Users\\simra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        
    elif "netbeans" in query:
        codePath="C:\\Program Files\\NetBeans 8.0.1\\bin\\netbeans64.exe"
        os.startfile(codePath)
        
    elif "chrome" in query:
        codePath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codePath)
        
    elif "firefox" in query:
        codePath="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        os.startfile(codePath)
        
    elif "dev" in query:
        codePath="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
        os.startfile(codePath)
        
    elif "quit" in query:
        speak("see you soon!")
        exit()
        
