# 🤖 JARVIS — Personal AI Assistant
### Built by **Tanya Panchal**

> A real-time voice-powered AI assistant that can hear, see, understand, and control your computer.  
> Powered by **Gemini Live API** — zero subscriptions, total digital autonomy.

---

## ✨ What is JARVIS?

JARVIS is a hands-free, voice-activated personal AI assistant. Say **"Hey Jarvis"** and it wakes up — stay quiet and it sleeps on its own. It runs on the **Gemini Flash Live** engine for ultra-fast responses and is built to grow with a plug-and-play skill system.

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| 🎙️ Wake Word | Say **"Hey Jarvis"** — local detection, never streams audio while asleep |
| ⚡ Instant Response | Speaks a short acknowledgment immediately while longer tasks run |
| 🧠 Persistent Memory | Remembers your preferences, projects, and context across sessions |
| 👁️ Visual Awareness | Real-time screen capture and webcam vision |
| 🖥️ System Control | Launch apps, adjust volume/brightness, WiFi, power — all by voice |
| 🔍 Web Search | News, research, price, compare modes — Gemini Grounded + DDG fallback |
| 📂 File Management | Move, rename, read, summarize local files |
| 💻 Code Helper | Inline code review, debugging, and generation |
| 🌐 Browser Control | Open URLs, navigate tabs by voice |
| 📨 Messaging | Send messages via WhatsApp, Telegram, and more |
| 🎬 YouTube Control | Search, play, and control YouTube by voice |
| ⏰ Smart Reminders | OS-native scheduled notifications |
| 🌤️ Weather Report | Live weather data personalized from memory |
| ✈️ Flight Finder | Live flight price and availability lookup |
| 📊 Hardware Monitor | CPU, RAM, GPU, temperature telemetry with voice alerts |
| ↩️ Undo | Reverse the last action — files, settings, and more |
| ⚠️ Real Confirmation | Shutdown/restart/WiFi require a button press — model can't self-confirm |
| 🎧 Audio Device Picker | Choose mic and speakers by name — filtered and measured |
| 🧩 Plugin System | Drop a `.py` file into `plugins/` — JARVIS learns a new skill instantly |
| 🎨 Live Theming | Recolour the HUD from a hue wheel or hex — applied instantly |
| 📱 Remote Dashboard | Control from your phone via QR code pairing |
| ⚡ Auto-Start on Boot | Registers with OS startup system |
| 📋 Clipboard Intelligence | Copy text → floating panel with Translate / Summarise / Explain / Fix |

---

## ⚡ Quick Start

```bash
git clone https://github.com/Tanupanchal26/JARVIS-ASSISTANT.git
cd JARVIS-ASSISTANT
python setup.py
python main.py
```

> Prefer manual install? `pip install -r requirements.txt` works too.

---

## 📋 Requirements

| Requirement | Details |
|---|---|
| **OS** | Windows 10/11, macOS, or Linux |
| **Python** | 3.11 or 3.12 |
| **Microphone** | Required for voice interaction |
| **Speakers** | Required for voice replies |
| **API Key** | Free Gemini API key → add to `config/api_keys.json` |
| **Wake Word** *(optional)* | One-click download from ⚙ → WAKE WORD |

---

## 🗂️ Project Structure

```
JARVIS/
├── main.py                   # Core loop — Gemini Live session, audio I/O, tool dispatch
├── ui.py                     # PyQt6 HUD — waveform, log panel, settings drawer
├── setup.py                  # OS-aware installer
├── plugins/                  # Drop-in skills (self-describing via PLUGIN dict + run())
├── actions/                  # Bundled skills — each self-describes via TOOL dict
│   ├── web_search.py
│   ├── screen_processor.py
│   ├── system_monitor.py
│   ├── computer_settings.py
│   ├── file_controller.py
│   ├── browser_control.py
│   ├── weather_report.py
│   └── ...
├── memory/
│   ├── memory_manager.py     # Persistent memory store
│   └── config_manager.py     # API keys, settings, toggles
├── core/
│   ├── prompt.txt            # Assistant personality
│   ├── undo.py               # Undo stack
│   ├── confirm.py            # Irreversible-action gate
│   ├── audio_devices.py      # Mic/speaker picker
│   ├── plugin_loader.py      # Plugin engine
│   └── wake_word.py          # Local "Hey Jarvis" detector
└── config/
    └── api_keys.json         # API key, OS, name, voice, UI colour
```

---

## 👩‍💻 About

**Made by Tanya Panchal**

A personal project to build a real-world JARVIS-style AI assistant from scratch.  
⭐ Star the repo if you find it useful!

| Platform | Link |
|---|---|
| GitHub | [Tanupanchal26](https://github.com/Tanupanchal26) |
