import streamlit as st

from st_audio.components import analyzer, pedalboard, sidebar

# Initialize page config
st.set_page_config(page_title='st-audio')

# Initialize session state
_ = st.session_state.setdefault('input_data', None)
_ = st.session_state.setdefault('board', [])

# Render main app
page = sidebar.load()

if page == 'pedalboard':
    pedalboard.load()
elif page == 'analyzer':
    analyzer.load()
