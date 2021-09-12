import streamlit as st


def load():
    st.sidebar.write('# 🔊 Welcome to `st-audio`')
    
    st.sidebar.write('## Import audio file')
    fp = st.sidebar.file_uploader('', type=['wav'])