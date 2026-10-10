# Build scripts

Internal scripts that generate assets for the course. Not student-facing.

## `generate-audio-demos.py`

Generates the audio demo files used in the Module 2 Week 2 reading
(`module-02-audio-editing-mixing/lessons/01-reading-digital-audio.html`). The reading
references these files in its embedded audio players for the in-text
sample rate and bit depth demonstrations.

### What it produces

Output directory: `assets/audio/module-02-week-02/`

| File | Sample rate | Bit depth | Purpose |
|---|---|---|---|
| `source-44k-16bit.wav` | 44.1 kHz | 16-bit | Reference source (CD quality) |
| `sr-8k-16bit.wav` | 44.1 kHz playback, 8 kHz bandwidth | 16-bit | Telephone-quality demo (anti-alias filtered) |
| `sr-4k-16bit.wav` | 44.1 kHz playback, 4 kHz bandwidth | 16-bit | Truly lo-fi demo (anti-alias filtered) |
| `bd-8bit-44k.wav` | 44.1 kHz | 8-bit (quantized) | Audible quantization noise |
| `bd-4bit-44k.wav` | 44.1 kHz | 4-bit (quantized) | Severely degraded |
| `alias-8k-no-filter.wav` | 44.1 kHz playback, 8 kHz bandwidth | 16-bit | Aliasing demo: same bandwidth as `sr-8k-16bit` but produced via naive decimation (no anti-alias filter), so high frequencies fold back as audible artifacts |

All six files play at 44.1 kHz. The sample-rate demos are band-limited
with polyphase filtering, matching what an ADC captures at a low rate.
The aliasing demo skips the filter, so high frequencies fold back. The
bit-depth demos are quantized to fewer levels.

### The source sound

A 7.5-second A major arpeggio (A3, C#4, E4, A4) of Karplus-Strong
plucked-string notes. The sharp attacks have the high-frequency content
that sample-rate reduction removes. The long decays into near-silence
are where quantization noise becomes audible.

### Re-running


```
python3 under-the-hood/build/generate-audio-demos.py
```

Requires `numpy` and `scipy`. The Karplus-Strong noise burst is
unseeded, so each run differs slightly in timbre and keeps the same
structure. For identical output, add `np.random.seed(42)` near the top
of the script.

## `generate-audio-demos-week-03.py`

Generates the audio demo files used in the Module 2 Week 3 reading
(`module-02-audio-editing-mixing/lessons/04-reading-editing-envelope.html`). Twelve
files in four sets.

### What it produces

Output directory: `assets/audio/module-02-week-03/`

Section 1 (the envelope concept) has three contrasting envelopes:

| File | Synthesis | Purpose |
|---|---|---|
| `env-sharp.wav` | Filtered noise burst with very fast envelope | Sharp attack, no sustain, fast release (woodblock-like) |
| `env-sustained.wav` | Sine mixture with curved 1.8 s attack + 1.5 s release | Slow swell, long sustain, gentle decay (pad-like) |
| `env-evolving.wav` | Filtered noise with slow LFO on cutoff | Continuous texture with no clear ASR boundaries |

Section 3 (editing changes envelope) has one source with four envelopes:

| File | Operation | Purpose |
|---|---|---|
| `edit-source.wav` | Karplus-Strong pluck, 3 s, A3 | Reference: complete attack-sustain-release |
| `edit-truncated.wav` | Source cut hard at 0.5 s | Demonstrates: cutting off the release |
| `edit-reversed.wav` | Source played backward | Demonstrates: attack ↔ release swap |
| `edit-fade-in.wav` | Source with 1 s linear fade-in | Demonstrates: replacing a sharp attack with a slow one |

Section 3 also has the edit-boundary seam (click pops at hard cuts):

| File | Operation | Purpose |
|---|---|---|
| `seam-hardcut.wav` | Two band-passed noise textures concatenated | Audible click at the boundary |
| `seam-crossfade.wav` | Same two textures with 200 ms crossfade | No audible click |

Section 2 (tape physics) has the time-pitch coupling set:

| File | Operation | Purpose |
|---|---|---|
| `tape-source.wav` | Voice recording from `assets/audio/source/voice-tape-demo.aif`, mono 44.1k | Reference: 1× speed, ~5.7 s |
| `tape-slow.wav` | Same source via `asetrate=33075,aresample=44100` | 0.75× speed, ~7.6 s, ~5 semitones lower |
| `tape-fast.wav` | Same source via `asetrate=58800,aresample=44100` | 1.33× speed, ~4.3 s, ~5 semitones higher |

The tape demos use ffmpeg's `asetrate` filter rather than DSP-based
time-stretch or pitch-shift. `asetrate` reinterprets the file's
sample rate without changing the sample data, which is mathematically
identical to what a tape machine does at non-standard playback speed:
duration and pitch shift together, by exactly the same ratio.

### Re-running

```
python3 under-the-hood/build/generate-audio-demos-week-03.py
```

Requires `numpy`, `scipy`, and `ffmpeg` (the latter for the tape
demos). The voice source must be present at
`assets/audio/source/voice-tape-demo.aif`; if it's missing, the
script prints a warning and skips the tape demos but still rebuilds
the other 9 files.

The Karplus-Strong source used in the editing demos uses a fixed
random seed (42), so output is deterministic across runs.

## `generate-audio-demos-week-05.py`

Generates the audio demo files and two SVG diagrams used in the Module 2 Week 5 reading
(`module-02-audio-editing-mixing/lessons/07-reading-dynamics.html`)
and the source for the dynamics tool's embedded demo
(`module-02-audio-editing-mixing/lessons/08-tool-mixing-dynamics.html`).
Nineteen audio files: one set for each of the reading's four main
sections (dynamic range, threshold and ratio, attack and release,
limiting and the loudness wars) and three supplements (normalization
contrast, timbre A/B, the dynamics tool's demo source).

### What it produces

Output directory: `assets/audio/module-02-week-05/`

- `range-wide.wav`, `range-narrow.wav`: Section 1 (dynamic range)
- `tr-source.wav`, `tr-light.wav`, `tr-medium.wav`, `tr-heavy.wav`: Section 2 (threshold and ratio)
- `ar-source.wav`, `ar-fast-attack.wav`, `ar-slow-attack.wav`,
  `ar-fast-release.wav`, `ar-slow-release.wav`: Section 3 (attack and release)
- `limit-natural.wav`, `limit-light.wav`, `limit-crushed.wav`: Section 4 (limiting and the loudness wars)
- `norm-quiet.wav`, `norm-loud.wav`: Section 2 supplement (normalization contrast, same shape at two peak levels)
- `timbre-scaled.wav`, `timbre-compressed.wav`: Section 2 supplement (timbre A/B, a scaled-only version and a compressed version with makeup gain, peak-matched)
- `dynamic-tool-demo.wav`: source audio for the dynamics tool's built-in demo button (`08-tool-mixing-dynamics.html`). The tool embeds this file as base64 inside the HTML; see `embed-tool-demo.py` below for the re-embed step.

Diagrams (`assets/images/module-02-week-05/`), rendered as the source of truth and inlined into the reading:

- `wide-vs-narrow.svg`: Section 1 (dynamic range), the source loop as wide and narrow waveform panels stacked on one shared vertical scale.
- `norm-quiet-vs-loud.svg`: Section 2 (normalizing), quiet and peak-normalized versions of one loop stacked under a shared dashed ceiling.

### Implementation notes

The compressor is a feed-forward digital compressor with a one-pole
peak detector and a 2 dB soft knee. Gain is computed in the log domain
and applied as a linear multiplier. Attack and release use exponential
time constants of the form `exp(-1/(t*sr))`.

Sections 1 and 4 (dynamic-range and limiter demos) use a real
Ableton-rendered stereo loop as source material: conga slaps at
maximum velocity, shaker and clave at low velocity. The natural
dynamic range of the loop is about 21 dB crest factor, with about 57 dB
between the loudest and quietest 100 ms windows.
The loop is at `assets/audio/source/dynamic-loop.wav`. These two
sections use stereo-linked compression (`compress_stereo`,
`limit_stereo`): a single sidechain detector reads `max(|L|, |R|)` so
both channels are reduced equally and the stereo image stays stable.

Sections 2 and 3 use synthesized mono sources: six hits at set levels
in Section 2, and a percussion loop with exact transient timing in
Section 3.

The Section 2 and 3 compression demos have no makeup gain. Every file
in those sections is normalized to a -3 dBFS peak at write time. The
dynamic-range pair (Section 1) and the limiter trio (Section 4) are
written without normalization: peaks match within each set, and
perceived loudness rises with the amount of compression.

The peak limiter has no lookahead, so fast transients can exceed the
ceiling by a couple of dB. A final hard-clip pass at the ceiling
enforces the peak exactly, so the peak meter reads identically across
files within a comparison set.

The narrow-version boost in `gen_dynamic_range` is calibrated for the
specific source loop (currently `NARROW_BOOST_DB = 18` for ~6 dB RMS
gap). If you change the source, sweep this value to recalibrate.

## `embed-tool-demo.py`

Re-embeds the dynamics tool's demo audio as base64 inside
`module-02-audio-editing-mixing/lessons/08-tool-mixing-dynamics.html`.
Run this after regenerating `dynamic-tool-demo.wav` if the embedded
copy should reflect the new audio.

### The embedded copy

Browsers block `fetch()` across origins under the `file://` protocol, so
fetching a sibling WAV from the tool's HTML fails when the page is
opened by double-clicking. The WAV is embedded in the HTML instead,
which takes the file from ~30 KB to ~1.4 MB.

The script reads the canonical WAV from
`assets/audio/module-02-week-05/dynamic-tool-demo.wav`, base64-encodes
it, and replaces the contents of the
`<script type="application/octet-stream" id="demo-audio-b64">` block
inside the tool HTML with the fresh data. No other parts of the tool
are touched.

### Re-running

```
python3 under-the-hood/build/embed-tool-demo.py
```

Standard library only. Idempotent.

## `generate-orientation-sample.py`

Generates `orientation-sample.wav`, the shared asset for the Module 2
Week 2 Audacity orientation lab
(`module-02-audio-editing-mixing/lessons/03-handout-audacity-orientation.html`).

### What it produces

Output directory: `assets/audio/module-02-week-02/`

| File | Sample rate | Bit depth | Length | Purpose |
|---|---|---|---|---|
| `orientation-sample.wav` | 48 kHz | 24-bit | 16.0 s | Stereo bell-like resonance for the Lab 1 import, cut, and fade exercises |

The lab copy is uploaded to `/public/module-02/orientation/` on the class
server; the repo copy is the source of truth.

### The sound

Struck-bell additive synthesis: eleven inharmonic partials at Risset bell
ratios over a 400 Hz base, each with its own T60, plus a filtered noise
burst at the onset for the mallet contact. Upper partials are given short
T60s so the strike brightness falls away in the first few seconds and
leaves the low ringing body behind; the spectral centroid runs from about
860 Hz at the onset to about 550 Hz by 7 s. A global `(1 - t/16) ** 1.25`
envelope reaches digital silence at the final sample.

Measured decay, peak per second: -3 dBFS at 0 s, -13 at 5 s, -17 at 7 s,
-29 at 12 s, -47 at 15 s. The audible-at-7-seconds requirement is in
[`assets/asset-recipes.md`](../../assets/asset-recipes.md).

The two channels share partial phases and differ by 4 cents of detune in
opposite directions, a 6 percent difference in decay rate, and a 4 ms
inter-channel delay. The result has slow beating and a wide image; the
mono sum is 1.7 dB below the stereo peak, with no deep cancellation.

### Re-running

```
python3 under-the-hood/build/generate-orientation-sample.py
```

Requires `numpy` and `scipy`. Fully seeded: every run produces byte-identical
output.
