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
print("Hello Vikas ,i am Jar