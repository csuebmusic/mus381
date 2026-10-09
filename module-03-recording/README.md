# Module 03 · recording, sample prep & library building

Wks 6 to 9 (Sep 21 to Oct 14) · 8 sessions of 100 minutes

---

## module purpose

In Module 2 students worked with sound that was handed to them. In Module 3 they make their own. By the end of the four weeks they can plug in a microphone, capture a clean recording, prepare the file for use, and organize it into a usable library.

The deliverable is the library: the curated, organized collection of their own sounds that students draw from in Module 4. The midterm has two parts, the library and a terminology exam covering Modules 1 through 3.

The module runs in this order: the basic recording chain from mic to computer → recording into Audacity → moving phone recordings into the library → other signal levels, cables, mics, and signal modifiers → how a mixer routes many signals at once (the Toft ATB in detail) → the live-sound scenario in lab → a walk around the MB2508 studio, with the studio-recording walkthrough (handout 08) for students to work through on their own time → the library submission and exam.

Two ideas apply in every session.

1. Signal flow is a sequence of decisions. Sound becomes signal, then a recording, then a sample, then part of a library. At every stage something is chosen: which mic, which signal level, which cable, which input, which interface, which prep step, which destination folder. Students should be able to look at any setup (a stage, a studio, a phone propped against a doorframe) and name the flow from acoustic source to stored file. The basic recording chain is the flow at every lab station; Session 3 (other signal levels, cables, mics, DI boxes, and preamps) and Sessions 5 to 7 (the console, the live-sound scenario, and the studio visit) widen it.
2. A recording and a sample are different things. A recording is what comes out of the mic; a sample is what goes into the library. Turning one into the other happens at two stages. While recording, students leave headroom (peaks around -12 to -6 dBFS). After recording, they denoise, trim with short fades, normalize, name, and file.

By the end of Wk 9, each student has a library of their own recordings, prepped to one standard and organized in a documented folder structure, ready to load into Ableton Live 11 in Module 4.

---

## learning outcomes

By the end of this module, students should be able to:

1. Describe signal flow from acoustic source to stored file, naming the components at each stage
2. Name the five stages of the basic recording chain (dynamic mic, XLR cable, audio interface, USB cable, computer) and the mic-level signal on the XLR cable
3. Distinguish dynamic, condenser, and (briefly) ribbon microphones, and know where each is used
4. Distinguish mic-level, instrument-level, and line-level signals, and match each to the correct input
5. Identify XLR, TS, TRS, and RCA cables and know what each one carries
6. Set up a recording session in Audacity from cold: select the input, set gain, monitor, record with headroom
7. Prepare a recorded sample for use: denoise, trim with short fades, normalize to -1 dBFS
8. Organize a sample library with a documented folder structure, consistent naming, and a README
9. Record audio on a phone (iPhone or Android) at 48 kHz, 24-bit, ready to add to the library
10. Describe how a mixer routes many signals at once, and what aux sends and buses do in live sound and in studio recording
11. Pass a cumulative terminology exam covering vocabulary from Modules 1 through 3

---

## concepts introduced

- Signal flow is the path sound takes from acoustic source to stored file. Every recording setup has one: a phone recording has a shorter flow, and a live show with a mixer has a wider one. Students should be able to point at any setup and trace it.
- The basic recording chain is dynamic mic → XLR cable → audio interface → USB cable → computer: three devices connected by two cables, with a mic-level signal on the XLR. It's the flow at every lab station.
- There are three transducer types. Dynamic mics (moving coil; SM57 and SM58 at the lab stations) are rugged and need no power. Condenser mics are more sensitive, capture more detail, and need phantom power. Ribbon mics are covered in the reading and not used in the lab.
- Polar patterns are taught at a beginner level. The lab mics are cardioid. Omni and figure-8 are the other two common patterns; super-cardioid, hyper-cardioid, and shotgun are introduced as variants.
- There are three signal levels: mic level (around 1 mV, needs a preamp), instrument level (around 100 mV, from a guitar or bass pickup, high impedance, needs a Hi-Z input), and line level (around 1 V, from a synth, a mixer, or an interface output). Line level comes as consumer (-10 dBV) and professional (+4 dBu). Each level needs its own kind of input.
- Four cable types cover most audio work. XLR is balanced and three-conductor, for mic level and balanced line level. TS is unbalanced and two-conductor, for instrument level (the guitar cable). TRS is three-conductor and carries either balanced line level or unbalanced stereo, depending on the gear at each end. RCA is unbalanced, one channel per plug, for consumer line level.
- A signal modifier converts a signal from one level to another. The DI box takes unbalanced instrument level to balanced mic level. The hardware preamp takes mic level to line level, often with a sonic character of its own.
- Recording with headroom means peaks around -12 to -6 dBFS while tracking. It leaves room for an unexpected loud moment and leaves the final level to be set in editing.
- The sample prep pipeline has three steps, applied to every raw recording before it's added to the library: denoise using a noise profile captured from silence, trim to the sound with a short fade at each end, and peak-normalize to -1 dBFS.
- Library organization means category folders, the [category]-[descriptor]-[variant].wav naming convention, and a README.txt at the root of the library.
- The mixer is where many signals combine and go out to different destinations: channel strips, faders, aux sends, subgroups, the master section. Students need to know what the parts are and what they do; they don't operate one for the exam.
- Aux sends and buses work the same way in every context, and what's connected to them changes. In live sound, aux sends feed the stage monitors so performers can hear themselves. In MB2508, Aux 1 and Aux 2 feed one shared stereo headphone cue to the live room.

---

## deliverable: the midterm

Two parts, both on Wed Oct 14 (Wk 9).

### sample library (Project 2)

A folder of the student's own recorded sounds, prepped through the pipeline and organized into a documented structure, submitted on the class server.

Prompt and rubric: [Project 2: sample library](https://csuebmusic.github.io/mus381/module-03-recording/projects/project-02-sample-library.html)

The library has at least 20 prepped sounds (20 to 25 is the target). Every sound is the student's own recording, made in the lab or on their phone; downloaded or borrowed sounds aren't allowed. Every sample is a mono WAV, 48 kHz, 24-bit, normalized to -1 dBFS, and named [category]-[descriptor]-[variant].wav (lowercase, hyphens, no spaces). Samples are sorted into category folders, with a README.txt the student writes at the root and the Audacity project in audacity-projects/. The rubric has five dimensions at 20 points each: recording quality, sample prep, organization, naming, and range and curation.

The library builds up across the module:

- Wed Wk 6: students record their first four sounds in Lab 1 (paper crumble and paper rip, each at two speeds), prep them, and set up the library folder and README.
- From Wk 6 on: students record on their phones outside class with the phone reference card.
- Wed Wk 7: Lab 2 moves phone recordings into Audacity and through the pipeline, with worktime for recording and prepping more.
- Wk 8: the Monday mixer lecture and the Wednesday live-sound lab. Students keep adding to the library between sessions; Lab 3 ends with a five-minute library check.
- Mon Wk 9: the MB2508 studio visit. Handout 08 goes home, and so does the midterm review packet (handout 09).
- Wed Wk 9: the library is due at the start of class, before the terminology exam.

### terminology exam

A cumulative in-class exam on Modules 1 through 3, closed-book, no devices, 50 points in four parts (define, identify, trace a signal flow, short answer). It runs in the second part of the Wed Wk 9 session, after every library is submitted and verified. The exam tests only what the midterm review packet covers.

Exam and answer key: [`exams/midterm-exam.md`](../exams/midterm-exam.md) (TA-facing only)

---

## listening assignments

### historical listening

The historical listening has two parts on one idea: every choice that turns sound into a record is a compositional choice.

Part one, recording as composition, is three field recordings on a spectrum of how present the recordist is, from the recordist vanishing into a place to the recordist narrating the listening: Francisco López, *La Selva* (1998); Chris Watson, "El Divisadero" from *El Tren Fantasma* (2011); Hildegard Westerkamp, *Kits Beach Soundwalk* (1989).

Part two, mixing as composition, is three records on a spectrum from the mix trying to disappear to the mix being the music: the Bill Evans Trio, "Gloria's Step" (1961); the Ronettes, "Be My Baby" (1963, a Phil Spector production); Augustus Pablo and King Tubby, "King Tubby Meets Rockers Uptown" (1976). The dub track's echoes are aux sends feeding an echo unit, the routing from the Toft reading.

Students answer five questions in one writeup, lastname-listening-03 (.docx or PDF, about 350 to 450 words), uploaded to Canvas. For López, a focused ten minutes is enough.

Assignment page: [listening: recording and mixing as composition](https://csuebmusic.github.io/mus381/module-03-recording/listening/historical.html)

Due Mon Oct 12 (Wk 9), before class.

### peer listening

After the midterm, students browse classmates' libraries in /public/mus-381-fall-2026/project-02-libraries/ on the class server (reachable from inside the lab only) and write 50 to 80 words on each of three or four libraries: whose library it is, one specific thing they noticed, and one file they'd borrow and how they'd use it in a piece. The response is lastname-peer-listening-03 (.docx or PDF, about 200 to 320 words), uploaded to Canvas. The libraries are discussed in class on Mon Wk 10, the first day of Module 4.

Assignment page: [peer listening: sample libraries](https://csuebmusic.github.io/mus381/module-03-recording/listening/peer-midterm.html)

Due Mon Oct 19 (Wk 10), before class.

---

## live pages

- [a simple recording chain](https://csuebmusic.github.io/mus381/module-03-recording/lessons/01-reading-recording-chain.html) (`lessons/01-reading-recording-chain.html`, Lecture 1)
- [recording into Audacity](https://csuebmusic.github.io/mus381/module-03-recording/lessons/02-handout-recording-into-audacity.html) (`lessons/02-handout-recording-into-audacity.html`, Lab 1)
- [recording on your phone](https://csuebmusic.github.io/mus381/module-03-recording/lessons/03-handout-recording-on-phone.html) (`lessons/03-handout-recording-on-phone.html`, reference card)
- [widening the flow](https://csuebmusic.github.io/mus381/module-03-recording/lessons/04-reading-widening-the-flow.html) (`lessons/04-reading-widening-the-flow.html`, Lecture 2)
- [phone recordings into Audacity](https://csuebmusic.github.io/mus381/module-03-recording/lessons/05-handout-phone-to-audacity.html) (`lessons/05-handout-phone-to-audacity.html`, Lab 2)
- [the mixer](https://csuebmusic.github.io/mus381/module-03-recording/lessons/06-reading-the-mixer.html) (`lessons/06-reading-the-mixer.html`, Lecture 3)
- [the mixer in practice · live sound](https://csuebmusic.github.io/mus381/module-03-recording/lessons/07-handout-the-mixer-in-practice.html) (`lessons/07-handout-the-mixer-in-practice.html`, Lab 3)
- [the mixer in practice · studio recording](https://csuebmusic.github.io/mus381/module-03-recording/lessons/08-handout-studio.html) (`lessons/08-handout-studio.html`, Lab 4)
- [midterm review](https://csuebmusic.github.io/mus381/module-03-recording/lessons/09-handout-midterm-review.html) (`lessons/09-handout-midterm-review.html`)
- [listening: recording and mixing as composition](https://csuebmusic.github.io/mus381/module-03-recording/listening/historical.html) (`listening/historical.html`)
- [peer listening: sample libraries](https://csuebmusic.github.io/mus381/module-03-recording/listening/peer-midterm.html) (`listening/peer-midterm.html`)
- [Project 2: sample library](https://csuebmusic.github.io/mus381/module-03-recording/projects/project-02-sample-library.html) (`projects/project-02-sample-library.html`)

---

## session overview

| Wk | Day | Focus |
|---|---|---|
| 6 | Mon Sep 21 | Session 1 · Lecture 1: a simple recording chain. Signal flow; the five-stage chain (dynamic mic, XLR cable, audio interface, USB cable, computer); reading a mic's spec sheet; balanced cables; the two lab interfaces. |
| 6 | Wed Sep 23 | Session 2 · Lab 1: recording into Audacity. Library folder set up, Audacity configured for mono recording, gain and monitor mix, noise-profile clip, four paper recordings (crumble slow and fast, rip slow and fast), the denoise → trim → normalize pipeline, export, library README, upload. Students pick up the phone reference card on the way out. |
| 7 | Mon Sep 28 | Session 3 · Lecture 2: widening the flow. Mic, instrument, and line level; XLR, TS, TRS, and RCA; condenser and ribbon mics; polar patterns; DI boxes and hardware preamps. |
| 7 | Wed Sep 30 | Session 4 · Lab 2: phone recordings into Audacity. LocalSend transfer, import, sample-rate check and resampling, the pipeline with a noise profile taken from the phone recording, export to a new category folder, worktime on the library. |
| 8 | Mon Oct 5 | Session 5 · Lecture 3: the mixer. The Toft ATB top to bottom: channel strip, in-line architecture, submasters, master section. |
| 8 | Wed Oct 7 | Session 6 · Lab 3: the mixer in practice · live sound. The Sound Below through one live show (FOH mix and five stage-monitor mixes on the same desk), then the Generate a band widget, where students route a random lineup themselves. |
| 9 | Mon Oct 12 | Session 7 · Lab 4: studio visit to MB2508. A walk around the live room, the control room, the Toft, the preamp rack, and the side rack. Handout 08 (the self-guided studio-recording walkthrough) and handout 09 (midterm review) go home. Module 3 listening due. |
| 9 | Wed Oct 14 | Session 8 · Midterm: library submission, then the terminology exam. |

Session 2 has block-by-block notes. The other sessions have a roadmap and notes on their reading or handout.

---

## pre-module preparation (Inés and the TA)

- Put paper at every station for Wed Wk 6. See paper supplies under Session 2.
- Inventory the recording gear in the lab's gear storage: one set per workstation of audio interface, headphones, dynamic mic, mic stand, and XLR cable. Check that nothing is missing before Wk 6.
- Confirm LocalSend is installed on every lab Mac before Wed Wk 7. Test it once in MB2525: a phone on campus Wi-Fi sees a lab Mac under Nearby devices, and a WAV sent from the phone shows up in that Mac's Downloads folder. If the test fails, tell Inés before Wednesday.
- Post a Canvas announcement by Mon Wk 7 telling students to install LocalSend on their phones before Wed Wk 7, with the App Store and Google Play links from Step 1 of [phone recordings into Audacity](https://csuebmusic.github.io/mus381/module-03-recording/lessons/05-handout-phone-to-audacity.html). The phone reference card has the same links.
- Gather lecture demo materials: physical XLR, TS, TRS, and RCA cables (Mon Wk 6 and Mon Wk 7), and a condenser mic and a DI box to hold up in the Mon Wk 7 lecture.
- Book MB2508 for Mon Wk 9 a few weeks ahead. The studio visit is a walk around the room, and the console doesn't have to be powered. If you plan to power it on to show signal moving, check the Toft the morning of: master fader down, MONITOR LEVEL at zero, and one signal path tested.
- Print handout 09 (midterm review) before Mon Wk 9, plus a few extra copies for students who lose theirs before Wednesday.

---

## module-wide concerns

### recurring confusions across the module

- Levels are still confusing. The interface gain knob, the interface headphone knob, the monitor mix (PreSonus Mixer knob or Behringer Direct Monitor), the in-line slider on the headphone cable, and Audacity's input meter are five different things. Only the gain knob changes the recording level.
- "My recording is too quiet" almost always means the gain knob is too low. If the recording looks fine on the meter but the headphones are quiet, check the headphone knob, then the in-line slider, then the monitor mix.
- "My recording is too loud or clipping" means the gain knob is too high. Reinforce the -12 to -6 dBFS target.
- "I can't hear myself while recording" means the monitor mix is turned toward Playback (PreSonus) or Direct Monitor isn't pressed in (Behringer).
- "My file disappeared" is the Module 2 problem again. Reinforce download at the start and upload at the end, every session: the library is now weeks of the student's own recordings.

### gear setup baseline (every Wednesday)

Same as Module 2. In Module 3 students also take the mic, stand, and XLR cable from gear storage. Each station's mic is a Shure SM57 or SM58; both are cardioid dynamics, and the handouts call either one "the dynamic mic."

### pacing across the module

Wed Wk 6 is tight on time. Every student needs to leave with four samples recorded, prepped through the full pipeline at least once, exported, and in a named folder. Plan the session so the full pipeline gets done, along with the recordings.

Wed Wk 7 has the module's one long unstructured stretch: the worktime half, after the phone transfers. Students who've been recording on their own time spend it on prep and organization; students who haven't spend it recording. Watch for a student with nothing to work on. Lab 2's "If you arrive without a recording" callout has them record one sound at the station before starting Step 1.

### when to escalate to Inés

Same as Module 2.

---

## Session 1 · Mon Wk 6: a simple recording chain

100 min · lecture · MB2525

### roadmap

The lecture names the umbrella concept (signal flow, the path from acoustic source to stored file) and then covers the basic recording chain stage by stage: dynamic mic → XLR cable → audio interface → USB cable → computer, three devices connected by two cables. Students should leave able to draw the five-stage chain from memory and say what kind of signal is on each cable.

The reading has six sections:

1. Signal flow, with the five-stage chain diagram.
2. The dynamic microphone: how it works (diaphragm, voice coil, magnet), then reading a spec sheet. The SM57 and SM58 (the two mics at the lab stations) share the cardioid polar pattern and differ in frequency response; the section covers presence peak and proximity effect.
3. The mic-level signal: why it needs a preamp, and what gain controls. A callout covers the two meanings of "level."
4. The XLR cable: balanced wiring, with a pause section on why in-phase signals double and out-of-phase signals cancel.
5. The audio interface: preamp, ADC, USB, and DAC, with the PreSonus AudioBox USB 96 and the Behringer U-Phoria UM2 compared control by control (inputs, gain, clip indicator, phantom power, direct monitoring and the monitor mix, headphone output, back panels).
6. Why audio interfaces vary in price: channel count, preamps, conversion, connection and latency, onboard DSP, digital I/O.

### reading

[a simple recording chain](https://csuebmusic.github.io/mus381/module-03-recording/lessons/01-reading-recording-chain.html)

### connection to Day 1

Students plugged a dynamic mic into input 1 of an interface on Day 1 and recorded in QuickTime. Point back to that setup when you name the stages.

---

## Session 2 · Wed Wk 6: recording into Audacity (Lab 1)

100 min · lab · MB2525

### roadmap

Students run the full record-and-prep pipeline once, end to end, with paper as the source material.

They record four sounds as separate clips on one mono track in one Audacity project:

1. Paper crumble, slow (8 to 10 seconds)
2. Paper crumble, fast (2 to 3 seconds)
3. Paper rip, slow (6 to 8 seconds)
4. Paper rip, fast (one quick motion)

The project opens with a dedicated noise-profile clip: 10 seconds of room tone, recorded once before any of the four sounds. The denoise step uses the profile captured from it. Each sound clip has a one-second silence buffer at the start and end; the buffer is for clean trimming, and the noise profile comes only from the room-tone clip. Reinforce the noise-profile-first pattern before recording starts.

Students build the library folder first, before opening Audacity, and save the Audacity project inside it after the test recording. The folder holds every sample they record this semester.

The prep pipeline runs on each of the four sounds after the noise profile has been captured once from the room-tone clip:

1. Denoise. Double-click the clip to select it, then Effect → Noise Removal and Repair → Noise Reduction…, sliders at 6, 6.00, 6 (a gentle starting point), OK.
2. Trim and fade. Select just the sound with the I-beam, then Edit → Remove Special → Trim Audio (Cmd + T). Zoom in (Cmd + 1), select about 50 ms at the new start and apply Effect → Fading → Fade In; zoom out (Cmd + F) and repeat at the end with Fade Out.
3. Normalize. Double-click the clip, Effect → Volume and Compression → Normalize…, peak amplitude -1.0 dB, Remove DC offset checked.

Each prepped sample is exported as its own mono WAV, 48 kHz, 24-bit: double-click the clip, File → Export Audio…, Format WAV (Microsoft), Channels Mono, Sample Rate 48000 Hz, Encoding Signed 24-bit PCM, Export Range Current selection. Files go into sample-library/paper/.

The naming convention for samples is the one on the lab handout:

```
[category]-[descriptor]-[variant].wav
```

Examples: `paper-crumble-slow.wav`, `paper-rip-fast.wav`. Lowercase, hyphens between words, no spaces or special characters.

The library folder structure:

```
~/Documents/netid/sample-library/
  paper/
    paper-crumble-slow.wav
    paper-crumble-fast.wav
    paper-rip-slow.wav
    paper-rip-fast.wav
  audacity-projects/
    sample-library.aup3
  README.txt            <- the student writes it: what's in the library, how it's organized
```

The library is at `~/Documents/netid/sample-library/` on the lab Mac and at `sample-library/` inside the student's own folder on the server. Students write the README in TextEdit as plain text, pasting in the template from Step 10 of the handout and filling in the bracketed parts.

At the end of the session, students upload the whole sample-library/ folder to the server as part of the end-of-session routine.

### handout

[recording into Audacity](https://csuebmusic.github.io/mus381/module-03-recording/lessons/02-handout-recording-into-audacity.html) (Lab 1)

Ten numbered steps from cold start to upload:

1. Set up the sample library folder (sample-library/ with paper/ and audacity-projects/).
2. Configure Audacity: Preferences → Audio Settings (Project Sample Rate 48000 Hz, Default Sample Format 24-bit PCM), then the Audio Setup button (Recording Device, Recording Channels 1 (Mono), Playback Device), then Tracks → Add New → Mono Track.
3. Set gain on the interface for peaks of -12 to -6 dBFS, with Audacity's meter live through Enable Silent Monitoring.
4. Set the monitor mix.
5. Do a test recording, delete the test clip, and save the project as sample-library.aup3 in audacity-projects/.
6. Capture the 10-second noise-profile clip.
7. Record the four paper sounds.
8. Run the prep pipeline on each clip.
9. Export each sample as a WAV.
10. Write the library README and upload to the server.

The handout has an inline SVG of the headroom target band, three Audacity screenshots (the five clips on one track and the two stages of the Noise Reduction dialog), and three short screen recordings (the Audio Setup dropdown, turning on silent monitoring, and a test recording). Callouts cover the gear to take from storage, the UM2's 16-bit capture into a 24-bit project, mono, silent monitoring, not normalizing to fix a quiet recording, saving the project, one noise profile for all four sounds, fades, what normalize does, and keeping the README current.

### phone-recording reference card

[recording on your phone](https://csuebmusic.github.io/mus381/module-03-recording/lessons/03-handout-recording-on-phone.html) (`lessons/03-handout-recording-on-phone.html`)

A separate reference card for recording outside class, stacked at the front of the room; Lab 1 tells students to pick one up before they leave. It recommends one field-recording app per platform: Lossless Field Recorder by edson engineering on iPhone (free, iOS 15 or later) and Field Recorder by Pfitzinger Voice Design on Android ($5.95 on Google Play). Both record 48 kHz, 24-bit WAV and give direct control over the recording, with no automatic processing. The card also has students install LocalSend on their phones for the Lab 2 transfer.

The card covers setup on each platform. On iPhone that's mic mode (bottom, front, back), frequency mode (48 kHz), and pickup pattern (start with omni and leave stereo off: library samples are mono). On Android it's the In:Raw input configuration, then Settings → Rec at 48 kHz with 24 bit file write, saved as a preset. It then covers the take (airplane mode, set the phone down, distance, the level meter with the same -12 to -6 dBFS target, wind) and a starter list of things that record well. Students leave recordings in the app until Lab 2, which moves them into Audacity and through the pipeline. Students keep using the card for the rest of the semester.

### pre-class checklist

- Walk the room: gear setup baseline (module-wide concerns above).
- In the lab's gear storage, confirm every set is present and intact: audio interface, headphones, dynamic mic, mic stand, XLR cable. Students take these out following the Session Routines card.
- Put paper at every station (paper supplies, below).
- Confirm Audacity has Effect → Noise Removal and Repair → Noise Reduction… on three stations during the walk-through. It's standard in Audacity 3.x.
- Test-record on the instructor station: the meter goes live after you click it and choose Enable Silent Monitoring, the gain knob moves the meter, and the headphones play the live input with the monitor mix turned toward Inputs.
- Open the Lab 1 handout on the projector and in the browser at each student station.
- Stack the phone reference cards at the front of the room.

### block-by-block

| Block | Time | Handout steps | Focus |
|---|---|---|---|
| 1. Folder, setup, and gain | 25 min | Steps 1–3 | Library folder, Audacity configuration, gain to -12 to -6 dBFS |
| 2. Monitor and test | 10 min | Steps 4–5 | Hear yourself, confirm the chain end to end, save the project |
| 3. Noise profile and recording | 20 min | Steps 6–7 | Room-tone clip, four paper sounds |
| 4. Prep pipeline | 25 min | Step 8 | Noise profile once, then the pipeline four times |
| 5. Export and upload | 15 min | Steps 9–10 | Mono WAV export, README, end-of-session upload |
| 6. Wrap and phone card | 5 min | | Phone reference card, preview Mon Wk 7 |

The 100 minutes assume students arrive on time and finish the start-of-session routine before Block 1. Students take the mic, stand, and XLR cable from gear storage for the first time since Day 1, and the routine runs longer than usual: allow 8 to 10 minutes. Demo the mic-and-XLR setup on the instructor station as students arrive, alongside the handout's today's gear callout. Monday's five-stage chain diagram is the model: students should be able to point at their own setup and name each stage.

Block 1 · folder, setup, and gain (25 min, Steps 1–3). Step 1 takes about 5 minutes. Students build `~/Documents/netid/sample-library/` with `paper/` and `audacity-projects/` inside it, before opening Audacity. Walk the room and check the folder at every station before anyone moves on.

Then walk through Step 2 on the projector with students mirroring at their stations. In Preferences → Audio Settings they confirm Project Sample Rate 48000 Hz and Default Sample Format 24-bit PCM. Students haven't opened the Audio Setup button before; they saw it as marker 5 in the orientation lab's empty-project tour. Today they set Recording Device, Recording Channels, and Playback Device. The PreSonus shows up as AudioBox USB 96 and the Behringer UM2 as USB Audio CODEC. Recording Channels → 1 (Mono) is the setting students miss. A student who records to a stereo track with a mono input gets the mic on the left channel and silence on the right; it's audible only if you pan hard, and the file is wrong. Then the mono track: Tracks → Add New → Mono Track.

Step 3 (set gain) takes most of the block. Demo on the projector: click the recording level meter, choose Enable Silent Monitoring, speak into the mic, watch the peaks. Reinforce the target against the handout's diagram: peaks of the loudest sound students are about to make should reach -12 to -6 dBFS. Then students set gain with a test crumble or a quick test rip on a small piece of scrap paper, saving their four full sheets for the real takes.

The error to expect in this block: students set gain by speech rather than by the paper sound. Speech into a dynamic mic at 15 to 20 cm reads quieter than a close paper rip, and they set gain too high. Demo the test-crumble approach explicitly.

Block 2 · monitor and test (10 min, Steps 4–5). Most students already hear themselves from Block 1. Step 4 confirms and adjusts the monitor mix: on PreSonus stations, turn the Mixer knob about three-quarters toward Inputs; on Behringer stations, press Direct Monitor in. A student who hears an echo has Audacity's audible input monitoring on: Transport → Transport Options → uncheck Enable audible input monitoring. Step 5 is one test recording of a spoken phrase. After it, students delete the test clip (double-click it, press Delete) and keep the empty mono track for the noise-profile clip in Block 3. Then they save the project with File → Save Project As… as `sample-library.aup3` in `sample-library/audacity-projects/`, and save every few minutes with Cmd + S from then on.

This block goes quickly.

Block 3 · noise profile and recording (20 min, Steps 6–7). Students skip or rush the noise-profile clip. Walk the room during the 10-second capture: every student still, hands off the mic, the cable, and the table, mouth closed. Movement or audible breathing contaminates the profile, and denoise in Block 4 then produces strange artifacts. Stop the clock if needed and have a student who moved redo it.

Then the four recordings. The handout says: hold the paper 15 to 20 cm from the mic, click Record, wait one full second of silence, make the sound, wait one full second more, click Stop. Watch for students who skip the silence and start the sound on Record. Without it they risk cutting off the start of the sound when they trim.

The four sounds are short (the slow crumble is about 8 to 10 seconds, the fast rip one motion). Most of the twenty minutes goes to four record, listen, keep-or-redo cycles. Encourage students to redo any take that didn't capture what they wanted (double-click the clip, Delete, record again).

By the end of Block 3, every student has five clips on one mono track: the noise-profile clip, then paper crumble slow, paper crumble fast, paper rip slow, paper rip fast. Have them save (Cmd + S) before moving on.

Block 4 · prep pipeline (25 min, Step 8). This step is procedure-dense and students rush it. Demo the full pipeline on the instructor station on one clip, start to finish, before students try it:

1. Capture the noise profile, once. Double-click the noise-profile clip → Effect → Noise Removal and Repair → Noise Reduction… → Get Noise Profile. The dialog closes. Audacity keeps the profile until it's replaced or the program closes.
2. Prep paper crumble slow (the second clip on the track). Double-click it, open Noise Reduction again, set 6, 6.00, 6, click OK. Select just the sound with the I-beam and press Cmd + T (Trim Audio). Zoom in with Cmd + 1 at the start, select about 50 ms, Effect → Fading → Fade In; zoom out with Cmd + F and repeat at the end with Fade Out. Double-click the trimmed clip, Effect → Volume and Compression → Normalize…, peak -1.0 dB, OK.

Students then repeat the pipeline for the other three sounds. By the end of the block: four clips, each denoised, trimmed, faded, and normalized to -1 dBFS.

Errors to expect in this block:

- Clicking Get Noise Profile on a sound clip instead of OK. The dialog closes without changing anything, and the student thinks denoise has been applied; the profile has been replaced with the sound clip. If a student opens Noise Reduction on a sound clip and clicks Get Noise Profile, step in.
- Selecting only part of a sound clip for denoise (just the loud middle, say). The unselected edges stay noisy. Double-clicking the clip selects the whole clip.
- Skipping the fades. The file clicks at the start or end. It's easy to miss on screen; remind the room when most students reach the trim.
- Trimming too tight and cutting off the natural decay of the sound. The handout says to select from where the sound starts to where it ends; let the ring or scrape decay into silence before the cut.

Block 5 · export and upload (15 min, Steps 9–10). Export first. Demo the first export on the instructor station: double-click the clip, File → Export Audio…, fill in the dialog, and point to Export Range → Current selection. Students leave Export Range at its default and get one file with every clip on the track, the noise-profile clip included. Walk the room during each student's first export and catch it there; the remaining three go right.

The first file is `sample-library/paper/paper-crumble-slow.wav`, and the other three follow the same pattern.

Then the README. Students open TextEdit and choose Format → Make Plain Text (Cmd + Shift + T) before pasting the template. A student who skips it saves an .rtf with styled text and smart quotes. Walk the room during this step.

Then the end-of-session upload. In FileZilla the left pane is on `~/Documents/netid/` and the right pane stays in the student's own folder; students drag `sample-library/` across, choosing Overwrite if source newer if asked. Watch which folder they drag: a student who drags the parent folder ends up with `netid/netid/sample-library/` on the server. Check a few uploads by opening `sample-library/paper/` in the student's server folder and counting four WAVs.

Block 6 · wrap and phone card (5 min). Students pick up a phone reference card on the way out. Say something like: "From this week on, you can add to your library on your own time with your phone. The card has the iPhone and Android setup. Next session covers other signal levels (instrument level, line level), condenser mics, DI boxes, and the cables that go with them."

Remind students to finish the end-of-session routine on the Session Routines card before leaving the station: disconnect and quit FileZilla, quit all apps, interface knobs back to zero, unplug everything (including the mic's XLR at both ends), return the gear (with the mic and stand) to gear storage, chair in.

### common confusions

- Recording device not set. The student clicks Record and no waveform appears. Audio Setup was skipped or the wrong device was chosen (the PreSonus is AudioBox USB 96, the UM2 is USB Audio CODEC). This shows up in Block 1; check Audio Setup → Recording Device on that station.
- Mono mic recorded to a stereo track. Recording Channels was left at 2 (Stereo). The mic is on the left channel and the right is silent; the waveform looks half-empty. Set Recording Channels to 1 (Mono), delete the stereo track, add a new mono track (Tracks → Add New → Mono Track), and record again.
- The meter shows nothing. The student is setting gain without silent monitoring on. Click the recording level meter and choose Enable Silent Monitoring; the menu item then reads Disable Silent Monitoring.
- Monitor mix turned toward Playback. The student can't hear the mic. On the PreSonus, turn the Mixer knob toward Inputs. On the Behringer, press Direct Monitor in. If the student hears the mic with an echo, Audacity's audible input monitoring is on; uncheck it in Transport → Transport Options.
- Noise-profile clip captured with movement. During the 10-second capture the student breathed audibly, shifted, or touched the cable. Denoise then subtracts things that aren't constant background and produces artifacts (a whispery, underwater sound). Record the noise-profile clip again and capture a new profile.
- Get Noise Profile and OK in the same dialog. Get Noise Profile captures the profile and closes the dialog with nothing audible changing, and students think it's broken. OK applies the reduction. Demo both on the projector and expect to repeat the distinction at individual stations.
- No silence buffer in a recording. The student started the sound on Record. Trimming then risks cutting off the start of the sound. Have them select from just inside the visible silence, leaving 10 to 20 ms before the waveform starts.
- Clicks at the trim points. The student skipped the 50 ms fades. Listen to one of their samples on headphones; if it clicks at the start or end, take them back to the fades.
- Export Range left at its default. One WAV with every clip in it instead of one sample. Catch it on the first export.
- README saved as .rtf. Format → Make Plain Text was skipped. Open the file in TextEdit, choose Format → Make Plain Text, and save over it, or delete it and start again from the template in the handout.
- An extra folder level on the server. The student dragged `netid/` instead of `sample-library/` and has `netid/netid/sample-library/`. Check by opening the upload destination; fix it by moving the inner folder up one level.

### pacing fallbacks

- Running long in Block 1 (gain). Students are probably stuck on silent monitoring. Demo it once more with the whole room watching, and have neighbors check each other's meters before moving on.
- Running long in Block 4 (prep). Students can prep three sounds in class and the fourth at their next session; the project goes up to the server with the library. Keep at least three full passes in class.
- Running short. Add a fifth recording: students invent a paper sound (paper sliding against itself, a sharp fold, a slow-motion crinkle) and name it themselves following the convention, choosing their own descriptor and variant.
- One station's interface fails partway through. Pair the student with a neighbor at a working station; they share the interface for recording and split the prep across two stations. Note the failed interface for after class.

### paper supplies

Standard 8.5×11 printer paper: four full sheets per student for the recordings, plus a stack of scrap at each station for the test crumble or rip in Step 3. A ream of 500 lasts several semesters. Avoid cardstock (its crackle is harsh) and tissue paper (it tears too quietly to register clearly on a dynamic mic).

### reminders for the TA

- Noise-profile clip first. Before students record any paper sound, they record 10 seconds of room tone. Walk the room during Step 6; a student who skips it can't denoise. The clip should look almost flat, with nothing audible in it.
- Peaks at -12 to -6 dBFS while recording. Don't let students push to -3 or above to be loud.
- Normalize doesn't fix a recording made too quiet. It evens out the peak level across recordings made at a good level.
- Students leave with the library folder set up and the README started. Check both before anyone leaves.

### after class

- Walk the room before locking up: interfaces, headphones, mics, stands, and XLR cables back in gear storage, interface knobs at zero, FileZilla and all apps quit, chairs in.
- Spot-check three or four student folders on the server at `netid/sample-library/`: four WAVs in `paper/`, README.txt at the root, the .aup3 in `audacity-projects/`.
- Listen to one or two samples per spot-checked folder on headphones: peaks at or near -1 dBFS, no clicks at the start or end, clean denoise without underwater artifacts.
- Note recurring quality problems (for example, three of four spot-checked folders had clicks) for a short recap at the start of Mon Wk 7.
- Note any interface or mic failures for repair before the next session.

---

## Session 3 · Mon Wk 7: widening the flow

100 min · lecture · MB2525

### roadmap

The basic chain from Session 1 used a dynamic mic, a mic-level signal, an XLR cable, and the interface's mic input. This lecture covers the signal levels, cables, mics, and modifiers students find outside that setup. The reading has five sections plus vocabulary.

1. The three signal levels. Mic level (around 1 mV) needs a preamp. Instrument level (around 100 mV, from a guitar or bass pickup) is high impedance and needs a Hi-Z input; the PreSonus marks both combo jacks Mic/Inst, and the Behringer has a separate Inst 2 jack. Line level (around 1 V, from a synth, a mixer, or an interface output) comes as consumer (-10 dBV, about 0.3 V) and professional (+4 dBu, about 1.2 V).
2. Cables for each level. XLR (recap from Lecture 1) carries mic level or balanced line level; a cable is passive, and the gear at each end sets the level. TS (tip-sleeve) is two-conductor and unbalanced, the guitar cable. TRS (tip-ring-sleeve) is three-conductor and carries either balanced mono (the PreSonus Main Outs) or unbalanced stereo (headphones), never both at once. RCA is unbalanced, one channel per plug, for consumer line level (a turntable's RCA output is phono level and needs a phono preamp). A TS plug fits a TRS jack and the connection becomes unbalanced; an XLR plug doesn't fit a quarter-inch jack.
3. Other mic types. The condenser (two plates, more sensitive, needs phantom power, which doesn't harm a modern balanced dynamic) and the ribbon (corrugated foil in a magnetic field, smooth and slightly dark, fragile, usually no phantom power, some older designs damaged by it). A photo compares an SM57, a Neumann U87, and a Royer R-121, with price ranges for each type.
4. Polar patterns beyond cardioid: omnidirectional and figure-8, plus super-cardioid, hyper-cardioid, and shotgun as variants. Multi-pattern condensers switch between them.
5. Signal modifiers. The DI box takes unbalanced instrument level to balanced mic level (passive with a transformer, or active and powered); the THRU jack feeds an amp at the same time. The hardware preamp takes mic level to line level, often with a sonic character; the reading names the Neve 1073 and the API 312. The section closes with a diagram of four paths into one interface.

### reading

[widening the flow](https://csuebmusic.github.io/mus381/module-03-recording/lessons/04-reading-widening-the-flow.html)

---

## Session 4 · Wed Wk 7: phone recordings into Audacity (Lab 2)

100 min · lab · MB2525

### roadmap

The session has two halves.

The first half moves one phone recording into Audacity and through the prep pipeline.

- Transfer with LocalSend. The student opens LocalSend on the Mac (the Receive tab shows the Mac's two-word LocalSend name), turns airplane mode off on the phone and joins campus Wi-Fi, shares the recording from the phone app to LocalSend, taps the Mac under Nearby devices, clicks Accept on the Mac, and moves the file from Downloads to `~/Documents/netid/`. Snags to expect: the phone is still in airplane mode from recording, or on cellular instead of campus Wi-Fi; the iPhone's Local Network permission for LocalSend is off (Settings → Privacy & Security → Local Network); the recording app doesn't list LocalSend in its share sheet, in which case the student opens LocalSend, goes to Send → File, and picks the recording. If a Mac never shows up under Nearby devices, use LocalSend's manual sending on the phone with the Mac's IP address (System Settings → Network on the Mac).
- Download the library from the server, open Audacity, confirm 48000 Hz and 24-bit PCM in Preferences, and save a new project as `sample-library-week-07.aup3` in `audacity-projects/`.
- Import with File → Import → Audio… (Cmd + Shift + I). Both recommended apps record 48 kHz, 24-bit WAV, which matches the project; students check the Rate and Format entries in the Audio Track Dropdown Menu (the … next to the track name). A stereo recording gets mixed down first: Tracks → Mix → Mix Stereo Down to Mono.
- Resampling is a conditional step for a file at another rate (a 44.1 kHz file, say): select the track and choose Tracks → Resample… → 48000. Every student still does the rate experiment once (Rate → 22050 in the track dropdown, play, then Cmd + Z) to hear the difference between reinterpreting a file's rate and resampling it.
- The prep pipeline is the one from Lab 1, with one change: the noise profile comes from a quiet second or two of the phone recording itself. From this session on, students record a second or two of silence at the start of every take.
- Export the sample as a mono WAV, 48 kHz, 24-bit, into a new category folder the student names (kitchen/, metal/, fabric/, and so on), and update the README's ORGANIZATION, CONTENTS, and Last updated lines.

The second half is worktime on the library: more phone recordings through the pipeline, new sounds recorded at the station with the dynamic mic, recordings from the hallway, stairwell, or courtyard, and reorganizing what's there. The TA circulates, asks questions, and catches students who are stuck. Students aim for at least two or three new prepped samples by the end of the session.

### handout

[phone recordings into Audacity](https://csuebmusic.github.io/mus381/module-03-recording/lessons/05-handout-phone-to-audacity.html) (Lab 2)

Seven steps, then the end-of-session upload: (1) send the recording from the phone to the Mac with LocalSend; (2) download the library and open a new Audacity project for the day; (3) import the phone recording and check its rate, format, and channel count; (4) when a file isn't at 48 kHz, with the reinterpret-or-resample experiment; (5) run the prep pipeline, with the noise profile taken from the phone recording; (6) export to a category folder and update the README; (7) worktime. The handout points to Lab 1, Step 8, for the full pipeline walkthrough with screenshots.

### common confusions

- The file won't open in Audacity. A recording from the iOS Voice Memos app is M4A, which the lab's Audacity doesn't open. The student records library sounds with one of the two recommended apps, which save WAV.
- The track has two waveform lanes. The recording is stereo. Mix it down with Tracks → Mix → Mix Stereo Down to Mono before prepping.
- Denoise sounds underwater. The noise profile caught something that isn't noise (a faint sound, a finger on the phone, a voice). Undo with Cmd + Z, take the profile from a different quiet region, and try again. If no part of the recording is quiet enough, skip denoise for that file; trim, fades, and normalize still give a usable sample.
- A student arrives with no phone recording. They record one sound at the station on their phone before Step 1 (the handout's "If you arrive without a recording" callout).

---

## Session 5 · Mon Wk 8: the mixer

100 min · lecture · MB2525

### roadmap

The lecture introduces the mixer as the place where many signals combine. Until now students have handled one signal at a time (one mic, one input, one recording). A mixer handles many at once and gives the engineer routing, processing, and combining tools a single audio interface doesn't have.

The lecture covers the console in MB2508, a 16-channel Toft Audio Designs Series ATB, top to bottom. The reading opens by defining the DAW and placing the mixer between the mics and the audio interface, with the analog-versus-digital distinction (a digital mixer such as a Behringer X32 or Allen & Heath SQ can be the audio interface; an analog console like the Toft needs a separate one). Then six sections:

1. The mixer as the place where signals combine: what a mixer does, Malcolm Toft and Trident, and the three kinds of strip (sixteen input strips, eight submaster strips, one master strip).
2. The channel strip, control by control: +48V, I/P REV, LINE, INPUT GAIN, phase reverse, the 80 Hz high-pass filter, the four-band EQ (±15 dB per band), six aux sends (Aux 1 always pre-fader; Auxes 2 to 6 switch with a PRE button), the monitor section, SOLO and MUTE, channel pan, the routing buttons (L-R and subgroup pairs 1-2, 3-4, 5-6, 7-8), and the fader (unity at 0, up to +10 above unity). Then the rear jacks: LINE, MON, INSERT, DIR. O/P (post-fader), and MIC. The section has six callouts that tie the strip back to earlier material: phase (to the XLR's balanced wiring in Lecture 1), the EQ (to Audacity's Filter Curve EQ, destructive against non-destructive), aux sends as a river with taps (with an SVG), how the pan knob splits a channel across a subgroup pair, TRS wired as an insert loop (a third use after Lecture 2's two), and insert send against aux send (which effects go on each).
3. In-line architecture: two inputs on every strip, what "monitor" means on this console, and the I/P REV button.
4. The submaster section: the stereo FX return, the bargraph meter (-20 to +15 dBu), the tape return block (AUX 5 and AUX 6 with PRE, MON LEVEL and MON PAN into the master mix, SOLO, TAPE), and the subgroup fader (the level out to the DAW). Then summing, with a drum-kit example on subgroup pair 1-2 and an SVG, and the four rows of submaster jacks on the back. Callouts cover aux buses and the two places a subgroup pair goes.
5. The master section: the VU meters, the six Aux Masters, the headphone output, the 2-track returns (with an A/B callout), SOLO MASTER, PHONES LEVEL, and the bargraph meters. Then the two outputs: MASTER O/P and the speaker output (MAIN SPKR or ALT SPKR, shaped by ALT MONITOR, MONO, and MONITOR LEVEL). The reading notes that MB2508 is wired differently and points to the Lab 4 handout. Then talkback (TALK TO AUXES and TALK TO GROUPS, with a slating callout) and the master fader.
6. The console as a creative space.

The reading closes with vocabulary and a further-exploration list: the Tape Op #69 review of the ATB, the Sound on Sound review of the ATB24, and the Shure Audio Systems Guide for Music Educators. The console's manual is on the studio shelf next to the console.

The reading has five photos: an overhead shot of a 16-channel ATB (via Retro Gear Shop), an annotated input strip, an annotated group/master section (shown in sections 4 and 5), and the rear input and output sections (credited to Toft Audio Designs / PMI Audio Group; the output section is shown in sections 4 and 5).

Lecture 3 doesn't cover the live-sound or studio scenarios. Lab 3 (Session 6) covers live sound, and handout 08 covers studio recording in MB2508.

### reading

[the mixer](https://csuebmusic.github.io/mus381/module-03-recording/lessons/06-reading-the-mixer.html)

---

## Session 6 · Wed Wk 8: the mixer in practice · live sound (Lab 3)

100 min · lab · MB2525

### roadmap

Students take the console from Monday's reading through one fully worked live-sound scenario, then route bands of their own in a widget. Students take nothing from gear storage. They work at their stations with the mixer reading open in another tab, and the TA demonstrates routing decisions on the projector.

The fictional band, The Sound Below, is a five-piece with twelve signals into the console:

| Player | Signals | Source | Level and cable |
|---|---|---|---|
| Vocalist | 1 | Dynamic mic | Mic level, XLR |
| Guitarist | 1 | Dynamic mic on the amp | Mic level, XLR |
| Bassist | 2 | DI box direct out (dry) and a dynamic mic on the amp (wet); the DI's thru jack feeds the amp | Mic level, XLR |
| Drummer | 4 | Kick and snare (dynamics), two overhead condensers (+48V) | Mic level, XLR |
| Keyboardist | 4 | Stage keyboard L and R, laptop L and R | Line level on TRS, through a four-channel DI box with the pads engaged, then mic level on XLR |

The sixteen-channel console has twelve channels in use.

Section 1 introduces the band, with callouts on why the bass gets two channels and why the keyboardist's signals are different.

Section 2, Scenario 1 (live sound, walked), puts the band in a small venue. The console sends the band to two destinations: the front-of-house (FOH) speakers for the audience, through the master mix at MASTER O/P to the FOH amps, and five stage monitors, one per performer, each fed by its own aux.

- From the stage to the console: the stage box (its jack number becomes the console channel number), the snake with its fan-out and return lines, and the keyboardist's DI box. Callouts cover two simpler alternatives for the keys (a TRS-to-XLR cable, or a stage box with TRS line inputs) and digital snakes.
- The channel chart: all twelve signals on MIC (XLR) jacks, channels 1 to 12, phantom power on only for the two overheads (channels 7 and 8).
- The FOH mix in three patches. Patch 1: channels 1 to 4 (vocal, guitar, bass DI, bass amp) straight to L-R. Patch 2: the drums (channels 5 to 8) to subgroup pair 1-2, TAPE up, MON LEVEL up, MON PAN hard left on 1 and hard right on 2, submaster faders down. Patch 3: keys and laptop (channels 9 to 12) to subgroup pair 3-4 the same way.
- The stage monitor mixes: Auxes 1 to 5, one per performer, all pre-fader (Aux 1 always is; Auxes 2 to 5 need PRE pressed on every channel), each Aux Master at about unity. AUX MASTERS jacks feed the snake's return lines back to the stage; the ProX snake in the photo has four returns, and a fifth monitor needs its own cable run. The section explains powered and passive stage monitors and ends with a table of the five blends and a callout on one source reaching six destinations.

Section 3, Scenario 2 (you try), is the widget. Generate a band pulls a random lineup from a pool of six, each adding one routing concept The Sound Below didn't cover: a string quartet (when to skip subgroups), a singer with a looper (a stereo line source on a subgroup pair), a punk trio with a double-mic'd kick, a jazz quartet (two stereo subgroup pairs), an electronic duo (stereo line sources on LINE inputs), and a folk band with a sit-in fiddler (a subgroup pair ready to mute). Students read the signal chart, build the channel chart themselves, then plan the FOH mix and the stage monitor mixes. Each section has a Show one approach button that reveals a worked solution with a trade-off note. Students answer on paper before revealing.

Aux sends, subgroups, and the master all route signal, and they look the same on the desk in every context; what's plugged into them and where their outputs go changes. The studio version, with Aux 1 and Aux 2 feeding one shared headphone cue in MB2508, is in handout 08, which students work through on their own time after the Wk 9 visit.

### handout

[the mixer in practice · live sound](https://csuebmusic.github.io/mus381/module-03-recording/lessons/07-handout-the-mixer-in-practice.html) (Lab 3)

The handout ends with a five-minute library check before students leave: naming, the README, one or two more sounds through the pipeline, and an upload if anything changed.

---

## Session 7 · Mon Wk 9: studio visit to MB2508 (Lab 4)

100 min · lab · MB2508 (studio)

### roadmap

The session moves to MB2508, where the Toft is, and students see a working studio in person. There's time for a walk around the room and to hand out the midterm materials; students don't record in this session. They see the two rooms (the live room where performers play, the control room where the engineer works), the Toft on its console desk, the preamp rack beside it (the Focusrite ISA 828 and OctoPre), the side rack built into the desk (the Furman PL-8, the Avid HDX I/O, the SSL XLogic G compressor, the PreSonus AudioBox USB 96, the Furman HDS-6), the monitor speakers and the subwoofer, and in the live room the two Hosa mic panels and the two Furman HR-6 headphone stations.

The studio-recording walkthrough isn't done in class. It's in handout 08, which students take home and work through on their own when the studio is free. The handout documents the gear room by room and walks one vocal mic from the live room to a finished recording. A student can follow it at the desk without an instructor.

The visit runs in this order:

- Walk students to MB2508 at the start of class. (about 5 min)
- Tour the two rooms and the wall between them: the live room (mics, the two Hosa mic panels, the two HR-6 stations), the control room (the Toft, the preamp rack, the side rack, the monitor speakers and the sub), and how signal crosses from one room to the other. The top Hosa panel is wired through the wall to the ISA, which feeds Toft channels 1 to 8; the bottom panel goes to the OctoPre, which feeds channels 9 to 16. (about 20 min)
- At the Toft, point out the input strips, submasters, master section, and master fader; the front-of-strip controls (phase, HPF, EQ, aux sends, monitor section, pan, routing buttons, fader); and the rear jacks on one input section (LINE, MON, INSERT, DIR. O/P, MIC). (about 25 min)
- Go through the side rack, naming each piece's job: the PL-8 powers the rack (the Toft has its own outlet and switch); the HDX I/O connects the Toft to Pro Tools (it takes submasters 3 to 8 and direct outs 9 to 16); the SSL is patched as a parallel compressor on Aux 5 and Aux 6, returning on LINE 13-14; the AudioBox connects a laptop (submasters 1 and 2 into its 1/4" instrument inputs to record, laptop playback back on LINE 9-10); the HDS-6 takes the headphone cue from Aux 1 and Aux 2 and sends it to the HR-6 stations over Ethernet. Point out the speaker wiring: the monitor speakers are on MASTER O/P and the sub is on MAIN SPKR. In this room the master fader sets the room level, the sub plays only while the master fader is up, MONITOR LEVEL sets how much sub is added, and SOLO, MONO, and ALT MONITOR reach only the sub. Say this explicitly: students who read the mixer reading expect MONITOR LEVEL to set the speaker volume. At the AudioBox, the Gain knobs stay at minimum and the submaster faders come up slowly; a line-level signal in the instrument inputs can distort and damage them. Point students to handout 08 for the detail. (about 20 min)
- Optional, if time and setup allow: power the console on and pass one signal through one channel strip to the monitor speakers, starting with the master fader down and MONITOR LEVEL at zero. If the studio isn't set up, the tour stays observational. (about 15 min)
- Hand out handout 08 (the studio-recording walkthrough, for students' own time) and handout 09 (the midterm review packet, for study before Wednesday). Remind students the library is due at the start of class Wednesday, uploaded and checked. (about 10 min)

### handout

[the mixer in practice · studio recording](https://csuebmusic.github.io/mus381/module-03-recording/lessons/08-handout-studio.html) (Lab 4)

A self-guided studio guide and walkthrough. It documents the gear room by room (the live room; the control room's two preamps, PL-8, HDX I/O, SSL, AudioBox, HDS-6, and speakers), then lists every jack on the back of the Toft and what's plugged into it, in tables for the input channels, the submasters, and the master section, plus the AudioBox and the HDS-6. Then it walks one vocal mic end to end in five parts:

1. The mic from Hosa panel 1 jack 1 through the ISA to Toft channel 1, routed to submasters 1-2 and up on the monitor speakers, with gain staged at the ISA first and the sub added last.
2. A reference track from the laptop through the AudioBox into channels 9 and 10 on L-R, where it plays in the room and stays off the recording.
3. The singer's headphone cue on Aux 1 and Aux 2 (both pre-fader) to the HR-6 stations.
4. Parallel compression on the vocal through the SSL, sent post-fader on Aux 5 and Aux 6 and returned on channels 13 and 14 to submasters 1-2.
5. Recording submasters 1-2 to the laptop through the AudioBox at 48 kHz, 24-bit, with the level set on the submaster faders.

Students save the session in `~/Documents/netid/recordings/` named lastname-projectname-version (for example, garcia-vocal-v1). The handout closes with comping the takes in Logic Pro (Take Folders, Quick Swipe Comping) and Ableton Live 11 (Take Lanes), each exported as a WAV at 48 kHz, 24-bit. It isn't walked in class.

### midterm review packet

[midterm review](https://csuebmusic.github.io/mus381/module-03-recording/lessons/09-handout-midterm-review.html)

Handed out at the end of Session 7 for study at home. It gathers the vocabulary for the terminology exam from Modules 1 through 3 into ten sections, each headed with the module and page it's drawn from: working in the lab; digital audio; sound and timbre; editing and the envelope; dynamics (transient is the one exam term); signal flow and the recording chain; signals, levels, and cables; the interface; the mixer; and from recording to sample, and the library. It explains the three kinds of thinking the exam asks for (define, identify from a description, trace a signal flow), suggests a cover-and-recall study method, and closes with "the thread that connects it all" (the signal path from air to file) and a test-yourself list of eighteen questions.

---

## Session 8 · Wed Wk 9: midterm (library submission and terminology exam)

100 min · library submission and exam · MB2525

### roadmap

Two parts.

Part 1, library submission (roughly the first 30 minutes). Students upload their final library to the server following the submission details on the Project 2 page. The TA checks each library before moving on:

- `sample-library/` is inside the student's own folder on the server
- samples are in category folders, with the Audacity project in `audacity-projects/`
- README.txt is at the root and filled in
- every sample is a mono WAV, 48 kHz, 24-bit
- every filename follows [category]-[descriptor]-[variant].wav
- there are at least 20 prepped samples

Once a library is verified, copy it into the peer-listening folder at `/public/mus-381-fall-2026/project-02-libraries/<lastname>/`. The peer-listening assignment, due Mon Oct 19 (Wk 10), reads from there.

Part 2, terminology exam (the remaining hour). Cumulative, Modules 1 through 3, closed-book, no devices, 50 points.

### exam scope

The exam and answer key are in [`exams/midterm-exam.md`](../exams/midterm-exam.md) (TA-facing). The exam tests only what the midterm review packet covers, in four parts: define in plain language (Part A), identify from a description (Part B), trace a signal flow from voice to WAV and back to the headphones (Part C), and short answer on the noise floor, balanced cables, clipping, and the prep pipeline (Part D). The packet's ten sections are the scope:

- Working in the lab: the local working folder, the class server, the session workflow, file naming, file extensions (Module 1)
- Digital audio: sample rate, bit depth, Nyquist, quantization, aliasing, SNR, headroom, ADC and DAC, file formats (Module 2)
- Sound and timbre: waveform, fundamental, partial, harmonic series, timbre (Module 2)
- Editing and the envelope: cut, trim, splice, fades, crossfade, time-stretch, pitch-shift, attack, sustain, release (Module 2)
- Dynamics: transient (Module 2)
- Signal flow and the recording chain: transducer types, phantom power, polar patterns, frequency response (Module 3)
- Signals, levels, and cables: mic, instrument, and line level; XLR, TS, TRS, RCA; balanced and unbalanced; phase; mono and stereo; DI box and hardware preamp (Module 3)
- The interface: preamp, gain, clipping, direct monitoring, monitor mix, latency (Module 3)
- The mixer: channel strip, fader, unity gain, bus, subgroup and submaster, master mix, aux send, pre-fader and post-fader, FOH, headphone cue, in-line console, analog and digital mixers (Module 3)
- From recording to sample: the prep pipeline, resampling, recording with headroom, library organization (Module 3)

---

## end-of-module assessment

### what success looks like

Students at the end of Module 3 can:

1. Trace the signal flow at any setup, from acoustic source to stored file
2. Set up a recording session from cold and capture a clean recording
3. Move a phone recording through the prep pipeline into their library
4. Find a sound in their own library by category or by name
5. Distinguish signal levels, cables, and transducer types
6. Describe what aux sends and buses do in live sound and in the studio
7. Pass the cumulative terminology exam

### signs of trouble across the cohort

- Libraries with no README or a one-line README. Reinforce in Module 4 with an exercise that has students find a sound in their library from the README.
- Files that peak at 0 dBFS. The normalize target was wrong; point students back to Lab 1, Step 8 (peak -1.0 dB).
- Files that click at the start or end. Students are trimming without the fades; reinforce the fade at every trim.
- Students who can't trace signal flow on the exam. Note it in the retrospective for Inés.

### into Module 4

The libraries from this module are the source material for Module 4. Students load their library into Ableton Live 11 in Wk 10 (Lab 1, audio editing) and build instruments from it in Wk 11 (Lab 2, sampling).

### retrospective

After Module 3 ends, write a short retrospective: what went well, what didn't, pacing notes, and questions from students that surprised you.

---

## what follows

Module 4 (Wks 10 to 13) is in Ableton Live 11: the DAW environment, audio editing, sampling, and mixing, then a transferable-concepts session in Adobe Audition on Mon Wk 13. Students build their final project from their own recorded material, starting with the library from this module.
