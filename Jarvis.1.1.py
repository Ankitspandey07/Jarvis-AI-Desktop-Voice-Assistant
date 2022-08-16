import pyttsx3  # for text to speech
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

'''its not excat AI but the basic defination of it.
as any work which human's do and is done by computer then it is termed as AI'''

print("Intializing Your Jarvis AI Desktop Assistent")
MASTER="ANKIT" #user name 

engine=pyttsx3.init('sapi5') #in order to use inbuild voices given by windows through api sapi5
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(text): # this function will pronounce whatever string is passed to it
    engine.say(text)
    engine.runAndWait()

def wishMe(): # this function will wish you as per the current time
    hour=datetime.datetime.now().hour 
    if hour>=0 and hour<12:
        speak("Good Morning..." + MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon..." + MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("I am Jarvis. How May i help you?...")

def takeCommand(): 
    # this function will take command from the user through microphone and return string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining....")
        r.pause_threshold = 1
        '''seconds of non-speaking audio before a phrase is considered complete
         in simple word if i m speaking and take gap of less then 1 sec (as i have set pause tym 1) then it won't stop 
         listing and run the program'''
        r.energy_threshold=500  #minimum audio energy to consider for recording as if there is too  much noise in background we shld increase energy threhold value accordingly
        audio=r.listen(source) #Records a single phrase from ``source``
    try :
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in') #we are using google engine to recognize users input giving it via microphone
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please")
        query="None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gamil.com', 587)
    #this is an email server which is opened at port 587. nd this we shld write in order to send email
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    #in order to do so we have to go on gogle nd allow less secure app section "On"
    '''To help keep your account secure, from May 30, 2022, ​​Google no longer supports 
    the use of third-party apps or devices which ask you to sign in to your Google
    Account using only your username and password.'''
    server.sendmail('sujeetsinghrathore1@gmail.com', to, content)
    server.close()

#main function starts....
if __name__ == "__main__":
    speak("Intializing Your Jarvis A I Desktop Assistent....")
    wishMe()
    while True:
        query=takeCommand().lower()


#logic for executing tasks as per the query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "") #here we are replacing wikipedia from query so that in wikipedia its doesnt search wikipedia again
            results = wikipedia.summary(query, sentences=2) # here reults will contain 2 sentences from wikipedia
            print(results)
            speak("According to wikipedia...")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            # url='youtube.com'
            # chrome_path='C:\Program Files\Google\Chrome\Application/chrome.exe %s'
            # webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            webbrowser.open("google.com")
            # url='google.com'
            # webbrowser.get('C:\\Program Files\\Google\Chrome\\Application\\chrome.exe %s ').open(url)

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open linked' in query:
            webbrowser.open("linked.com")

        elif 'open linked' in query:
            webbrowser.open("linked.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open my resume' in query:
            webbrowser.open("C:\\Users\\sujee\OneDrive\\Desktop\\VS Stdio\\Projects\\Web_development\\Curriculam_Activity.html")
            
        elif 'play music' in query:
            songs_dir="C:\\Users\\sujee\\Music\\songs"
            songs=os.listdir(songs_dir)
            #print(songs)
            os.startfile(os.path.join(songs_dir, songs[1]))
            # s=random.choice(songs)
            # os.startfile(os.path.join(songs_dir, s))  #in order to play random song

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to ankit' in query:
            try:
                speak("what should I send")
                content=takeCommand()
                to="Ankitspandeyofficial@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry Sir! I am unable to send this email")
                
        elif 'quit' in query:
            quit()
