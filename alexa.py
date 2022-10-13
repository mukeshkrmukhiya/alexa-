import sys
import wikipedia
import speech_recognition as sr
rec_ny = sr.Recognizer()

import pywhatkit 
import datetime

Dtime = datetime.datetime.now()



import pyttsx3 
engine_ttv = pyttsx3.init()

voices = engine_ttv.getProperty("voices")
engine_ttv.setProperty("voice", voices[1].id)
# engine_ttv.setProperty("rate", 120)
def talk(txt):
    engine_ttv.say(txt)
    engine_ttv.runAndWait()

def take_cmd():
    try: 
        with sr.Microphone() as source:
            print("Listening...")
            talk("Listening")
            voice_cmd = rec_ny.listen(source)
            text_conv_cmd = rec_ny.recognize_google(voice_cmd)
            
            print(text_conv_cmd)
            # print("random text ")
            global sm_cmd
            sm_cmd = text_conv_cmd.lower()
           
            
            if "alexa" in sm_cmd: 
                if "hey alexa" in sm_cmd: 
                    text_conv_cmd = sm_cmd.replace("hey alexa", '')
                if "hi alexa" in sm_cmd: 
                    text_conv_cmd = sm_cmd.replace("hi alexa", '')
                else:
                    text_conv_cmd = sm_cmd.replace("alexa", '')
                print(text_conv_cmd)   
        # talk(text_conv_cmd)
    except:
        pass
    return text_conv_cmd


def run_alexa():
    command = take_cmd()
    print(command)

    if "stop" in command:
        sys.exit()
    elif "play" in command:
        play_cmd = command.replace("play", "")
        print("playing..." + play_cmd )
        talk("playing " + play_cmd)
        pywhatkit.playonyt(play_cmd)
    elif "time" in command:
        strf_time = Dtime.strftime("%I "+ "%M " + "%p ")
        print(strf_time)
        talk(strf_time)
    elif "date" in command:
        strf_date = Dtime.strftime("%d "+ "%B " + "%Y ")
        talk(strf_date)
    elif "what is"or "who is" or "tell me about" in command:
        Qsn_cmd = command.replace("what is " , "")
        Qsn_cmd = command.replace("who is" , "")
        Qsn_cmd = command.replace("tell me about" , "")
        
        inform = wikipedia.summary(Qsn_cmd, 3)
        print(inform)
        talk(inform)      
    else: 
        talk("Sorry, please say again ")
    



        
         


# while "alexa" in sm_cmd
# print("printing sm_cmd: " + sm_cmd)

while True :
    run_alexa()

