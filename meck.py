import os
import time
import asyncio
import tempfile
import threading
import numpy as np
import pygame
import sounddevice as sd
from scipy.io.wavfile import write

from faster_whisper import WhisperModel
from openai import OpenAI
import edge_tts

# ============================================
# GROQ API
# ============================================

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

# ============================================
# WHISPER MODEL
# ============================================

model = WhisperModel(
    "small",
    compute_type="int8"
)

# ============================================
# SETTINGS
# ============================================

SAMPLE_RATE = 16000

WAKE_WORD = "mecknown"
INTERRUPT_WORD = "mecknown"

VOLUME_THRESHOLD = 200

IDLE_TIMEOUT = 60

idle_mode = False

last_interaction_time = time.time()

interrupt_speaking = False

# ============================================
# CHAT MEMORY
# ============================================

messages = [
    {
        "role": "system",
        "content": (
            "You are Meck, a futuristic AI assistant. "
            "Reply naturally and clearly. "
            "Use the same language as the user. "
            "If the user speaks English reply in English. "
            "If the user speaks Malayalam reply in Malayalam. "
            "If the user speaks Manglish reply naturally in Manglish. "
            "Keep responses short and conversational."
        )
    }
]

# ============================================
# PLAY CLICK SOUND
# ============================================

def play_click():

    try:

        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.music.load("click.mp3")

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pass

    except:
        pass

# ============================================
# RECORD AUDIO
# ============================================

def record_audio(filename, duration=4):

    play_click()

    print("\nListening...")

    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype='int16'
    )

    sd.wait()

    volume = np.abs(audio).mean()

    print(f"Volume Level: {volume}")

    if volume < VOLUME_THRESHOLD:

        print("No voice detected.")

        return False

    write(filename, SAMPLE_RATE, audio)

    return True

# ============================================
# TRANSCRIBE AUDIO
# ============================================

def transcribe_audio(filename):

    segments, _ = model.transcribe(
        filename,
        vad_filter=True,
        beam_size=5
    )

    text = ""

    for segment in segments:

        text += segment.text

    return text.strip()

# ============================================
# DETECT MALAYALAM
# ============================================

def detect_malayalam(text):

    text = text.lower()

    # Malayalam Unicode
    if any('\u0D00' <= c <= '\u0D7F' for c in text):
        return True

    # Manglish words
    manglish_words = [
        "entha",
        "eda",
        "macha",
        "bro",
        "sheri",
        "alle",
        "aano",
        "evide",
        "ille",
        "pinne",
        "njan",
        "nee",
        "venam",
        "cheyy",
        "poyi",
        "vanno"
    ]

    for word in manglish_words:

        if word in text:
            return True

    return False

# ============================================
# ASK GROQ
# ============================================

def ask_groq(prompt):

    global messages

    messages.append({
        "role": "user",
        "content": prompt
    })

    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        stream=True,
        temperature=0.7,
        max_tokens=120
    )

    full_reply = ""

    print("\nMeck: ", end="", flush=True)

    for chunk in stream:

        if chunk.choices[0].delta.content:

            content = chunk.choices[0].delta.content

            print(content, end="", flush=True)

            full_reply += content

    print()

    messages.append({
        "role": "assistant",
        "content": full_reply
    })

    return full_reply

# ============================================
# INTERRUPT LISTENER
# ============================================

def interrupt_listener():

    global interrupt_speaking

    while pygame.mixer.music.get_busy():

        audio = sd.rec(
            int(1 * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='int16'
        )

        sd.wait()

        volume = np.abs(audio).mean()

        if volume < VOLUME_THRESHOLD:
            continue

        write("interrupt.wav", SAMPLE_RATE, audio)

        heard = transcribe_audio("interrupt.wav")

        print(f"\nInterrupt Heard: {heard}")

        if INTERRUPT_WORD.lower() in heard.lower():

            print("\nInterrupt detected!")

            interrupt_speaking = True

            pygame.mixer.music.stop()

            break

# ============================================
# SPEAK
# ============================================

async def speak(text):

    global interrupt_speaking

    interrupt_speaking = False

    # AUTO VOICE SWITCH
    if detect_malayalam(text):

        voice = "ml-IN-MidhunNeural"

    else:

        voice = "en-US-ChristopherNeural"

    try:

        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate="-5%"
        )

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        ) as file:

            temp_path = file.name

        await communicate.save(temp_path)

        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.music.load(temp_path)

        pygame.mixer.music.play()

        # START INTERRUPT LISTENER
        thread = threading.Thread(
            target=interrupt_listener,
            daemon=True
        )

        thread.start()

        while pygame.mixer.music.get_busy():

            if interrupt_speaking:

                pygame.mixer.music.stop()

                break

            await asyncio.sleep(0.1)

        pygame.mixer.music.unload()

        try:
            os.remove(temp_path)
        except:
            pass

    except Exception as e:

        print(f"\nTTS Error: {e}")

# ============================================
# WAKE WORD LISTENER
# ============================================

def listen_for_wake_word():

    print("\n====================")
    print("      IDLE MODE")
    print("====================")
    print("Waiting for wake word...")

    while True:

        audio = sd.rec(
            int(2 * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='int16'
        )

        sd.wait()

        volume = np.abs(audio).mean()

        if volume < VOLUME_THRESHOLD:
            continue

        write("wake.wav", SAMPLE_RATE, audio)

        heard = transcribe_audio("wake.wav")

        print(f"Wake Heard: {heard}")

        if WAKE_WORD.lower() in heard.lower():

            print("\nWake word detected!")

            play_click()

            return

# ============================================
# MAIN LOOP
# ============================================

async def main():

    global idle_mode
    global last_interaction_time

    print("\n==============================")
    print("        MECK AI READY")
    print("==============================")
    print("Languages:")
    print("- English")
    print("- Malayalam")
    print("- Manglish")
    print("==============================")

    while True:

        # IDLE CHECK
        if time.time() - last_interaction_time > IDLE_TIMEOUT:

            idle_mode = True

        # IDLE MODE
        if idle_mode:

            listen_for_wake_word()

            idle_mode = False

            last_interaction_time = time.time()

        # RECORD
        success = record_audio(
            "input.wav",
            duration=2
        )

        if not success:
            continue

        # TRANSCRIBE
        user_text = transcribe_audio("input.wav")

        print(f"\nYou: {user_text}")

        if not user_text:
            continue

        # UPDATE TIMER
        last_interaction_time = time.time()

        # EXIT
        if "exit" in user_text.lower():

            print("\nGoodbye!")

            break

        # ASK AI
        reply = ask_groq(user_text)

        # SPEAK
        await speak(reply)

# ============================================
# RUN
# ============================================

asyncio.run(main())