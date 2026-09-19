import torch
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

# Use correct device detection
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the model
model = ChatterboxTTS.from_pretrained(device=device)

# Text to synthesize
text = "Welcome to your first AI voice test with Chatterbox!"

# Generate speech
wav = model.generate(text)

# Save audio to file
ta.save("test_output.wav", wav, model.sr)

print("✅ Voice audio saved as 'test_output.wav'")
