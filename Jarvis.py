import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def Pass(pass_inp):

       password = "admin"

       passss  = str(password)

       if passss==str(pass_inp):

              speak("Access Granted .")

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

              speak("i am jarvis sir, online and ready to help you master garvit prakash")
              

             



              import main
              

       else:
             
              speak("Access Not Granted .")



if __name__ == "__main__" :



       speak("i am  Password Protected i can only unlocked by garvit prakash .")



       speak("Kindly Provide The Password To Access .")



       passssssss = TakeCommand()



       Pass(passssssss)
