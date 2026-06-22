# 🎙️ Alexa Voice Assistant

A Python voice assistant that responds to a wake word, plays music, opens websites, fetches live news, and answers questions using the Groq LLaMA AI API.

---

## ✨ Features

- 🔔 **Wake word detection** — say "Alexa" to activate
- 🌐 **Open any website** — say "open netflix" or "open github" and it figures out the URL
- 🎵 **Play music** — looks up songs from your local library or searches YouTube automatically
- 📰 **Live news** — fetches top US headlines using the NewsAPI
- 🤖 **AI responses** — anything else gets answered by LLaMA 3.1 via Groq
- 🔊 **Text-to-speech** — fully voice-driven responses using pyttsx3

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

Create a `.env` file in the root folder and add:

```
api_key=your_groq_api_key_here
news_apikey=your_newsapi_key_here
```

- Get your **Groq API key** → [console.groq.com](https://console.groq.com)
- Get your **NewsAPI key** → [newsapi.org](https://newsapi.org)

---

## 🙋 Author

Built by **Laiba** — a Python developer building practical AI-powered projects.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE)..