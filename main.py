import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener= sr.Recognizer()
friday=pyttsx3.init()
voices = friday.getProperty("voices")
friday.setProperty('voice',voices[0].id)
def talk(text):
    friday.say(text)
    friday.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'friday' in command:
                 command=command.replace('friday', '')
            else:
                print("call me friday")
    except:
        pass
    return command

def run_friday():
    command=take_command()
    if 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('curreunt time is' + time)
    elif 'play' in command:
        song= command.replace('play', '')
        talk ('playing' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about'   in command:
        look_for =command.replace('tell me about', '')
        info=wikipedia.summary(look_for,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('sorry ,  i have a boyfriend')
    elif 'how ' in command:
        talk('i am fine what about you')
    else:
        talk("i did not get it but i am going to search it for you")
        pywhatkit.search(command)
while True :
    run_friday()
