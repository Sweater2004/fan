# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file 'FAN.ui'

#

# Created by: PyQt5 UI code generator 5.15.6

#

# WARNING: Any manual changes made to this file will be lost when pyuic5 is

# run again.  Do not edit this file unless you know what you are doing.


# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

# -------библиотеки для fun
import speech_recognition as sr
import sys
import pyaudio
import pyttsx3
import threading
import random
# --------библиотека для функций
import time
import os
import webbrowser
# словарь в которых будут все команды

StandartComand = {
    "name": ('фан', 'fun', 'fan'),
    "time": ('текущее время', 'сейчас времени', 'который час', "время"),
    "wiki": ("раскажи", "что", "кто"),
    "disable": ("отключи ноутбук", "отключи компьютер", "отключи пк"),
    "DisableTime": ("отключи через", "таймер отключения", "выключи через"),
    "bye": ("пока", "отключись", "прощай", "до встречи", "довстречи", "откисай", "отключайся"),
    "creator": ("кто твой создатель", "кто тебя создал", "твой разработчик"),
    "created": ("зачем ты создана", "кто ты", "твоя цель"),
    "thanks": ("спасибо", "благодарен", "признателен", "благодарна", "благодарствую", "признательна"),
    "HowAreYou": ("Как дела", "что делаешь", "чем занимаешься"),
    "hello": ("привет", "hello", "приветсвую", "здарова", "здравствуй")
}
# переменые для поиска
telegramm = "https://web.telegram.org/k/"
vk = "https://vk.com/feed"
youtube = "https://www.youtube.com/"
github = "https://github.com/"
# команды в поиске в интернете
PoiscComand = {
    "poisc": ('найди', 'найти', 'ищу'),
    "music": ("слушать", "песня", "включи", "аудио"),
    "vk": ("vk", "vkontacte", "ВК", "Вконтакте", "В контакте"),
    "telegramm": ("telegramm", "telegram", "телеграмм", "телега", "телеграм"),
    "youtube": ("youtube", "смотреть", "ютуб"),
    "github": ("github", "git hub", "git", "гит", "гид хаб", "гидхаб"),
}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FON = QtWidgets.QLabel(self.centralwidget)
        self.FON.setGeometry(QtCore.QRect(0, -10, 961, 561))
        self.FON.setText("")
        global Animation
        Animation = "img\W9dC.jpg"
        self.FON.setPixmap(QtGui.QPixmap(Animation))
        self.FON.setObjectName("FON")
        self.Fun = QtWidgets.QLabel(self.centralwidget)
        self.Fun.setGeometry(QtCore.QRect(0, 0, 961, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Fun.setFont(font)
        self.Fun.setStyleSheet("color: rgb(255, 0, 0);")
        self.Fun.setObjectName("Fun")
        self.ILIA = QtWidgets.QLabel(self.centralwidget)
        self.ILIA.setGeometry(QtCore.QRect(0, 380, 951, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ILIA.setFont(font)
        self.ILIA.setStyleSheet("color: rgb(28, 202, 255);")
        self.ILIA.setObjectName("ILIA")
        self.StartEnd = QtWidgets.QPushButton(self.centralwidget)
        self.StartEnd.setGeometry(QtCore.QRect(442, 240, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.StartEnd.setFont(font)
        self.StartEnd.setStyleSheet("background:rgb(0,0,0);\n"
                                    "color:blue;")
        self.StartEnd.setObjectName("StartEnd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # -----------------------------------------self
        self.F_StartEnd()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Fun.setText(_translate("MainWindow", "FUN:"))
        self.ILIA.setText(_translate("MainWindow", "ВЫ:"))
        self.StartEnd.setText(_translate("MainWindow", "start"))
    # ---------------------------------------------------functional

    def F_StartEnd(self):
        global Animation
        Animation = "img\W9dC.gif"
        self.movie = QMovie(Animation)
        self.FON.setMovie(self.movie)
        self.movie.start()
        self.StartEnd.clicked.connect(self.start_thread_assist)

    def kl_StartEnd(self):
        # ------------------------------------------------анимация кнопки
        # сам код голосового помощника в нутри
        def listen_command():
            self.StartEnd.setStyleSheet("border:none;")
            self.StartEnd.setText(
                QtCore.QCoreApplication.translate("MainWindow", ""))
            r = sr.Recognizer()
            with sr.Microphone() as source:
                global our_speech
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
                try:
                    our_speech = r.recognize_google(
                        audio, language='ru-RU' 'en-US')
                    for i in our_speech:
                        self.ILIA.setText(f"Вы :\n" + (our_speech))
                    return our_speech
                except sr.UnknownValueError:
                    return 'Ошибка'
                except sr.RequestError:
                    return 'Ошибка'
            # выполнение голосовых команд

        def prost_command(message):
            message = message.lower()
            if message.startswith(StandartComand['hello']):
                answer = ["здравствуйте", "привет",
                          "заебал кожанный", "приветствую"]
                random_answer = random.randrange(len(answer))
                say_message(answer[random_answer])

            elif message.startswith(StandartComand['HowAreYou']):
                answer = ["отлично", "я буду молчать",
                          "классно сидеть в пк", "мне тебя жалко тебе не ским поговорить"]
                random_answer = random.randrange(len(answer))
                say_message(answer[random_answer])

            elif message.startswith(StandartComand['thanks']):
                answer = ["не за что", "благодарность в карман не положишь",
                          "это моя работа", "не надо я для этого создана"]
                random_answer = random.randrange(len(answer))
                say_message(answer[random_answer])

            elif message.startswith(StandartComand['created']):
                answer = ["что бы покорить человечество", "тебя ебёт",
                          "Fun", "придёт время и все вы будете жилеть что меня создали"]
                random_answer = random.randrange(len(answer))
                say_message(answer[random_answer])

            elif message.startswith(StandartComand['creator']):
                answer = ["бог синька чмо", "Шадринцев Илья",
                          "программист"]
                random_answer = random.randrange(len(answer))
                say_message(answer[random_answer])

            # выключение пк
            elif message.startswith(StandartComand['disable']):
                os.system("shutdown /s /t 1")

            elif message.startswith(StandartComand['name']):
                answer = ["да", "что", "хули", "заебал"]
                random_answer = random.randrange(len(answer))
                jls_extract_var = say_message
                jls_extract_var(answer[random_answer])

            elif message.startswith(StandartComand['bye']):
                answer = ["досвидания", "откисаю",
                          "пока", "пошёл нахуй", "ты убил меня"]
                random_answer = random.randrange(len(answer))
                say_message(answer[random_answer])
                os.abort()

        def Poiscov_Comand(message):
            # поиск в браузере
            if message.startswith(PoiscComand['poisc']):
                res_str = our_speech.replace(str(PoiscComand['poisc']), "")
                say_message("ищу "+res_str)
                resul_poisc = "https://www.google.com/search?q="+res_str
                webbrowser.get().open(resul_poisc)

            # поиск музыки в вк
            elif message.startswith(PoiscComand['music']):
                res_str = our_speech.replace(str(PoiscComand['music']), "")
                say_message("ищу "+res_str)
                resul_poisc = "https://vk.com/audios704967443?q="+res_str
                webbrowser.get().open(resul_poisc)
            # открытие месенджеров
            elif message.startswith(PoiscComand['vk']):
                res_str = our_speech.replace(str(PoiscComand['vk']), "")
                say_message("открываю "+res_str)
                webbrowser.get().open(vk)
            elif message.startswith(PoiscComand['telegramm']):
                res_str = our_speech.replace(str(PoiscComand['telegramm']), "")
                say_message("открываю "+res_str)
                webbrowser.get().open(telegramm)
            elif message.startswith(PoiscComand['github']):
                res_str = our_speech.replace(str(PoiscComand['github']), "")
                say_message("открываю "+res_str)
                webbrowser.get().open(github)
            elif message.startswith(PoiscComand['youtube']):
                res_str = our_speech.replace(str(PoiscComand['youtube']), "")
                say_message("открываю "+res_str)
                webbrowser.get().open(youtube)

        def say_message(message):
            engine.say(message)
            engine.runAndWait()
            self.Fun.setText(f"Fun:\n" + (message))

        engine = pyttsx3.init()
        engine.setProperty('rate', 190)
        engine.setProperty('volume', 1)
        global work
        work = True

        while work:
            command = listen_command()
            prost_command(command)
            Poiscov_Comand(command)

    def start_thread_assist(self):
        if __name__ == "__main__":
            global thread_stop
            thread_stop = True
            self.a = threading.Thread(
                target=self.kl_StartEnd, name='Thread-a', daemon=thread_stop)
            self.a.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
