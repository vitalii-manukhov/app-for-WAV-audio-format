from app_v1.modification_audio import change_volume, change_speed
from app_v1.modification_audio import save_audio_new

from utils.config import settings
import librosa
import numpy as np
import os
from pydub import AudioSegment


# def test_change_speed():
#     """
#     Тестирование функции change_speed
#     для трёх сценариев:
#     Сделать аудио быстрее, медленнее или не изменить
#     """
#     # fast
#     audio_path = settings.get_audio_path("guitar_1.wav")
#     y, sr = librosa.load(audio_path)
#     factor = 2
#     result = change_speed(audio_path, factor)

#     assert result is not None
#     assert isinstance(result, np.ndarray)
#     assert len(result) < len(y)

#     # slow
#     audio_path = settings.get_audio_path("guitar_1.wav")
#     y, sr = librosa.load(audio_path)
#     factor = 0.5
#     result = change_speed(audio_path, factor)

#     assert result is not None
#     assert isinstance(result, np.ndarray)
#     assert len(result) > len(y)

#     # no change
#     audio_path = settings.get_audio_path("guitar_1.wav")
#     y, sr = librosa.load(audio_path)
#     factor = 1
#     result = change_speed(audio_path, factor)

#     assert result is not None
#     assert isinstance(result, np.ndarray)
#     assert len(result) == len(y)


# def test_change_volume():
#     """
#     Тестирование функции change_volume
#     для трёх сценариев:
#     Сделать аудио громче, тише или не изменить
#     """
#     # loud
#     audio_path = settings.get_audio_path("guitar_1.wav")
#     factor = 20
#     result = change_volume(audio_path, factor)

#     assert result is not None
#     assert isinstance(result, AudioSegment)

#     # silent
#     audio_path = settings.get_audio_path("guitar_1.wav")
#     factor = -20
#     result = change_volume(audio_path, factor)

#     assert result is not None
#     assert isinstance(result, AudioSegment)

#     # no change
#     audio_path = settings.get_audio_path("guitar_1.wav")
#     factor = 0
#     result = change_volume(audio_path, factor)

#     assert result is not None
#     assert isinstance(result, AudioSegment)


def test_save_audio_new():
    """
    Тестирование функции save_audio_new
    """
    # Изменение скорости
    audio_path = settings.get_audio_path("guitar_1.wav")
    y, sr = librosa.load(audio_path)
    factor_speed = 3
    result = change_speed(audio_path, factor_speed)

    audio_new_path = audio_path.split('.')[0] + "_new.wav"
    if os.path.isfile(audio_new_path):
        os.remove(audio_new_path)
    save_audio_new(audio_path, result)

    # Изменение громкости
    factor_volume = -20
    result = change_volume(audio_new_path, factor_volume)

    os.remove(audio_new_path)
    save_audio_new(audio_path, result)

    # Загрузка изменённого файла
    y_new, sr_new = librosa.load(audio_new_path)

    assert len(y) > len(y_new)
    assert sr == sr_new
