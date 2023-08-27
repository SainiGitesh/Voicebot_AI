import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
import openai
import numpy as np
from config import apikey

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def ai(prompt):
    openai.api_key = apikey
    count = 0
    text=f"User: {prompt}\n Hidden Group Member: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]

    if not os.path.exists("Chats"):
        os.mkdir("Chats")

    with open(f"Chats/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        count = count + 1
        f.write(text)
    # text += f"{response['choices'][0]['text']} \n"
    try:
        # print(response["choices"][0]["text"])
        print(f"Hidden Group Member: {response['choices'][0]['text']}")
        return speaker.Speak(response["choices"][0]["text"])

    except Exception as e:
        return "Google it, u guys are adults!"
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f" User said: {query}")
            return query
        except Exception as e:
            return speaker.Speak("Can't understand.. please repeat again")

if __name__ == '__main__':
    speaker.Speak("Hi, I am Hidden Group Member, How can I help you today?")
    x=1
    while x>=1:
        print('Listening...!')
        task = takeCommand()
        ai(prompt=task)
        #chat(task)
        speaker.Speak("Anything Else? Yes or No")
        print('Listening...!')
        task = takeCommand()
        if 'Yes' or "i have another question" in task.lower():
            speaker.Speak("Go ahead then, Ask me what you want to know")
            x+=1
        elif "no" or "thank you" or "thanks" in task.lower():
            speaker.Speak("Goodbye then!")
            x=0
        else:
            speaker.Speak("Don't waste my time")
