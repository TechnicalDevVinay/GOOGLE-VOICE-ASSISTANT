import wolframalpha
import pyttsx3

engine = pyttsx3. init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "EHAJ4P-QVL2YU9AA3"   
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calculator(query):
    Term = str(query)
    Term = Term.replace("Google","")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("multiply","*")
    Term = Term.replace("divide by","/")
    Term = Term.replace("mod","%")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")