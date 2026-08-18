"""
Generates the Module 2 Week 2 lab asset `orientation-sample.wav`.

Produces (1 file):

  - orientation-sample.wav : stereo bell-like resonance, 16.0 s, 48 kHz / 24-bit

The lab (module-02-audio-editing-mixing/lessons/03-handout-audacity-orientation.html)
has students import the file, select from roughly 7 s to the end, delete the
selection, and apply a fade-out to what remains. The sound therefore has to be
clearly audible at the 7-second mark and has to taper visibly across the whole
16 s so the waveform reads as a decay on screen.

Synthesis: struck-bell additive model. A set of inharmonic partials at Risset
bell ratios, each with its own decay time (the bright upper partials die away in
the first seconds, the low partials ring on), plus a short filtered-noise strike
transient at the onset. A global power-curve envelope carries the whole sound to
silence at 16.0 s; it is gentle enough that the sound is still around -8 dBFS at
the 7-second mark, so the region students select is both audible and visible on
the waveform. The two channels share partial phases and differ by a few cents of
detune, a small decay-rate difference, and a 4 ms inter-channel delay, which
gives slow beating and a wide image while still summing cleanly to mono.

Output: assets/audio/module-02-week-02/

Re-run with: python3 under-the-hood/build/generate-orientation-sample.py
Requires numpy and scipy. Fully seeded: every run produces identical output.
"""

import os
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

# ----- Output paths -----

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(REPO_ROOT, "assets", "audio", "module-02-week-02")
os.makedirs(OUT_DIR, exist_ok=True)

SR = 48000
DURATION = 16.0
BASE_FREQ = 400.0
PEAK_DBFS = -3.0

# Risset bell partial ratios. Each entry is (ratio, amplitude, T60 in seconds).
# The T60s are long relative to the 16 s file: the global envelope below sets
# the overall shape, and the partial decays handle timbre over time. Upper
# partials are given short T60s so the strike's brightness falls away in the
# first seconds and leaves the low ringing body behind.
PARTIALS = [
    (0.56, 2.00, 120.0),
    (0.92, 1.40, 100.0),
    (1.19, 1.60, 90.0),
    (1.71, 2.20, 60.0),
    (2.00, 2.67, 70.0),
    (2.74, 1.40, 22.0),
    (3.00, 1.20, 22.0),
    (3.76, 1.00, 10.0),
    (4.07, 1.00, 10.0),
    (5.43, 0.60, 5.0),
    (6.79, 0.40, 3.5),
]

# Global envelope: (1 - t/DURATION) ** GLOBAL_CURVE, reaching exactly zero at
# the final sample.
GLOBAL_CURVE = 1.25


# ----- Helpers -----

def write_wav24(path, audio, sr=SR, peak_dbfs=PEAK_DBFS):
    """Normalize to peak_dbfs and write as 24-bit stereo WAV."""
    audio = np.asarray(audio, dtype=np.float64)
    peak = np.max(np.abs(audio))
    if peak > 0:
        audio = audio * ((10 ** (peak_dbfs / 20)) / peak)
    scaled = np.clip(np.round(audio * 8388607), -8388608, 8388607).astype(np.int32)
    # scipy writes int32 as 32-bit PCM; pack the low three bytes by hand.
    raw = scaled.astype("<i4").tobytes()
    packed = bytearray()
    for i in range(0, len(raw), 4):
        packed += raw[i:i + 3]
    _write_wav_header(path, bytes(packed), sr, channels=audio.shape[1], bits=24)
    print(f"Wrote {path} ({len(audio)/sr:.2f} s, {sr} Hz, 24-bit, {audio.shape[1]} ch)")


def _write_wav_header(path, data, sr, channels, bits):
    import struct
    block_align = channels * bits // 8
    byte_rate = sr * block_align
    with open(path, "wb") as f:
        f.write(b"RIFF")
        f.write(struct.pack("<I", 36 + len(data)))
        f.write(b"WAVEfmt ")
        f.write(struct.pack("<IHHIIHH", 16, 1, channels, sr, byte_rate, block_align, bits))
        f.write(b"data")
        f.write(struct.pack("<I", len(data)))
        f.write(data)


def strike_transient(n, sr=SR, seed=7):
    """Short filtered-noise burst: the mallet contact before the body rings."""
    rng = np.random.default_rng(seed)
    noise = rng.normal(0, 1.0, n)
    sos = butter(2, [1200 / (sr / 2), 9000 / (sr / 2)], btype="band", output="sos")
    filt = sosfilt(sos, noise)
    t = np.arange(n) / sr
    env = np.exp(-t * 55.0)
    attack_n = int(0.0015 * sr)
    env[:attack_n] *= np.linspace(0, 1, attack_n)
    return filt * env * 0.15


def bell_channel(detune_cents, decay_trim, transient_seed):
    """One channel of the bell: summed partials, each with its own decay."""
    n = int(DURATION * SR)
    t = np.arange(n) / SR
    rng = np.random.default_rng(3)  # shared across channels: keeps mono sum clean
    out = np.zeros(n)
    for ratio, amp, partial_t60 in PARTIALS:
        freq = BASE_FREQ * ratio * (2 ** (detune_cents / 1200))
        t60 = partial_t60 * decay_trim
        decay = np.exp(-6.908 * t / t60)
        phase = rng.uniform(0, 2 * np.pi)
        out += amp * decay * np.sin(2 * np.pi * freq * t + phase)
    out += strike_transient(n, seed=transient_seed)
    return out


def build():
    n = int(DURATION * SR)
    left = bell_channel(detune_cents=-4.0, decay_trim=1.00, transient_seed=11)
    right = bell_channel(detune_cents=+4.0, decay_trim=0.94, transient_seed=23)

    # Small inter-channel delay widens the image without collapsing in mono.
    delay_n = int(0.004 * SR)
    right = np.concatenate([np.zeros(delay_n), right])[:n]

    stereo = np.stack([left, right], axis=1)

    # Global envelope: carries the sound to true silence at the final sample.
    t = np.arange(n) / SR
    env = (1.0 - t / DURATION) ** GLOBAL_CURVE
    stereo *= env[:, None]

    write_wav24(os.path.join(OUT_DIR, "orientation-sample.wav"), stereo)


if __name__ == "__main__":
    build()
