from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
import pyttsx3

engine = pyttsx3
engine = pyttsx3.init()
engine.say("Hello there")
engine.runAndWait()

def talktoMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#listens for commands

def myCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am ready for your next command")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)


    try:
        command = r.recognize_google(audio)
        print("You said:" + command + '/n')

#loop back to continue to listen for commands

    except sr.UnknownValueError:
        assistant(MyCommand())

    return command

#if statements for executing commands


def assistant(command):

    if 'open Reddit python' in command:
        chrome_path = '/usr/bin/google-chrome'
        url = 'https://www.reddit.com/r/python'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        talkToMe('Chillin bro')

    if 'Hello there' or 'hello there' in command:
        engine.say('General Kenobi')

    if 'email' in command:
        talktoMe('Who is the recipient')
        recipient = myCommand()

        if 'John' in recipient:
            talkToMe('What should I say')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com' , 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('endercrafterdm@gmail.com' , '13256478912')

            #send message
            mail.sendmail(
                mail.sendmail('endercrafterdm@gmail.com' , 'endercrafterdm@gmail.com')








            )

            #close connection
            mail.close()

            talkToMe('Email sent')

talktoMe('I am ready for your command')

while True:
    assistant(myCommand())