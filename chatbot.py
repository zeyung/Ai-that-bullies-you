import os
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(dotenv_path=".env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Record audio from microphone
def record_audio(filename="input.wav", duration=5, fs=44100):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("Recording finished.")

# 2. Transcribe audio using Whisper
def transcribe_audio(filename="input.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result["text"]

# 3. Get response from OpenAI
def chatbot_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    record_audio()
    transcription = transcribe_audio()
    print("You said:", transcription)
    response = chatbot_response(transcription)
    print("Chatbot:", response)