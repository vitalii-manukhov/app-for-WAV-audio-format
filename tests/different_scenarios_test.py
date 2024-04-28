from app_v1.modification_audio import change_speed, change_volume
from app_v1.modification_audio import save_audio_new
from app_v1.transcription_audio import transcription_audio
from app_v1.transcription_audio import save_text_to_json

from utils.config import settings
import os
import whisper


def test_guitars():
    """
    Тестирование модификации аудифайлов с гитарой
    """
    # # 1.
    # # Изменение скорости
    audio_path = settings.get_audio_path("guitar_2.wav")
    factor_speed = 10
    result = change_speed(audio_path, factor_speed)

    audio_new_path = audio_path.split('.')[0] + "_new.wav"
    if os.path.isfile(audio_new_path):
        os.remove(audio_new_path)
    save_audio_new(audio_path, result)

    # Изменение громкости
    factor_volume = 20
    result = change_volume(audio_new_path, factor_volume)

    os.remove(audio_new_path)
    save_audio_new(audio_path, result)

    # 2.
    # Изменение скорости
    audio_path = settings.get_audio_path("guitar_3.wav")
    factor_speed = 0.1
    result = change_speed(audio_path, factor_speed)

    audio_new_path = audio_path.split('.')[0] + "_new.wav"
    if os.path.isfile(audio_new_path):
        os.remove(audio_new_path)
    save_audio_new(audio_path, result)

    # Изменение громкости
    factor_volume = -10
    result = change_volume(audio_new_path, factor_volume)

    os.remove(audio_new_path)
    save_audio_new(audio_path, result)


def test_speeches():
    """
    Тестирование распознавания аудифайлов с речью
    """
    # 1.
    audio_path = settings.get_audio_path("speech_2.wav")
    audio = whisper.load_audio(audio_path)
    text = transcription_audio(audio)

    base = audio_path.split('.')[0]
    json_path = f"{base}_transcription.json"

    if os.path.isfile(json_path):
        os.remove(json_path)

    save_text_to_json(audio_path, text)

    # 2.
    audio_path = settings.get_audio_path("speech_6.wav")
    audio = whisper.load_audio(audio_path)
    text = transcription_audio(audio)

    base = audio_path.split('.')[0]
    json_path = f"{base}_transcription.json"

    if os.path.isfile(json_path):
        os.remove(json_path)

    save_text_to_json(audio_path, text)
