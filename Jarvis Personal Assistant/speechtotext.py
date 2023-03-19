import pyaudio
import pyttsx
import time
import threading
import webbrowser as wb
import speech_recognition as sr
r=sr.Recognizer()
eng=pyttsx.init()
location="INDIA" 

eng.setProperty('rate',150);
#eng.say("Hello Vikas ,i am Jarvis  What can i Do for you ? ");
#eng.runAndWait()
print("Hello Vikas ,i am Jarvis What can i Do for you ?");
print("Speak Something :--");
#r.energy_threshold = 4000

while 1:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                pinger=r.recognize_google(audio)
              
            try:
                if(len(pinger)>1):
                  print("you Speak : "+pinger);
                  #eng.say("you speak "+pinger);
                  #eng.runAndWait()
                  
                if (pinger == "what is the time right now") :
                    eng.say(time.ctime());
                    eng.runAndWait()
                    print(time.ctime());
                    continue
                  
                elif "where is " in pinger:
                   pinger=pinger.split(" ")
                   if len(pinger)>3:
                     location=pi