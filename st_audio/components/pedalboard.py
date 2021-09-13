import os
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
                st.session_state.output_data = None
                st.experimental_rerun()
        else:
            st.write('Empty board 🙃')
        # Define pedalboard plugins
        left, right = st.columns((1, 10))
        with right:
            name = st.selectbox('New plugin', options=['...'] + plugins.all())
            if name != '...':
                plugin = plugins.make(name)
        with left:
            if (name != '...') and st.button('➕'):
                st.session_state.board.append(plugin)
                st.experimental_rerun()
        # Apply effetcts on audio
        if len(st.session_state.board) and st.button('Run!'):
            with st.spinner('Applying effects...'):
                board = Pedalboard([p.value for p in st.session_state.board],
                               sample_rate=sample_rate)
                st.session_state.output_data = board(audio)
        # Save results
        if st.session_state.output_data is not None:
            left, right = st.columns((1, 1))
            with left:
                _filename = st.text_input('Filename', f'processed-{st.session_state.input_data.name}')
                filename = os.path.join('data', _filename)
            with right:
                if st.button('Save 💾'):
                    utils.dump_audio(filename=filename,
                                     data=st.session_state.output_data,
                                     sample_rate=sample_rate)
        
            with open(filename, 'rb') as f:
                st.audio(f.read(), format='audio/wav')

        
