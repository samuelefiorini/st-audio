import streamlit as st

from pedalboard import Pedalboard

from . import plugins, utils

def load():
    if st.session_state.input_data is not None:
        audio, sample_rate = utils._load_audio(st.session_state.input_data)        
        # Summarize current pedalboard
        if len(st.session_state.board):
            st.write('### Plugins on board:')
            st.write(' ➞ '.join([p.name for p in st.session_state.board]))
            if st.button('♻️ Clean board'):
                st.session_state.board = []
                st.experimental_rerun()
        else:
            st.write('Empty board 🙃')

        # Create pedalboard
        left, right = st.columns((1, 10))
        with right:
            name = st.selectbox('New plugin', options=['...'] + plugins.all())
            if name != '...':
                plugin = plugins.make(name)
        with left:
            if (name != '...') and st.button('+'):
                st.session_state.board.append(plugin)
                st.experimental_rerun()



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
