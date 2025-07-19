# 🗣️🤖 VOICE ASSISTANT WITH FACIAL RECOGNITION 

## 📌 Overview

This project is a **fully interactive voice assistant** built using **Python**, integrated with **facial recognition** for security and **GUI interface** using PyQt5.
It accepts voice commands to perform a wide variety of tasks like:

- Opening websites
- Taking screenshots
- Playing/pausing YouTube
- Checking weather
- Telling time/day
- Managing schedule
- Performing calculations
- And much more...

Additionally, the assistant **authenticates the user** via facial recognition before executing commands, ensuring a secure user experience.

---

## 🚀 Features

- 🎤 **Voice Interaction** using `speech_recognition` and `pyttsx3`
- 🧑‍💻 **Face Recognition** using OpenCV and Haar Cascades
- 📆 **Daily Scheduling** with task file support
- 🌐 **Web Automation**: Opens websites, performs searches
- 🔐 **Password + Facial Verification**
- 🎵 **Media Control** (YouTube, local music)
- 📸 **Camera & Screenshot Access**
- 🌡️ **Weather Report**
- 🧮 **Calculator via WolframAlpha**
- 🔊 **Volume, Screen Mode Controls**
- 🕹️ **Keyboard/Mouse Automation** using `pyautogui`
- 📚 **Google Translate & Dictionary Support**
- 📰 **News Reader** (via web scraping)
- 🪟 **Desktop App GUI** using PyQt5

---

## 🖥️ GUI Details

- GUI designed with **PyQt5**
- Animated GIFs for visual interaction
- Real-time **time & date** display
- Start/Stop button for assistant

---

## 🧪 Technologies Used

| Feature              | Library/Module             |
|----------------------|-----------------------------|
| GUI                  | PyQt5                       |
| Voice Input/Output   | speech_recognition, pyttsx3 |
| Facial Recognition   | OpenCV (LBPH + HaarCascade) |
| Web Scraping         | BeautifulSoup, requests     |
| Notifications        | Plyer, pygame               |
| File Automation      | os, ctypes, datetime        |
| Browser Automation   | webbrowser                  |
| Screen/Keyboard Ctrl | pyautogui                   |

---

## 🧑‍🔬 How It Works

### Step 1: Launch
- Run the `main.py` script.
- Face recognition window opens.
- System asks for voice password.
- If verified, GUI loads.

### Step 2: Interact
- Click the **RUN** button on GUI.
- Speak commands like:
  - *"open youtube"*
  - *"what is the time"*
  - *"schedule my day"*
  - *"click my photo"*
  - *"volume up"*, etc.

---

## 🔒 Security

- ✅ **Face Recognition** (with LBPH model)
- ✅ **Voice Password** authentication

Only authorized users can interact with the assistant.



## 🛠️ Tips for Usage

- Store your password in `password.txt`
- Train the face recognizer using OpenCV (not shown in this file)
- Modify file paths (music, GUI GIFs) if needed
- Run the assistant using:



## 🧠 Future Improvements

- Add **chat-based interface** as fallback
- Integrate with **Google Calendar / APIs**
- Enable **mobile interaction via socket/Flask**
- Store task memory in a **database**

