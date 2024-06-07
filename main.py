import speech_recognition as sr
import pyaudio
import pywhatkit

def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Nimadir gapiring...")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f"Siz aytingiz: {text}")
    return text


text = get_audio()

pywhatkit.playonyt(text)
