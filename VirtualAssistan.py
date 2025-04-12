import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import google_auth_oauthlib
from time import ctime
import webbrowser
import time
import googlemaps
import sounddevice as sd
from scipy.io.wavfile import write
import fileinput
from webbrowser import Chrome
import googlesamples

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command(ask = False):
    try:
        with sr.Microphone() as source:
            if ask:
                print(ask)
                talk(ask)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
        print('Sorry, I did not get that.')
        talk('Sorry, I did not get that.')
    except sr.RequestError:
        print('Sorry, my speech service is down.')
        talk('Sorry, my speech service is down.')
    return command


def run_alexa():
    command = take_command()
    time.sleep(1)
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        url = 'https://open.spotify.com/search/' + song
        webbrowser.get().open(url)
        talk('asking spotify to play ' + song)
    if 'watch' in command:
        video = command.replace('watch', '')
        pywhatkit.playonyt(video)
        talk('opening')
    if 'calculate the bmi' in command:
        height = input('give a height: ')
        weight = input('give a weight: ')
        print(('the weight is', + int(weight)) + ('the height is', + float(height)))
        talk(('the weight is', + int(weight)) + ('the height is', + float(height)))
        bmi = int(weight) / float(height) ** 2
        float(bmi)
        print('the BMI is', + bmi)
        talk('the BMI is' + str(bmi))
        if bmi < 18.5:
            print('under weight')
            talk('under weight')
        else:
            print('normal')
            talk('normal')
    if 'find the sum' in command:
        number1 = input('give 1st number: ')
        number2 = input('give 2nd number: ')
        print('you gave me a number : '+number1+' and '+number2)
        talk('you gave me a number : '+number1+' and '+number2)
        n1_n2 = int(number1) + int(number2)
        int(n1_n2)
        print('the sum is', + n1_n2)
        talk('the sum is' + str(n1_n2))
    if 'find the difference' in command:
        number1 = input('give 1st number: ')
        number2 = input('give 2nd number: ')
        print('you gave me a number : ' + number1 + ' and ' + number2)
        talk('you gave me a number : ' + number1 + ' and ' + number2)
        n1_n2 = int(number1) - int(number2)
        int(n1_n2)
        print('the product is', + n1_n2)
        talk('the product is' + str(n1_n2))
    if 'find the product' in command:
        number1 = input('give 1st number: ')
        number2 = input('give 2nd number: ')
        print('you gave me a number : ' + number1 + ' and ' + number2)
        talk('you gave me a number : ' + number1 + ' and ' + number2)
        n1_n2 = int(number1) * int(number2)
        int(n1_n2)
        print('the product is', + n1_n2)
        talk('the product is' + str(n1_n2))
    if 'find the quotient' in command:
        number1 = input('give 1st number: ')
        number2 = input('give 2nd number: ')
        print('you gave me a number : ' + number1 + ' and ' + number2)
        talk('you gave me a number : ' + number1 + ' and ' + number2)
        n1_n2 = int(number1) / int(number2)
        int(n1_n2)
        print('the quotient is', + n1_n2)
        talk('the quotient is' + str(n1_n2))
    if 'start voice record' in command:
        fs = 44100
        duration = take_command('how long?: ')
        dur = int(duration)
        print('Recording...')
        rv = sd.rec(int(dur * fs), samplerate=fs, channels=2)
        sd.wait()
        write(input("name a file: "), fs, rv)
        print('Recorded')
    elif 'what' in command:
        question = command.replace('what', '')
        pywhatkit.info(question, 5)
        print(question)
        talk(question)
    if 'image' in command:
        image = command.replace('show the image of', '')
        url = 'https://www.google.com/search?q=' + image
        webbrowser.get().open(url)
        talk('here is what i found for the image of' + image)
    if 'where' in command:
        place = command.replace('where is', '')
        url = 'https://www.google.com/maps/place/' + place + '/@' + '/data='
        webbrowser.get().open(url)
        talk('the location of' + place)
    elif 'time' in command:
        print(ctime())
        talk(ctime())
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'are you there' in command:
        print('Yes I am')
        talk('Yes I am')
    if 'how are you' in command:
        print('I am good, I hope you too')
    if 'name' in command:
        print('My name is Alexa.')
        talk('My name is Alexa')
    elif 'are you in relationship' in command:
        print('Yes i am, i have relationship with wifi.')
        talk('Yes i am, i have relationship with wifi.')
    elif 'i love you' in command:
        print('i love you too.')
        talk('i love you too.')
    elif 'guess the most handsome in the world' in command:
        print('the most handsome in the world is Peter Dela Cruz')
        talk('the most handsome in the world is Peter Dela Cruz')
    elif 'exit' in command:
        exit()

time.sleep(1)
print('listening...')
talk('How can I help you')
while True:
    run_alexa()

