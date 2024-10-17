from openai import OpenAI 
from apikey import api_data 
import os 
import speech_recognition as sr # Converts voice to text 
import pyttsx3 #read out text output to voice.(java office)
import webbrowser



Model="gpt-4o"
client=OpenAI(api_key=api_data)

def Reply(question):
    completion=client.chat.completions.create(
        model=Model,
        messages=[
            {'role':"system","content":"You are a helpful assistent"},
            {'role':'user','content':question}
        ],
        max_tokens=200
            
    )
    answer = completion.choices[0].message.content 
    return answer

# text to speech 
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait() 

speak("helllo,good morning!")

def takeCommand():

    r=sr.Recoginzer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1 #wait for 1 sec 

    try:
        print('Recogninzing ......')
        query = r.recognize_google(audio,language = 'en-in')
        print("User Said:{} \n".format(query))
    except Exception as e:
        print("Say that again......")
        return "None" 
    return query 

if _ _name_ _ == 