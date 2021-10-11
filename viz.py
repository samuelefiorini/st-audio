import numpy as np
import plotly.graph_objects as go
import streamlit as st
from scipy import signal


def audio_data(data: np.array, sample_rate: float, key: str = ''):
    """Show audio data.

    Plot audio data amplitude and spectrogram.

    Args:
        data (np.array): Audio data.
        sample_rate (float): Sample rate.
    """    
    # Plot audio signal
    fig1 = go.Figure()
    fig1.add_trace(
        go.Scatter(
            y = data,
            x = np.arange(len(data))/sample_rate
        ))
    fig1.update_layout(width=800)
    fig1.update_xaxes(title='Time [s]')

    with st.sidebar.expander(f'{key.title()} Spectrogram parameters', expanded=True):
        window_length = st.slider('Window length (s)', 0.005, .5, 0.05, key=f'{key}_window_length')
        nyquist_frequency = int(sample_rate/2)
        maximum_frequency = st.slider('Maximum frequency (Hz)', 5000, nyquist_frequency, 5500, key=f'{key}_maximum_frequency')

    # Spectrogram
    freq, time, Sxx = signal.spectrogram(data,
                                         fs=sample_rate,
                                         nperseg=int(window_length * sample_rate))

    fig2 = go.Figure()
    fig2.add_trace(go.Heatmap(x=np.sort(time),
                                    y=np.sort(freq),
                                    z=10 * np.log10(Sxx),
                                    colorscale='Viridis',
                                    colorbar={'title': 'dB'}))
    fig2.update_layout(width=800)
    fig2.update_yaxes(title='Frequency [Hz]')
    fig2.update_xaxes(title='Time [s]')
    
    # Show figures
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
