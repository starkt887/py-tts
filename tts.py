
from gtts import gTTS
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

inputFiles=getAllFiles()
if len(inputFiles)>0:
    empytVOFiles()
    language = 'hi' #en
    accent="co.in" #"us" "co.uk" "co.in"
    for id,inpFile in enumerate(inputFiles):
        try:
            f=open(f"inputtextfiles\\{inpFile}","r",encoding="utf-8")
            

            fileText = f.read().strip()
            fileName=inpFile.split(".")[0]
            myobj = gTTS(text=fileText, lang=language,tld=accent, slow=False)
            myobj.save(f"outputVOfiles\\{fileName}.mp3")
       
            os.system(f"start outputVOfiles\\{fileName}.mp3")
        except:
            print("something went wrong!")

