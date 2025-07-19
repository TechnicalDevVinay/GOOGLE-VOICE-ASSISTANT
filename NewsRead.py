import requests
import json
import pyttsx3
import speech_recognition

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

def LatestNews(query):
   
    DictApi = {"technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=7918811373994bb388574c24b1f8ffb4",
               "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=7918811373994bb388574c24b1f8ffb4",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=7918811373994bb388574c24b1f8ffb4",
               "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=7918811373994bb388574c24b1f8ffb4",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=7918811373994bb388574c24b1f8ffb4",
               "business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=7918811373994bb388574c24b1f8ffb4",}
    
    content = None
    url = None
    results = ("Which field news do you want, [technology] , [sports] , [health], [science] , [entertainment] , [business]")
    print(results)
    speak(results)
    
    field = takeCommand().lower()
    for key ,value in DictApi.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        results = ("Do you want to continue listening news then say 6 or else if you want to stop listening say 5")
        print(results)
        speak(results)
        a = takeCommand().lower()
        if str(a) == "6":
            pass
        elif str(a) == "5":
            break
        
    speak("thats all")
