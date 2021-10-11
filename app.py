import numpy as np
import soundfile as sf
import streamlit as st
from pedalboard import Pedalboard

import viz
from plugins import plugins


#@st.cache
def load_audio(filename: str) -> tuple:
    """Load input audio file.

    Args:
        filename (str): Audio filename

    Returns:
        audio (np.array), sample_rate (float)
    """
    return sf.read(filename)


#@st.cache
def run_board(effects: list, audio: np.array, sample_rate: float) -> np.array:
    """Run board on input audio data.

    Args:
        board (list): List of Pedalboard effects.
        audio (np.array): Input audio data.

    Returns:
        Output (effected) audio data
    """
    board = Pedalboard(effects, sample_rate=sample_rate)
    return board(audio)


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
audio_file = st.file_uploader('', type=['wav'])
if audio_file is not None:
    st.title('Input track')
    audio = audio_file.getvalue()
    st.audio(audio, format='audio/wav')
    
    # Convert audio to numpy and extract sample_rate
    input_audio_data, sample_rate = load_audio(audio_file)

    # Extract effects
    effects = [e['effect'] for e in dict(filter(lambda x: x[1]['in_use'], pedalboard.items())).values()]
    
    # Show input spectrum
    viz.audio_data(input_audio_data, sample_rate, key='input')

    if len(effects):
        st.title('Output track')
        output_audio_data = run_board(effects, input_audio_data, sample_rate)

        # Write the audio back as a wav file:
        filename = f'./data/processed-{audio_file}.wav'
        with sf.SoundFile(filename, 'w', samplerate=sample_rate, channels=len(output_audio_data.shape)) as f:
            f.write(output_audio_data)
        st.audio(filename, format='audio/wav')
    
        # Show output spectrum
        viz.audio_data(output_audio_data, sample_rate, key='output')
