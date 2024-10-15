import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import sys
import os
import random
import smtplib
import csv

GMAIL_ID = os.getenv('GMAIL_ID')
GMAIL_PASS = os.getenv('GMAIL_PASS')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

def takecommand():
    '''
    Is takes commands from the user.
    '''
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        command.energy_threshold = 500
        audio = command.listen(source)
    
    try:
        print("Recognizing...")
        query = command.recognize_google(audio)
        print(f"User said : {query}")

    except Exception as e:
        print(e)
        speak("Say that again bro.")
        return "None"
    
    return query    

def send_email(name):
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            if name in row[0]:
                to = row[1]
                speak("What should be the Subject of Email ?")
                subject = takecommand()
                speak(f"What should I say to {name}?")
                content = takecommand()
                message = 'Subject: {}\n\n{}'.format(subject, content)
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(GMAIL_ID, GMAIL_PASS)
                s.sendmail(GMAIL_ID, to, message)
                s.quit()
                speak("Email has been sent!")
                return
        speak("User not found, try again.")

def closeApp(appname):
    os.system(f'TASKKILL /F /IM {appname}')

def open_chrome(website=None):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new(website)

def process_command(query):
    if 'hey bot' in query:
        speak("Hi, How can I help?")

    elif 'wikipedia' in query:
        speak("Searching Wikipedia.........")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 4)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open chrome' in query:
        open_chrome("google.com")

    elif 'open youtube' in query:
        open_chrome("youtube.com")

    elif 'open instagram' in query:
        open_chrome("instagram.com")

    elif 'play music' in query:
        music_dir = 'D:\\Songs'
        songs = os.listdir(music_dir)
        n = random.randint(1, len(songs)-1)
        print(n)
        os.startfile(os.path.join(music_dir, songs[n]))

    elif 'open code' in query:
        code_path = "C:\\Users\\vatsa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    elif 'send email' in query:
        try :
            speak("Whom do you want to send an email?")
            name = takecommand().lower()
            send_email(name)
        except Exception as e:
            speak(e)

    elif 'date' in query:
        speak(datetime.now().date())

    elif 'time' in query:
        time = datetime.now().timetuple()
        time = f"{time[3]} and {time[4]}"
        speak(time)

    elif 'exit' in query:
        speak("Thank you, Byee.")
        sys.exit()

    elif 'close chrome' in query:
        closeApp("chrome.exe")
        # os.system('TASKKILL /F /IM chrome.exe')

    elif 'stop music' in query:
        closeApp("Microsoft.Media.Player.exe")
        # os.system('TASKKILL /F /IM Microsoft.Media.Player.exe')

    # else:
    #     speak("Say it again bro...")

def main():
    wishMe()
    while True:
        speak("Listening....")
        # print("Listening to your command.")
        query = takecommand().lower()
        process_command(query)

if __name__ == "__main__":
    main()