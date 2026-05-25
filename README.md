Meck AI Assistant

Meck AI is a real-time multilingual AI voice assistant inspired by Jarvis, built completely in Python using Groq AI, Faster-Whisper, and Edge-TTS. The project focuses on creating a lightweight yet powerful personal assistant experience capable of understanding natural speech, maintaining conversation memory, switching languages automatically, and responding with realistic voice output.

Unlike basic chatbots, Meck AI behaves like a real assistant by continuously listening for user interaction, entering idle mode during inactivity, supporting wake-word activation, and allowing live interruption while speaking.

The assistant was designed to run on low-end hardware such as an Intel i3 laptop with 4GB RAM while still providing fast AI responses using cloud-based inference through Groq’s ultra-low latency API.

Features
Real-Time Voice Interaction
Converts speech to text using Faster-Whisper
Generates AI responses using Groq LLMs
Speaks responses using Edge-TTS
Multilingual Support

Supports:

English
Malayalam
Manglish (Malayalam written in English)

The assistant automatically detects the language being spoken and switches voice output accordingly.
