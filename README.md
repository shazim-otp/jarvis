# Meck AI Assistant

Meck AI is a real-time AI voice assistant inspired by Jarvis, built using Python, Groq AI, Faster-Whisper, and Edge-TTS.

It supports:
- Real-time voice interaction
- English, Malayalam, and Manglish
- Wake-word activation
- Interrupt-based conversation
- Idle listening mode
- Conversation memory
- Low-latency AI responses

---

# Features

- Real-time AI voice assistant
- Groq AI integration
- Faster-Whisper speech recognition
- Edge-TTS realistic voice synthesis
- English + Malayalam + Manglish support
- Wake-word activation (`meck`)
- Interrupt responses while speaking
- Idle mode after inactivity
- Conversation memory
- Automatic language detection
- Click sound feedback

---

# Technologies Used

- Python 3.11
- Groq API
- Faster-Whisper
- Edge-TTS
- Pygame
- NumPy
- SoundDevice
- SciPy

---

# Requirements

- Python 3.11
- Microphone
- Internet connection
- Windows or Linux

---

# Install Python 3.11

Download Python 3.11:

https://www.python.org/downloads/release/python-3110/

While installing:
- Enable **Add Python to PATH**

---

# Clone Project

```bash
git clone https://github.com/yourusername/meck-ai.git
cd meck-ai
```

---

# Create Virtual Environment

## Windows

```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

## Linux

```bash
python3.11 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install openai faster-whisper edge-tts pygame numpy sounddevice scipy
```

Optional better pygame version:

```bash
pip uninstall pygame
pip install pygame-ce
```

---

# Get Groq API Key

1. Open:
https://console.groq.com/keys

2. Create API key

3. Copy the key

---

# Add API Key

Open:

```text
meck.py
```

Replace:

```python
api_key="YOUR_GROQ_API_KEY"
```

with:

```python
api_key="your_actual_groq_api_key"
```

---

# Add Click Sound

Place a sound file named:

```text
click.mp3
```

inside the project folder.

This plays whenever Meck starts listening.

---

# Run Meck AI

```bash
py -3.11 meck.py
```

---

# How It Works

## Normal Mode

- Meck listens to your voice
- Converts speech to text
- Sends request to Groq AI
- Speaks AI response

---

## Interrupt Mode

While Meck is speaking, say:

```text
meck
```

to interrupt the response instantly.

---

## Idle Mode

After 1 minute of inactivity:
- Meck enters idle mode
- Only listens for wake word

Say:

```text
meck
```

to wake it again.

---

# Supported Languages

- English
- Malayalam
- Manglish

Examples:

```text
What is AI?
```

```text
entha cheyyunne
```

```text
ഇന്നത്തെ കാലാവസ്ഥ എന്താ
```

---

# Project Structure

```text
MeckAI/
│
├── meck.py
├── click.mp3
├── input.wav
├── interrupt.wav
├── wake.wav
├── venv/
└── README.md
```

---

# Recommended Hardware

Minimum:
- Intel i3
- 4GB RAM
- Integrated graphics

Recommended:
- 8GB RAM
- SSD
- Good microphone

---

# Future Improvements

- GUI interface
- ESP32 smart-home control
- Face recognition
- Emotion detection
- Offline AI mode
- Mobile companion app
- Vision support using OpenCV

---

# Author

Built by Shazim using Python and AI technologies.
