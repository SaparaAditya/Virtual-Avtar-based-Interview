# import sounddevice as sd
# from scipy.io.wavfile import write
# import speech_recognition as sr


# fs = 44100  # Sample rate
# seconds = 5  # Duration of recording

# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# sd.wait()  # Wait until recording is finished
# write('output.wav', fs, myrecording)  # Save as WAV file


# def extract_text_from_wav(wav_file):
#     # Initialize the recognizer
#     recognizer = sr.Recognizer()

#     # Load audio file
#     with sr.AudioFile(wav_file) as source:
#         audio_data = recognizer.record(source)  # Record the entire audio file

#     try:
#         # Recognize speech using Google Speech Recognition
#         text = recognizer.recognize_google(audio_data)
#         return text
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print(f"Could not request results from Google Speech Recognition service; {e}")

# # Usage
# wav_file = "output.wav"
# text = extract_text_from_wav(wav_file)
# print("Extracted text:", text)

import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr

fs = 44100  # Sample rate
seconds = 5  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file

def extract_text_from_wav(wav_file):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)  # Record the entire audio file

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Usage
wav_file = "output.wav"
text = extract_text_from_wav(wav_file)
print("Extracted text:", text)

