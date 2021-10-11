import streamlit as st

from pedalboard import (Chorus, Compressor, Convolution, Gain, LadderFilter,
                        Limiter, Phaser, Reverb)


def _make_chorus() -> Chorus:
    description = '''
    A basic chorus effect. This audio effect can be controlled via the speed and depth of the LFO controlling
    the frequency response, a mix control, a feedback control, and the centre delay of the modulation.
    Note: To get classic chorus sounds try to use a centre delay time around 7-8 ms with a low feeback volume
    and a low depth. This effect can also be used as a flanger with a lower centre delay time and a lot of feedback,
    and as a vibrato effect if the mix value is 1.
    '''
    effect = Chorus(rate_hz=st.slider('Rate (Hz)', 1., 10., 1., 1., key='chorus_rate_hz'),
                    depth=st.slider('Depth', 0., 20., .25, 0.1, key='chorus_depth'),
                    centre_delay_ms=st.slider('Centre delay (ms)', 1., 25., 7., 1., key='chorus_centre_delay_my'),
                    feedback=st.slider('Feedback', 0., 10., 0., 0.5, key='chorus_feedback'),
                    mix=st.slider('Mix', 0., 1., 0.5, 0.1, key='chorus_mix'))
    return description, effect


def _make_compressor() -> Compressor:
    description = '''
    A dynamic range compressor, used to amplify quiet sounds and reduce the volume of loud sounds.
    '''
    effect = Compressor(threshold_db=st.slider('Threshold (dB)', -100, 10, 0, 5, key='compressor_threshold_db'),
                        ratio=1 / st.slider('Ratio (x:1)', 1, 50, 1, 1, key='compressor_ratio'),
                        attack_ms=st.slider('Attack (ms)', 1, 500, 1, 10, key='compressor_attack_ms'),
                        release_ms=st.slider('Release (ms)', 1, 500, 100, 10, key='compressor_release_ms'))
    return description, effect


def _make_convolution():
    description = '''
    An audio convolution, suitable for things like speaker simulation or reverb modeling.
    '''
    effect = None
    impulse_response_filename = st.file_uploader('Impulse response', type=['wav'], key='convolution_impulse_response_filename')
    mix = st.slider('Mix', 0., 1., 0.5, 1.0, key='convolution_mix')
    if impulse_response_filename:
        effect = Convolution(impulse_response_filename=impulse_response_filename,
                             mix=mix)
    return description, effect

def _make_gain():
    description = '''
    Increase or decrease the volume of a signal by applying a gain value (in decibels). No distortion or other effects are applied.
    '''
    effect = Gain(gain_db=st.slider('Gain (dB)', -100, 10, 0, 5, key='gain_db'))
    return description, effect

def _make_ladderfilter():
    description = '''
    Multi-mode audio filter based on the classic Moog synthesizer ladder filter.
    '''
    mode = st.selectbox('Mode', ['LPF12', 'HPF12', 'BPF12', 'LPF24', 'HPF24', 'BPF24'], key='ladderfilter_mode')
    effect = LadderFilter(mode=LadderFilter.Mode.__dict__[mode],
                          cutoff_hz=st.slider('Cutoff (Hz)', 20., 20_000., 200., 100., key='ladderfilter_cutoff_hz'),
                          resonance=st.slider('Resonance', 0., 1., 0.5, 0.1, key='ladderfilter_resonance'),
                          drive=st.slider('Drive', 1., 10., 1., .1, key='ladderfilter_drive'))
    return description, effect

def _make_limiter():
    description = '''
    A simple limiter with standard threshold and release time controls, featuring two compressors and a hard clipper at 0 dB.
    '''
    effect = Limiter(threshold_db=st.slider('Threshold (dB)', -100, 10, 0, 5, key='limiter_threshold_db'),
                     release_ms=st.slider('Release (ms)', 1, 500, 100, 10, key='limiter_release_ms'))
    return description, effect


def _make_phaser():
    description = '''
    A 6 stage phaser that modulates first order all-pass filters to create sweeping notches in the magnitude frequency response.
    This audio effect can be controlled with standard phaser parameters: the speed and depth of the LFO controlling the frequency
    response, a mix control, a feedback control, and the centre frequency of the modulation.
    '''
    effect = Phaser(rate_hz=st.slider('Rate (Hz)', 1., 10., 1., 1., key='phaser_rate_hz'),
                    depth=st.slider('Depth', 0., 20., .5, 0.1, key='phaser_depth'),
                    centre_frequency_hz=st.slider('Cutoff (Hz)', 20., 20_000., 1300., 100., key='phaser_cutoff_hz'),
                    feedback=st.slider('Feedback', 0., 1., 0., 0.1, key='phaser_feedback'),
                    mix=st.slider('Mix', 0., 1., 0.5, 0.1, key='phaser_mix'))
    return description, effect

def _make_reverb():
    description = '''
    Performs a simple reverb effect on a stream of audio data. This is a simple stereo reverb, based on the technique and tunings used in FreeVerb.
    '''
    effect = Reverb(room_size=st.slider('Mix', 0., 1., 0.5, 0.1, key='reverb_room_size'),
                    damping=st.slider('Damping', 0., 1., 0.5, 0.1, key='reverb_damping'),
                    wet_level=st.slider('Mix', 0., 1., 0.33, 0.1, key='reverb_wet_level'),
                    dry_level=st.slider('Mix', 0., 1., 0.4, 0.1, key='reverb_dry_level'),
                    width=st.slider('Width', 0., 1., 1., 0.1, key='reverb_width'),
                    freeze_mode=st.slider('Width', 0., 1., 0., 0.1, key='reverb_freeze_mode'))
    return description, effect

# Dict of plugins to import
plugins = {
        'Chorus': _make_chorus,
        'Compressor': _make_compressor,
        'Convolution': _make_convolution,
        'Gain': _make_gain,
        'Ladderfilter': _make_ladderfilter,
        'Limiter': _make_limiter,
        'Phaser': _make_phaser,
        'Reverb': _make_reverb
    }
