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

#def _dump_audio(data:)
#with sf.SoundFile('./processed-output-stereo.wav', 'w', samplerate=sample_rate, channels=len(effected.shape)) as f:
#    f.write(effected)