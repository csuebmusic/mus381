# Asset recipes

Per-asset specifications: what each shared asset is, what it sounds like or looks like, how to recreate or substitute it. Internal build-time information.

> **Scope:** internal. The TA does not need any of this during the semester. The TA only needs to know an asset exists at its expected path. If something is missing, escalate to Inés; recipes here are for whoever rebuilds or substitutes the asset, which means Inés or a future maintainer of the course infrastructure.

The pattern: each module's section lists the prep-time assets needed for that module's lessons. For each asset: the path where it lives, what it is, and the recipe (length, format, what it sounds like / shows, pedagogical fit, substitution notes).

This file complements the build-script docs in [`../build/README.md`](../build/README.md). Build scripts cover assets that are programmatically generated (audio demos for digital-audio readings, diagrams that need scripted layout). This file covers assets that are produced by hand: recorded audio, photographed gear, captured screenshots, anything where the recipe is human-readable rather than scripted.

---

## Module 02 — Audio editing & mixing

### Wed Wk 2 lab handout · `orientation-sample.wav`

**Path on NAS:** `shared/module-02/orientation/orientation-sample.wav`

**Used in:** Lab 1 (`module-02-audio-editing-mixing/lessons/03-handout-audacity-orientation.html`)

**What it is:** a stereo bell-like resonance or sustained ringing texture, ~16 seconds, that gradually decays to silence across its full length.

**Format:** WAV, 48 kHz, 24-bit, stereo.

**Pedagogical fit:** the audible envelope shape (slow decay across the full clip) is what makes the lab work. Students cut into the decay around the 7-second mark and apply a fade to what remains; the visible taper across both stereo channels makes the editing moves easy to see on the waveform, and the audible fade-then-silence is what tells them the edit succeeded.

**Substitution:** Inés has the canonical file. If a substitute is ever needed: any stereo sustained sound with an audible decay (~10–18 s) works. Candidates: a long bowed note that fades, a struck rim recorded in stereo, a sampler-generated bell-like timbre. Avoid sounds with a hard ending (the lab's Step 5 depends on the decay being there for the fade to land on).

---

### Wed Wk 2 lab handout · Audacity screenshots

**Folder:** `assets/images/module-02-week-02/`

**Used in:** Lab 1 (`module-02-audio-editing-mixing/lessons/03-handout-audacity-orientation.html`)

**Status:** `audacity-settings.png` re-captured June 2026 (shows 48000 Hz / 24-bit). `audacity-export.png` still needs a re-capture at 48000 Hz / Signed 24-bit PCM, with Channels Stereo and File Name `lastname-orientation.wav`, to match the lab's export step (the orientation sample is stereo); the current file still shows the old 44100 Hz / 16-bit.

| Filename | Content |
|---|---|
| `audacity-settings.png` | Preferences → Audio Settings: Quality section showing Project Sample Rate 48000 Hz, Default Sample Rate 48000 Hz, Default Sample Format 24-bit |
| `audacity-interface-empty.png` | Empty Audacity main window with eight numbered orange markers placed directly on the regions identified in Step 3's annotation key (menu bar, transport, tools, level meters, Audio Setup, ruler, track area, selection toolbar) |
| `audacity-imported.png` | Main window with `orientation-sample.wav` imported as a stereo track, showing the ringing-decay waveform across both channels |
| `audacity-selection.png` | Same window with a region selected from roughly 7s to the end of the file (visible blue highlighted region in the waveform and timeline) |
| `audacity-fade-out.png` | Same window after the cut + fade-out: file now ends around 7.5s, last ~2.5s shows the visible fade taper |
| `audacity-export-prompt.png` | The "How would you like to export?" interstitial dialog with two options (Share to audio.com / On your computer) and the "Don't show again" checkbox |
| `audacity-export.png` | Export Audio dialog: filename `thiebaut-orientation.wav`, format WAV (Microsoft), Stereo, 48000 Hz, Signed 24-bit PCM, Entire Project |

**About the annotations on `audacity-interface-empty.png`:** the eight numbered markers are baked into the PNG itself (orange filled circles with white numbers, placed directly on the regions they identify). The handout's annotation key below the figure provides the legend. If the screenshot is ever re-captured, the new version will need fresh annotations drawn on; the numbering should match the order in the handout's Step 3 key.

Note that the empty Audacity window does not display the project sample rate anywhere visible. In Audacity 3.6 the project rate lives inside the Audio Setup dropdown, not in the main window's status bar. The annotation key reflects this; marker 5 (Audio Setup) describes the dropdown as the home for host, device, channel, and project-rate settings.

---

## Module 03 — Recording, sample prep & library building

### Wed Wk 6 lab handout · Audacity screenshots

**Folder:** `assets/images/module-03-week-06/`

**Used in:** Lab 1 (`module-03-recording/lessons/02-handout-recording-into-audacity.html`)

**Status:** captured (Inés's Mac, May 2026). If re-capture is needed, the table below documents what each screenshot shows.

| Filename | Content |
|---|---|
| `audacity-five-clips.png` | One mono track holding five clips in sequence: flat noise-profile clip first, then the four paper-sound clips of varying duration and amplitude |
| `audacity-noise-reduction-profile.png` | The Noise Reduction dialog in its Step 1 state, with the Get Noise Profile button at the top |
| `audacity-noise-reduction-apply.png` | The Noise Reduction dialog in its Step 2 state, with three sliders set to defaults (12 / 6.00 / 3) and OK at the bottom |

---

### Mon Wk 7 lecture · Cable and microphone images

**Folder:** `assets/images/module-03-week-07/`

**Used in:** `module-03-recording/lessons/04-reading-widening-the-flow.html` (the Wk 7 lecture reading)

**Status:** provided by Inés (third-party product photos, manufacturer cross-sections, and pinout diagrams). Markers, where present, stay in the source style; only the `.annotation-key` / figcaption beneath is in the course voice (per `visual-conventions.md`).

| Filename | Shows |
|---|---|
| `xlr-pinout.jpg` | XLR plug with its three conductors traced (two signal, one ground); the balanced-cable illustration |
| `ts-pinout.jpg` | Quarter-inch TS plug: tip carries signal, sleeve carries ground (unbalanced, instrument level) |
| `trs-pinout.jpg` | Quarter-inch TRS plug: the extra ring adds a third conductor (balanced line, or stereo) |
| `trs-stereo-pinout.jpg` | TRS carrying unbalanced stereo to headphones (left, right, common) |
| `rca-pinout.jpg` | Stereo RCA pair: red = right, white = left, outer sleeve = ground |
| `three-mic-types-comparison.jpg` | Side-by-side of dynamic, condenser, and ribbon transducer types |
| `condenser-microphone-cross-section.webp` | Cutaway of a condenser capsule |
| `ribbon-microphone-cross-section.jpg` | Cutaway of a ribbon element |
| `typical-microphone-polar-patterns.png` | Polar-pattern reference (omni, cardioid, figure-8) |
| `radial-prodi-di-box.jpg` | A DI box (Radial ProDI), the instrument-to-mic-level modifier |
| `rme-quadmic-preamp.jpg` | A hardware preamp (RME QuadMic), the mic-to-line-level modifier |

**Substitution:** any equivalent product photo, cutaway, or pinout diagram for the same component works; the captions describe the function, not a specific brand.

---

### Mon Wk 8 lecture + Wed Wk 8 lab · Console images

**Folder:** `assets/images/module-03-week-08/`

**Used in:** `module-03-recording/lessons/06-reading-the-mixer.html` (Wk 8 lecture reading) and `module-03-recording/lessons/07-handout-the-mixer-in-practice.html` (Lab 3)

**Status:** provided. The annotated front-panel photos were sourced separately; the rear-panel photos are credited to Toft Audio Designs / PMI Audio Group; the top-down overview is credited to Retro Gear Shop. The two annotated photos carry baked-in labels in their source style.

| Filename | Shows | Used in |
|---|---|---|
| `console-overview.jpg` | Top-down view of the studio's 16-channel Toft ATB; chapter-opening overview | 06-reading-the-mixer |
| `input-strip-annotated.png` | A single input strip, front panel, every control labeled (aux masters, EQ bands, monitor section, fader) | 06-reading-the-mixer |
| `group-master-annotated.png` | The group/master section: eight submaster strips plus the master strip (used in sections 4 and 5) | 06-reading-the-mixer |
| `rear-input-section.png` | Rear input jacks per channel: LINE / MON / INSERT / DIR. O/P + XLR | 06-reading-the-mixer |
| `rear-output-section.png` | Rear output section: subgroup outs, monitor returns, effects returns, aux masters, master out | 06-reading-the-mixer |
| `analog-stage-box-with-snake.jpg` | A stage box with a multicore snake; the live-sound input scenario | 07-handout-the-mixer-in-practice |

**Substitution:** the annotated strip photos are specific to the Toft ATB and would need re-annotating against the same console if re-captured; the overview and stage-box photos can be swapped for any equivalent console / stage-box image.

---

### Mon Wk 9 studio visit · Studio gear images

**Folder:** `assets/images/module-03-week-09/`

**Used in:** `module-03-recording/lessons/08-handout-studio.html` (Lab 4, the self-guided studio walkthrough)

**Status:** provided (manufacturer product photos of the MB2508 side-rack gear).

| Filename | Shows |
|---|---|
| `focusrite-isa-828-mkii.png` | Focusrite ISA 828 MkII, first preamp in the live-room rack |
| `focusrite-octopre-platinum.jpg` | Focusrite OctoPre Platinum, second preamp in the live-room rack |
| `hosa-pdr-369-mic-panel.jpg` | Hosa 16-jack mic input panel (one per preamp; jacks 9-16 unused) |
| `ssl-xlogic-g-compressor.jpg` | SSL XLogic G Series bus compressor |
| `behringer-xenyx-qx1204usb.webp` | Behringer Xenyx QX1204USB, the desk mixer doing three jobs at once |
| `rane-mh4-headphone-console.jpg` | Rane MH4 headphone amp (one cue mix, four players) |
| `avid-hdx-io.webp` | Avid HDX I/O, the bridge between the analog console and Pro Tools |
| `db25-to-trs-fan-cable.webp` | DB25-to-8×TRS fan cable |
| `db25-to-xlr-fan-cable.webp` | DB25-to-8×XLR fan cable |

**Substitution:** any equivalent manufacturer product photo for the same unit works.
