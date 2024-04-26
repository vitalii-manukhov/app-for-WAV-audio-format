from app_v1.modification_audio import change_volume, change_speed
from app_v1.modification_audio import save_audio_new

from utils.config import settings
import librosa
import numpy as np
import os


def test_change_speed():
    """
    Тестирование функции change_speed
    для трёх сценариев:
    Сделать аудио быстрее, медленнее или не изменить
    """
    # fast
    audio_path = settings.get_audio_path("guitar_1.wav")
    y, sr = librosa.load(audio_path)
    factor = 2
    result = change_speed(y, factor)

    assert result is not None
    assert isinstance(result, np.ndarray)
    assert len(result) < len(y)

    # slow
    audio_path = settings.get_audio_path("guitar_1.wav")
    y, sr = librosa.load(audio_path)
    factor = 0.5
    result = change_speed(y, factor)

    assert result is not None
    assert isinstance(result, np.ndarray)
    assert len(result) > len(y)

    # no change
    audio_path = settings.get_audio_path("guitar_1.wav")
    y, sr = librosa.load(audio_path)
    factor = 1
    result = change_speed(y, factor)

    assert result is not None
    assert isinstance(result, np.ndarray)
    assert len(result) == len(y)


def test_change_volume():
    """
    Тестирование функции change_volume
    для трёх сценариев:
    Сделать аудио громче, тише или не изменить
    """
    # loud
    audio_path = settings.get_audio_path("guitar_1.wav")
    y, sr = librosa.load(audio_path)
    factor = 2
    result = change_volume(y, factor)

    assert result is not None
    assert isinstance(result, np.ndarray)
    assert np.all(result > y)

    # silent
    audio_path = settings.get_audio_path("guitar_1.wav")
    y, sr = librosa.load(audio_path)
    factor = 0.5
    result = change_volume(y, factor)

    assert result is not None
    assert isinstance(result, np.ndarray)
    assert np.all(result < y)

    # no change
    audio_path = settings.get_audio_path("guitar_1.wav")
    y, sr = librosa.load(audio_path)
    factor = 2
    result = change_volume(y, factor)

    assert result is not None
    assert isinstance(result, np.ndarray)
    assert np.all(result == y)


def test_save_audio_new():
    """
    Тестирование функции save_audio_new
    """
    audio_path = settings.get_audio_path("guitar_1.wav")
    y, sr = librosa.load(audio_path)
    factor = 2
    result = change_speed(y, factor)
    result = change_volume(result, factor)

    audio_new_path = audio_path.split('.')[0] + "_new.wav"

    if os.path.isfile(audio_new_path):
        os.remove(audio_new_path)

    save_audio_new(audio_path, result, sr)

    y_new, sr_new = librosa.load(audio_path)

    assert len(y) > len(y_new)
    assert np.all(y[:len(y_new)] < y_new)
    assert sr == sr_new
