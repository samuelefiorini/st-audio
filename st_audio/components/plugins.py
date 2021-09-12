from functools import namedtuple
from typing import Union

import streamlit as st

from pedalboard import (Chorus, Compressor, Convolution, Gain, LadderFilter,
                        Limiter, Phaser, Reverb)

# Define a new plugin
Plugin = namedtuple('Plugin', ['name', 'value'])


def all() -> list:
    """Return list of all available plugins.

    Returns:
        Available plugins name
    """
    return [
        'Chorus', 'Compressor', 'Convolution', 'Gain', 'LadderFilter',
        'Limiter', 'Phaser', 'Reverb'
    ]


def make(
    name: str,
) -> Union[Chorus, Compressor, Convolution, Gain, LadderFilter, Limiter,
           Phaser, Reverb]:
    """Make a new plugin from its name and parameters

    Args:
        name (str): Plugin name (see https://github.com/spotify/pedalboard#usage).

    Raises:
        ValueError: In case of unknown plugin.

    Returns:
        Pedalboard native plugin
    """
    with st.expander(name, expanded=True):
        if name.lower() == 'chorus':
            plugin = _make_chorus()
        elif name.lower() == 'compressor':
            plugin = _make_compressor()
        elif name.lower() == 'convolution':
            plugin = _make_convolution()
        elif name.lower() == 'gain':
            plugin = _make_gain()
        elif name.lower() == 'ladderfilter':
            plugin = _make_ladderfilter()
        elif name.lower() == 'limiter':
            plugin = _make_limiter()
        elif name.lower() == 'phaser':
            plugin = _make_phaser()
        elif name.lower() == 'reverb':
            plugin = _make_reverb()
        else:
            raise ValueError(f'Plugin {name} not known.')    
    return Plugin(name, plugin)


def _make_chorus() -> Chorus:
    st.write('''
    A basic chorus effect.
    
    This audio effect can be controlled via the speed and depth of the LFO controlling the frequency response, a mix control, a feedback control, and the centre delay of the modulation.
    
    Note: To get classic chorus sounds try to use a centre delay time around 7-8 ms with a low feeback volume and a low depth. This effect can also be used as a flanger with a lower centre delay time and a lot of feedback, and as a vibrato effect if the mix value is 1.
    ''')
    return Chorus(rate_hz=st.slider('Rate (Hz)', 1., 10., 1., 1.),
                  depth=st.slider('Depth', 0., 20., .25, 0.1),
                  centre_delay_ms=st.slider('Centre delay (ms)', 1., 25., 7., 1.),
                  feedback=st.slider('Feedback', 0., 10., 0., 0.5),
                  mix=st.slider('Mix', 0., 1., 0.5, 0.1)
                  )


def _make_compressor() -> Compressor:
    st.write('''
        A dynamic range compressor, used to amplify quiet sounds and reduce the volume of loud sounds.
        ''')
    return Compressor(threshold_db=st.slider('Threshold (dB)', -100, 10, 0, 5),
                      ratio=1 / st.slider('Ratio (x:1)', 1, 50, 1, 1),
                      attack_ms=st.slider('Attack (ms)', 1, 500, 1, 10),
                      release_ms=st.slider('Release (ms)', 1, 500, 100, 10))


def _make_convolution():
    pass


def _make_gain():
    pass


def _make_ladderfilter():
    pass


def _make_limiter():
    pass


def _make_phaser():
    pass


def _make_reverb():
    pass