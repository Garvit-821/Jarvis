import requests
import matplotlib.pyplot as plt
import os
from PIL import Image
import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[2].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

Api_Key = "KrsOGOZLgYGcxYVBLZld2U65PevfTyOfbdqy7ggK"

def NasaNews(Date):

    Speak("Extracting Data From Nasa . ")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params = {'date':str(Date)}
    
    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "E:\\Y O U T U B E\\J A R V I S  S E R I E S\\H O W  T O  M A K E  J A R V I S\\" + str(FileName)

    Path_2 = "E:\\Y O U T U B E\\J A R V I S  S E R I E S\\H O W  T O  M A K E  J A R V I S\\DataBase\\NasaDataBase\\" + str(FileName)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()

    Speak(f"Title : {Title}")
    Speak(f"According To Nasa : {Info}")

def Summary(Boby):

    list__ = ('1','2','3','4','5')

    value = random.choice(list__)

    path = "E:\\PROJECTS\\Jarvis\\NasaDataBase\\Images Used\\" + str(value) + ".jpg"

    os.startfile(path)

    name = str(Boby)

    url = "https://hubblesite.org/api/v3/glossary/" + str(name)

    r = requests.get(url)

    Data = r.json()

    if len(Data) != 0:

        retur =  Data['definition']

        Speak(f"According To The Nasa : {retur}")

    else:

        Speak("No Data Available , Try Again Later!")

#def MarsImage():

  #  name = 'curiosity' 

   # date = '2020-12-3'

   # Api_ = str(Api_Key)

    #url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"

    #r = requests.get(url)

    #Data = r.json()

    #Photos = Data['photos'][:20]

    #try:

     #   for index , photo in enumerate(Photos):
#
 #           camera = photo['camera']

         #   rover = photo['rover']

         #   rover_name = rover['name']

         #   camera_name = camera['name']

         #   full_camera_name = camera['full_name']

        #    date_of_photo = photo['earth_date']

          #  img_url = photo['img_src']

         #   p = requests.get(img_url)

         #   img = f'{index}.jpg'

         #   with open(img,'wb') as file:
            #    file.write(p.content)

         #   Path_1 = ("E:\\PROJECTS\\Jarvis\\NasaDataBase"+str(img))

         #   Path_2 = ("E:\PROJECTS\Jarvis\NasaDataBase\\"+str(img))
#
         #   os.rename(Path_1,Path_2)
#
         #   os.startfile(Path_2)

         #   Speak(f"This Image Was Captured With : {full_camera_name}")

         #   Speak(f"This Image Was Captured On : {date_of_photo}")

  #  except:
     #   Speak("There IS An Error!")


   
def Astro(start_date,end_date):

    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"

    r = requests.get(url)

    Data = r.json()

    Total_Astro = Data['element_count']

    neo = Data['near_earth_objects']

    Speak(f"Total Astroid Between {start_date} and {end_date} Is : {Total_Astro}")

    Speak("Extact Data For Those Astroids Are Listed Below .")

    for body in neo[start_date]:

        id = body['id']

        name = body['name']

        absolute = body['absolute_magnitude_h']

        print(id,name,absolute)

