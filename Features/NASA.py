import requests
import os
from PIL import Image
import time
fileopen = open("Data\\NASA_API.txt","r")
API = fileopen.read()
fileopen.close()

def NasaNews(_Date):
    # Speak("Extracting Data From Nasa ..... ")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(API)
    Parameter = {'date':str(_Date)}
    r = requests.get(Url,params = Parameter)
    Data = r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    with open("Database\\image_Info.txt","a") as j:
        j.write("\n" + Title + "\n")
        j.write(Info + "\n")
    Image_r = requests.get(Image_Url)
    FileName = str(_Date) + '.jpg'
    with open(FileName,'wb') as f:
        f.write(Image_r.content)
    Path_1 = "D:\\All Mess\\Jarvis AI Main Project\\" + str(FileName)
    Path_2 = "DataBase\\NASA_Images\\" + str(FileName)
    try:
        os.rename(Path_1, Path_2)
    except:
        os.remove(Path_1)
        img = Image.open(Path_2)
    img = Image.open(Path_2)
    img.show()
    # Speak(f"Title : {Title}")
    
   
NasaNews('2012-11-22')