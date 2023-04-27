try:
    import speech_recognition as sr
    import pyttsx3
    import pywhatkit
    import datetime
    import wikipedia
    import pyjokes
    import wolframalpha
except:
     print("I need internet connection")
     breakpoint()

client = wolframalpha.Client("QTQX2R-43GUV6L7YX")
res = client.query('weather current location')
# print(next(res.results).text)

r = sr.Recognizer()
engine = pyttsx3.init()  # initialize python text reader
voices = engine.getProperty('voices')
engine.setProperty('volume', 1.0)  # assistant volume
engine.setProperty('rate', 150)  # word saying speed
engine.setProperty('voice', voices[1].id)  # change voice to female. male is index 0
engine.say('my name is rashmika')
engine.say('I am your assistant, how can i help you ?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            r.adjust_for_ambient_noise(source)  # cancelling noise
            # voice = r.record(source, duration=5)
            voice = r.listen(source)  # listen receiver voice
            print('recording...')
            command = r.recognize_google(voice)  # connect to google voice api
            command = command.lower()
            if 'alexa' in command:  # remove assistant's name
                command = command.replace('alexa', '')
                print(command)

            return command

    except:
        pass


def run_alexa():
    command = take_command()
    try:
        if command:
            if 'play' in command:
                song = command.replace('play', '')
                talk('playing' + song)
                pywhatkit.playonyt(song)  # connect youtube
                print(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')  # set current time
                print(time)
                talk('current time is ' + time)
            elif 'who is' in command:
                person = command.replace('who is', '')
                print(person)
                info = wikipedia.summary(person, 1)  # connect to wikipedia
                print(info)
                talk(info)
            elif 'joke' in command:
                talk(pyjokes.get_joke())  # connect joke
            elif 'who are you' in command:
                talk('I am rashmika.')
            else:
                talk(command)
                print(command)
        else:
            talk('please say something')

    except:
        talk('something went wrong')
# talk(next(res.results).text)
while True:
    run_alexa()
# except:
#     print("I need internet connection")