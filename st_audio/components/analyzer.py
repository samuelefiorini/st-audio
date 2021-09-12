from datetime import timedelta

import streamlit as st

from . import utils


def load():
    if st.session_state.input_data is not None:
        audio, sample_rate = utils._load_audio(st.session_state.input_data)        
        st.write(f"_Duration_: {timedelta(seconds=audio.shape[0] / sample_rate)} | _Sample rate_: {sample_rate} Hz")
