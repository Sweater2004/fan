import pyttsx3
import speech_recognition as sr
import sys
xczv=sys.path.append("C:/Program Files/FUN/goloSo.py" )
import goloSo 
import pyautogui
from subprocess import call
import time
from threading import Thread 
def listen_command(): 
            r = sr.Recognizer()  
            with sr.Microphone() as source:  
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)  
                audio = r.listen(source)  
                try:  
                    our_speech = r.recognize_google(audio, language='ru-RU' 'en-US')
                    return our_speech  
                except sr.UnknownValueError:                  
                    return 'Ошибка'  
                except sr.RequestError:  
                    return 'Ошибка' 

def asd(message):
    message = message.lower()
    if 'запуск' in message:
        qwerty=Thread(target = func2)
        say_message('Голосовой помощник Fun готов к работе сэр!')
        qwerty.start()  
        call(["python", "C:/Program Files/FUN/goloSo.py"])
        qwerty.join()
    elif "Fun" in message:
        qwerty=Thread(target = func2)
        say_message('Голосовой помощник Fun готов к работе сэр!')
        qwerty.start()  
        call(["python", "C:/Program Files/FUN/goloSo.py"])
        qwerty.join()
    elif "Fan" in message:
        qwerty=Thread(target = func2)
        say_message('Голосовой помощник Fun готов к работе сэр!')
        qwerty.start()  
        call(["python", "C:/Program Files/FUN/goloSo.py"])
        qwerty.join()
    elif "фан" in message:
        qwerty=Thread(target = func2)
        say_message('Голосовой помощник Fun готов к работе сэр!')
        qwerty.start()  
        call(["python", "C:/Program Files/FUN/goloSo.py"])
        qwerty.join()
    elif "запуск фан" in message:
        qwerty=Thread(target = func2)
        say_message('Голосовой помощник Fun готов к работе сэр!')
        qwerty.start()  
        call(["python", "C:/Program Files/FUN/goloSo.py"])
        qwerty.join()
    elif "запуск fan" in message:
        qwerty=Thread(target = func2)
        say_message('Голосовой помощник Fun готов к работе сэр!')
        qwerty.start()  
        call(["python", "C:/Program Files/FUN/goloSo.py"])
        qwerty.join()
    elif "запуск fun" in message:
        qwerty=Thread(target = func2)
        say_message('Голосовой помощник Fun готов к работе сэр!')
        qwerty.start()  
        call(["python", "C:/Program Files/FUN/goloSo.py"])
        qwerty.join()
    elif "fun запуск" in message:
        qwerty=Thread(target = func2)
        say_message('Голосовой помощник Fun готов к работе сэр!')
        qwerty.start()  
        call(["python", "C:/Program Files/FUN/goloSo.py"])
        qwerty.join()
    elif "фан запуск" in message:
        qwerty=Thread(target = func2)
        say_message('Голосовой помощник Fun готов к работе сэр!')
        qwerty.start()  
        call(["python", "C:/Program Files/FUN/goloSo.py"])
        qwerty.join()
            

    
    
def func2():  
    time.sleep(7) 
    pyautogui.press('z')
    time.sleep(1)
    pyautogui.press('z')
    time.sleep(1)
    pyautogui.press('z')
def say_message(message):
    engine.say(message)
    engine.runAndWait()




engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

while True:
    command = listen_command()
    asd(command)
