import sounddevice as sd
import scipy.io.wavfile as wav
from Speak import Speak
from Listen import MicExecution
import os

def AudioRecording():
    Speak("Ok, Sir, tell me the time duration")
    Time = float(MicExecution())  # Convert to float
    # Set the parameters for audio recording
    duration = Time  # Recording duration in seconds
    sample_rate = 44100  # Sample rate (samples per second)
    Speak("Sir, Tell me the File Name")
    File_Name = MicExecution()
    output_file = f"C:\\Users\\shubh\\OneDrive\\Pictures\\Audio\\{File_Name}.wav"

    try:
        # Start recording
        Speak(f"Recording audio for {duration} seconds...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
        sd.wait()

        # Save the recorded audio to a WAV file
        wav.write(output_file, sample_rate, audio_data)

        Speak(f"Audio recording saved")
        
        # Speak "Here is your audio" after successful recording
        Speak("Audio Recording finished. Here is your audio.")
        
        # Open the folder containing the recorded audio
        os.startfile("C:\\Users\\shubh\\OneDrive\\Pictures\\Audio")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        Speak("An error occurred during audio recording.")
    

