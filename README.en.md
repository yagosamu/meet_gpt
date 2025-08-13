# MeetGPT – Meeting Transcription

A Python Web App to capture meeting audio in real time, transcribe it with Whisper, and generate smart summaries with GPT. Ideal for documenting decisions, enabling quick reviews, and serving as a base for virtual assistants and accessibility solutions.

## Table of Contents
- Overview
- Features
- How it works
- Architecture and folders
- Tech stack
- Prerequisites
- Installation
- Configuration
- Run
- Usage
- Customization
- Security and best practices
- Troubleshooting
- Roadmap
- Contributing
- License

## Overview
MeetGPT is a Streamlit-based Web App that:
- Captures microphone audio via WebRTC.
- Transcribes audio in near real time with OpenAI Whisper.
- Produces concise summaries with agreements using GPT.
- Stores and organizes meeting history locally.

## Features
- In-browser recording (microphone).
- Incremental transcription every ~5 seconds.
- Automatic summary generation with:
  - One-paragraph text (up to 300 characters).
  - Agreements/action items as bullet points.
- Meetings organized by timestamp and optional title.
- View both summary and full transcription.

## How it works
Main flow in `app.py`:
1. Audio capture with `streamlit-webrtc` (SENDONLY).
2. Audio frame aggregation with `pydub`:
   - `audio.mp3` (full meeting)
   - `audio_temp.mp3` (rolling window)
3. Every ~5 seconds, `audio_temp.mp3` is sent for transcription:
   - `OpenAI Whisper (model="whisper-1")`
   - Default language is auto-detected unless configured.
4. The incremental transcription is concatenated, displayed, and saved to `transcricao.txt`.
5. In the saved meetings tab:
   - You can add a title.
   - A summary is generated with GPT (`gpt-3.5-turbo-1106`) using a structured prompt.
   - The summary is saved to `resumo.txt`.

## Architecture and folders
- UI: Streamlit (two tabs)
  - Record Meeting
  - Saved Transcriptions
- Local persistence: `arquivos/` at the project root.

Output per meeting:
```
arquivos/
└── YYYY_MM_DD_HH_MM_SS/
    ├── audio.mp3
    ├── audio_temp.mp3
    ├── transcricao.txt
    ├── resumo.txt
    └── titulo.txt
```

## Tech stack
- Python
- Streamlit
- streamlit-webrtc (browser WebRTC)
- pydub + FFmpeg
- OpenAI API (Whisper + GPT)
- python-dotenv

## Prerequisites
- Python 3.9+
- FFmpeg available on PATH
- OpenAI API key

Install FFmpeg:
- macOS (Homebrew): `brew install ffmpeg`
- Ubuntu/Debian: `sudo apt-get update && sudo apt-get install -y ffmpeg`
- Windows (Chocolatey): `choco install ffmpeg`

## Installation
1. Clone:
   ```
   git clone https://github.com/<owner>/<repo>.git
   cd <repo>
   ```
2. Optional venv:
   - macOS/Linux:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
3. Install deps:
   ```
   pip install -r requirements.txt
   ```
   Or:
   ```
   pip install streamlit streamlit-webrtc pydub openai python-dotenv
   ```

## Configuration
Create a `.env` file at the project root:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Run
Start Streamlit:
```
streamlit run app.py
```
Open:
```
http://localhost:8501
```
Allow microphone access when prompted.

## Usage
1. “Record Meeting” tab
   - Grant mic permission.
   - Start speaking. Transcription updates roughly every 5 seconds.
   - When you stop, files are saved under `arquivos/`.

2. “Saved Transcriptions” tab
   - Select a meeting by timestamp/title.
   - If no title, type one and click Save.
   - The summary is generated on-demand (if not present) and displayed alongside the transcription.

## Customization
- Transcription language:
  - Sidebar selector: Auto, Portuguese (pt), English (en).
- Summary language:
  - Sidebar selector: Portuguese or English.
- Models:
  - Transcription: `whisper-1`
  - Summary (chat): `gpt-3.5-turbo-1106`
- Summary prompt:
  - Defined in `locales.py` under each language.
- Storage:
  - Base folder `arquivos/` can be changed in `app.py`.

Suggested `requirements.txt`:
```
streamlit>=1.33
streamlit-webrtc>=0.47
pydub>=0.25
openai>=1.0
python-dotenv>=1.0
```

## Security and best practices
- Do not commit your `OPENAI_API_KEY`.
- Add `.env` to `.gitignore`.
- For sensitive meetings, consider encryption at rest and data retention policies.
- Monitor API costs and rate limits.

## Troubleshooting
- Microphone issues:
  - Check browser/OS permissions for `localhost:8501`.
  - Use HTTPS in production for WebRTC.
- pydub/FFmpeg errors:
  - Ensure `ffmpeg` is installed and on PATH.
- Summary not generated:
  - Verify `OPENAI_API_KEY` and OpenAI rate limits.
- High latency:
  - Tune the chunk interval (currently ~5s) and check CPU/network.
- Missing `arquivos/`:
  - It’s created on first use; ensure write permissions.

## Roadmap
- Export summary/transcription to PDF/Markdown.
- Speaker diarization and timestamps.
- Automatic action item extraction.
- Multilingual support with auto-detection.
- Custom STUN/TURN for production.
- DB integration (SQLite/PostgreSQL).
- User authentication.

## Contributing
- Open an issue describing the change/bug.
- Fork, branch, and open a PR with a clear description.