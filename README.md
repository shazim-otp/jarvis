# Meck AI Assistant

A real-time multilingual AI voice assistant inspired by Jarvis, built using Python, Groq AI, Faster-Whisper, and Edge-TTS.

Meck AI can
- Understand voice commands
- Speak English, Malayalam, and Manglish
- Maintain conversation memory
- Support wake-word activation
- Interrupt responses in real time
- Enter idle mode automatically
- Run on low-end hardware

---

# Demo Video

Demo URL:
https://shazim-otp.github.io/jarvis/

---

# GitHub Repository

https://github.com/shazim-otp/jarvis

---

# Features

- Real-time speech recognition
- AI-powered responses using Groq
- Multilingual support
- Wake-word activation
- Idle listening mode
- Interrupt support
- Conversation memory
- Smart silence detection
- Realistic neural voice output
- Low-latency cloud AI processing

---

# Why I Built This

I built Meck AI because I wanted to create my own real-time AI voice assistant inspired by Jarvis.

I was interested in combining:
- speech recognition
- conversational AI
- multilingual interaction
- realistic voice synthesis

into a single lightweight assistant.

Another goal was making the assistant work on low-end hardware while still providing fast AI responses using cloud-based inference.

I also wanted to support Malayalam and Manglish conversations because most voice assistants do not properly support regional language interaction.

---

# Challenges Faced

Some challenges while building this project included:

- Reducing AI response delay
- Handling microphone background noise
- Preventing false detections
- Supporting Malayalam and Manglish speech
- Managing real-time interruption while speaking
- Creating smooth wake-word activation
- Running efficiently on low-end hardware

---

# What I Learned

During this project I learned how to:

- Use Groq AI APIs
- Implement speech-to-text systems
- Generate realistic AI voice responses
- Process microphone audio in real time
- Build multilingual conversational systems
- Handle audio playback and interruption
- Use multithreading in Python

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Main programming language |
| Groq API | AI response generation |
| Faster-Whisper | Speech recognition |
| Edge-TTS | Voice synthesis |
| Pygame | Audio playback |
| NumPy | Audio processing |
| SoundDevice | Microphone recording |
| SciPy | WAV handling |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/shazim-otp/jarvis.git
cd jarvis
```

## Create Virtual Environment

### Windows

```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

### Linux

```bash
python3.11 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install openai faster-whisper edge-tts pygame numpy sounddevice scipy
```

---

# Setup Groq API

1. Visit:
https://console.groq.com/keys

2. Create a new API key

3. Replace:

```python
api_key="YOUR_GROQ_API_KEY"
```

with your actual key.

---

# Running The Project

```bash
py -3.11 meck.py
```

---

# Supported Languages

- English
- Malayalam
- Manglish

Example:

```text
What is AI?
```

```text
entha cheyyunne bro
```

```text
ഇന്നത്തെ കാലാവസ്ഥ എന്താ?
```

---

# System Architecture

```text
User Voice
    ↓
Microphone Input
    ↓
Faster-Whisper Speech Recognition
    ↓
Groq AI Processing
    ↓
AI Response Generation
    ↓
Edge-TTS Voice Synthesis
    ↓
Speaker Output
```

---

# Future Improvements

- Desktop GUI
- ESP32 smart-home integration
- Vision system using OpenCV
- Offline AI mode
- Mobile companion app
- Smart automation system

---

# Hardware Used

- Intel i3 processor
- 4GB RAM
- Integrated Intel HD Graphics

The project was optimized specifically for low-end hardware.

---

# Author

Built by Shazim using Python and AI technologies.
