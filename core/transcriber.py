import whisper
import os

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")
_model = None


def load_model():
    global _model
    if _model is None:
        print(f"Loading whisper model: {WHISPER_MODEL} ...")
        _model = whisper.load_model(WHISPER_MODEL)
        print("whisper model loaded successfully")
    return _model


def transcribe_chunk_whisper(chunk_path: str) -> str:
    model = load_model()
    result = model.transcribe(chunk_path, task="transcribe")
    return result["text"]  # type: ignore


def transcribe_chunk(chunk_path: str, language: str = "english") -> str:
    if language.lower() != "english":
        raise ValueError("Only English transcription is supported.")
    return transcribe_chunk_whisper(chunk_path)


def transcribe_all(chunks: list, language: str = "english") -> str:
    if language.lower() != "english":
        raise ValueError("Only English transcription is supported.")

    full_transcript = ""
    print("Using whisper for English transcription.")

    for i, chunk in enumerate(chunks):
        print(f" Transcribing chunk {i + 1}/{len(chunks)}...")
        text = transcribe_chunk(chunk, language=language)
        full_transcript += text + " "

    print("Transcription complete.")
    return full_transcript.strip()








