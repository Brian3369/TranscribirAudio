import warnings
warnings.filterwarnings("ignore")
import whisper
model = whisper.load_model("base")
result = model.transcribe("Archivos/Tech support conversation, present perfect.mp3")
print(result["text"])
