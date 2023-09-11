from Speak import Speak
from Listen import MicExecution

import os

def Notes():
    def create_note(note_title, note_content):
        try:
        
            directory_path = "C:\\Users\\shubh\\OneDrive\\Pictures\\Notes"  # Get the directory path from the user
            Speak("Tell Me The File Name")
            file_name = MicExecution()  # Get the file name from the user
            file_path = os.path.join(directory_path, f"{file_name}.txt")

            with open(file_path, "a") as f:
                f.write(f"### {note_title} ###\n")
                f.write(note_content + "\n")
                f.write("=" * 30 + "\n")
            Speak("Note saved.")
            os.startfile(directory_path)
            Speak("Here Is Your Note.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    Speak("Tell Me the Note Title")
    note_title = MicExecution()
    Speak("Tell Me The Note Content")
    note_content = MicExecution()
    create_note(note_title, note_content)


