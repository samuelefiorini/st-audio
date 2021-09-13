from typing import Union

import numpy as np
import soundfile as sf
import streamlit as st


@st.cache
def _load_audio(data: 'UploadedFile') -> Union[np.array, int]:
    """Load data with PySoundFile.

    See https://pysoundfile.readthedocs.io/en/latest/#soundfile.read

    Args:
        data (st.UploadedFile): File uploaded via Streamlit.

    Returns:
        Union[np.array, int]: audio data and sample rate
    """
    return sf.read(data)

def dump_audio(filename: str, data: np.array, sample_rate: float) -> None:
    """Dump audio data to wav file.

    Args:
        filename (str): Wav file name
        data (np.array): Audio data.
        sample_rate (float): Sample rate (Hz)
    """
    sf.write(filename, data, sample_rate)
    #with sf.SoundFile(filename, 'w', samplerate=sample_rate, channels=len(data.shape)) as f:
    #    f.write(data)