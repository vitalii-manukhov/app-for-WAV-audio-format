import whisper
import numpy as np
import os
import json
from utils.config import settings

model = whisper.load_model(
    name="medium",
    download_root=settings.WHISPER_DOWNLOAD_PATH)

parameters = {
    "task": "transcribe",
    "fp16": False
}


def transcription_audio(audio: np.ndarray) -> str:
    """
    """
    result = whisper.transcribe(model, audio, **parameters)
    return result["text"]


def save_text_to_json(audio_path: str, text: str) -> None:
    result = {
        "transcription": text
    }

    base = audio_path.split('.')[0]
    json_outpath = f"{base}_transcription.json"

    if os.path.isfile(json_outpath):
        i = 1
        while os.path.isfile(f"{base}_{i}_transcription.json"):
            i += 1
        json_outpath = f"{base}_{i}_transcription.json"

    with open(json_outpath, 'w', encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False)
