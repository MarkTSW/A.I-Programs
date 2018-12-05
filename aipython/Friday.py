from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

class friday:
    def talkToMe(audio):
        print(audio)
        tts = gTTS(text = audio, lang = 'en')
        tts.save('audio.mp3')
        os.system('mpg123 audio.mp3')
    def myCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("I am ready to talk")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration = 1)
        try:
            command = r.recognize_google(audio)
            print("You said : " + command + "/n")
        except sr.UnknownValueError:
            assistant(myCommand())
        return command
    def assistant(command):
        if "open gmail" in command:
            firefox_path = "/etc/firefox-60.0.2/firefox/firefox"
            url = "https://mail.google.com/mail/u/0/?tab=wm#inbox"
            webbrowser.get(firefox_path).open(url)
        if "Hello Buddy what's up" in command:
            talkToMe("Nice")
        if "email" in command:
            talkToMe("Who is the dude")
            recipient = myCommand()
            talkToMe("What should i say")
            content = myCommand()
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("username", "password")
            mail.sendmail("PERSON NAME", "emailaddress@gmail.com", content)
            mail.close()
            talkToMe("Email send"
    talkToMe("What is next")﻿