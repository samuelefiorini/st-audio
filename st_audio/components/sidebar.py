import streamlit as st

# App pages
__pages__ = {
    '🎛️ Pedalboard': 'pedalboard',
    '🔬 Analyzer': 'analyzer'
}


def load():
    st.sidebar.write('## 🎙️ Toolbox')
    choice = st.sidebar.radio('', __pages__.keys())
    
    st.sidebar.write('## 📂 Import file')
    audio_file = st.sidebar.file_uploader('', type=['wav'])
    st.session_state.input_data = audio_file
    if audio_file is not None:
        audio = audio_file.getvalue()
        st.sidebar.write('🎧 **Play input track**')
        st.sidebar.audio(audio, format='audio/wav')


    st.write(f'## {choice}')
    return __pages__[choice]