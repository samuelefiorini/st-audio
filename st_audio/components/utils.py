import numpy as np
import soundfile as sf
import streamlit as st
from typing import Union


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
