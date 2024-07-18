import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
vID=1
vName="siri"
engine.setProperty('voice',voices[vID].id)

def speak(audio):
        # print(audio,"\n")

        # label["text"]=audio
        print(audio)
        engine.say(audio)
        engine.runAndWait()

def start_listening():
        
        with sr.Microphone() as source:
            speak("Listening")
            recognizer.pause_threshold=1
            recognizer.energy_threshold=800
            audio = recognizer.listen(source)
        try:
            # label["text"] = "Recognising..."
            print('Recognizing...')
            query = recognizer.recognize_google(audio, language='en-in')
            speak("You said " + query)
            return query
        except Exception as e:
            # print(e)
            speak("Say that again please....")
            return "None"

        return query
    
text = start_listening()
print(text)
    
    