import cv2
import pyautogui
import numpy as np
import time
import os
from win32api import GetSystemMetrics
from Speak import Speak
from Listen import MicExecution

def ScreenRecording():
    # Get screen width and height
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    dim = (width, height)
    
    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    # Prompt the user for the recording duration
    Speak("How many seconds do you want to record?")
    Time = float(MicExecution()) 
    duration = Time  # Convert the user input to a float
    
    # Prompt the user for the file name
    Speak("Tell Me File Name")
    FileName = MicExecution()
    
    # Create the output VideoWriter with the specified file name
    output = cv2.VideoWriter(f"C:\\Users\\shubh\\OneDrive\\Pictures\\Recording\\{FileName}.avi", fourcc, 20.0, dim)
    
    end_time = time.time() + duration
    
    try:
        while True:
            # Capture the screen frame
            image = pyautogui.screenshot()
            frame = np.array(image)
            
            # Convert the color format to BGR (compatible with OpenCV)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Write the frame to the video file
            output.write(frame)
            
            # Check if the recording duration has elapsed
            if time.time() > end_time:
                break
    except Exception as e:
        Speak(f"An error occurred: {str(e)}")
    
    # Release the VideoWriter
    output.release()
    Speak("Recording finished.")
    os.startfile("C:\\Users\\shubh\\OneDrive\\Pictures\\Recording")
    Speak("Here Is Your Screen Recording")

