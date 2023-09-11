import smtplib 
import ssl 
from email.message import EmailMessage
from Speak import Speak
from Listen import MicExecution
from time import sleep


def Gmail(Query):
    Speak("Tell Me Subject ")
    sleep(3)
    subject = MicExecution()
    Speak("Tell Me body ")
    sleep(3)
    body = MicExecution()
    Speak("Tell Me Sender_email ")
    sleep(3)
    sender_email ="Shubhamthorat2001@gmail.com" #MicExecution()
    Speak("Tell Me receiver_email ")
    sleep(3)
    receiver_email = "Shubhamthorat070@gmail.com" #MicExecution()
    Speak("Tell Me password")
    sleep(3)
    password = "lbzwdpvtsyozjjbq"

    Speak("I am working....")
    sleep(3)

    message = EmailMessage()
    message["From"] = sender_email
    message['To']= receiver_email
    message['Subject']= subject
    message.set_content(body)


    context = ssl.create_default_context()
    Speak("sending Email!")
    with smtplib.SMTP_SSL("smtp.gmail.com",465, context= context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,message.as_string())

    Speak("sucessfull")