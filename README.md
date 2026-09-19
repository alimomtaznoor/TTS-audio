# AI Audio Generator

A Python-based text-to-speech application built using the open-source **Chatterbox TTS** model. This project explores AI-powered speech generation, voice conditioning, and expressive audio synthesis.

## Features

- Text-to-speech generation using Chatterbox TTS
- Zero-shot voice conditioning using an audio reference
- Adjustable speech expressiveness
- WAV audio generation
- Python-based inference workflow
- GPU-accelerated inference with CUDA
- Built-in watermarking provided by the underlying model

## Tech Stack

- **Python**
- **PyTorch**
- **Chatterbox TTS**
- **Torchaudio**
- **CUDA**
- **Perth Watermarker**

## How It Works

The application takes text as input and passes it through the Chatterbox TTS model to generate an audio waveform.

For voice-conditioned generation, an audio sample can also be provided as a reference.

```text
Text Input
    ↓
Chatterbox TTS Model
    ↓
Speech Generation
    ↓
WAV Audio Output

With a reference voice:

Text + Reference Voice
          ↓
    Chatterbox TTS
          ↓
   Generated Speech
          ↓
       WAV File
Installation

Install the required package:

pip install chatterbox-tts

Or install Chatterbox from source:

git clone https://github.com/resemble-ai/chatterbox.git
cd chatterbox
pip install -e .

Python 3.11 is recommended.

Usage
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

model = ChatterboxTTS.from_pretrained(device="cuda")

text = "Hello, this is an example of AI-generated speech."

wav = model.generate(text)

ta.save("output.wav", wav, model.sr)
Voice-Conditioned Generation

A reference audio file can be provided to generate speech using a different voice:

import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

model = ChatterboxTTS.from_pretrained(device="cuda")

text = "This example uses a reference voice."

audio_prompt = "reference.wav"

wav = model.generate(
    text,
    audio_prompt_path=audio_prompt
)

ta.save("voice_output.wav", wav, model.sr)
Example Use Cases

This project can be used for:

AI voice applications
Voice-based assistants
Audio content generation
Conversational AI prototypes
Accessibility applications
Interactive media
AI audio experimentation
Project Structure
.
├── example_tts.py
├── example_vc.py
├── requirements.txt
└── README.md
Responsible AI

Generated audio from Chatterbox includes watermarking designed to help identify AI-generated speech.

This project is intended for responsible experimentation and development with synthetic audio. Do not use generated voices to impersonate people, deceive others, or create harmful content.

Acknowledgements

This project uses the open-source Chatterbox TTS model developed by Resemble AI.

The project also builds upon several open-source components:

Chatterbox
CosyVoice
Real-Time-Voice-Cloning
HiFT-GAN
Llama 3
S3Tokenizer
Perth Watermarker
License

This project uses and builds upon open-source components. Please refer to the respective upstream repositories for their individual license terms.
