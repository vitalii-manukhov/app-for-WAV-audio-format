import librosa
import soundfile as sf
import numpy as np
import os
from pydub import AudioSegment

# audio_path: str = ""
# y, sr = librosa.load(audio_path)
# factor = ...
# audio_new = change_speed(y, factor)
# save_audio_new(audio_path, audio_new, sr)


def change_speed(audio: np.ndarray, factor: float) -> np.ndarray:
    """
    """
    return librosa.effects.time_stretch(audio, rate=factor)


# audio_path: str = ""
# factor = ...
# audio_new = change_volume(audio_path, factor)


def change_volume(audio_path: str, factor: float) -> np.ndarray:
    """
    """
    audio_segment = AudioSegment.from_file(audio_path)
    new_audio_segment = audio_segment + factor
    result = np.array(new_audio_segment.get_array_of_samples())
    return result


def save_audio_new(audio_path: str, audio_new: np.ndarray, sr: float) -> None:
    base = audio_path.split('.')[0]
    audio_outpath = base + "_new.wav"

    if os.path.isfile(audio_outpath):
        i = 1
        while os.path.isfile(f"{base}_new_({i}).wav"):
            i += 1
        audio_outpath = f"{base}_new_({i}).wav"

    sf.write(audio_outpath, audio_new, sr)
