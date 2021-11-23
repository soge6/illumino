from typing import Text
import speech_recognition
import pyttsx3

recongnizer = speech_recognition.Recognizer()

while True:
    try:

        with speech_recognition.Microphone() as mic:

            recongnizer.adjust_for_ambient_noise(mic, duration=0.2 )
            audio =  recongnizer.listen(mic)

            Text = recongnizer.recognize_google(audio)
            Text = Text.lower()


            print(f"Recognized {Text}")

    except speech_recognition.UnknownValueError():

        recongnizer = speech_recognition.Recognizer()
        continue