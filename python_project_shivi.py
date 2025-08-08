import speech_recognition as sr
import webbrowser
import time
from gtts import gTTS
import os
import playsound 

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()

def speak(text):
    print("Assistant:", text)
    tts = gTTS(text=text, lang='en', slow=False)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def processCommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "open my profile" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com/feed/")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/shashwatchamp")

if __name__ == "__main__":
    speak("Initializing Shivi")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if "hey siri" in word.lower():
                speak("What do you want me to do?")
                time.sleep(1)  # wait to ensure the sentence is spoken before mic access

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print("Command received:", command)
                    processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase")
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print("Unexpected error:", e)

