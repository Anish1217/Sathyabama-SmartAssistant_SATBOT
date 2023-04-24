import nltk
from nltk.stem import WordNetLemmatizer
import pyttsx3
import sys
import re
from urllib.request import urlopen
from time import strftime
import webbrowser
import smtplib
import requests
import subprocess
from bs4 import BeautifulSoup
import wikipedia
import wolframalpha
import ctypes
import subprocess
import datetime
import speech_recognition as sr
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import os
import math
from datetime import datetime, timedelta
import io
import random
import string
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
from subprocess import call


class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


root = tk.Tk()
root.title("Satbot Assistant")
lbl = ImageLabel(root)
lbl.pack()
lbl.load(r'\Users\dell\Desktop\Satbot\Satbot.gif')


def mainWin():
    root.destroy()


root.after(3000, mainWin)
root.mainloop()


engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 170)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

welcomeMessage = 'Hello, I am Satbot, your Assistant. What can I do for you ?'
print(welcomeMessage)
engine.say(welcomeMessage)
engine.runAndWait()

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

app_id = 'wolfram_API'


def newCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Your wish is my command...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        print('Sorry I can\'t understand')
        command = newCommand()
    return command


def SatbotResponse(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def assistant(command):
    if 'your name' in command:
        SatbotResponse('My name is Satbot. Nice to meet you!')
    elif 'who are you' in command:
        SatbotResponse('I\'m Satbot, your assistant! What can i do for you ?')
    elif 'a joke' in command:
        SatbotResponse(
            'My neighbor has been mad at his wife for sunbathing. I personally am on the fence.')
    elif 'old are you' in command:
        SatbotResponse('I was launched in November 2022 by Jayanth Tunk')
    elif 'what can you do' in command:
        SatbotResponse(
            'I can do a lot of things, to help you throughout your day.')
    elif 'help me' in command:
        SatbotResponse('I\'m here to help, you can ask me what I can do.')
    elif 'you single' in command:
        SatbotResponse('I am in a relationship with Harry Potter3')
    elif 'languages do you speak' in command:
        SatbotResponse(
            'I currently speak English but I am also learning a lot of other languages ')
    elif 'love you' in command:
        SatbotResponse(
            'I love myself too...')
    elif 'are you dating someone' in command:
        SatbotResponse(
            'I am currently dating Harsha BRO ! who is also called as daddy ')

    # Greet Satbot
    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            SatbotResponse('Hello, Good morning!')
        elif 12 <= day_time < 16:
            SatbotResponse('Hello, Good afternoon!')
        elif 16 <= day_time < 18:
            SatbotResponse('Hello, Good evening!')
        else:
            SatbotResponse('Hello, Good night!')
    elif 'thank you' in command:
        SatbotResponse('You\'re Welcome!')

    # Make Satbot stop
    elif 'exit' in command:
        SatbotResponse('Bye bye. Have a nice day!')
        sys.exit()

    # Open Twitter
    elif 'open twitter' in command:
        reg_ex = re.search('open twitter (.*)', command)
        url = 'https://www.twitter.com/'
        if reg_ex:
            handle = reg_ex.group(1)
            url = url + handle
        webbrowser.open(url)
        SatbotResponse(
            'Opening Twitter.')

    elif 'open instagram' in command:
        reg_ex = re.search('open instagram (.*)', command)
        url = 'https://www.instagram.com/'
        if reg_ex:
            handle = reg_ex.group(1)
            url = url + handle
        webbrowser.open(url)
        SatbotResponse(
            'Opening Instagram.')

    elif 'open sathyabama' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\CB_3.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
        SatbotResponse(
            'Opening Sathyabama Website')

    elif 'open placements' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\CB_4.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
        SatbotResponse(
            'Opening Sathyabama Placements')
    elif 'open lms' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\CB_5.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
        SatbotResponse(
            'Opening Sathyabama LMS')
    elif 'open erp' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\CB_6.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
        SatbotResponse(
            'Opening Sathyabama ERP')

    elif 'open map' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\Map.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
        SatbotResponse(
            'Opening Sathyabama Map')

    elif 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        SatbotResponse(
            'Opening Reddit.')

    elif 'open' in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain + ".com"
            webbrowser.open(url)
            SatbotResponse(
                'Opening ' + domain)

    # Make a search on Google
    elif 'search' in command:
        reg_ex = re.search('search (.+)', command)
        if reg_ex:
            subject = reg_ex.group(1)
            url = 'https://www.google.com/search?q=' + subject
            webbrowser.open(url)
            SatbotResponse(
                'Searching for ' + subject + ' on Google.')

    # Make a type command
    elif 'type' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\CB_1.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()

    # Play a song on Youtube
    elif 'play' in command:
        reg_ex = re.search('play (.+)', command)
        if reg_ex:
            searchedSong = reg_ex.group(1)
            url = 'https://www.youtube.com/results?q=' + searchedSong
            try:
                source_code = requests.get(url, headers=headers, timeout=15)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, "html.parser")
                songs = soup.findAll('div', {'class': 'yt-lockup-video'})
                song = songs[0].contents[0].contents[0].contents[0]
                hit = song['href']
                webbrowser.open('https://www.youtube.com' + hit)
                SatbotResponse('Playing ' + searchedSong + ' on Youtube.')
            except Exception as e:
                webbrowser.open(url)
                SatbotResponse('Searching for ' +
                               searchedSong + ' on Youtube.')

    # Send Email
    elif 'email' in command:
        SatbotResponse('Who is the recipient?')
        recipient = newCommand()
        if 'someone' in recipient:
            SatbotResponse('What should I say to him?')
            content = newCommand()
            try:
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('sender_email', 'sender_password')
                mail.sendmail('sender_email', 'receiver_email', content)
                mail.close()
                SatbotResponse(
                    'Email has been sent successfuly.')
            except Exception as e:
                print(e)
        else:
            SatbotResponse('I don\'t know anyone named ' + recipient + '.')

    # Get current time
    elif 'time' in command:
        now = datetime.datetime.now()
        SatbotResponse('Current time is %d:%d.' %
                       (now.hour, now.minute))

    # Get recent news
    elif 'news' in command:
        try:
            news_url = "https://news.google.com/news/rss"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()
            soup_page = BeautifulSoup(xml_page, "html.parser")
            news_list = soup_page.findAll("item")
            for news in news_list[:5]:
                SatbotResponse(news.title.text)
        except Exception as e:
            print(e)

    # Lock the device
    elif 'lock' in command:
        try:
            SatbotResponse("Locking the device.")
            ctypes.windll.user32.LockWorkStation()
        except Exception as e:
            print(str(e))

    # Sathyabama Python programs COD LAB
    elif 'binary to decimal' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\BinaryToDecimal.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
            SatbotResponse(
                'Python program to convert Binary to decimal')

    elif 'lowercase to uppercase' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\LowercaseToUppercase.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
            SatbotResponse(
                'Python program to convert Lowercase to Uppercase')

    elif 'merge sort' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\MergeSort.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
            SatbotResponse(
                'Python program to implement Merge Sort')
    elif 'palindrome' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\Panlindrome.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
            SatbotResponse(
                'Python program to check whether number is Palindrome or not.')

    elif 'prime or not' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\PrimeOrNot.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
            SatbotResponse(
                'Python program to check whether number is prime or not.')

    elif 'pyramid' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\Pyramid.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
            SatbotResponse(
                'Python program to print pyramid pattern')

    elif 'reverse digits' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\ReverseDigits.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
            SatbotResponse(
                'Python program to reverse digits')

    elif 'vowel or consonant' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\VowelOrConsonant.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
            SatbotResponse(
                'Python program to check if the alphabet is Vowel or consonant')

    elif 'fibonacci series' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\FibnacciSeries.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()
            SatbotResponse(
                'Python program to print Fibonacci Series')

    # Setting Alarm
    elif 'alarm' in command:
        class Callpy(object):
            def __init__(self, path=r"C:\Users\dell\Desktop\Satbot\CB_2.py"):
                self.path = path

            def call_python_file(self):
                call(["python", "{}".format(self.path)])
        if __name__ == "__main__":
            c = Callpy()
            c.call_python_file()

    # Ask general questions
    elif 'tell me about' in command:
        reg_ex = re.search('tell me about (.*)', command)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                SatbotResponse(wikipedia.summary(topic, sentences=3))
        except Exception as e:
            SatbotResponse(e)
    elif any(c in command for c in ("what is", "what\'s")):
        reg_ex = re.search(' (.*)', command)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                SatbotResponse(wikipedia.summary(topic, sentences=2))
        except Exception as e:
            SatbotResponse(e)
    else:
        try:
            # wolframalpha
            client = wolframalpha.Client(app_id)
            res = client.query(command)
            answer = next(res.results).text
            SatbotResponse(answer)
        except:
            try:
                # wikipedia
                SatbotResponse(wikipedia.summary(command, sentences=2))
            except Exception as e:
                SatbotResponse(e)

    ######

    ######
while True:
    assistant(newCommand())
