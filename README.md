# 🎙️ Alexa Voice Assistant

A Python-based voice assistant that listens for a wake word and responds to voice commands — opening websites, playing music, fetching live news, and answering questions using the Groq LLaMA AI API.

---

## ✨ Features

- 🔔 **Wake word detection** — say "Alexa" to activate
- 🌐 **Open any website** — say "open netflix" or "open github" and it figures out the URL
- 🎵 **Play music** — looks up songs from your local library or searches YouTube automatically
- 📰 **Live news** — fetches top US headlines using the NewsAPI
- 🤖 **AI responses** — anything else gets answered by LLaMA 3.1 via Groq
- 🔊 **Text-to-speech** — fully voice-driven responses using pyttsx3

---

## 🗂️ Project Structure

```
voice-assistant-python/
│
├── main.py           # Main assistant script
├── music.py          # Dictionary of song names and their URLs
├── .env              # API keys (not pushed to GitHub)
├── .gitignore        # Ignores .env and other sensitive files
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/voice-assistant-python.git
cd voice-assistant-python
```

### 2. Install dependencies

```bash
pip install pyttsx3 speechrecognition pywhatkit requests openai python-dotenv pyaudio
```

> **Note for Windows users:** If `pyaudio` fails to install, download the correct `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually.

### 3. Create your `.env` file

Create a file named `.env` in the root folder and add your API keys:

```
api_key=your_groq_api_key_here
news_apikey=your_newsapi_key_here
```

- Get your **Groq API key** → [console.groq.com](https://console.groq.com)
- Get your **NewsAPI key** → [newsapi.org](https://newsapi.org)

### 4. Set up your music library

In `music.py`, add your songs as a dictionary:

```python
musicLibrary = {
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "blinding lights": "https://www.youtube.com/watch?v=4NRXx6U8ABQ",
    # add more songs here
}
```

### 5. Run the assistant

```bash
python main.py
```

---

## 🗣️ Voice Commands

| Command | Action |
|---|---|
| "Alexa" | Activates the assistant |
| "open youtube" | Opens YouTube |
| "open google" | Opens Google |
| "open facebook" | Opens Facebook |
| "open instagram" | Opens Instagram |
| "open `<any site>`" | Opens `www.<site>.com` |
| "play `<song name>`" | Plays from library or searches YouTube |
| "news" | Reads top US headlines |
| Anything else | Answered by LLaMA 3.1 AI |

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `api_key` | Your Groq API key for LLaMA AI responses |
| `news_apikey` | Your NewsAPI key for fetching headlines |

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `pyttsx3` | Text-to-speech engine |
| `speechrecognition` | Captures and transcribes voice input |
| `pywhatkit` | YouTube search and playback |
| `requests` | Fetches news from NewsAPI |
| `openai` | Groq API client for LLaMA |
| `python-dotenv` | Loads API keys from `.env` |
| `pyaudio` | Microphone access |

---

## 🔒 .gitignore

Make sure your `.env` file is never pushed to GitHub. Create a `.gitignore` file with:

```
.env
__pycache__/
*.pyc
```

---

## 🙋 Author

Built by **Laiba** — a Python developer building practical AI-powered projects.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).