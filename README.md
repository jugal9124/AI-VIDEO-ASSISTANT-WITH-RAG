# AI-VIDEO-ASSISTANT-WITH-RAG

A simple Python application that turns meeting or video audio into a searchable AI assistant.
It transcribes audio, summarizes content, extracts action items, decisions, open questions, and supports chat-style queries over the transcript.

## 🚀 What it does

- Downloads audio from a YouTube link or converts a local audio file
- Splits audio into manageable chunks
- Uses Whisper for speech-to-text transcription
- Generates a meeting title and summary
- Extracts action items, decisions, and open questions
- Builds a RAG-based chatbot so you can ask questions about the transcript

## 🧩 Project structure

- `main.py` — command-line entry point
- `app.py` — Streamlit user interface
- `core/` — transcription, summarization, extraction, and RAG logic
- `utils/` — audio download and processing helpers
- `vector_db/` — local Chroma vector store data

## ✅ Prerequisites

- Python 3.14 or newer
- A virtual environment (recommended) made using `uv`
- `ffmpeg` installed and available on your system `PATH`
- A Mistral API key for the chatbot

## 📦 Install

1. Open a terminal in the project folder.
2. Create and activate a virtual environment:
    Automatically active When run the Application

```powershell
uv init
```

3. Install dependencies:

```powershell
uv add -r requirements.txt
```

## 🔧 Setup

Create or update the `.env` file with your Mistral API key:

```text
MISTRAL_API_KEY=your_api_key_here
WHISPER_MODEL=small
```

If you need a different Whisper model, change the `WHISPER_MODEL` value.

## ▶️ Run the app

### Streamlit UI

```powershell
streamlit run app.py
```

Open the Streamlit URL shown in the terminal.

### CLI mode

```powershell
python main.py
```

Then follow the prompts to provide a YouTube URL or local file path and choose a language.

## 📁 How to use

- For a YouTube recording, paste the URL.
- For a local file, enter the correct file path.
- The app converts audio to WAV, extracts text, and builds the analysis pipeline.
- Use the chat section to ask questions about the transcript.

## ⚠️ Notes

- The app currently supports English transcription by default.
- Make sure `ffmpeg` is installed separately; the app only uses `ffmpeg-python` as a wrapper.
- The RAG chat feature uses `mistral-small-latest` from Mistral.

## 💡 Troubleshooting

- If you see `No module named torchvision`, install it with:

```powershell
pip install torchvision
```

- If Streamlit does not use the correct environment, verify the active interpreter in VS Code.

## 🧠 Improvements

This project is built to be extended with better language support, more accurate audio chunking, and additional extraction features.
