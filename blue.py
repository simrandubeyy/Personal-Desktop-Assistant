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
    




def sendEmail(to, content):# to whom and what
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('simren.dubey@spit.ac.in','dubey1998')
    server.sendmail('simren.dubey@spit.ac.in',to,content)
    server.close()
    

def beautiful_soup(url):
            request = requests.get(url)
            soup = BeautifulSoup(request.text, "lxml")
            #print(soup.prettify())
            return soup

            


#def respond(query):
    #if "what is your name" in query:
     #   print("My name is Blue")
     #   speak("My name is Blue")
    
        
    

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
        
   


     
    #music in PC    
    elif "play music" in query:
        music_dir = "C:\\ganne"
        songs =os.listdir(music_dir)
        print(songs)#will print list of the songs 
        
        os.startfile(os.path.join(music_dir,songs[0]))
        
      
        
        
        
    #real time time        
    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
      
        
        
        
        
        
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
        
        
        
    elif "email" in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "simrendubey@spit.ac.in"
            sendEmail(to, content)
            speak("Email has been send")
            
        except Exception as e:
            print(e)
            speak("Sorry bhai email nahi bhej sakta hu mai")
            
    elif "name" in query:
        print("My name is Blue")
        speak("My name is Blue")
        
        
    elif "jokes" in query:
        foo = ['Why did the teddy bear say no to dessert?\n\tBecause she was stuffed\n'
               'What did the left eye say to the right eye?\n\tBetween us, something smells!\n'
               'What do you get when you cross a vampire and a snowman?\n\tFrost bite!\n'
               'What did one plate say to the other plate\n\t?Dinner is on me\n'
               'When you look for something, why is it always in the last place you look?\n\tBecause when you find it, you stop looking\n'
               'What is brown, hairy and wears sunglasses?\n\tA coconut on vacation.\n'
               ]
        rando=secrets.choice(foo)
        print(rando) 
        speak(rando)

        
    elif "search" in query:
        speak("what do you want to search")
        search = takeCommand("what do you want to search")
        Path='https://google.com/search?q='+ search
        webbrowser.get().open(Path)
        speak("Here is what I found on web")
        print('Here is what I found on web ' + search) 
        
    elif "location" or "place" in query:
        speak("which place do you want to search")
        location = takeCommand("which place do you do you want to search")
        url='https://google.nl/maps/place/'+ location + '/&amp;'
        webbrowser.get().open(url)
        speak("Here is what I found on web")
        print('Here is what I found on web ' + location)
        
    elif "news" or "headline" in query:
        soup = beautiful_soup('https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en')
        for headlines in soup.find_all('a', {'class': 'VDXfz'}):
            resultss=headlines.find_next('span').text        
            print(resultss)
                #beautiful_soup(url)
            speak(resultss)
            
        
    elif "alarm" or "Wake me" in query:
        speak("What time do you want to set the alarm for")
       # os. system('clear')
        speak("Set the hour")
        alarmH = int(input("What hour do you want the alarm to ring? "))
        speak("Set the minute")
        alarmM = int(input("What minute do you want the alarm to ring? "))
        amPm = str(input("am or pm? "))
       # os. system('clear')
        print("Waiting for alarm",alarmH,alarmM,amPm)
        if (amPm == "pm"):
            alarmH = alarmH + 12
        while(1 == 1):
            if(alarmH == datetime.datetime.now().hour and
               alarmM == datetime.datetime.now().minute) :
                print("Time to wake up")
                speak("Get up")
                playsound('C:/ganne/Baby Shark.mp3')
                break
    
           


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
                      
    elif "speedtest" or "speed" or "test" in query:
        ay=speedtest.Speedtest()
        print("Speed test is here")
        speak("Blue is here to give you Speed test")
        
        print("Upload Speed")
        speak("Upload Speed")
        speak(ay.upload())
        print(ay.upload())
        
        print("download speed")
        speak("download speed")
        speak(ay.download())
        print(ay.download())
        
        print("Ping result")
        speak("Ping result")
        speak(ay.results.ping)
        print(ay.results.ping)'''
        
