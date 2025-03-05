import os
from gtts import gTTS

audio = "MyAudio.mp3"

language = 'en'

mytext = input("Enter your text-to-speech : ")

myobj = gTTS(text=mytext, lang=language, slow=True )

myobj.save(audio)

os.system("start MyAudio.mp3")
