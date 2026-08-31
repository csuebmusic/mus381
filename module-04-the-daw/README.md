# Module 04 — The DAW

**Weeks 10–15 · instruction Wks 10–13 (7 sessions), final project Wks 14–15**

---

## Module purpose

Modules 2 and 3 lived in Audacity: students edited handed-to-them sound (Module 2) and recorded their own (Module 3). Module 4 moves into Ableton Live, the destination DAW for the course, and the place where the two earlier skill sets converge. Students load the sample library they built in Module 3 and start making pieces from their own recorded material.

The module is built around a single beginner question: what is a DAW, and what can you do in it that a destructive waveform editor like Audacity can't? Each session answers part of that. The arc:

introduce the DAW environment (Session view vs Arrangement view, the timeline, nondestructive editing) → edit audio in Ableton (import the library, warp, arrange clips) → meet the sampler instruments (Simpler and Drum Rack) and trigger them from MIDI for the first time → sample in practice (build something playable from library sounds) → mix in Ableton (the channel strip, sends and returns, group tracks, built-in EQ and dynamics) → step out of Ableton for one session to see the same concepts in an advanced audio editor (Adobe Audition), so the skills read as portable rather than app-specific → final project.

Three throughlines:

1. **Nondestructive editing is the new mental model.** Audacity edits the file: a cut removes samples, a fade rewrites them. Ableton edits a *view* of the file: the clip points at the audio, and the edits (start, end, fades, warp, gain) are instructions layered on top. Nothing happens to the source. This is the conceptual jump of the module, and it reframes everything they learned about editing in Module 2. Lead with it in Session 1 and reinforce it every time a student is afraid of "ruining" a sample.

2. **Your library is the raw material.** Every audio session in this module pulls from the student's own Module 3 sample library. The "find a sound in your library and use it" loop is the payoff of the midterm: a student who organized their library well will move fast here; a student who didn't will feel the friction, which is itself the lesson. The Module 3 README flags this as a forward promise to deliver, and it runs across Sessions 2 through 4.

3. **Concepts transfer; tools differ.** The module opens by teaching "a DAW" through Ableton specifically, and closes (Session 7, Adobe Audition) by showing the same ideas under a different UI with different names. Sample rate, bit depth, gain staging, EQ, compression, fades, multitrack arrangement: every one of them exists in any serious audio tool. Students leave knowing they learned transferable concepts, not just where Ableton's buttons are. This matters especially for the art majors, who already live in the Adobe suite and will recognize Audition's place in it.

By the end of Wk 13, students should be able to set up an Ableton session from cold, import and warp audio from their library, build a short playable idea with a sampler instrument, mix it with the built-in devices, and articulate which of those skills would carry to any DAW. Wks 14–15 turn that fluency into the final project.

---

## Reference scope (Ableton Live 11 manual)

The lab runs **Ableton Live 11 Suite**. Live is a large DAW; this module deliberately teaches a curated subset and does not try to cover it. The sections below are the source of truth for drafting each week's lessons: menu paths and terminology all match Live 11, and lessons are drafted against the manual rather than from memory. Staying inside this list is the point, not a limitation to apologize for.

**No embedded screenshots.** This module's lessons don't reproduce Ableton screenshots. The reading and the labs run alongside a live instructor walk-through and link the version-pinned Live 11 manual sections directly, so students see the current UI in the app rather than a static capture. (An earlier draft embedded Live 11 captures under `assets/images/module-04-week-10/`; that was dropped when the reading became a live-class companion, and the folder was removed.)

**Video companion (TA + students).** Ableton's [Learn Live](https://www.ableton.com/en/live/learn-live/) video library covers most of the topics below (sorted into Setup, Interface, Instruments & Effects, Workflows) and is linked from the Session 1 reading. It's a useful fallback when a manual page is dense or a student learns better from video, and a good place for the TA to send students who want a second pass on a concept. The videos track the current shipping version (Live 12 at time of writing) rather than Live 11, so the UI may look slightly newer; for the beginner-level concepts in this module the difference is cosmetic. Use it as a companion, not a substitute for the version-pinned manual links, which stay the source of truth for menu paths and terminology.

**Week 10 (the environment + audio editing):**
- First Steps — https://www.ableton.com/en/live-manual/11/first-steps/
- Live Concepts — https://www.ableton.com/en/live-manual/11/live-concepts/
- Arrangement View, audio portions only (audio tracks and clips on the timeline; skip the MIDI-clip and Session-view-launch material, which arrive in Wk 11 or stay out of scope) — https://www.ableton.com/en/live-manual/11/arrangement-view/
- Clip View — https://www.ableton.com/en/live-manual/11/clip-view/
- Audio Clips, Tempo, and Warping — https://www.ableton.com/en/live-manual/11/audio-clips-tempo-and-warping/

**Week 11 (sampling + MIDI as trigger):**
- Simpler — https://www.ableton.com/en/live-manual/11/live-instrument-reference/#simpler
- Drum Racks — https://www.ableton.com/en/live-manual/11/instrument-drum-and-effect-racks/#drum-racks
- Editing MIDI Notes and Velocities — https://www.ableton.com/en/live-manual/11/editing-midi-notes-and-velocities/ (scoped to just enough to trigger: drawing and editing notes)
- Monitoring — https://www.ableton.com/en/live-manual/11/routing-and-i-o/#monitoring (the track Monitor setting, paired with arming a MIDI track to play the instrument; moved here from Wk 12 since Live work in this module never records audio)

**Week 12 (mixing):**
- Internal Routings — https://www.ableton.com/en/live-manual/11/routing-and-i-o/#internal-routings
- Mixing — https://www.ableton.com/en/live-manual/11/mixing/
- Live Audio Effect Reference — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/ . The locked effect set, the same effect types from Modules 2 and 3, now as Live devices, split into inserts (where chain order matters) and sends (shared on return tracks):

*Insert effects, in chain order:*
1. Utility — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#utility (first and/or last in the chain, when needed)
2. EQ Eight — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#eq-eight
3. Auto Filter — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#auto-filter
4. Compressor — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#compressor
5. Glue Compressor — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#glue-compressor (for the master or a bus)
6. Limiter — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#limiter
7. Multiband Dynamics — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#multiband-dynamics

*Send effects:*
- Hybrid Reverb — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#hybrid-reverb
- Reverb — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#reverb
- Delay — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#delay
- Echo — https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#echo

**Week 13 (Adobe Audition):** outside the Ableton manual. Audition runs on the lab Macs, so Session 7 is a hands-on follow-along (handout 05); it links Adobe's own get-started guide rather than the Live manual.

**Exporting (used across the module):** Exporting Audio and Video — https://www.ableton.com/en/live-manual/11/managing-files-and-sets/#exporting-audio-and-video . Students export finished work at 48 kHz / 32-bit. Needed first when they render a short arrangement, then again at mixing and for the final project.

---

## Learning outcomes

By the end of this module, students should be able to:

1. Describe the difference between Session view and Arrangement view and say which they'd reach for in a given situation
2. Explain nondestructive editing: that a clip is a view of a file, and edits are instructions layered on top rather than changes to the source
3. Import audio from their own sample library into an Ableton set and arrange it on the timeline
4. Use warping at a basic level: turn it on and off, understand that it maps a sample to the set's tempo, and know when they want it versus when they don't
5. Load a sample into Simpler and play it across a MIDI keyboard; load samples onto a Drum Rack and trigger them from pads
6. Explain the beginner-level model of MIDI: that a MIDI note is data (which pitch, when, how hard) that triggers an instrument, and that the instrument is what makes the sound
7. Mix a small session using Ableton's built-in tools: track faders, pan, sends to a return track, group tracks, and the built-in EQ and compressor
8. Map Ableton's mixer onto the console architecture from Module 3: track fader = channel fader, send = aux send, group = subgroup, Master = master bus
9. Recognize the same core concepts (sample rate, bit depth, editing, EQ, dynamics, multitrack) in a different tool (Adobe Audition, an advanced audio editor) and articulate that the concepts are portable across tools

---

## Key concepts introduced

- **DAW (digital audio workstation):** Audacity is an *audio editor*, not a DAW: it records and edits audio but has no instruments, no MIDI, and no full mixer. Ableton is the first DAW students meet: multitrack, nondestructive, with instruments and a built-in mixer. Define the term here and draw the editor-vs-DAW line explicitly, since the last two modules were spent in an editor. (Inés is firm on this: do not call Audacity a DAW.)
- **Session view vs Arrangement view:** Session view is the clip grid, for trying ideas and looping; Arrangement view is the linear timeline, for committing to a structure. Two views of one set. Beginners do most early work in Arrangement (it resembles Audacity's timeline) and meet Session view as the thing that's genuinely new.
- **Clip:** a reference to audio (or to MIDI), with its own start, end, gain, fades, and warp settings. The unit of work in Ableton. The key idea: the clip is not the file; it points at the file.
- **Nondestructive editing:** edits live on the clip, not the source audio. Contrast explicitly with Audacity, where edits rewrote samples. This is the reframe of the module.
- **Warping:** Ableton's time-stretching. A warped clip follows the set's tempo; warp markers pin moments in the audio to moments in the bar. Beginner level: warp on means "stretch to match the project tempo," warp off means "play at the recorded speed." When you want each: warp on for loops and rhythmic material you want locked to a grid; warp off for one-shots and sounds where the original timing is the point.
- **Sample rate is constant; bit depth steps at export:** the Module 3 library is already 48 kHz and Module 4 sets run at 48 kHz, so library files import with nothing to convert. The only format change is bit depth: students export at 32-bit, up from the 24-bit they worked in through Modules 2–3. The rate that matters for the deliverable is set at export.
- **MIDI (beginner model):** data, not sound. A MIDI note carries pitch, timing, and velocity (how hard). The note triggers an instrument; the instrument makes the audio. "The piano roll says play C3 now, medium-hard; Simpler turns that into the sound of your sample at that pitch." First real encounter is as a *trigger* for the sampler instruments, not as composition.
- **Simpler:** an instrument that plays one sample across the keyboard. A MIDI note picks the pitch; the sample plays back faster (higher) or slower (lower). Has a volume envelope (attack, decay, sustain, release) that shapes each note.
- **Drum Rack:** a grid of pads, each pad holding one sample. A MIDI note triggers a pad. The way students build a kit from their own library sounds and play or sequence it.
- **The Ableton mixer:** track faders, pan, sends, return tracks, group tracks, the Master track. Introduced as the digital version of the Module 3 console: the same channel-strip / aux / subgroup / master architecture, rendered in software.
- **Sends and return tracks:** a send routes a copy of a track's signal to a return track, where an effect (reverb, delay) lives. One reverb, many tracks feeding it. This is exactly the aux-send mechanism from the Toft, now in Ableton; name the connection explicitly.
- **Group tracks:** several tracks folded into one for combined level and processing. Ableton's subgroups. The connection back to the console's subgroup strips.
- **Built-in devices (mixing):** the same effect types from Modules 2 and 3, now as Live devices, in two roles. Insert effects sit in a track's chain where order matters (gain via Utility, EQ, filtering, compression, limiting, multiband dynamics); send effects live on return tracks and are shared across tracks (reverbs, delays). What each does and where it sits, mapped onto the EQ and dynamics from Module 2 and the aux-send architecture from Module 3. Full locked list in Reference scope.
- **Transferable concepts (Audition coda):** sample rate, bit depth, gain, fades, EQ, compression, multitrack. The Session 7 point is that these are properties of digital audio and audio production, not of Ableton. Audition is the worked example of "the same ideas, a different tool."

---

## Deliverable: Final project

**Weeks 14–15 + finals.**

**Built:** `projects/final-project.html`.

- Open prompt: any kind of piece (audio-driven, sampler-driven, or combined) that demonstrates fluency with the semester's skills. Built in Ableton.
- Length: 2 to 3 minutes.
- Source material: every sound must be student-recorded (their Module 3 library plus anything new they record). No pre-recorded, found, or downloaded sound, and no pre-made loops. One exception: they may use another student's recording *with permission*, and must credit it. Crediting is the teaching point; credits go in a `lastname-final-credits.txt` file in the working folder.
- Draft 1 due Wed Wk 14: a complete rough pass, submitted to the working folder for instructor/TA written feedback. No in-class listening (no time).
- Draft 2 due Wed Wk 15: the revision, after acting on the Draft 1 feedback.
- Final during finals: WAV 48 kHz / 32-bit, `lastname-final.wav`, to the server working folder and the class folder. Optional SoundCloud for portfolio.
- Rubric (out of 100, no revision criterion): Technique & tools 35, Form & shape 30, Sound material & sourcing 20, Mix & craft 15.
- A cumulative final exam runs during finals week (covers the whole course), separate from this project. Exam and answer key: [`exams/final-exam.md`](../exams/final-exam.md) *(TA-facing)*.

### Final review packet

[`lessons/06-handout-final-review.html`](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/06-handout-final-review.html)

A take-home study packet for the cumulative final, parallel to the Module 3 midterm review. It gathers the Module 4 vocabulary (the DAW, the clip, nondestructive editing, warping, MIDI as a trigger, the sampler instruments, the mixer-as-console mapping, inserts vs sends) and the three cross-course anchors the final still tests (sample rate, clipping, bit depth at export), and closes with a self-check that mirrors the exam's question style. Handed out at the last class meeting (Wed Wk 15) for study before the finals-week exam, and on the course site throughout. The exam (`exams/final-exam.md`) is built to stay inside what this packet covers, the way the midterm is pinned to its review handout.

---

## Listening assignment

**Module 4 historical listening (one, sample manipulation):** the lineage of building music from recorded sound, from musique concrète through hip-hop and sampling into contemporary producers who chop and recontextualize samples. It closes the loop the course opened with: Module 2's musique concrète listening was the same idea with tape and razor blades; this is the same idea in a DAW. Anchored to Wk 11 (the sampling sessions).

No peer listening in Module 4: final pieces are shared in the class folder for everyone to hear, with no formal written response assignment.

**Due:** Mon Wk 13, before class.

**Built:** `listening/historical.html`. Works: Grandmaster Flash (1981), DJ Shadow (1996), The Avalanches (2000), J Dilla (2006), plus a student-choice contemporary piece. Photos in place (Flash at the turntables; an Akai MPC60) in `assets/images/module-04-week-11/`, alongside a lineage timeline SVG. Photo credits resolved.

---

## Student-facing materials

- [`lessons/01-reading-the-daw-environment.html`](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/01-reading-the-daw-environment.html) — Into the DAW
- [`lessons/02-handout-audio-editing.html`](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/02-handout-audio-editing.html) — Audio Editing in Ableton
- [`lessons/03-handout-sampling-in-practice.html`](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/03-handout-sampling-in-practice.html) — Sampling in Ableton
- [`lessons/04-handout-mixing-in-practice.html`](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/04-handout-mixing-in-practice.html) — Mixing in Ableton
- [`lessons/05-handout-transferable-concepts.html`](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/05-handout-transferable-concepts.html) — Adobe Audition
- [`lessons/06-handout-final-review.html`](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/06-handout-final-review.html) — Final Review
- [`listening/historical.html`](https://csuebmusic.github.io/mus381/module-04-the-daw/listening/historical.html) — Listening: Sampling
- [`projects/final-project.html`](https://csuebmusic.github.io/mus381/module-04-the-daw/projects/final-project.html) — Final project

---

## Session overview

**How the materials map to sessions.** Each week runs on one document. The module **reading** (`01-reading-the-daw-environment.html`) is met Monday of Wk 10 as the module's map and is referred back to all module. The three **handouts** (`02` audio editing, `03` sampling, `04` mixing) each drive a full week, both the Monday session and the Wednesday session: the TA works through the handout while students follow hands-on, so concept and doing happen together rather than splitting into a separate lecture and lab. There are no standalone Monday lecture documents for Wks 11 and 12; the week's handout carries both days. Wk 13 is the exception, a Monday-only Audition follow-along (`05-handout-transferable-concepts.html`), since Wed Wk 13 is Veterans Day. Handout `06` is the take-home **final review packet**, not a session document: it is handed out at the last class meeting for study before the finals-week exam, parallel to the Module 3 midterm review.

| Wk | Day | Focus |
|---|---|---|
| 10 | Mon | Session 1 · Reading (the module map), then begin Lab 1 (handout 02). What a full DAW is, Session vs Arrangement view, the clip, nondestructive editing as the reframe of everything from Module 2. Students also create their final-project Set. |
| 10 | Wed | Session 2 · Lab 1 continues (handout 02). Import your library, place clips on the Arrangement timeline, basic clip edits (start/end, fades, gain), an introduction to warping. |
| 11 | Mon | Session 3 · Begin Lab 2 (handout 03). MIDI as trigger: a MIDI note triggers an instrument; the instrument makes the sound. Simpler plays one sample across the keyboard; Drum Rack is a grid of one-sample pads. |
| 11 | Wed | Session 4 · Lab 2 continues (handout 03). Load library sounds into Simpler and a Drum Rack, sequence a short MIDI part, build one short playable idea from the student's own samples. |
| 12 | Mon | Session 5 · Begin Lab 3 (handout 04). The Ableton mixer as the digital console: track faders, pan, sends and return tracks, group tracks, the Master. EQ and Compressor mapped onto Module 2 and the Module 3 console. |
| 12 | Wed | Session 6 · Lab 3 continues (handout 04). Commit the session to audio (freeze and flatten the MIDI tracks, consolidate), then mix: levels, pan, a reverb return, groups, EQ and compression. |
| 13 | Mon | Session 7 · Transferable concepts, through Adobe Audition (handout 05). *(Mon only; Wed is Veterans Day.)* The same concepts in a different tool: sample rate, bit depth, editing, EQ, dynamics, multitrack, under Audition's UI and names. The point is portability of skills, aimed in part at the art majors already in the Adobe suite. |
| 14 | Mon / Wed | Final project worktime; Draft 1 due Wed Wk 14. |
| 15 | Mon / Wed | Final project revision; Draft 2 due Wed Wk 15. Final review packet (handout 06) handed out for the finals-week exam. |
| Finals | — | Final piece to the server + class folder; cumulative final exam. |

Block-by-block facilitation, demo scripts, common confusions, and pacing fallbacks for each session will be filled in below as the module is built out.

---

## Pre-module preparation (Inés / TA)

- **Ableton Live 11 Suite** is the lab version. Handout screenshots, menu paths, and manual references all target Live 11 (see Reference scope above for the exact sections). Suite confirms everything in scope is installed; Simpler and Drum Rack are in every edition regardless.
- **MIDI keyboards inventoried and tested at every station.** They enter the gear list this module (the Module 4 handout gear tier adds the MIDI keyboard). Confirm each one is present, connects over USB through the hub, and registers in Ableton's MIDI preferences.
- **Adobe Audition installed and tested on the lab Macs.** Audition runs at every station, so Session 7 is a hands-on follow-along. Confirm it launches under the campus Adobe license before Wk 13.
- **A starter session for the mixing lab.** Session 6 mixes a prepared multitrack session staged on the server: a longer piece with several instruments, some MIDI and some audio, so there is MIDI to commit and audio to consolidate. Inés provides it; stage it at `/public/module-04/` before Wk 12, alongside the noise recording the Wk 13 Audition follow-along uses.
- **Final-project Set.** Students create their own project Set in Session 1 (the reading ends by walking them through it), named `lastname-project`, and build it in the end-of-class block of each lab. Nothing to pre-stage; be ready to help with the create-and-save step on Day 1.
- **Library readiness check.** Sessions 2 through 4 assume each student has a usable Module 3 library on the server. Spot-check that libraries survived the midterm and are findable before Wk 10.

---

## Module-wide concerns

### Recurring confusions to expect across the module

- The clip-vs-file distinction: students expect Audacity behavior (edits change the file) and are surprised or worried that Ableton edits seem reversible. Reframe as a feature, not a bug.
- Warp on when they wanted it off (a one-shot stretched to the grid sounds wrong) or off when they wanted it on (a loop drifting out of time). The "loops want warp, one-shots don't" rule of thumb.
- MIDI vs audio tracks confused: dropping a sample expecting it to play as a note, or drawing MIDI on an audio track. The trigger model (note → instrument → sound) is the fix.
- Sends vs inserts: putting a reverb directly on a track (insert) when they meant to share one reverb across tracks (send to a return). Maps to the Module 3 aux-vs-insert distinction.

### Gear setup baseline (every Wednesday)

Same as Module 3, minus the mic and XLR (the lab sessions here are not recording sessions), plus the MIDI keyboard: audio interface, headphones, MIDI keyboard, connected over the USB hub. Confirm each MIDI keyboard registers in Ableton before the room fills.

### Pacing across the module

The pressure point is **Session 3 → 4** (the MIDI-as-trigger jump). MIDI is the one genuinely new abstraction in a module otherwise built on familiar material (audio, editing, mixing). If the trigger model doesn't register on the Monday (Session 3), the Wednesday lab stalls. Plan the Monday to leave students able to state the note → instrument → sound chain before they build with it on Wednesday.

The other risk is **Session 7 (Audition)** turning into an Audition tutorial. It isn't one. The session is about portability of concepts; Audition is the example. Keep the emphasis on "you already know this; here it is wearing different clothes," not on Audition's feature set.

### When to escalate to Inés

Same as Modules 2 and 3.

---

## Session 1 · Mon Wk 10: The DAW environment, through Ableton

**100 min · Reading, then Lab 1 begins · MB2525**

### Roadmap

The module's framing question: what is a DAW, and what's new about it after two modules in an audio editor (Audacity)? Introduce Session view vs Arrangement view, the clip as a reference to audio, and **nondestructive editing** as the reframe of everything they did in Module 2. Students should leave able to say what a clip is and why editing one doesn't touch the underlying file. After the reading, the session moves into Lab 1: students create their final-project Set, which the reading introduces, and begin handout 02 (Wednesday continues it).

### Reading

`lessons/01-reading-the-daw-environment.html`

### Manual (Live 11)

First Steps; Live Concepts.

### Connection to earlier modules

Module 2 taught editing as something you do *to a file*. This lecture reframes editing as something you do *to a clip*, with the file untouched underneath. The relief of "you can't ruin your source" is worth naming out loud: beginners edit timidly, and nondestructive editing is permission to experiment.

---

## Session 2 · Wed Wk 10: Audio editing in Ableton (Lab 1)

**100 min · Lab-style · MB2525**

### Roadmap

Students pull their Module 3 library down from the server, import sounds into an Ableton set, and edit them on the Arrangement timeline: clip start and end, fades, clip gain, duplicating and arranging. Warping is introduced here, at the moment a clip's tempo relationship first matters. (The library is already at 48 kHz, so it imports into the 48 kHz set with nothing to convert.)

### Handout

`lessons/02-handout-audio-editing.html` — Lab 1

### Manual (Live 11)

Arrangement View (audio portions); Clip View; Audio Clips, Tempo, and Warping.

---

## Session 3 · Mon Wk 11: Simpler and Drum Rack

**100 min · Lab 2 begins (Mon of the week) · MB2525**

### Roadmap

The one genuinely new abstraction of the module: **MIDI as a trigger**. Build the model carefully: a MIDI note is data (pitch, timing, velocity), a MIDI note triggers an instrument, the instrument makes the sound. Then the two sampler instruments. **Simpler** plays one sample across the keyboard, with a volume envelope (attack, decay, sustain, release) shaping each note. **Drum Rack** is a grid of pads, each pad one sample, each triggered by a MIDI note. Both are framed as ways to *play* the student's library rather than just arrange it.

### Handout

`lessons/03-handout-sampling-in-practice.html` — Lab 2. One document for the whole week: this Monday session works through the concept material (the trigger model, Simpler, Drum Rack), and Session 4 on Wednesday continues into the hands-on build.

### Manual (Live 11)

Simpler; Drum Racks; basic MIDI editing (Editing MIDI Notes and Velocities), enough to trigger.

---

## Session 4 · Wed Wk 11: Basic sampling in practice (Lab 2)

**100 min · Lab-style · MB2525**

### Roadmap

Hands-on with the Session 3 instruments. Students load their own library sounds into Simpler and a Drum Rack, draw or play a short MIDI part, and build one short playable idea from their own samples. The first time the library becomes an instrument rather than a folder.

### Handout

`lessons/03-handout-sampling-in-practice.html` — Lab 2. The same handout begun on Monday (Session 3); Wednesday continues into the hands-on build.

---

## Session 5 · Mon Wk 12: Basic mixing in Ableton

**100 min · Lab 3 begins (Mon of the week) · MB2525**

### Roadmap

The Ableton mixer as the **digital version of the Module 3 console**. Walk the mapping explicitly: track fader = channel fader, pan = pan, send to a return = aux send, group track = subgroup, Master track = master bus. Then the built-in devices that do the mixing work, the same effect types students met in Modules 2 and 3, now as Live devices. Insert effects sit in a track's chain and their order matters (Utility, EQ Eight, Auto Filter, Compressor, then the bus and master tools: Glue Compressor, Limiter, Multiband Dynamics). Send effects live on return tracks and are shared across tracks (Hybrid Reverb, Reverb, Delay, Echo), which is the aux-send mechanism from the Toft. Mixing is reframed as the same set of decisions students met on the Toft, now in software they can actually drive. Full locked list in Reference scope.

### Handout

`lessons/04-handout-mixing-in-practice.html` — Lab 3. One document for the whole week: this Monday session works through the mixer concepts, and Session 6 on Wednesday continues into committing to audio and mixing.

### Manual (Live 11)

Internal Routings; Mixing; Live Audio Effect Reference (locked insert + send set, see Reference scope).

### Connection to earlier modules

Two threads converge here: Module 2's EQ and compression (what these devices do) and Module 3's console architecture (how the routing is shaped). Name both. The console lecture in Module 3 was deliberately "what the desk is"; this is the first time students drive that architecture themselves.

---

## Session 6 · Wed Wk 12: Mixing in practice (Lab 3)

**100 min · Lab-style · MB2525**

### Roadmap

The Wednesday half of the mixing week. Students download a prepared multitrack session from the server, then commit it to audio before mixing: freeze and flatten the MIDI tracks, consolidate each track to one clip, so creation and mixing stay separate jobs. Then they mix: levels, pan, a shared reverb return, groups, and EQ and compression where they help. The prepared session keeps the time on mixing moves rather than setup.

### Handout

`lessons/04-handout-mixing-in-practice.html` — Lab 3. The same handout begun on Monday (Session 5); Wednesday continues into committing to audio and mixing.

---

## Session 7 · Mon Wk 13: Transferable concepts, through Adobe Audition

**100 min · Hands-on follow-along · MB2525** *(Mon only; Wed Wk 13 is Veterans Day.)*

### Roadmap

Step out of Ableton to show that the module's concepts belong to digital audio, not to one app. Adobe Audition is the worked example: its waveform editor and multitrack session hold the same ideas students have been using all module, under different names and a different UI. Frame Audition as an advanced audio editor in the Adobe suite, a hybrid: it has nondestructive editing and live processing like a DAW, but no instruments or MIDI, so it is not a DAW. That hybrid status is the point of using it as the transfer example, since the editing and processing concepts carry even into a tool that is not a full DAW. Walk sample rate, bit depth, editing, fades, EQ, compression, and multitrack in Audition's terms, each time pointing back to where they met it in Ableton or Audacity. The takeaway: the skills are portable; the next tool will look different and work the same. Pitched in part at the art majors, who already use the Adobe suite and will recognize Audition's place in it.

### Handout

`lessons/05-handout-transferable-concepts.html`

---

## End-of-module assessment

### What success looks like

Students at the end of Module 4 should be able to:

1. Set up an Ableton session and import audio from their own library
2. Edit clips nondestructively and warp where appropriate
3. Trigger a sampler instrument from MIDI and build a short playable idea
4. Mix a small session with faders, pan, sends, groups, EQ, and compression
5. Recognize the same concepts in a different tool (an advanced audio editor) and articulate that the skills transfer

### Forward promises and bridges

- **Sound Design bridge:** synthesis (oscillators, filters, envelopes, LFOs, the instruments left out of this module) is the entry point of Sound Design. Students who want to make sound from scratch rather than from recordings go to Sound Design next.

### What gets logged

After Module 4 ends, write a short retrospective: pacing, what worked, what the final-project drafts revealed about which skills stuck.

---

## What follows

The final project (Wks 14–15 + finals) turns the module's fluency into a piece. Beyond the course, Module 4's deliberate gap (synthesis) is the doorway to Sound Design: this module makes music from recorded sound, and Sound Design picks up where students make sound from scratch.
