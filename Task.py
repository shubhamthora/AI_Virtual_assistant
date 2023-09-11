import datetime
import wikipedia
import pywhatkit
import pyautogui
from Speak import Speak
from Listen import MicExecution
import webbrowser
from time import sleep
import pywhatkit
from googletrans import Translator
import os
import pyautogui
import requests
import datetime
from playsound import playsound
import keyboard
from Speak import Speak
import requests
from AIBrain import ReplyBrain
def Date():
    date=datetime.date.today()
    Speak(date)
def Day():
    day=datetime.datetime.now().strftime("%A")
    Speak(day)
def Time():
    time=datetime.datetime.now().strftime("%H:%M")
    Speak(time)

def NonInputExecution(query):
    query=str(query)
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
    else:
        pass
    Speak("COmmand is Completed")
   
def CloseAPPS():
        Speak("Ok , Wait A second!")
        Speak("Tell Me Which Application You Want To close")
        Query = MicExecution()
        if "ms word" or 'Ms Word' in Query:
            os.system("TASKKILL /F /im WINWORD.EXE")
        elif 'Chrome' or 'chrome'in Query:
            os.system("TASKKILL /f /im chrome.exe")
        elif 'PowerPoint' or 'powerpoint' or 'power point' in Query:
            os.system("TASKKILL /F /im POWERPNT.EXE")
        elif 'code' or 'code' in Query:
            os.system("TASKKILL /F /im Code.exe")
        elif 'MS Browser' or 'ms browser' in Query:
            os.system("TASKKILL /F /im msedge.exe")
        elif 'Excel' or 'excel' in Query:
            os.system("TASKKILL /F /im EXCEL.EXE")  
        elif 'Brave' or 'brave' in Query:
            os.system("TASKKILL /F /im brave.exe")
        Speak("Your Command Has Been Succesfully Completed!") 

def screenshot():
        Speak("Ok , What Should I Name That File ?")
        path = MicExecution()
        path1name = path + ".png"
        path1 = "C:\\Users\\shubh\\OneDrive\\Pictures\\Screenshots\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Users\\shubh\\OneDrive\\Pictures\\Screenshots")
        Speak("Here Is Your ScreenShot")
    
# Import DateTime to convert Unix time to DateTime format
import datetime
def weather():
    # Enter your API key from the Open Weather website
    APIKey = '095588d455bd5e949de58087fc98d16d'

    # store the base url
    BaseURL = 'https://api.openweathermap.org/data/2.5/weather'

    # view the specific data, rather than hard to read dictionary and list data
    # Store and print greeting
    Speak('Welcome to your weather tracker! Which City do you want to view?')
    # Input the relevant City name
    Speak('Tell me a City name')
    City=MicExecution()
    RequestURL = f'{BaseURL}?appid={APIKey}&q={City}'
    Response = requests.get (RequestURL)
    # If the response is 'ok' then get the whole JSON weather data as a Python dictionary
    if Response.status_code == 200:
        Data = Response.json ()
        weather = Data['weather'][0]['description']
        temperature = round(Data['main']['temp']-273.15,2)
        sunrise = datetime.datetime.utcfromtimestamp(Data['sys']['sunrise']+ Data['timezone'])
        sunset = datetime.datetime.utcfromtimestamp(Data['sys']['sunset']+ Data['timezone'])
        Speak(f'weather summery:{weather}')
        Speak(f'temperature is {temperature} celsius')
        Speak(f'sunrise time is {sunrise}')
        Speak(f'sunset time is s{sunset}')

    else:
        print("hmm...that doesn't look quite right, try again")
def Translate():
    Speak("Tell Me the Line")
    Text = MicExecution()
    line=str(Text)
    translate=Translator()
    result=translate.translate(line)
    data=result.text
    Speak(data)
    return data

def InputExecution(query):
    query= query.lower()
    if "wikipedia" in query:
        try:
            Speak("Tell Me What you want to search")
            query=MicExecution()
            name=str(query).replace("who is","").replace("about","").replace("what is","")
            result=wikipedia.summary(name)
            print(result)
            return True
        except:
            Speak("Sorry! Sir Something is wrong")
            return True  
    elif "google" in query:
        query = query.replace("google", "").strip()  # Remove "google" and any leading/trailing spaces
        pywhatkit.search(query)
        Speak("This site I have found.")
        return True  
    elif "play" in query:
         query=str(query).replace("Play","")#.replace("search on youtube","")
         pywhatkit.playonyt((query))
         Speak("Your video Has Been Started! , Enjoy Sir!")
         return True  
    elif "open" in query:
            Nameoftheapp = query.replace("open ","")
            pyautogui.press('win')
            sleep(1)
            keyboard.write(Nameoftheapp)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5) 
            Speak("Command is completed.") 
            return True
    elif "youtube search " in query:
            query = query.replace("youtube search","")
            query = query.replace("youtube","")
            query = query.replace("jarvis","")
            Link  = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(Link)
            Speak("Command is completed.")
            return True  
            return True
    elif 'my location' in query:
        Speak("Ok Sir , Wait A Second!")
        webbrowser.open('https://goo.gl/maps/hLsrfrPtVUnLM15W6')  
        return True     
    #elif 'what do you remember' in query:
        #remeber = open('C:\\Users\\shubh\\AI JARVIS DEMO\\New\\Brain\\AIBrain.txt','r')
        #Speak("You Tell Me That" + remeber.read())
    elif 'screenshot' in query:
        screenshot()
        return True     
    elif 'translate' in query:
        Translate()
        return True  

    elif 'weather' in query:
        weather()  
        return True  

    elif "close" in query:
        CloseAPPS()
        return True  
      
    elif 'exit' in query:
            Speak("Thanks for giving me your time")
            exit()
    

    else:
        
        pass


