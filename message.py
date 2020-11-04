import sqlite3
import pyttsx3
import datetime
import speech_recognition as sr
import serial as s
import time
import random
import wikipedia
import wolframalpha
import os
from database import get_answer
app = wolframalpha.Client("KQ5JJX-48W2UWTH47")
engine = pyttsx3.init()

# Make this a list so that it's easy to parse
good_morning = (" Life gives us new opportunities every day..so hoping today will be full of good luck and prosperity for you!","May everything you dreamed about last night comes true!","Good morning sir . I hope you have a wonderful day.","Life never gives you a second chance. So, enjoy every bit of it. Why not start with this beautiful morning. Good morning sir ","Life is full of uncertainties. But there will always be a sunrise after every sunset. ","Each day is an opportunity to grow. I hope you make the most of it. ","Every morning brings you new hopes and new opportunities. Don’t miss any one of them while you’re sleeping. Good morning ","Every sunrise marks the rise of life over death, hope over despair, and happiness over suffering.","Wake up and make yourself a part of this beautiful morning. A beautiful world is waiting outside your door. Have an enjoyable time!","Welcome this beautiful morning with a smile on your face. I hope you’ll have a great day today.","The best way to start a day is waking up early in the morning and enjoying nature with a cup of coffee. I hope you’re doing this right now.","There is no way you can miss the beauty of today’s morning. I wish this message be your alarm for today.","Mornings define our day. It’s all about how we start every morning. So, get up and make a good start of yet another beautiful day.","Breathing in the fresh morning air makes you healthier and wiser. Don’t ignore the blessings that every morning offers to us.have a good time.","I know you slept tight all night. Now wake up and welcome a new sun so bright, here to make your day right.","you have been blessed with yet another day. What a wonderful way of welcoming the blessing with such a beautiful morning!  "," May you have a day full of sweet wonders ahead!","Sending you good vibes to start your morning with positive energy!","sun has risen wake up to see the most beautiful sunrise ever!!","May your day goes as bright as the sun is today! ","Waking up in such a beautiful morning is a guaranty for a day that’s beyond amazing. I hope you’ll make the best of it.","Nothing is more refreshing than a beautiful morning that calms your mind and gives you reasons to smile.Wishing you a great day.","Another day has just started. Welcome the blessings of this beautiful morning. Rise and shine like you always do. ","Wake up like the sun every morning and light up the world your awesomeness. You have so many great things to achieve today."," no matter how hard yesterday was, today is a new beginning, so buckle up and start your day.")

# Says the given input
def say(audio):
    engine.setProperty("rate",173.8)
    engine.say(audio)
    engine.runAndWait()

# Listens to the microphone for any command
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}")
    except Exception as e:
        print("say that again please....")
        say("say that again please....")
        return"None"
    return query


try:
    ser = s.Serial('com3', 9600, timeout=0)
except Exception as error:
    print("sorry..no device connected at specified port")
    say("i could not find a device connected at the port")
def main():
    while True:
        query = takecommand().lower()
        answer = get_answer(query)
        if answer == "greetings":
            say("hello sir how may i help you?")
        elif query == "sleep" or  query == "sleep jarvis" or query ==  "jarvis sleep" or query ==  "sleep mode jarvis" :
            say("As you wish sir")
            def takecommand2():
                r1 = sr.Recognizer()
                with sr.Microphone() as sou1:
                    audio1 = r1.listen(sou1)
                try:
                    wake = r1.recognize_google(audio1, language='en-in')
                    return wake
                except Exception:
                    wake = "no"
                    return wake
            while True:
                wake = takecommand2().lower()
                if wake == "wake up jarvis" or wake == "jarvis" or wake == "are you there jarvis" or wake == "wake up":
                    break
            while wake!= "wake up jarvis" or wake != "jarvis" or wake != "are you there jarvis" or wake == "wake up":
                time.sleep(1)
                break
            say("yes sir..how may i help you?")
        elif query == "initiate chatbot" or query == 'initiate chartboard':
            import chatbot
        elif "weather" in query or "temperature" in query or "what is the temperature" in query or "jarvis temprature of" in query or "tell me the temprature" in query:
            query = query.replace("jarvis", "")
            print("Okay..searching")
            try:
                result = app.query(query)
                resut1 = next(result.results).text
                print(resut1)
                say("temprature is")
                say(resut1)
            except Exception:
                print("umm. i think you are disconnected from internet")
                print(Exception)
        elif answer == "time":
            now = datetime.now()
            current = now.strftime("%H hours : %M minutes")
            print(current)
            say(current)
        elif answer == "give help":
            print("How can i help you??")
            print("I can tell you the Time,talk,tell the weather")
            say("How can i help you??...I can tell you the Time,talk,tell the weather")
        elif answer == "firefox":
            say("opening sir..")
            print("opening sir..")
            time.sleep(5)
        elif answer == "close_c":
            say("closing sir...")
            print("closing..")
            os.system('TASKKILL /F /IM chrome.exe')
            print("\n" * 70)
            time.sleep(3)
        elif answer == "close_p":
            say("closing sir...")
            print("closing..")
            os.system('TASKKILL /F /IM pycharm-community-2020.2.1.exe')
            print("\n" * 70)
            os.startfile("C:\\Users\\pc\\AppData\\Local\\Mozilla Firefox\\firefox.exe")
        elif answer == "close_f":
            say("closing sir...")
            print("closing....")
            os.system('TASKKILL /F /IM firefox.exe')
            print('\n'*50)
        elif answer == "chrome":
            say("opening sir..")
            print("opening sir..")
            os.startfile("chrome.exe")
            time.sleep(5)
        elif answer == "pycharm":
            say("I know what to do sir...")
            print("I know what to do sir...")
            os.startfile("E:\\pycharm-community-2020.2.1.exe")
            time.sleep(5)
        elif answer == "maths_help":
            while True:
                say("what help do you need in maths")
                print("what help do you need in maths")
                def takecommand3():
                    r1 = sr.Recognizer()
                    with sr.Microphone() as sou1:
                        audio1 = r1.listen(sou1)
                    try:
                        print("listening...")
                        question = r1.recognize_google(audio1, language='en-in')
                        print(question)
                        return question
                    except Exception:
                        print("recognizing...")
                        return "say that again please..."
                question = takecommand3().lower()
                h = 1
                if question == "say that again please...":
                    say("say that again please....")
                    h = 0
                elif question != "say that again please..." and h!=0:
                    say("Okay..searching")
                    print("Okay..searching")
                if h!= 0 :
                    try:
                        result = app.query(question)
                        print(next(result.results).text)
                        say(next(result.results).text)
                    except Exception:
                        print("i think you are disconnected from internet")
                        say("i think you are disconnected from internet")

                elif h == 0:
                    print("what to search i could not understand you")
                    say("what to search i could not understand you")
                    questiona = takecommand3().lower()
                    if questiona == "say that again please...":
                        say("i guess you do not need any help........ending maths protocol")
                        break
                    elif question != "say that again please...":
                        try:
                            result = app.query(question)
                            print(next(result.results).text)
                            say(next(result.results).text)
                        except Exception:
                            print("i think you are disconnected from internet")
                            say("i think you are disconnected from internet")
                print("do you want to end the maths protocol??")
                say("do you want to end the maths protocol??")
                question = takecommand3().lower()
                if question == "end this" or question == "end maths protocol jarvis" or question == "end maths protocol" or question == "terminate maths jarvis" or question == "terminate maths" or question == "close maths protocol" or question == "close maths" or question == "and matt protocol" or question == "and maths protocol" or question == "and match protocol" or question == "and max protocol":
                    break
                else:
                    pass
        elif "joke" in query:
            import pyjokes
            joke = pyjokes.get_joke("english")
            print(joke)
            say(joke)


main()