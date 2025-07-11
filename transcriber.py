import whisper

model = whisper.load_model("base")
result = model.transcribe("N Coast Hwy 4.m4a")
print(result["text"])