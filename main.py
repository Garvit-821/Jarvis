import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
from Features import GoogleSearch
import requests
import bs4




engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def startup():

    speak("Initializing Jarvis")

    speak("Starting all systems applications")

    speak("Installing and checking all drivers")

    speak("Caliberating and examining all the core processors")

    speak("Checking the internet connection")

    speak("Wait a moment sir")
    
    speak("All drivers are up and running")

    speak("All systems have been activated")

    speak("Now I am online")

    print("Initializing Jarvis")

    print("Starting all systems applications")

    print("Installing and checking all drivers")

    print("Caliberating and examining all the core processors")

    print("Checking the internet connection")

    print("Wait a moment sir")

    print("All drivers are up and running")

    print("All systems have been activated")

    print("Now I am online")

    hour = int(datetime.datetime.now().hour)


def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:

        speak("Good Morning!")



    elif hour>=12 and hour<18:

        speak("Good Afternoon!")   



    else:

        speak("Good Evening!")  



    speak("I am Jarvis Sir. Please tell me how may I help you master garvit")       



def speak(audio):

    engine.say(audio)

    engine.runAndWait()



        
def takeCommand():

    #It takes microphone input from the user and returns string output



    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")


        r.pause_threshold = 1

        audio = r.listen(source)



    try:

        print("Recognizing...")    

        query = r.recognize_google(audio, language='en-in')

        print("User said: {query}\n")




    except Exception as e:


        # print(e)    

        speak("sir can you please say it again i was unable to understand it...")  
        return "None"

    return query
def covidcase (Country):
    countries = str(Country).replace(" ","")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovored = Data

    speak(f"Cases : {cases}")
    speak(f"Deaths : {Death}")
    speak(f"Recovered : {recovored}")

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.login('youremail@gmail.com', 'your-password')

    server.sendmail('youremail@gmail.com', to, content)

    server.close()

if __name__ == "__main__":

    #startup()

    wishMe()

while True:

# if 1:

    query = takeCommand().lower()



    # Logic for executing tasks based on query

    if 'wikipedia' in query:

        speak('Searching Wikipedia...')

        query = query.replace("wikipedia", "")

        results = wikipedia.summary(query, sentences=2)

        speak("According to Wikipedia")

        print(results)

        speak(results)

    elif 'hey' in query:

        speak("yes sir")

    elif 'tell me about your functions' in query:

        speak("yes sir , i am jarvis an artificial intelligence developed by garvit prakash. my full form is Just A Rather Very Intelligent System. i can do certain functions like open chrome apps,sending emails, sending messages on whatsapp ,solving problems , playing music , logout and shutdown mainfram computers etc. i can also perform task like ,playing music through directories, many more you can explore them by using me sir")

    elif 'open youtube' in query:

        webbrowser.open("youtube.com")

    elif 'scan' in query:

        speak("ok sir,   i have identified him from your contacts, he is your father mr gaurav prakash, born on 14 oct, he is currently working in disha publications as cheif technical officer")

    elif 'wake up' in query:

        speak("hello sir , what do you like to have , music or something else by the way you can carry on you important work ")



    elif 'no jarvis i have to do some important work' in query:

        speak("ok sir you can do it but do you want me to play some relaxtion music")

    elif 'yes jarvis' in query:

        webbrowser.open("https://www.youtube.com/watch?v=FTqrQsSIKR0")

    elif 'open google' in query:

        webbrowser.open("google.com")

    elif 'thanks jarvis' in query:

        speak("mention not sir i was made for your helping assistant")

    elif 'jarvis can you play some music' in query:

        speak("sure sir which one due you like to listen ")

    elif 'play of your choice' in query:

        speak("ok sir")

        song  =   webbrowser.open("https://www.youtube.com/watch?v=BZS2u7e31bM")
    elif 'what is the speed of internet' in query:
        webbrowser.open("fast.com")

    elif 'search google' in query:
        GoogleSearch(query)
 

    elif 'nice jarvis great choice' in query:

        speak("thanks sir You made me so I should be like you sir")

    elif 'tell me a joke' in query:

        joke = pyjokes.get_joke()

        print(joke)

        speak(joke)

        speak ("hahhahahaha")


    elif 'play avengers' in query:
        avengers = "paste the path to your movie folder"

        os.startfile(avengers)

    elif 'open website' in query:
        WebPath = ('Paste your website code')
        os.startfile(WebPath)


        run['']

    elif 'open Github' in query:

        webbrowser.open("https://github.com/Garvit-821") 



    elif 'tell about me' in query:

        try :

            webbrowser.open("https://www.google.com/search?q=Garvit+Prakash&oq=Ga&aqs=chrome.1.69i57j69i59l2j69i60j69i61j69i60l3.2386j0j1&sourceid=chrome&ie=UTF-8")  

            speak("Sir according to google' garvit prakash, born on 29th januray, he is a young author and passionate about science and codding ")

        except Exception as d:

            speak("sorry i am unable to search")



    elif 'show my youtube channel' in query :

        webbrowser.open("youtube.com/@factplanet_821")



    elif 'play my favourite music' in query:

        speak("sure sir")

        webbrowser.open("https://www.youtube.com/watch?v=pAgnJDJN4VA")



    elif 'show youtube history' in query:

        history  =  webbrowser.open('brave://history/')



    elif 'solve a problem' in query:

        speak("Sorry Garvit Sir, but i am still writing algorithms to solving some maths problems")



    elif 'i need assistance' in query:

        asist_path = "paste your gesture hand MOuse and keyboard program link" #in case you have not build it yet then you can have my respiortery 
        os.startfile(asist_path)

        run = ['']



    elif 'logout jarvis' in query:

        os.system("shutdown -l")



    elif 'shutdown jarvis' in query:

        os.system("shutdown /s /t 1")



    elif 'the time' in query:

        strTime = datetime.datetime.now().strftime("%H:%M:%S")    

        speak(f"Sir, the time is {strTime}")



    elif 'open code' in query:

        codePath = "E:\PROJECTS\Jarvis\main_.py"

        os.startfile(codePath)



    elif 'jarvis send an email' in query:

        try:

            speak("What should I say?")

            content = takeCommand()

            to = takeCommand()    

            sendEmail(to, content)

            speak("Email has been sent!")

        except Exception as e:

            print(e)

            speak("Sorry Garvit Sir. I am not able to send this email")
        
    elif 'covid cases' in query:

        speak("Which Country's Information ?")

        cccc = takeCommand()

        covidcase(cccc)

    elif 'mars images' in query:

            from Nasa import MarsImage

            MarsImage()
    elif 'space news' in query:


            speak("Tell Me The Date For News Extracting Process .")

            Date = takeCommand()

            from Features import DateConverter

            Value = DateConverter(Date)

            from Nasa import NasaNews

            NasaNews(Value)

    elif 'about' in query:
            from Nasa import Summary
            query = query.replace("jarvis ","")
            query = query.replace("about ","")
            Summary(query)
    elif 'write a note' in query:

        from notepad_automation import Notepad

        Notepad()

    elif 'dismiss' in query:

        from notepad_automation import CloseNotepad

        CloseNotepad()

  


    
        







