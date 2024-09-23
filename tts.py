# Import the required module for text 
# to speech conversion
from gtts import gTTS
# This module is imported so that we can 
# play the converted audio
import os

f=open("inputtextfiles\\input.txt","r",encoding="utf-8")
# The text that you want to convert to audio
mytext = f.read().strip()
mytext=" ".join(mytext.split()) 
# print(mytext)
# text to speech setup and convert the speech in playable mp3 file
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("outputVOfiles\\output.mp3")
# export to mp3

os.system("start outputVOfiles\\output.mp3")

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed

# Saving the converted audio in a mp3 file named
# welcome 


# Playing the converted file