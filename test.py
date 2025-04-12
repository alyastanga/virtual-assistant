from time import ctime
import webbrowser
import pywhatkit
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import scipy
import googlemaps
from datetime import datetime
import time

command = input('input some command: ')
command.lower()


def run_command():
    
    if 'time' in command:
        print(ctime())
    if 'song' in command:
        song = command.replace('song', '')
        song = input('what song?')
        url = 'https://open.spotify.com/search/' + song
        webbrowser.get().open(url)
        print('asking spotify to play ' + song)
    if 'where' in command:
        place = command.replace('where is', '')
        geocode = gmaps
    if 'what' in command:
        question = command.replace('what is', '')
        pywhatkit.search(question)
        print(question)
    if 'watch' in command:
        video = command.replace('watch', '')
        pywhatkit.playonyt(video)
    if 'image' in command:
        image = command.replace('show the image of', '')
        url = 'https://www.google.com/search?q=' + image
        webbrowser.get().open(url)
        print('here is what i found for the image of' + image)
    if 'bmi' in command:
        height = input('give a height: ')
        weight = input('give a weight: ')
        print(('the weight is', + int(weight)) + ('the height is', + float(height)))
        bmi = int(weight) / float(height) ** 2
        float(bmi)
        print('the BMI is', + bmi)
        if bmi < 18.5:
            print('You are under weight')
        else:
            print('You are normal')
    if 'open' in command:
        asked = input('website: ')
        url = 'https://' + asked + '.com'
        webbrowser.get().open(url)
    if 'record' in command:
        fs = 44100
        duration = input('how long?: ')
        dur = int(duration)
        print('Recording...')
        rv = sd.rec(int(dur * fs), samplerate=fs, channels=2)
        sd.wait()
        write(input("name a file: "), fs, rv)
        print('Recorded')
