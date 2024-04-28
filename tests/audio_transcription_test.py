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
    """
    Тестирование расшифровки аудио в текст
    """
    # 1.
    audio_path = settings.get_audio_path("speech_4.wav")
    audio = whisper.load_audio(audio_path)
    result = transcription_audio(audio)
    expected = """
    Экономика — хозяйственная деятельность,
     а также совокупность общественных отношений,
     которые складываются в системе производства,
     распределения, обмена и потребления товаров и услуг.
     В результате этой деятельности непрерывно воспроизводятся блага,
     обеспечивающие жизнедеятельность людей.
    """

    assert result is not None
    assert isinstance(result, str)

    similarity = similar(result, expected)

    print("1.")
    print("Схожесть:\n", similarity)
    print("Текст:\n", result)

    assert similarity > 0.9

    # 2.
    audio_path = settings.get_audio_path("speech_3.wav")
    audio = whisper.load_audio(audio_path)
    result = transcription_audio(audio)
    expected = """
    Первичный сектор экономики. Вторичный сектор экономики.
     Третичный сектор экономики. Четверичный сектор экономики.
    """

    assert result is not None
    assert isinstance(result, str)

    similarity = similar(result, expected)

    print("2.")
    print("Схожесть:\n", similarity)
    print("Текст:\n", result)

    assert similarity > 0.7

    # 3.
    audio_path = settings.get_audio_path("speech_5.wav")
    audio = whisper.load_audio(audio_path)
    result = transcription_audio(audio)
    expected = """
    Горизонт.
    """

    assert result is not None
    assert isinstance(result, str)

    similarity = similar(result, expected)

    print("3.")
    print("Схожесть:\n", similarity)
    print("Текст:\n", result)

    assert similarity > 0.3


def test_save_text_to_json():
    """
    Тестирование сохранения текста в формате json
    """
    audio_path = settings.get_audio_path("speech_1.wav")
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
