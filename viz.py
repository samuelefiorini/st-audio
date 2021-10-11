import os
from datetime import timedelta

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from scipy.signal import windows
import streamlit as st
from plotly.subplots import make_subplots
from scipy import signal

from . import utils


# def specgram2d(y, srate=44100, ax=None, title=None):
  
#   if not ax:
#     ax = plt.axes()
#     ax.set_title(title, loc='center', wrap=True)
#     spec, freqs, t, im = ax.specgram(y, Fs=fs, scale='dB', vmax=0)
#     ax.set_xlabel('time (s)')
#     ax.set_ylabel('frequencies (Hz)')
#     cbar = plt.colorbar(im, ax=ax)
#     cbar.set_label('Amplitude (dB)')
#     cbar.minorticks_on()
#     return spec, freqs, t, im
# fig1, ax1 = plt.subplots()
# specgram2d(x, srate=fs, ax=ax1)
# plt.show()


def show_spectre(data: np.array, sample_rate: float):

    fig = go.Figure()    
    fig.add_trace(
        go.Scatter(
            y = data,
            x = np.arange(len(data))/sample_rate
        ))
    st.plotly_chart(fig, use_container_width=True)


    #ax = plt.axes()
    #Sxx, freq, time, _ = ax.specgram(data, Fs=sample_rate, scale='dB')

    with st.sidebar.expander('Spectrogram parameters', expanded=True):
        window_length = st.sidebar.slider('Window length (s)', 0.005,   .5, 0.05)
        nyquist_frequency = int(sample_rate/2)
        maximum_frequency = st.sidebar.slider('Maximum frequency (Hz)', 5000, nyquist_frequency, 5500)

    # Spectrogram
    freq, time, Sxx = signal.spectrogram(data,
                                         fs=sample_rate,
                                         nperseg=int(window_length * sample_rate))

    
    fig = go.Figure()
    fig.add_trace(go.Heatmap(x=np.sort(time),
                                    y=np.sort(freq),
                                    z=10 * np.log10(Sxx),
                                    colorscale='Viridis',
                                    colorbar={'title': 'dB'}))

    fig.update_yaxes(title='Hz')
    st.plotly_chart(fig, use_container_width=True)


    

def load():

    if st.session_state.input_data is not None:
        audio, sample_rate = utils._load_audio(st.session_state.input_data)
        st.write(f"_Duration_: {timedelta(seconds=audio.shape[0] / sample_rate)} | _Sample rate_: {sample_rate} Hz")

        show_spectre(audio, sample_rate)
