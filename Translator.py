from fileinput import close
from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans #pip install googletrans
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition 
import os
from playsound import playsound
import time

engine = pyttsx3. init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query

def translategl(query):
    speak("SURE SIR")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")
    translation = translator.translate(query, src = "auto", dest= b,)   
    text = translation.text
    print(translation.text)
    

    #translator = Translator()
    #translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
    #print(translation.text)




    try : 
        speakgl = gTTS(text=text, lang=b, slow= False)
        speakgl.save("C:\\Google Assistant\\1660560576516-voicemaker.in-speech.mp3")
        os.startfile("C:\\Google Assistant\\1660560576516-voicemaker.in-speech.mp3")
        time.sleep(10)
        os.close("C:\\Google Assistant\\1660560576516-voicemaker.in-speech.mp3")
    except:
        print("Unable to translate")

