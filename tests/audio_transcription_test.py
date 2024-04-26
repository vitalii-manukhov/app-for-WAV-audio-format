from app_v1.transcription_audio import transcription_audio
from app_v1.transcription_audio import save_text_to_json

from utils.config import settings
import whisper
from difflib import SequenceMatcher
import os
import json


def similar(result: str, expected: str):
    return SequenceMatcher(None, result, expected).ratio()


def test_transcription_audio():
    audio_path = settings.get_audio_path("speach_1.wav")
    audio = whisper.load_audio(audio_path)
    result = transcription_audio(audio)
    expected = ""

    assert result is not None
    assert isinstance(result, str)

    similarity = similar(result, expected)
    assert similarity > 0.5


def test_save_text_to_json():
    audio_path = settings.get_audio_path("speach_1.wav")
    audio = whisper.load_audio(audio_path)
    text = transcription_audio(audio)

    base = audio_path.split('.')[0]
    json_path = f"{base}_transcription.json"

    if os.path.isfile(json_path):
        os.remove(json_path)

    save_text_to_json(audio_path, text)
    expected = {
        "transcription": text
    }

    with open(json_path, 'r') as file:
        result = json.load(file)

        assert result == expected
