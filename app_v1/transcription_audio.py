import whisper
import numpy as np
import os
import json

# audio_path: str = ""
# audio = whisper.load_audio(audio_path)
# audio_new = transcription_audio(audio, factor)
#

model = whisper.load_model("small")

parameters = {
    "task": "transcribe"
}


def transcription_audio(audio: np.ndarray) -> str:
    """
    """
    text = whisper.transcribe(model, audio, **parameters)
    return text


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

    with open(json_outpath, 'w') as file:
        json.dump(result, file)
