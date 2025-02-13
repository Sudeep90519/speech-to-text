import os
from logger import logging
import speech_recognition as sr
import pyaudio
from gtts import gTTS #using google test to speech library
from pydub import AudioSegment
import pyttsx3




def textToSpeech(x:str,fn:str):

    logging.info("Test to speech conversion initated")
    # taking input
    # txt = input('Please enter your text below:\n')
    #specifylanguage
    language = 'en'
    #type conversion to str
    # text = str(txt)
    #making api calls to Google translate via gtts
    speech = gTTS(text=x,lang=language,slow=False,tld="co.in")
    #file name
    # fn = str(input('Please enter the filename to save the output audio file below:\n'))
    #saving the file
    speech.save(fn + '.wav')
    #playning the file
    os.system(f'start {fn}.wav')
    logging.info("Text to speech conversion successful !")



def speechToText(x):
    logging.info("Speech to text conversion initiated")

    r = sr.Recognizer()
    #indication to begin speaking
    print("Recognizing your text.............press CTRL+C to terminate")

    while(1):
        try:

            with sr.Microphone() as src:
                r.adjust_for_ambient_noise(src,duration=0.5)
                input_audio = r.listen(src)
                text = r.recognize_google(input_audio)
                print(text)

        except KeyboardInterrupt:
            logging.debug("Keyboard Interrupt to terminate the operation")
            return "terminating due to keyboard interrupt"
            

        except sr.UnknownValueError:
            logging.error("UnknownValueError:Voice not recognised/No audio ")
            return "Voice not recognised/No audio"
            
            
def textFileToSpeech(text):
    language = 'en'

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    

def audioFileToText(ft):
    r = sr.Recognizer()
    input= ft
    # Load the audio file using pydub
    sound = AudioSegment.from_file(ft)  # Load the audio file using pydub
    sound.export("temp_converted.wav", format="wav")  # Export as WAV

    # Now use the converted WAV file for speech recognition
    file = sr.AudioFile('temp_converted.wav')
    with file as src:
        audio = r.record(src)
    text = r.recognize_google(audio)
    return text  


        