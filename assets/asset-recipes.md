# Asset recipes

Per-asset specs for assets made by hand (recorded audio, photographs, screenshots): where each one is, what it is, and how to recreate or substitute it. Generated assets are documented with their scripts in [`under-the-hood/build/README.md`](../under-the-hood/build/README.md).

For Inés and anyone who rebuilds the course infrastructure. The TA only needs each asset at its path, and reports a missing one to Inés.

---

## Module 02 · audio editing & mixing

### Wed Wk 2 lab handout · `orientation-sample.wav`

The server copy is `/public/module-02/orientation/orientation-sample.wav`, used in Lab 1 (`module-02-audio-editing-mixing/lessons/03-handout-audacity-orientation.html`). It's a 16-second stereo bell resonance that decays to silence across its full length, WAV, 48 kHz, 24-bit.

The source of truth is `assets/audio/module-02-week-02/orientation-sample.wav`, written by [`generate-orientation-sample.py`](../under-the-hood/build/generate-orientation-sample.py); upload that copy to the server path. The synthesis is documented in the build README.

A substitute is any stereo sustained sound of about 10 to 18 seconds with a gradual decay and no hard ending, such as a long bowed note that fades, a struck rim recorded in stereo, or a sampler bell. It stays clearly audible at the 7-second mark, where students cut and fade in Step 5.

---

### Wed Wk 2 lab handout · Audacity screenshots

The files are in `assets/images/module-02-week-02/`, used in Lab 1 (`module-02-audio-editing-mixing/lessons/03-handout-audacity-orientation.html`). They were re-captured in June 2026 at the 48 kHz, 24-bit standard.

| Filename | Content |
|---|---|
| `audacity-settings.png` | Preferences → Audio Settings: Quality section showing Project Sample Rate 48000 Hz, Default Sample Rate 48000 Hz, Default Sample Format 24-bit |
| `audacity-interface-empty.png` | Empty Audacity main window with eight numbered orange markers on the regions in Step 3's annotation key (menu bar, transport, tools, level meters, Audio Setup, ruler, track area, selection toolbar) |
| `audacity-imported.png` | Main window with `orientation-sample.wav` imported as a stereo track, showing the decay across both channels |
| `audacity-selection.png` | Same window with a region selected from about 7 s to the end of the file |
| `audacity-fade-out.png` | Same window after the cut and fade-out: the file ends around 7.5 s, with the fade taper over the last 2.5 s |
| `audacity-export-prompt.png` | The "How would you like to export?" dialog with two options (Share to audio.com, On your computer) and the "Don't show again" checkbox |
| `audacity-export.png` | Export Audio dialog: filename `thiebaut-orientation.wav`, WAV (Microsoft), Stereo, 48000 Hz, Signed 24-bit PCM, Entire Project |

The markers on `audacity-interface-empty.png` are drawn into the PNG, numbered in the order of the handout's Step 3 key.

The empty Audacity 3.6 window shows no project sample rate; the rate is inside the Audio Setup dropdown. Marker 5 (Audio Setup) is described in the key as the place for host, device, channel, and project-rate settings.

---

## Module 03 · recording, sample prep & library building

### Wed Wk 6 lab handout · Audacity screenshots

The files are in `assets/images/module-03-week-06/`, used in Lab 1 (`module-03-recording/lessons/02-handout-recording-into-audacity.html`). Inés captured them on her Mac in May 2026.

| Filename | Content |
|---|---|
| `audacity-five-clips.png` | One mono track holding five clips in sequence: the flat noise-profile clip, then the four paper-sound clips of varying duration and amplitude |
| `audacity-noise-reduction-profile.png` | The Noise Reduction dialog in its Step 1 state, with the Get Noise Profile button at the top |
| `audacity-noise-reduction-apply.png` | The Noise Reduction dialog in its Step 2 state, with three sliders at their defaults (12 / 6.00 / 3) and OK at the bottom |

---

### Mon Wk 7 lecture · cable and microphone images

The files are in `assets/images/module-03-week-07/`, used in `module-03-recording/lessons/04-reading-widening-the-flow.html` (the Wk 7 lecture reading). Inés provided them: third-party product photos, manufacturer cross-sections, and pinout diagrams.

| Filename | Shows |
|---|---|
| `xlr-pinout.jpg` | XLR plug with its three conductors traced (two signal, one ground) |
| `ts-pinout.jpg` | Quarter-inch TS plug: tip for signal, sleeve for ground (unbalanced, instrument level) |
| `trs-pinout.jpg` | Quarter-inch TRS plug: the ring is a third conductor (balanced line, or stereo) |
| `trs-stereo-pinout.jpg` | TRS with unbalanced stereo to headphones (left, right, common) |
| `rca-pinout.jpg` | Stereo RCA pair: red is right, white is left, outer sleeve is ground |
| `three-mic-types-comparison.jpg` | Dynamic, condenser, and ribbon transducer types side by side |
| `condenser-microphone-cross-section.webp` | Cutaway of a condenser capsule |
| `ribbon-microphone-cross-section.jpg` | Cutaway of a ribbon element |
| `typical-microphone-polar-patterns.png` | Polar-pattern reference (omni, cardioid, figure-8) |
| `radial-prodi-di-box.jpg` | A DI box (Radial ProDI) |
| `rme-quadmic-preamp.jpg` | A hardware preamp (RME QuadMic) |

A substitute is any equivalent product photo, cutaway, or pinout diagram of the same component. The captions describe the function, not a brand.

---

### Mon Wk 8 lecture and Wed Wk 8 lab · console images

The files are in `assets/images/module-03-week-08/`, used in `module-03-recording/lessons/06-reading-the-mixer.html` (the Wk 8 lecture reading) and `module-03-recording/lessons/07-handout-the-mixer-in-practice.html` (Lab 3). The annotated front-panel photos were sourced separately and keep their source labels. The rear-panel photos are credited to Toft Audio Designs / PMI Audio Group, and the top-down overview to Retro Gear Shop.

| Filename | Shows | Used in |
|---|---|---|
| `console-overview.jpg` | Top-down view of the studio's 16-channel Toft ATB | 06-reading-the-mixer |
| `input-strip-annotated.png` | One input strip, front panel, every control labeled (aux masters, EQ bands, monitor section, fader) | 06-reading-the-mixer |
| `group-master-annotated.png` | The group/master section: eight submaster strips and the master strip (sections 4 and 5) | 06-reading-the-mixer |
| `rear-input-section.png` | Rear input jacks per channel: LINE, MON, INSERT, DIR. O/P, XLR | 06-reading-the-mixer |
| `rear-output-section.png` | Rear output section: subgroup outs, monitor returns, effects returns, aux masters, master out | 06-reading-the-mixer |
| `analog-stage-box-with-snake.jpg` | A stage box with a multicore snake, for the live-sound input scenario | 07-handout-the-mixer-in-practice |

The annotated strip photos are specific to the Toft ATB; a re-capture is re-annotated against the same console. The overview and stage-box photos can be replaced with any equivalent console or stage-box image.

---

### Mon Wk 9 studio visit · studio gear images

The files are in `assets/images/module-03-week-09/`, used in `module-03-recording/lessons/08-handout-studio.html` (Lab 4). They're manufacturer product photos of the MB2508 gear. The handout has no photos of the Furman HDS-6 hub or the HR-6 stations. The AudioBox photo in handout 08 is `module-03-week-06/presonus-audiobox-usb96-front.png`.

| Filename | Shows |
|---|---|
| `focusrite-isa-828-mkii.png` | Focusrite ISA 828 MkII, first preamp in the control-room preamp rack |
| `focusrite-octopre-platinum.jpg` | Focusrite OctoPre Platinum, second preamp in the control-room preamp rack |
| `hosa-pdr-369-mic-panel.jpg` | Hosa 16-jack mic input panel (one per preamp; jacks 9-16 unused) |
| `ssl-xlogic-g-compressor.jpg` | SSL XLogic G Series bus compressor |
| `avid-hdx-io.webp` | Avid HDX I/O, the interface between the console and Pro Tools |
| `db25-to-trs-fan-cable.webp` | DB25-to-8×TRS fan cable |
| `db25-to-xlr-fan-cable.webp` | DB25-to-8×XLR fan cable |

A substitute is any manufacturer product photo of the same unit.

---

## Module 04 · the DAW

### Mon Wk 11 listening · sampling-lineage photos

The files are in `assets/images/module-04-week-11/`, used in `module-04-the-daw/listening/historical.html` (the Module 4 historical listening). Inés provided them, with credits resolved.

| Filename | Shows |
|---|---|
| `flash-turntables.jpg` | Grandmaster Flash at two turntables with a mixer between them and two copies of the same record |
| `mpc60.jpg` | An Akai MPC60: sixteen pads, each holding a sample played by hand |

A substitute is any equivalent photo of a two-turntable DJ setup or an MPC-family sampler. The captions describe the function, not a specific image.

Module 4's lessons have no Ableton screenshots; they link the Live 11 manual. The listening's lineage timeline is an inline SVG in the HTML.
