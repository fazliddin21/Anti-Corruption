import pyttsx3
import speech_recognition as sr

import pandas as pd
data = pd.read_excel(r"C:\Users\user\Desktop\google asistent\CreeD\open_data.csv")
b=pd.DataFrame(data)
    # search for transfers
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold=1
        audio = r.listen(source, timeout=0, phrase_time_limit=5)

        try:
            print("recognizing...")
            query = r.recognize_google(audio, language="uz")
            print(query)
        except:
            speak("qaytadan ayting iltimos")


if __name__=='__main__':
    # speak("Assalomu aleykum, men Creedman va men korrupsiyaga qarshi kurashadigan suniy ongman")
    speak(b)
    takecommand()

