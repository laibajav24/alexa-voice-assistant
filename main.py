import os
import pywhatkit
import pyttsx3
import webbrowser
import speech_recognition as sr
import requests
from openai import OpenAI
from dotenv import load_dotenv
from music import musicLibrary

# Load the environment variables from the .env file
load_dotenv()


#news api
news_apikey = os.getenv("news_apikey")

# Initialize the AI response client
client = OpenAI(
    api_key=os.getenv("api_key"),
    base_url="https://api.groq.com/openai/v1"
)


response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response.choices[0].message.content)
recognizer=sr.Recognizer()

#function for speach comand
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

#command function
def processCommand(c):
    c = c.lower().strip()
    print("Command:", c)

    if "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        speak("Opening facebook")
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
        speak("Opening instagram")
    elif c.startswith("open "):
        site = c.replace("open ", "").strip()
        # remove common words people might say
        site = site.replace("website", "").replace("web", "").replace("the", "").strip()
        url = f"https://www.{site}.com"
        speak(f"Opening {site}")
        webbrowser.open(url)

    elif c.startswith("play "):
        # Extract the full song name after "play "
        song = c.replace("play ", "").strip()
        
        # Look up the song link directly in your imported dictionary
        if song in musicLibrary:
            link = musicLibrary[song]
            speak(f"Playing {song}")
            webbrowser.open(link) # Opens the link in your browser
        else:

            
            speak(f"Searching online for {song}")
            # Automatically searches YouTube and plays the top result
            pywhatkit.playonyt(song)
            
    elif "news" in c:
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_apikey}")
        data=r.json()
        for article in data["articles"]:
            print(article["title"])
            speak(article["title"])
    else:
        try:

            response = client.chat.completions.create(

                model="llama-3.1-8b-instant",

                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI voice assistant."
                    },

                    {
                        "role": "user",
                        "content": c
                    }
                ]

            )

            reply = response.choices[0].message.content

            print("AI:", reply)

            speak(reply)

        except Exception as e:

            print("Error:", e)

            speak("Sorry, I could not connect to AI.")

if __name__=="__main__":
    speak("initializing alexa")
    while True:
      
        print("Listening...")
        
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("recognizing...")
            
                audio=recognizer.listen(source,timeout=2,phrase_time_limit=1)
            
            word=recognizer.recognize_google(audio)
            word = word.lower().strip()
            print(f"you said {word}")

            #reply you said alexa
            if "alexa" in word:
                speak("yeah")
                #listen for command
                with sr.Microphone() as source:

                    print("alexa is activated, listening for command...")
                    print("recognizing...")

                    recognizer.adjust_for_ambient_noise(source, duration=1)

                    audio=recognizer.listen(source,timeout=5,phrase_time_limit=5)
                    command=recognizer.recognize_google(audio)
                    #process command
                    processCommand(command)

                # command(command)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except Exception as e:
            print(f"Could not request results; {e}")