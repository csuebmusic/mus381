# Module 04 · the DAW

**Wks 10–15 · instruction Wks 10–13 (7 sessions), final project Wks 14–15 and finals**

---

## module purpose

Modules 2 and 3 used Audacity: students edited sound they were given (Module 2) and recorded their own (Module 3). Module 4 moves into Ableton Live, the course's DAW, and puts both skill sets to work in one program. Students load the sample library they built in Module 3 and make pieces from their own recorded material.

The module answers one beginner question: what is a DAW, and what can you do in it that a destructive audio editor like Audacity can't? Each session answers part of it. The arc:

the DAW environment (Session View and Arrangement View, the timeline, nondestructive editing) → audio editing in Ableton (import the library, edit and arrange clips, warp) → the sampler instruments (Simpler and Drum Rack), triggered from MIDI for the first time → a short playable idea built from library sounds → mixing in Ableton (the channel strip, sends and returns, group tracks, built-in EQ and dynamics) → one session in Adobe Audition, an audio editor, showing the same concepts in a different program → final project.

Three throughlines:

1. Nondestructive editing is the new mental model. Audacity edits the file: a cut removes samples, a fade rewrites them. Ableton edits a clip: the clip points at the audio file, and the edits (start, end, fades, warp, gain) are instructions stored on the clip. The source file doesn't change. This reframes everything students learned about editing in Module 2. Lead with it in Session 1 and come back to it every time a student is afraid of ruining a sample.

2. The student's library is the raw material. Labs 1 and 2 (Sessions 1–4), the Audition lab (Session 7), and the final project all use the student's own Module 3 sample library. Lab 3 (Sessions 5–6) uses a prepared session from the server. A student with a well-organized library moves fast in Labs 1 and 2; a student without one spends the time searching, so point them back to their naming and folders.

3. Concepts transfer; tools differ. The module teaches "a DAW" through Ableton, and Session 7 shows the same concepts in Adobe Audition under a different interface and different names. Sample rate, bit depth, gain staging, EQ, compression, fades, and multitrack arrangement exist in any audio program. Many students, the art majors especially, already use the Adobe suite and know where Audition belongs in it.

By the end of Wk 13, students should be able to set up an Ableton Set from scratch, import and warp audio from their library, build a short playable idea with a sampler instrument, mix it with the built-in devices, and name which of those skills apply in any DAW. Wks 14–15 turn that fluency into the final project.

---

## reference scope (Ableton Live 11 manual)

The lab runs **Ableton Live 11 Suite**. This module teaches the subset of Live listed below. These sections are the source of truth for drafting each week's lessons: menu paths and terminology match Live 11. Draft lessons against the manual, not from memory.

Module 4 pages don't embed Ableton screenshots. The reading and the labs run alongside a live instructor walk-through and link the version-pinned Live 11 manual sections, so students see the current interface in the app.

Ableton's [Learn Live](https://www.ableton.com/en/live/learn-live/) video library covers most of the topics below (sorted into Setup, Interface, Instruments & Effects, and Workflows) and is linked from the reading. Send students there for a second pass on a concept or when a manual page is dense. The videos show the current shipping version of Live (Live 12), so the interface may look newer than the lab's Live 11; for the concepts in this module the difference is cosmetic. Menu paths and terminology come from the Live 11 manual links.

Week 10 (the environment and audio editing):
- First Steps: https://www.ableton.com/en/live-manual/11/first-steps/
- Live Concepts: https://www.ableton.com/en/live-manual/11/live-concepts/
- Arrangement View, audio portions only (audio tracks and clips on the timeline; skip the MIDI-clip and Session View launch material, which comes in Wk 11 or stays out of scope): https://www.ableton.com/en/live-manual/11/arrangement-view/
- Clip View: https://www.ableton.com/en/live-manual/11/clip-view/
- Audio Clips, Tempo, and Warping: https://www.ableton.com/en/live-manual/11/audio-clips-tempo-and-warping/

Week 11 (sampling and MIDI as a trigger):
- Simpler: https://www.ableton.com/en/live-manual/11/live-instrument-reference/#simpler
- Drum Racks: https://www.ableton.com/en/live-manual/11/instrument-drum-and-effect-racks/#drum-racks
- Editing MIDI Notes and Velocities, scoped to drawing and editing notes: https://www.ableton.com/en/live-manual/11/editing-midi-notes-and-velocities/
- MIDI and Key Remote Control (connecting the MIDI keyboard): https://www.ableton.com/en/live-manual/11/midi-and-key-remote-control/
- Arming tracks: https://www.ableton.com/en/live-manual/11/recording-new-clips/#arming-record-enabling-tracks
- Monitoring, the track Monitor setting paired with arming a MIDI track to play the instrument (Live work in this module doesn't record audio): https://www.ableton.com/en/live-manual/11/routing-and-i-o/#monitoring

Week 12 (mixing):
- Track Freeze (freezing before flattening): https://www.ableton.com/en/live-manual/11/computer-audio-resources-and-strategies/
- Consolidate (Arrangement View): https://www.ableton.com/en/live-manual/11/arrangement-view/
- Internal Routings: https://www.ableton.com/en/live-manual/11/routing-and-i-o/#internal-routings
- Mixing: https://www.ableton.com/en/live-manual/11/mixing/
- Live Audio Effect Reference: https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/ . The locked effect set is the same effect types from Modules 2 and 3, now as Live devices, in two roles: inserts (in a track, group, or master chain, where order matters) and sends (shared on return tracks).

*Insert effects, by where they go (as handout 04 places them):*
- Utility, on every track, first in the chain: https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#utility
- EQ Eight, on a track, before Compressor: https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#eq-eight
- Compressor, on a track, after EQ Eight: https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#compressor
- Auto Filter, on a track, often at the end of the chain after the dynamics: https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#auto-filter
- Multiband Dynamics, on a single track when one band needs its own control (the de-esser): https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#multiband-dynamics
- Glue Compressor, on a group: https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#glue-compressor
- Limiter, on the master, last in the chain: https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#limiter

*Send effects (return A holds Reverb and return B holds Delay in the lab's default Set; Hybrid Reverb and Echo are the swaps):*
- Reverb: https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#reverb
- Hybrid Reverb: https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#hybrid-reverb
- Delay: https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#delay
- Echo: https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/#echo

Week 13 (Adobe Audition) is outside the Ableton manual. Audition runs on the lab Macs, so Session 7 is a hands-on lab (Lab 4, handout 05). The handout links three guides instead of the Live manual: Adobe's Get started with Adobe Audition, a beginner's walkthrough, and John Roach's Adobe Audition Beginners Guide (PDF).

Exporting is used across the module: Exporting Audio and Video, https://www.ableton.com/en/live-manual/11/managing-files-and-sets/#exporting-audio-and-video . Students export finished work at 48 kHz, 32-bit. They export in Labs 1, 2, and 3 and for the final project.

---

## learning outcomes

By the end of this module, students should be able to:

1. Describe the difference between Session View and Arrangement View and say which they'd reach for in a given situation
2. Explain nondestructive editing: a clip is a view of a file, and edits are instructions stored on the clip, with the source unchanged
3. Import audio from their own sample library into an Ableton Set and arrange it on the timeline
4. Use warping at a basic level: turn it on and off, understand that it maps a sample to the Set's tempo, and know when they want it and when they don't
5. Load a sample into Simpler and play it across a MIDI keyboard; load samples onto a Drum Rack and trigger them from pads
6. Explain the beginner-level model of MIDI: a MIDI note is data (which pitch, when, how hard) that triggers an instrument, and the instrument makes the sound
7. Mix a small session using Ableton's built-in tools: track faders, pan, sends to a return track, group tracks, and the built-in EQ and compressor
8. Map Ableton's mixer onto the console architecture from Module 3: track fader = channel fader, send = aux send, group track = subgroup (the Toft's submaster), Master track = master mix
9. Recognize the same core concepts (sample rate, bit depth, editing, EQ, dynamics, multitrack) in a different program (Adobe Audition, an audio editor) and explain that the concepts apply across programs

---

## concepts introduced

- A **DAW** (digital audio workstation) is one program that records, edits, arranges, and mixes sound and plays instruments: multitrack, nondestructive, with instruments, MIDI, and a built-in mixer. Audacity is an *audio editor*: it records and edits audio but has no instruments, no MIDI, and no full mixer. Ableton is the first DAW students meet. Define the term here and draw the line between audio editor and DAW explicitly, since students spent two modules in an audio editor. Don't call Audacity a DAW.
- **Session View and Arrangement View** are two views of one Set. Session View is the clip grid for trying ideas and launching loops; Arrangement View is the timeline, left to right, for committing to a structure. Students build in Arrangement View throughout the module (it resembles Audacity's timeline). Session View appears in the reading and Lab 1 as the clip grid (Tab switches views), and in Lab 3 as the view that shows the mixer. Students don't launch clips in this module; Lab 3 tells them to leave the empty clip slots alone.
- A **clip** is a reference to an audio file (or to MIDI), with its own start, end, gain, fades, and warp settings. It's the unit of work in Ableton. The clip isn't the file; it points at the file.
- **Nondestructive editing** means edits are stored on the clip, not in the source audio. Contrast it explicitly with Audacity, where edits rewrote samples. The reading pairs it with **live processing**, where an effect on a track processes the sound during playback and never changes the recording.
- **Warping** is Ableton's time-stretching. A warped clip follows the Set's tempo; warp markers pin moments in the audio to moments in the bar. At this level, warp on means "stretch to match the Set's tempo," and warp off means "play at the recorded speed." Warp on is for loops and rhythmic material students want locked to the grid; warp off is for one-shots and sounds where the original timing matters. Students leave the warp mode at its default.
- The sample rate stays the same, and the bit depth steps up at export. The Module 3 library is already 48 kHz and Module 4 Sets run at 48 kHz, so library files import with nothing to convert. Students export at 32-bit, up from the 24-bit they worked in through Modules 2–3. The bit depth for a deliverable is set at export.
- **MIDI** (beginner model) is data, not sound. A MIDI note has pitch, timing, and velocity (how hard). The note triggers an instrument; the instrument makes the audio. "The piano roll says play C3 now, medium-hard; Simpler turns that into the sound of your sample at that pitch." Students first use MIDI as a *trigger* for the sampler instruments, and they sequence by drawing notes, not by recording a performance. Lab 2 explains the 0 to 127 range of velocity and pitch (middle C is note 60, labeled C3 in Live).
- **Simpler** is an instrument that plays one sample across the keyboard. A MIDI note picks the pitch; the sample plays back faster (higher) or slower (lower), with C3 as the root key. Students use two of its modes. Classic holds the note while the key is down and has the volume envelope (attack, decay, sustain, release). One-Shot plays the whole sample on every press and replaces the envelope with Fade In and Fade Out. Slicing mode is left for later.
- A **Drum Rack** is a grid of pads, each pad holding one sample and triggered by its own MIDI note (the bottom-left pad is C1). Each filled pad is a Simpler. Students build a kit from their own library sounds and sequence it.
- **The Ableton mixer** has track faders, pan, sends, return tracks, group tracks, and the Master track. Introduce it as the software version of the Module 3 console: the same channel-strip, aux, subgroup, and master layout.
- A **send** routes a copy of a track's signal to a **return track**, where an effect (reverb, delay) is loaded. One reverb takes signal from many tracks. It's the aux-send mechanism from the Toft, now in Ableton; name the connection explicitly.
- **Group tracks** fold several tracks into one channel for combined level and processing. A group track is Ableton's subgroup, the console's subgroup strip (the Toft labels its subgroups submasters).
- **Bouncing** prints what a track plays into a fixed audio file. In Lab 3 students bounce each MIDI track in two steps: Freeze Track (reversible), then Flatten (permanent). They do it on a separate mixing copy of the Set, so the original keeps its notes and instruments.
- **Built-in devices** are the same effect types from Modules 2 and 3, now as Live devices, in two roles. Insert effects go in a track, group, or master chain, where order matters. Send effects are loaded on return tracks and shared across tracks. Map each onto the EQ and dynamics from Module 2 and the aux-send architecture from Module 3. The locked list, with where each insert goes, is in reference scope.
- **Transferable concepts** (the Audition session) are sample rate, bit depth, gain staging, fades, EQ, compression, and multitrack arrangement. These are properties of digital audio and audio production, not of Ableton. Audition is the worked example of the same concepts in a different program.

---

## deliverable: final project

**Wks 14–15 and finals.**

Built: [final project](https://csuebmusic.github.io/mus381/module-04-the-daw/projects/final-project.html) (`projects/final-project.html`).

- The prompt is open: any kind of piece (arranged audio clips, sampler-driven, or both) that demonstrates fluency with the semester's skills, built in Ableton Live.
- The piece is 2 to 3 minutes long.
- Every sound must be student-recorded: the Module 3 library plus anything new they record. No pre-recorded, found, or downloaded sound, and no pre-made loops. One exception: a student may use another student's recording *with permission* and must credit it. Credits go in `lastname-final-credits.txt` in the working folder; if every sound is their own, the file says so.
- Students start the project Set in Session 1, following the end of the reading: a folder named `final` inside `~/Documents/netid/`, holding a Live Set named `lastname-final-v1`. They save versions as they go (`lastname-final-v1`, `v2`, `v3`). Labs 1–3 each end with a "before class ends: your project" block for adding the day's work to it. The project page tells students to start in Wk 12 at the latest.
- Draft 1 is due Wed Wk 14: a complete rough pass, end to end, even if it's unmixed. Students submit it to their working folder, and you give written feedback. There's no in-class listening for drafts.
- Draft 2 is due Wed Wk 15: the revision, after acting on the Draft 1 feedback.
- The final version is due during finals week (the exact date is on Canvas). The WAV is 48 kHz, 32-bit, named `lastname-final.wav`. The server folder `final/` holds the master copy of the `.als` Set, all version saves, recordings, the credits file, and the final WAV; a copy of the WAV also goes in `/public/mus-381-fall-2026/final-pieces/` for the class.
- The rubric is out of 100, with no revision criterion: technique & tools 35, form & shape 30, sound material & sourcing 20, mix & craft 15. Style, genre, and where the length falls within 2 to 3 minutes aren't graded.
- A cumulative final exam runs during finals week (it covers the whole course), separate from this project. Exam and answer key: [`exams/final-exam.md`](../exams/final-exam.md) *(TA-facing)*.

### final review packet

[final review](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/06-handout-final-review.html) (`lessons/06-handout-final-review.html`)

A take-home study packet for the cumulative final, parallel to the Module 3 midterm review. It gathers the Module 4 vocabulary in ten sections (what a DAW is, the two views, the clip and nondestructive editing, warping, MIDI as a trigger, the sampler instruments, the Ableton mixer as the digital console, inserts and sends with the insert chain order, concepts that apply across tools, and library to finished piece), with the three cross-course anchors the final still tests (sample rate, clipping, bit depth at export) in section 9. It closes with a test-yourself list that mirrors the exam's question style. Hand it out at the last class meeting (Wed Wk 15) for study before the finals-week exam; it's on the course site throughout. The exam (`exams/final-exam.md`) stays inside what this packet covers, the way the midterm matches its review handout.

---

## listening assignment

[listening: sampling](https://csuebmusic.github.io/mus381/module-04-the-daw/listening/historical.html) (`listening/historical.html`)

Module 4 has one historical listening assignment, on sampling: building music from recorded sound, from musique concrète through turntables, the MPC, and the DAW. The page ties back to Module 2's musique concrète listening (the same idea on tape) and to the Wk 11 sampling lab. Students listen to four pieces: Grandmaster Flash (1981), DJ Shadow (1996), The Avalanches (2000), and J Dilla (2006), plus one sampling piece of their choice from the last 20 years. They answer four questions, the last asking for one concrete thing they want to try in their final project. The page has two photos (Grandmaster Flash at the turntables, an Akai MPC60) and a lineage timeline SVG.

It's due Mon Wk 13, before class, on Canvas: `lastname-listening-04.docx` (or PDF), about 250 to 350 words. It's the last historical listening assignment of the course.

Module 4 has no peer listening. Final pieces go in the class folder for everyone to hear, with no written response assignment.

---

## student-facing materials

- [into the DAW](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/01-reading-the-daw-environment.html) (`lessons/01-reading-the-daw-environment.html`), the module reading
- [audio editing in Ableton](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/02-handout-audio-editing.html) (`lessons/02-handout-audio-editing.html`), Lab 1
- [sampling in Ableton](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/03-handout-sampling-in-practice.html) (`lessons/03-handout-sampling-in-practice.html`), Lab 2
- [mixing in Ableton](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/04-handout-mixing-in-practice.html) (`lessons/04-handout-mixing-in-practice.html`), Lab 3
- [Adobe Audition](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/05-handout-transferable-concepts.html) (`lessons/05-handout-transferable-concepts.html`), Lab 4
- [final review](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/06-handout-final-review.html) (`lessons/06-handout-final-review.html`)
- [listening: sampling](https://csuebmusic.github.io/mus381/module-04-the-daw/listening/historical.html) (`listening/historical.html`)
- [final project](https://csuebmusic.github.io/mus381/module-04-the-daw/projects/final-project.html) (`projects/final-project.html`)

---

## session overview

The module reading (`01-reading-the-daw-environment.html`) opens Monday of Wk 10 as the map of the module, and the class refers back to it all module. After it, each week runs on one handout. The three Ableton lab handouts (`02` audio editing, `03` sampling, `04` mixing) each run a full week, Monday and Wednesday: you work through the handout while students follow hands-on. Wks 11 and 12 have no separate Monday lecture document. Wk 13 is a Monday-only Audition lab (Lab 4, `05-handout-transferable-concepts.html`); there's no Wednesday class (Veterans Day). Handout `06` is the take-home final review packet, not a session document.

| Wk | Day | Focus |
|---|---|---|
| 10 | Mon | Session 1 · Reading (the module map), then begin Lab 1 (handout 02). What a DAW is, Session View and Arrangement View, the clip, nondestructive editing. Students create their final-project Set (`lastname-final-v1`). |
| 10 | Wed | Session 2 · Lab 1 continues (handout 02). Import the library, place clips on the Arrangement timeline, clip edits (start and end, gain, fades), a 30-second arrangement, warping in a second version, export. |
| 11 | Mon | Session 3 · Begin Lab 2 (handout 03). Connect the MIDI keyboard. MIDI as a trigger: a MIDI note triggers an instrument; the instrument makes the sound. Simpler plays one sample across the keyboard; a Drum Rack is a grid of one-sample pads. |
| 11 | Wed | Session 4 · Lab 2 continues (handout 03). Build a Drum Rack kit from library sounds, sequence a short part by drawing notes, build one short playable idea from the student's own samples, export. |
| 12 | Mon | Session 5 · Begin Lab 3 (handout 04). The Ableton mixer as the digital console: track faders, pan, sends and return tracks, group tracks, the Master. Inserts and sends mapped onto Module 2 and the Module 3 console. |
| 12 | Wed | Session 6 · Lab 3 continues (handout 04). Bounce the prepared session to audio (freeze and flatten the MIDI tracks, consolidate), then mix: levels, pan, groups, inserts, reverb and delay sends, export. |
| 13 | Mon | Session 7 · Lab 4, Adobe Audition (handout 05). *(Mon only; no class Wed, Veterans Day.)* The same concepts in a different program: editing, fades, noise reduction, multitrack levels and pan, EQ, sample rate and bit depth, under Audition's interface and names. Module 4 listening due before class. |
| 14 | Mon / Wed | Final project worktime; Draft 1 due Wed Wk 14. |
| 15 | Mon / Wed | Final project revision; Draft 2 due Wed Wk 15. Final review packet (handout 06) handed out for the finals-week exam. |
| Finals | | Final piece to the server and the class folder; cumulative final exam. |

Block-by-block facilitation, demo scripts, and pacing fallbacks for each session aren't written yet.

---

## pre-module preparation (Inés / TA)

- Check the Ableton install. The lab version is **Ableton Live 11 Suite**. Menu paths and manual links on the pages all target Live 11 (see reference scope above for the exact sections). Simpler and Drum Rack are in every edition.
- Check the lab's default Live Set. A new Set opens with two audio tracks, two MIDI tracks, and two return tracks, with Reverb on return A and Delay on return B. Handouts 02 to 04 assume this layout.
- Inventory and test the MIDI keyboards at every station before Wk 11. Confirm each one is present, connects over USB through the station hub, shows in full color in Audio MIDI Setup's MIDI Studio, and appears in Live's Link, Tempo & MIDI preferences. Lab keyboards don't auto-arm: students turn on the keyboard's **Track** switch in those preferences and arm the MIDI track.
- Install and test Adobe Audition on the lab Macs before Wk 13. Audition runs at every station, so Session 7 is hands-on. Confirm it launches under the campus Adobe license.
- Stage the files for Labs 3 and 4 in `/public/module-04/` before Wk 12. Session 6 uses a prepared session: a longer piece with several instruments, some played from MIDI and some recorded as audio, so there are MIDI tracks to bounce and clips to consolidate. Inés provides it. The noise recording for the Wk 13 Audition lab goes in the same folder.
- Be ready for the final-project Set. Students create it in Session 1, following the end of the reading: a folder named `final` inside `~/Documents/netid/`, and a Live Set saved in it as `lastname-final-v1`. Nothing to pre-stage; help with the create-and-save step on the day.
- Check library readiness before Wk 10. Sessions 1 through 4 and Session 7 assume each student has a usable Module 3 library in `sample-library/` in their own server folder. Spot-check that the libraries are there and findable after the midterm.

---

## module-wide concerns

### recurring confusions to expect across the module

- Students expect Audacity behavior (edits change the file) and are surprised or worried that Ableton edits can be undone. Tell them that's the point: the source is always safe, so they can experiment.
- Students turn warp on when they wanted it off (a one-shot stretched to the grid sounds wrong) or off when they wanted it on (a loop drifting out of time). Give them the rule of thumb from Lab 1: loops want warp, one-shots don't.
- Students confuse MIDI and audio tracks: they drop a sample on an audio track expecting to play it as an instrument, or try to draw notes on an audio track. The trigger model (note → instrument → sound) is the fix, and instruments go on MIDI tracks.
- Students put a reverb directly on a track (insert) when they meant to share one reverb across tracks (send to a return). It maps to the aux-versus-insert distinction from Module 3.

### gear for each session

The reading has no gear callout. Each lab handout lists the gear to take from the lab's gear storage:

- Lab 1 (Sessions 1–2) uses an audio interface and headphones.
- Lab 2 (Sessions 3–4) uses an audio interface, headphones, and a MIDI keyboard. The keyboard plugs into the USB hub at the station.
- Lab 3 (Sessions 5–6) uses an audio interface and headphones. The MIDI keyboard stays in storage.
- Lab 4 (Session 7) uses an audio interface and headphones.

No session in this module uses a mic or XLR cable. In Wk 11, confirm each MIDI keyboard registers in Live before the room fills.

### pacing across the module

Plan for **Session 3 → 4** (MIDI as a trigger). MIDI is the one new abstraction in a module otherwise built on familiar material (audio, editing, mixing). Plan the Monday (Session 3) so students can state the note → instrument → sound chain before they build with it on Wednesday; the Wednesday build depends on it.

Keep **Session 7 (Audition)** on the concepts, not on Audition's feature set. The message is "you already know this; here it is under different names."

### when to escalate to Inés

Same as Modules 2 and 3.

---

## Session 1 · Mon Wk 10: the DAW environment, through Ableton

**100 min · reading, then Lab 1 begins · MB2525**

### roadmap

The module's framing question: what is a DAW, and what's new about it after two modules in an audio editor (Audacity)? The reading covers what a DAW is, a short history from tape to the DAW, nondestructive editing, live processing, MIDI, and the DAWs students are likely to meet. It ends by walking students through creating the final-project Set (`final` folder, `lastname-final-v1`). Students should leave able to say what a clip is and why editing one doesn't touch the underlying file. After the reading, the session moves into Lab 1 (handout 02); Wednesday continues it.

The reading has start-of-session download and end-of-session upload callouts and no gear callout. Lab 1's gear (audio interface, headphones) comes out when the lab begins.

### reading

[into the DAW](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/01-reading-the-daw-environment.html) (`lessons/01-reading-the-daw-environment.html`)

### manual (Live 11)

First Steps; Live Concepts.

### connection to earlier modules

Module 2 taught editing as something you do *to a file*. This reading reframes editing as something you do *to a clip*, with the file untouched underneath. Say out loud that they can't ruin their source: beginners edit timidly, and nondestructive editing lets them experiment.

---

## Session 2 · Wed Wk 10: audio editing in Ableton (Lab 1)

**100 min · lab · MB2525**

### roadmap

Lab 1 sets up Live (the lab interface as Live's audio device, ins and outs), then students download their `sample-library/` from the server, add it to Live's browser, and drag four to six sounds onto audio tracks in Arrangement View. They edit clips in Clip View (start and end, clip gain, fades), arrange three or more sounds into about thirty seconds, and save as `lastname-wk10-v1`. They save a copy as `lastname-wk10-v2` and do all warping there (warp on for a loop, off for a one-shot, mode left at default). The library is already 48 kHz, so it imports into the 48 kHz Set with nothing to convert. They export `lastname-wk10-edit.wav` at 48 kHz, 32-bit, run **Collect All and Save**, and upload both Project folders and the WAV.

Watch for:
- In Live's audio device list, the Behringer UM2 shows as USB Audio CODEC and the PreSonus AudioBox as AudioBox USB 96.
- If a student hears nothing, the handout's check is Live's audio device, headphones in the interface (not the Mac), and the interface headphone level.
- Live opens in Session View. Tab switches to Arrangement View and brings the timeline back.

### handout

[audio editing in Ableton](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/02-handout-audio-editing.html) (`lessons/02-handout-audio-editing.html`), Lab 1

### manual (Live 11)

Arrangement View (audio portions); Clip View; Audio Clips, Tempo, and Warping; Exporting Audio and Video.

---

## Session 3 · Mon Wk 11: Simpler and Drum Rack

**100 min · Lab 2 begins · MB2525**

### roadmap

This is the module's one new abstraction: **MIDI as a trigger**. Build the model carefully: a MIDI note is data (pitch, timing, velocity), a MIDI note triggers an instrument, and the instrument makes the sound. Students start a Set named `lastname-wk11` and connect the MIDI keyboard: check it in Audio MIDI Setup's MIDI Studio (Cmd-2), then turn on its **Track** switch in Live's Preferences under Link, Tempo & MIDI. Then the two sampler instruments, on MIDI tracks. **Simpler** plays one sample across the keyboard; students try Classic mode (the ADSR envelope) and One-Shot mode (Fade In and Fade Out). A **Drum Rack** is a grid of pads, each pad one sample (a Simpler), each triggered by a MIDI note. Frame both as ways to *play* the student's library, not only arrange it.

Watch for:
- A silent keyboard: check the Track switch in preferences, the track's **Arm** button (lab keyboards don't auto-arm), and the track's Monitor setting (Auto, not Off).
- A keyboard row shown in red in Live's MIDI Ports list means Live can't reach it; reseat the USB cable and check MIDI Studio.
- Simpler's root is C3; a sample may sound higher or lower than students expect. Transpose shifts the mapping.

### handout

[sampling in Ableton](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/03-handout-sampling-in-practice.html) (`lessons/03-handout-sampling-in-practice.html`), Lab 2. One document for the whole week: this Monday session works through the keyboard setup and the concept material (the trigger model, Simpler, Drum Rack), and Session 4 continues into the hands-on build.

### manual (Live 11)

MIDI and Key Remote Control; Simpler; Arming tracks; Monitoring; Drum Racks; Editing MIDI Notes and Velocities (drawing and editing notes, enough to trigger).

---

## Session 4 · Wed Wk 11: sampling in practice (Lab 2)

**100 min · lab · MB2525**

### roadmap

Hands-on with the Session 3 instruments. Students load their own library sounds into Simpler and a Drum Rack (three or four pads), make a MIDI clip, and sequence a short part by drawing notes in the MIDI Note Editor (Draw Mode, B). The keyboard is for hearing the instrument; students don't record MIDI. They vary velocity in the lane under the notes. They build one short playable idea, about fifteen to thirty seconds, from their own samples, export `lastname-wk11-idea.wav` at 48 kHz, 32-bit, run **Collect All and Save**, and upload. This is the first time the library is played as an instrument.

A fresh MIDI clip opens with Loop on, so dragging its edge repeats the content. Students turn Loop off to resize the clip, draw the part, then turn Loop back on and set the loop brace.

### handout

[sampling in Ableton](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/03-handout-sampling-in-practice.html) (`lessons/03-handout-sampling-in-practice.html`), Lab 2. The same handout begun on Monday (Session 3); Wednesday continues into the hands-on build.

---

## Session 5 · Mon Wk 12: mixing in Ableton

**100 min · Lab 3 begins · MB2525**

### roadmap

The Ableton mixer as the **digital version of the Module 3 console**. Walk the mapping explicitly: track fader = channel fader, pan = pan, send to a return = aux send, group track = subgroup (the Toft's submaster), Master track = master mix. Then the built-in devices, the same effect types students met in Modules 2 and 3, now as Live devices. Insert effects go in a chain and their order matters: Utility on every track, EQ Eight before Compressor on a track, Auto Filter often at the end, Multiband Dynamics when one band needs control (the de-esser), Glue Compressor on a group (Ableton's version of the SSL bus compressor from the Module 3 studio), and a Limiter last on the master. Send effects are loaded on return tracks and shared across tracks: return A holds Reverb (Hybrid Reverb is the swap) and return B holds Delay (Echo is the swap). That's the aux-send mechanism from the Toft. The full locked list is in reference scope.

Lab 3 has no videos; the manual pages linked at each step are the reference. Students leave the MIDI keyboard in storage.

### handout

[mixing in Ableton](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/04-handout-mixing-in-practice.html) (`lessons/04-handout-mixing-in-practice.html`), Lab 3. One document for the whole week: this Monday session works through the mixer concepts, and Session 6 continues into bouncing to audio and mixing.

### manual (Live 11)

Internal Routings; Mixing; Live Audio Effect Reference (the locked insert and send set; see reference scope).

### connection to earlier modules

Module 2's EQ and compression (what these devices do) and Module 3's console architecture (how the routing is laid out) both apply here. Name both.

---

## Session 6 · Wed Wk 12: mixing in practice (Lab 3)

**100 min · lab · MB2525**

### roadmap

The Wednesday half of the mixing week. Students copy the prepared session's project folder from `/public/module-04/` into `~/Documents/netid/`, open it, and listen once through before changing anything. They save the original, then **Save As** `lastname-wk12-mix` and work only in that copy. They bounce each MIDI track to audio (right-click, **Freeze Track**, then **Edit → Flatten**) and consolidate every track into one clip (Cmd-A, Cmd-J). Then they mix in Session View (Tab): levels first, pan (kick and bass centered), a group with Cmd-G, inserts where they hear the need (EQ Eight, Compressor, Glue Compressor on a group, Limiter on the master), and Send A (reverb) and Send B (delay). They export `lastname-wk12-mix.wav` at 48 kHz, 32-bit, run **Collect All and Save**, and upload.

Watch for:
- Flatten is permanent and there's no unflatten. Check students are in `lastname-wk12-mix` before they flatten; the original Set keeps every note and instrument.
- Students who run short on time set levels and a little pan, export that, and upload.

### handout

[mixing in Ableton](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/04-handout-mixing-in-practice.html) (`lessons/04-handout-mixing-in-practice.html`), Lab 3. The same handout begun on Monday (Session 5); Wednesday continues into bouncing to audio and mixing.

### manual (Live 11)

Track Freeze; Consolidate; Mixing; the device pages for EQ Eight, Compressor, Glue Compressor, Limiter, Reverb, Hybrid Reverb, Delay, Echo, Utility, Auto Filter, and Multiband Dynamics.

---

## Session 7 · Mon Wk 13: Adobe Audition (Lab 4)

**100 min · lab · MB2525** *(Mon only; no class Wed Wk 13, Veterans Day.)*

### roadmap

Step out of Ableton to show that the module's concepts belong to digital audio, not to one program. Adobe Audition is the worked example. It has two editors: the Waveform Editor edits one file destructively, like Audacity, and the Multitrack Editor edits clips nondestructively, like Ableton. Audition has nondestructive editing and live effects but no instruments or MIDI, so by this course's definition it's an audio editor, not a DAW.

Students follow handout 05 hands-on:
1. Make a multitrack session at 48000 Hz, 32-bit, saved in its own folder in `~/Documents/netid/` (Audition saves a `.sesx` file).
2. Download a handful of library sounds into the session folder and import them.
3. In the Waveform Editor, delete a selection and add fades with the fade handles.
4. Download the noise recording from `/public/module-04/`, capture a noise print, and apply Noise Reduction at about 70 to 80 percent (past about 90 percent the sound turns hollow). It's the same two-step move as the noise profile in their Audacity sample-prep pipeline.
5. Try the Spectral Frequency Display: select a bright shape and delete it or use Auto Heal (four seconds or less).
6. In the Multitrack Editor, set levels and pan and add a Parametric Equalizer from the Effects Rack. Optionally try clip stretching: Varispeed links pitch and duration, like Audacity's Change Speed and Pitch; the other stretch types hold pitch, like Ableton's warp.
7. Export a multitrack mixdown as WAV, 48 kHz, 32-bit, and upload the working folder.

Nothing in this session is graded or submitted. As you walk through each step, point back to where students met the concept in Ableton or Audacity.

### handout

[Adobe Audition](https://csuebmusic.github.io/mus381/module-04-the-daw/lessons/05-handout-transferable-concepts.html) (`lessons/05-handout-transferable-concepts.html`), Lab 4

---

## end-of-module assessment

### what success looks like

Students at the end of Module 4 should be able to:

1. Set up an Ableton Set and import audio from their own library
2. Edit clips nondestructively and warp where appropriate
3. Trigger a sampler instrument from MIDI and build a short playable idea
4. Mix a small session with faders, pan, sends, groups, EQ, and compression
5. Recognize the same concepts in a different program (an audio editor) and explain that the skills transfer

### bridge to Sound Design

Synthesis (oscillators, filters, envelopes, LFOs, the instruments this module leaves out) is the entry point of Sound Design. Students who want to make sound from scratch, not from recordings, take Sound Design next.

### what gets logged

After Module 4 ends, write a short retrospective: pacing, what worked, and what the final-project drafts showed about which skills stuck.

---

## what follows

The final project (Wks 14–15 and finals) turns the module's fluency into a piece. Beyond the course, synthesis, which Module 4 leaves out, is where Sound Design begins: this module makes music from recorded sound, and Sound Design makes sound from scratch.
