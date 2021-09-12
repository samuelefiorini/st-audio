import streamlit as st

from st_audio.components import analyzer, pedalboard, sidebar

# Initialize page config
st.set_page_config(page_title='st-audio')

# Initialize session state
for key in ['input_data']:
    _ = st.session_state.setdefault(key, None)

# Render main app
page = sidebar.load()

if page == 'pedalboard':
    pedalboard.load()
elif page == 'analyzer':
    analyzer.load()
