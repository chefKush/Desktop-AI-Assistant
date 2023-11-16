import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")
    speak("I am your desktop assistant . Please tell me how may i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences = 1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")
        
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")
        
        elif 'open my gmail' in query:
            speak('opening your gmail')
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            songs_dir="E:\\NEW SONGS"
            song=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,song[0]))
            #os.startfile(songs_dir) ...(if music path is given correctly this line is enough to play the music) 

        elif 'the time' in query:
            Hour = datetime.datetime.now().strftime("%H")
            Minutes = datetime.datetime.now().strftime("%M")
            speak(f"Sir , The time is {Hour} hours {Minutes} Minutes")

        elif 'open code' in query:
            Codepath = '"C:\\Users\\KUSHI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(Codepath)

        elif 'bye' in query:
            speak('byee , see you again')
            break