import streamlit as st

from pedalboard import Pedalboard

from . import plugins, utils

@st.cache
def make_board(plugins: list, sample_rate: float) -> Pedalboard:
    return Pedalboard(board, sample_rate=sample_rate)

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
            board = make_board(st.session_state.board,
                    sample_rate=sample_rate)
            with st.spinner('Applying effects...'):
                st.session_state.output_data = board(audio)
        # Save results
        if st.session_state.output_data is not None:
            st.write(type(st.session_state.output_data))

        
