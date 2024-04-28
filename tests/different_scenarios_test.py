from app_v1.modification_audio import change_speed, change_volume
from app_v1.modification_audio import save_audio_new

from utils.config import settings
import os
import librosa


def test_guitars():
    """
    Тестирование модификации аудифайлов
    со звуками гитары
    """
    # 1.
    # Изменение скорости
    audio_path = settings.get_audio_path("guitar_2.wav")
    y, sr = librosa.load(audio_path)
    factor_speed = 10
    result = change_speed(y, factor_speed)

    audio_new_path = audio_path.split('.')[0] + "_new.wav"
    if os.path.isfile(audio_new_path):
        os.remove(audio_new_path)
    save_audio_new(audio_path, result, sr)

    # Изменение громкости
    factor_volume = 20
    result = change_volume(audio_new_path, factor_volume)

    os.remove(audio_new_path)
    save_audio_new(audio_path, result, sr)

    # 2.
    # Изменение скорости
    audio_path = settings.get_audio_path("guitar_3.wav")
    y, sr = librosa.load(audio_path)
    factor_speed = 0.1
    result = change_speed(y, factor_speed)

    audio_new_path = audio_path.split('.')[0] + "_new.wav"
    if os.path.isfile(audio_new_path):
        os.remove(audio_new_path)
    save_audio_new(audio_path, result, sr)

    # Изменение громкости
    factor_volume = -10
    result = change_volume(audio_new_path, factor_volume)

    os.remove(audio_new_path)
    save_audio_new(audio_path, result, sr)
