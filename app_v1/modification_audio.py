import librosa
import soundfile as sf
import numpy as np
import os
from pydub import AudioSegment
from typing import Union


def change_speed(audio_path: str, factor: float) -> np.ndarray:
    """
    """
    y, sr = librosa.load(audio_path)
    return librosa.effects.time_stretch(y, rate=factor)


def change_volume(audio_path: str, factor: int) -> AudioSegment:
    """
    """
    sound = AudioSegment.from_file(audio_path)
    return sound + factor


def save_audio_new(audio_path: str,
                   audio_new: Union[AudioSegment, np.ndarray]) -> None:
    base = audio_path.split('.')[0]
    audio_outpath = base + "_new.wav"

    if os.path.isfile(audio_outpath):
        i = 1
        while os.path.isfile(f"{base}_new_({i}).wav"):
            i += 1
        audio_outpath = f"{base}_new_({i}).wav"

    if isinstance(audio_new, AudioSegment):
        audio_new.export(audio_outpath, format="wav")
    elif isinstance(audio_new, np.ndarray):
        y, sr = librosa.load(audio_path)
        sf.write(audio_outpath, audio_new, sr)
