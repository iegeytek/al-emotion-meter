# TechBot AI Assistant

TechBot is a simple AI-based chatbot that can interact with users either via **text** or **voice**, detect emotional sentiment from the user's input, and send that emotional state to an **ESP32** microcontroller via serial communication. It is designed to simulate natural human-like interactions and be responsive in real-time.

## Features

- 🎤 Voice recognition using `speech_recognition`
- 🔊 Text-to-speech responses with `pyttsx3`
- 📄 Text input/output option
- 😊 Emotion detection (happy, sad, angry, surprised, in love, etc.)
- 📡 Serial communication with an ESP32 device
- 🚪 Graceful exit commands
- 🧠 Rule-based response generation

## Technologies Used

- Python 3.x
- `speech_recognition`
- `pyttsx3`
- `serial` (pyserial)
- `gTTS` (optional, for alternative voice output)
- ESP32 (for receiving emotion data)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/techbot-ai-assistant.git
   cd techbot-ai-assistant

Required Packages Python:
pip install pyttsx3 speechrecognition pyserial
For Sound: pip install gTTS

