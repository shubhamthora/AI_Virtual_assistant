import tkinter as tk
import pyttsx3
import speech_recognition as sr
from Main import MainTaskExecution
from Speak import Speak
from Qna import QuestionsAnswer
from AIBrain import ReplyBrain
from Speak import Speak
from Main import TasksExecutor
from flask import Flask
from Speak import Speak

# Constants
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class VoiceAssistant:
    def __init__(self):
        self.window = tk.Tk()
        self._setup_main_window()

        # Voice Assistant Constants
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Voice Assistant")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # Create a text widget
        self.text_widget = tk.Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                    font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=tk.DISABLED)

        # Add a microphone button
        mic_button = tk.Button(self.window, text="Microphone", font=FONT_BOLD, width=20, bg=BG_GRAY,
                               command=self.listen_using_microphone)
        mic_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def listen_using_microphone(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                Speak("Listening")
                print("Listening...")
                audio = self.recognizer.listen(source,timeout=10)

                print("Recognizing...")
                command = self.recognizer.recognize_google(audio,language="en-hi").lower()
                print("You said: " + command)

                # Process the recognized command and generate a response
                response = self.process_text_input(command)

                # Display user and bot messages
                self.display_message(f"You:  {command}")
                self.display_message(f"Assistant:  {response}")

                # Speak the bot's response
                self.speak(response)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

    def display_message(self, message):
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, message + "\n\n")
        self.text_widget.configure(state=tk.DISABLED)
        self.text_widget.see(tk.END)

    def process_text_input(self, command):
        # Implement your logic to process the recognized command and generate a response
        # You can replace this placeholder logic with your actual processing logic
        Data = str(command).replace(".","")

        # Execute the main task based on user input
        ValueReturn = MainTaskExecution(Data)
        
        if ValueReturn == True:
            ValueReturn = ""
            

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply=QuestionsAnswer(Data)
            Speak(Reply)
            return True

        else:
            
            replay = ReplyBrain(Data)
            return replay
            
     
    def speak(self, text):
        # Convert text to speech and play it
        self.engine.say(text)
        self.engine.runAndWait() 

if __name__ == "__main__":
    app = VoiceAssistant()
    app.run()