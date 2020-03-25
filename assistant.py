import pyttsx3          # this module convert text into speech 
import speech_recognition as sr   # for speech recognizing through mic
import pyaudio          # pyaudio module is for audio I/O library
import wikipedia        # to search anything over wikipedia
import datetime         # to find the current time 
import webbrowser       # for browsing anything
import os               # to interact with operating system
import random           # to play random songs
import smtplib          # to send email we need to import this module
from fpdf import FPDF

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)    
# here voices[0].id is for a man sound and voices[1]
# for a woman sound
engine.setProperty('voice',voices[1].id) 

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def WishMe():
   hour=int(datetime.datetime.now().hour)
   if (hour>=0 and hour<12):
      speak("good morning sir!")
   elif hour>=12 and hour<18:
      speak("good afternoon sir!")
   elif hour>=18 and hour<0:
      speak("good evening sir!")
   else:
      speak("good night sir!")
   speak("I am twitty sir,How may i help you!")

def takeCommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold =1
      audio = r.listen(source)
   
   try:
      print("Recognizing...")
      query = r.recognize_google(audio,language="en-in")
      print(f"user said: {query}\n")
   
   except Exception as e:
      speak("Please speak again!")
      return "None"
   return query

def sendEmail(to, Content):
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.login('janusingh9889@gmail.com','******')
   server =sendmail('janusingh9889@gmail.com',to, content)
   server.close()

if __name__=="__main__":
   WishMe()
   #while True:
   if 1:
      query=takeCommand().lower()
      #logic for executing task
      if "from wikipedia" in query:
         speak("searching wikipedia...")
         query = query.replace("wikipedia","")
         result = wikipedia.summary(query, sentences=2)
         speak("according to wikipedia..")
         print(result)
         speak(result)
      elif "open youtube" in query:
         webbrowser.open("https://youtube.com")
         
      elif "open sbs" in query:
         webbrowser.open("https://www.sbsstc.ac.in/")

      elif "open google" in query:
         webbrowser.open("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
      
      elif "play music" in query:
         music_dir ="E:\music"
         music = os.listdir(music_dir)
         r1=random.randint(0,len(music)-1)
         os.startfile(os.path.join(music_dir, music[r1]))
      
      elif "the time" in query:
         time = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir the time is {time}")
      
      elif "play video" in query:
         video_dir ="E:\\video"
         video = os.listdir(video_dir)
         r1=random.randint(0,len(video)-1)
         os.startfile(os.path.join(video_dir, video[r1]))
      
      elif "open visual" in query:
         vs_path ="C:\\Users\\Yogesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(vs_path)
      
      elif "change pdf" in query:
         f1=open("okk.txt",'r')
         ss=f1.readline()
         pdf=FPDF()
         pdf.add_page()
         pdf.set_font("Arial",size=12)
         pdf.cell(200,10,txt=ss ,ln=1,align="C")
         pdf.cell(200,10,txt="big boss",ln=2,align="C")
         pdf.output("6.pdf")
         print("file changed..")
         f1.close()
      
      elif "send email" in query:
         try:
            speak("what should i say?")
            content =takeCommand()
            to ="yogesh21051998@gmail.com"
            sendEmail(to, content)
            speak("email has been sent!")
         except Exception as e:
            print(e)
            speak("sorry,i am unable to send the email at the moment")
