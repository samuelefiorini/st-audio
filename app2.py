import plotly.graph_objects as go
import soundfile as sf
import streamlit as st
from pedalboard import Pedalboard

from plugins import plugins


def spectrogram():
    pass

# Make pedalboard in sidebar
pedalboard = {}
st.sidebar.title('⚡ Pedalboard')
for key, builder in plugins.items():
    with st.sidebar.expander(key, expanded=False):
        help, effect = builder()
        toggle = st.checkbox('Activate', key=f'toggle_{key}', help=help)
    pedalboard[key] = dict(
        in_use=toggle,
        effect=effect
    )

# Load input song
st.write('# 📂 Import audio file')
audio_file = st.file_uploader('', type=['wav'])
if audio_file is not None:
    audio = audio_file.getvalue()
    st.write('🎧 **Play input track**')
    st.audio(audio, format='audio/wav')
    
    # Convert audio to numpy and extract sample_rate
    data, sample_rate = sf.read(audio)

    st.write(data)

    # Make pedalboard
    board = list(dict(filter(lambda x: x[1]['in_use'], pedalboard.items())).values())
    #board = Pedalboard(board, sample_rate=sample_rate)


    # Show input spectrum

    # Show output spectrum
