import os
import pyttsx3
import datetime


engine = pyttsx3. init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("google","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            speak("Alarm ringing,sir")
            os.startfile("C:\\Google Assistant\\Copines.mp3")
        elif currenttime + "00:00:40" == Alarmtime:
            exit()

ring(time)