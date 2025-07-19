
import webbrowser
import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    
    try:
        print("Understanding....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query 

query = takeCommand().lower()

engine = pyttsx3. init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchgoogle(query):
    if "google search" in query:
        import wikipedia as googleScrap
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("this what i have found on searching in google")
        pywhatkit.search(query)
        
        try:
          result = googleScrap.summary(query, sentences=5)
          speak(result)

        except:
          speak("No data available vinay sir")


def searchYoutube(query):
    if "youtube" in query:
        speak("This is what i found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("Google","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("google","")
        results=wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)


def searchAmazon(query):
    if "amazon" in query:
        speak("This is what i found for your search!")
        query = query.replace("amazon search","")
        query = query.replace("google","")
        web = "https://www.amazon.in/s?k=" + query
        webbrowser.open(web)
        speak("Done, Sir")


def searchDictionary(query):
    if "dictionary" in query:
        speak("This is what i found for your search!")
        query = query.replace("dictionary search","")
        query = query.replace("google","")
        web = "https://www.dictionary.com/browse/" + query
        pywhatkit.search(query)
        webbrowser.open(web)
        speak("Done, Sir")        

def searchDestination(query):
    if "destination" in query:
        speak("This is what i found for your search!")
        query = query.replace("destination search","")
        query = query.replace("google","")
        web = "https://www.google.com/maps/dir//" + query
        pywhatkit.search(query)
        webbrowser.open(web)
        speak("Done, Sir")        
       