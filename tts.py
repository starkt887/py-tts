# Import the required module for text to speech conversion
from gtts import gTTS
# This module is imported so that we can do some os operations
import os



# print(mytextArr)

def getAllFiles():
    filesInDir=os.listdir("inputtextfiles")
    print(f"input files={filesInDir}")
    return filesInDir

def empytVOFiles():
    filesInDir=os.listdir("outputVOfiles")
    if len(filesInDir)>0:
        for file in filesInDir:
            os.remove(f"outputVOfiles\\{file}")
        print("emptied the folder")
    else:
        print("folder is empty")
    # print(os.listdir("outputVOfiles"))'

inputFiles=getAllFiles()
if len(inputFiles)>0:
    empytVOFiles()
    language = 'en'
    accent="co.uk" #"us"
    for id,inpFile in enumerate(inputFiles):
        try:
            f=open(f"inputtextfiles\\{inpFile}","r",encoding="utf-8")
            
            # The text that you want to convert to audio
            fileText = f.read().strip()
            fileName=inpFile.split(".")[0]
            myobj = gTTS(text=fileText, lang=language,tld=accent, slow=False)
            myobj.save(f"outputVOfiles\\{fileName}.mp3")
            # export to mp3
            os.system(f"start outputVOfiles\\{fileName}.mp3")
        except:
            print("something went wrong!")

# os.system("start outputVOfiles\\output.mp3")



#Algorithm
# text to speech setup and convert the speech in playable mp3 file
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
# Saving the converted audio in a mp3 file named
# Playing the converted file


# unused code
# mytext=" ".join(mytext.split()) 