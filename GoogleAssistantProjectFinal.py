from Googleui import Ui_googlegui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt 
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from PyQt5 import QtGui




import pyttsx3
import speech_recognition
import datetime
import pyautogui
import os
from plyer import notification
from pygame import mixer
import webbrowser
import time
import ctypes
import cv2
import requests
from bs4 import BeautifulSoup
import cv2
import sys
from NewsRead import takeCommand

from wishMe import greetMe



   

engine = pyttsx3. init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",210)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

for i in range(3):
    speak("Speak Password to open Google Assistant :- ")
    a = takeCommand().lower()
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR !")
        break
    elif (i==2 and a!=pw):
        speak("Your chances are over,closing")
        exit()

    elif (a!=pw):
        print("Try Again")


def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")   

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")

    speak("Please tell me, How can I help you ?")

def TaskExecution():
    pyautogui.press("esc")
    speak("verification successful")
    speak("welcome back sir")
    

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()
        

    def takeCommand(self):
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
            query =  "None"
        return query

    def greetMe():
            hour  = int(datetime.datetime.now().hour)
            if hour>=0 and hour<=12:
                speak("Good Morning,sir")
            elif hour >12 and hour<=18:
                speak("Good Afternoon ,sir")

            else:
                speak("Good Evening,sir")

            speak("Please tell me, How can I help you ?")  

    def TaskExecution(self):
        greetMe()
    
        
        while True:
            self.query =self.takeCommand().lower()


            if "go to sleep" in self.query:
                self.query = self.query.replace("go to sleep","")
                self.query = self.query.replace("google","")
                speak("Ok sir , you can call me  anytime")
                break

            elif "open youtube" in self.query:
                self.query = self.query.replace("open youtube","")
                self.query = self.query.replace("google","")
                webbrowser.open("youtube.com")

            elif "open google" in self.query:
                self.query = self.query.replace("open google","")
                self.query = self.query.replace("google","")
                webbrowser.open("google.com")
            
            

            elif "open facebook" in self.query:
                self.query = self.query.replace("open facebook","")
                self.query = self.query.replace("google","")
                webbrowser.open("facebook.com")

            elif "open whatsapp" in self.query:
                self.query = self.query.replace("open whatsapp","")
                self.query = self.query.replace("google","")
                webbrowser.open("https://web.whatsapp.com/")

            elif "schedule my day" in self.query:
                    self.query = self.query.replace("schedule my day","")
                    self.query.replace("google","")
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    self.query = self.takeCommand().lower()
                    if "yes" in self.query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in self.query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

            elif "show my schedule" in self.query:
                file = open("tasks.txt","r")
                content = file.read()
                file.close()
                mixer.init()
                mixer.music.load("notification.mp3")
                mixer.music.play()
                notification.notify()
                title = "My schedule :-",
                message = content,
                timeout = 15                   

            elif "translate" in self.query:
                from Translator import translategl
                self.query = self.query.replace("translate","")
                self.query = self.query.replace("google","")
                translategl(self.query)

            elif "i am fine" in self.query:
                self.query = self.query.replace("i am fine","")
                self.query = self.query.replace("google","")
                speak("That's great,sir")
                results = ("That's great,sir") 
                print(results)

            elif "how are you" in self.query:
                self.query = self.query.replace("how are you","")
                self.query = self.query.replace("google","")
                speak("I am good sir")
                results = ("I am good sir")
                print(results)

            elif "who created you" in self.query:
                self.query = self.query.replace("who created you","")
                self.query = self.query.replace("google","")
                speak("vinay tawde a dumb fellow created me")
                results = ("vinay tawde a dumb fellow created me")
                print(results)

            elif "hello" in self.query:
                self.query = self.query.replace("hello","")
                self.query = self.query.replace("google","")
                speak("Ok sir, how are you ?")
                results = ("Ok sir, how are you ?")
                print(results)    

            elif "pause" in self.query:
                self.query = self.query.replace("pause","")
                self.query = self.query.replace("google","")
                pyautogui.press("k")
                speak("video paused")

            elif "play" in self.query:
                self.query = self.query.replace("play","")
                self.query = self.query.replace("google","")
                pyautogui.press("k")
                speak("video played")

            elif "mute" in self.query:
                self.query = self.query.replace("mute","")
                self.query = self.query.replace("google","")
                pyautogui.press("m")
                speak("video muted")

            elif "unmute" in self.query:
                self.query = self.query.replace("unmute","")
                self.query = self.query.replace("google","")
                pyautogui.press("m")
                speak("video unmuted")
            
            elif "next video" in self.query:
                pyautogui.keyDown("shift")
                pyautogui.press("n")
                time.sleep(1)
                pyautogui.keyUp("shift")

            elif "volume up" in self.query:
                self.query = self.query.replace("volume up","")
                self.query = self.query.replace("google","")
                from keyboard import volumeup
                speak("Turning volume up,  sir")
                volumeup()

            elif "volume down" in self.query:
                self.query = self.query.replace("volume down","")
                self.query = self.query.replace("google","")
                from keyboard import volumedown
                speak("Turning volume down, sir")
                volumedown()

            elif "full screen" in self.query:
                self.query = self.query.replace("full screen","")
                self.query = self.query.replace("google","")
                pyautogui.press("f")
                speak("Switching to fullscreen, sir")
            
            elif "theatre screen" in self.query:
                self.query = self.query.replace("theatre screen","")
                self.query = self.query.replace("google","")
                pyautogui.press("t")
                speak("Switching to fullscreen, sir")
           
            elif "stop theatre screen" in self.query:
                self.query = self.query.replace("stop theatre screen","")
                self.query = self.query.replace("google","")
                pyautogui.press("t")
                speak("Switching to fullscreen, sir")

            elif "stop full screen" in self.query:
                self.query = self.query.replace("full screen","")
                self.query = self.query.replace("google","")
                pyautogui.press("f")
                speak("Switching back to normal screen, sir")
        
            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(3)
                pyautogui.keyUp("alt")
        
            elif "webcam" in self.query:
                self.query = self.query.replace("webcam","")
                self.query = self.query.replace("google","")
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()  
            
            elif "screenshot" in self.query:
                self.query = self.query.replace("screenshot","")
                self.query = self.query.replace("google","")
                speak("sir please hold the screen for few seconds, i am taking screenshot")
                time.sleep(1)
                speak("sir, please name this scrennshot file")
                img = pyautogui.screenshot()
                name = self.takeCommand().lower()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshotis saved in our main file.")
            

            elif "what is the time" in self.query:
                self.query = self.query.replace("what is the time","")
                self.query = self.query.replace("google","")
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
    
            elif  "music" in self.query:
                self.query = self.query.replace("music","")
                self.query = self.query.replace("google","")
                music_dir = "C:\\MUSIC"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[3]))

            elif "set an alarm" in self.query:
                self.query = self.query.replace("set an alarm ","")
                self.query = self.query.replace("google","")
                print("input time example:- 10 and 10") 
                speak("Set the time")
                speak("Please tell the time :- ")
                a = self.takeCommand().lower()
                alarm(a)
                speak("Done,sir")
    #a = input("Please tell the time :- ")

            elif "remember that" in self.query:
                rememberMessage = self.query.replace("google","")
                rememberMessage = self.query.replace("remember that","")
                speak("You told me"+rememberMessage)
                remember = open("Remember.txt","a")
                remember.write(rememberMessage)
                speak("Done, Sir")
                remember.close()     
            elif "what do you remember" in self.query:
                remember = open("Remember.txt","r")
                rememberMessage = self.query.replace("google","")
                speak("You told me" + remember.read())
                speak("Done, Sir")
            
            elif "news" in self.query:
                self.query = self.query.replace("news","")
                self.query = self.query.replace("google","")
                from NewsRead import LatestNews
                LatestNews(self.query)

            elif "calculate" in self.query:
                self.query = self.query.replace("calculate","")
                self.query = self.query.replace("google","")
                from CalculateValues import WolfRamAlpha
                from CalculateValues import Calculator
                self.query = self.query.replace("Google","")
                self.query = self.query.replace("calculate","")
                Calculator(self.query)
                

            elif "restart system" in self.query:
                self.query = self.query.replace("restart  system ","")
                self.query = self.query.replace("google","")
                speak("Are You sure you want to restart?")
                a= self.takeCommand().lower()
                if str(a) == "yes":
                    os.system("shutdown /r /t 1")

                elif str(a) == "no":
                    break
            
            elif "shutdown system" in self.query:
                self.query = self.query.replace("shutdown system","")
                self.query = self.query.replace("google","")
                speak("Are You sure you want to shutdown?")
                a= self.takeCommand().lower()
                if str(a) == "yes":
                    os.system("shutdown /s /t 1")

                elif str(a) == "no":
                    break
            
            elif "sleep system" in self.query:
                self.query = self.query.replace("lock system","")
                self.query = self.query.replace("google","")
                speak("locking the device")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")




            elif "lock system" in self.query:
                self.query = self.query.replace("lock system","")
                self.query = self.query.replace("google","")
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
    #a = self.takeCommand().lower()
            #if str(a) == "6":
                #pass
            #elif str(a) == "5":
                #break        
            
            elif "text translator" in self.query:
                self.query = self.query.replace("text translator","")
                self.query = self.query.replace("google","")
                webbrowser.open("https://translate.google.com/")

            elif "open" in self.query:
                self.query = self.query.replace("open","")
                self.query = self.query.replace("google","")
                from Dictapp import openappweb
                openappweb(self.query)

            elif "close" in self.query:
                self.query = self.query.replace("close","")
                self.query = self.query.replace("google","")
                from Dictapp import closeappweb
                closeappweb(self.query)    
            
            elif "click my photo" in self.query:
                self.query = self.query.replace("click my photo","")
                self.query = self.query.replace("google","")
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(1)
                speak("SMILE")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                speak("closing camera")
                pyautogui.keyDown("alt")
                pyautogui.press("F4")
                pyautogui.keyUp("alt")

            elif "stop song" in self.query:
                self.query = self.query.replace("stop song","")
                self.query = self.query.replace("google","")
                pyautogui.press("space")
                speak("stop song")
            
            elif "start song" in self.query:
                self.query = self.query.replace("start song","")
                self.query = self.query.replace("google","")
                pyautogui.press("space")
                speak("start song")

            elif "weather" in self.query:
                self.query = self.query.replace("weather","")
                self.query = self.query.replace("google","")
                search = "temperature in mumbai"
                url = f"https://www.google.com/search?q={search}"
                r  = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div", class_ = "BNeawe").text
                speak(f"current{search} is {temp}")

            elif "which day it is" in self.query:
                self.query = self.query.replace("which day it is","")
                self.query = self.query.replace("google","")
                tellDay

            elif "finally sleep" in self.query:
                self.query = self.query.replace("finally sleep","")
                self.query = self.query.replace("google","")
                speak("Going to sleep,sir")
                exit()
            
            

        #def searchDictionary(self.query):
        #if "dictionary" in self.query:
        #   speak("This is what i found for your search!")
        #  self.query = self.query.replace("dictionary search","")
        #    self.query = self.query.replace("google","")
        #  web = "https://www.dictionary.com/browse/" + self.query
        ##  webbrowser.open(web)
        ## speak("Done, Sir") 






            elif "google" in self.query:
                from SearchNow import searchgoogle
                searchgoogle(self.query)
            elif "youtube" in self.query:
                from SearchNow import searchYoutube
                searchYoutube(self.query)
            elif " wikipedia" in self.query:
                from SearchNow import searchWikipedia
                searchWikipedia(self.query)

            elif "amazon" in self.query:
                from SearchNow import searchAmazon
                searchAmazon(self.query)
        
            elif "dictionary" in self.query:
                from SearchNow import searchDictionary
                searchDictionary(self.query)
            
            elif "destination" in self.query:
                from SearchNow import searchDestination
                searchDestination(self.query)



startExecution = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = Ui_googlegui()
        self.gui.setupUi(self)
        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)

    def startTask(self):

        self.gui.movie = QtGui.QMovie("C:/Google Assistant/GUI/f48e7a6487df38a0aed24fec6c4adbff (1).gif")
        self.gui.label.setMovie(self.gui.movie) 
        self.gui.movie.start()
        self.gui.movie = QtGui.QMovie("C:/Google Assistant/GUI/ProtoPie-voice-feature-visualization-gif (1).gif")
        self.gui.label_2.setMovie(self.gui.movie) 
        self.gui.movie.start()
        self.gui.movie = QtGui.QMovie("C:/Google Assistant/GUI/xiaoyi-status.gif")
        self.gui.label_3.setMovie(self.gui.movie) 
        self.gui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.gui.textBrowser.setText(label_time)
        self.gui.textBrowser_2.setText(label_date)              

app = QApplication(sys.argv)
google = Gui_Start()
google.show()

if __name__ == "__main__" :


        recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
        recognizer.read('Trainer/trainer.yml')   #load trained model
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

        font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


        id = 2 #number of persons you want to Recognize


        names = ['','vinay']  #names, leave first empty bcz counter starts from 0


        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
        cam.set(3, 640) # set video FrameWidht
        cam.set(4, 480) # set video FrameHeight
        
        #Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        flag = True

        while True:

            ret, img =cam.read() #read the frames using the above created object
            
            
            converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

            faces = faceCascade.detectMultiScale( 
                converted_image,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
            )

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

                id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

                # Check if accuracy is less them 100 ==> "0" is perfect match 
                if (accuracy < 100):
                    id = names[id]
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    TaskExecution()
                    results = "user identified"
                    speak(results)
                    print(results)
                    speak("Press RUN BUTTON TO START ME")
                    pyautogui.press("esc")
                         

                else:
                    id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    results="User has not been  identified"
                    speak(results)
                    print(results)
                    speak("closing")

                    sys.exit()
                
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
            cv2.imshow('camera',img) 

            k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            

        # Do a bit of cleanup
cam.release()
cv2.destroyAllWindows()
exit(app.exec_())

