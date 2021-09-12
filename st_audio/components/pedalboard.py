import streamlit as st

from . import utils
from pedalboard import (Chorus, Compressor, Convolution, Gain, LadderFilter,
                        Limiter, Pedalboard, Phaser, Reverb)


def load():
    if st.session_state.input_data is not None:
        audio, sample_rate = utils._load_audio(st.session_state.input_data)        
        




# Make a Pedalboard object, containing multiple plugins:
#board = Pedalboard([
#    Compressor(threshold_db=-50, ratio=25),
#    Gain(gain_db=30),
#    Chorus(),
#    LadderFilter(mode=LadderFilter.Mode.HPF12, cutoff_hz=900),
#    Phaser(),
#    Convolution("./guitar_amp.wav", 1.0),
#    Reverb(room_size=0.25),
#], sample_rate=sample_rate)

# Pedalboard objects behave like lists, so you can add plugins:
#board.append(Gain(gain_db=10))
#board.append(Compressor(threshold_db=-25, ratio=10))
#board.append(Limiter())

# Run the audio through this pedalboard!
#effected = board(audio)
