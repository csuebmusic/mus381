# Final exam: cumulative

Instructor-facing. It has the exam and the answer key. Copy the exam section as the student handout, and keep the answer key for grading.

## Administration

- **When:** Finals week, in the slot set by the registrar's final-exam schedule (the exact date and time are on the syllabus). Separate from the final project, which is uploaded the same week.
- **Format:** Individual, in class, closed-book, no devices. Same conditions as the Wk 9 midterm.
- **Scope:** Cumulative, Modules 1 through 4, weighted toward Module 4 (the DAW). From Modules 1 through 3 it re-tests sample rate, clipping, and bit depth at export.
- **Total:** 60 points. Rescale to the final exam's weight in the syllabus.

### what each part tests

Every question has a sibling in the final review packet (`module-04-the-daw/lessons/06-handout-final-review.html`): the Module 4 vocabulary, plus sample rate, clipping, and bit depth at export. A new version stays inside what the packet covers. The four parts follow the midterm's format: define, identify from a description, trace or map, and short answer.

---

# MUS 381: final exam (cumulative)

Name: ___________________________     Date: ___________

Closed book. No devices. 60 points total.

## Part A: Define in plain language (16 points, 2 each)

Give a one or two sentence definition for each term.

1. Nondestructive editing
2. Clip (in Ableton)
3. Warping
4. MIDI note (say what data it carries)
5. Send and return track
6. Group track
7. Sample rate
8. Clipping

## Part B: Identify from a description (16 points, 4 each)

9. An Ableton Set has two ways of looking at the same music. One is a grid of small clips you can fire off and loop while you try ideas. The other is a left-to-right timeline where the music plays back in a fixed order. Name each view, and say which one you'd use to commit to a final arrangement.

10. You drop one of your library samples onto an instrument that plays it back across the whole keyboard: higher keys play it faster, lower keys slower, and each note has its own attack, decay, sustain, and release. Name that instrument. Then name the other sampler instrument from the module, the one that puts a different sample on each pad of a grid.

11. A producer wants a single reverb shared across four tracks rather than four separate copies. Describe the routing they would set up in Ableton: where the reverb goes, and what each of the four tracks uses to feed it. Then name the feature on our Module 3 Toft console that this is the digital version of.

12. Audacity records and edits audio, but by this course's definition it isn't a DAW. Name two things a DAW has that Audacity doesn't.

## Part C: Trace and map (14 points)

13. **(8 points)** Map the Ableton mixer onto the Module 3 Toft console. For each Ableton element below, name the console counterpart it corresponds to:
    - a track's fader
    - a track's pan control
    - a send to a return track
    - a group track
    - the Master track

14. **(6 points)** You're working with two sounds: a one-shot vocal sample, and a drum loop you want locked to your set's tempo. For each one, say whether you turn warp on or off, and why.

## Part D: Short answer (14 points)

15. **(4 points)** Explain nondestructive editing using the clip-and-file idea. When you shorten a clip or add a fade in Ableton, what happens to the underlying audio file, and why does that mean you can't ruin your source recording?

16. **(4 points)** Explain the beginner model of MIDI as a trigger. What does a MIDI note carry, what does it do, and what actually makes the sound the listener hears?

17. **(3 points)** Across the course you worked in Audacity, on the studio console, and in Ableton. Name two concepts that appear in all three, and explain what that means for the next audio tool you learn.

18. **(3 points)** Your library files are 48 kHz, 24-bit. Your Ableton Set runs at 48 kHz. When you import a library sound into the Set, what converts and what doesn't? At what bit depth do you export the finished piece?

---

# Answer key

Award full credit when the student conveys the idea, even if the wording differs. Spelling of terms isn't graded; using the right idea is.

## Part A (2 points each)

1. Edits are stored on the clip, not on the audio file. The file's samples are untouched, so any edit can be changed or undone and the source always survives. *(Full credit for "edits the clip, not the file.")*
2. A clip is a reference to audio (or to MIDI) with its own start, end, gain, fades, and warp settings. The clip points at the file; it isn't the file.
3. Warping is Ableton's time-stretching. Warp on stretches a clip to follow the set's tempo; warp off plays it back at its recorded speed. *(1 point for "time-stretch to the tempo," 1 for the on/off distinction.)*
4. A MIDI note is data, not sound: which pitch, when it happens, and how hard (velocity). It holds no audio itself.
5. A send routes a copy of a track's signal to a return track, which holds a shared effect (such as reverb). Many tracks feed the one effect.
6. A group track folds several tracks into one for combined level and processing. It's Ableton's version of a subgroup.
7. Sample rate is how many samples are taken per second, in Hz or kHz. The course standard is 48 kHz. *(1 point for "samples per second," 1 for the unit or the 48 kHz standard.)*
8. Clipping happens when a signal goes past the digital ceiling (0 dBFS) and its peaks are flattened off. Clipping in a recording can't be undone in editing. In a mix, the summed signal can also clip at the master; a Limiter at the end of the master chain keeps the export under the ceiling. *(Full credit for "past 0 dBFS, peaks flattened"; the recording-versus-mix distinction isn't required.)*

## Part B (4 points each)

9. **Session View** is the grid of clips, for trying ideas and looping. **Arrangement View** is the linear timeline. You commit to a final arrangement in **Arrangement View**. *(2 for naming both views correctly, 2 for picking Arrangement for the final structure.)*
10. **Simpler** plays one sample across the keyboard; in Classic mode each note has an attack-decay-sustain-release envelope. **Drum Rack** is the grid of pads, one sample per pad. *(2 each.)*
11. The reverb goes on a **return track**. Each of the four tracks turns up its **send** to that return, so all four feed the one reverb. On the Toft this is the **aux send and aux return** (the auxiliary send routing). *(2 for the return-plus-sends routing, 2 for naming the aux send/return on the console.)*
12. Any two of: instruments, MIDI, a full mixer. Audacity is an audio editor: it records and edits audio, and those are the parts it lacks. *(2 for each.)*

## Part C

13. **(8 points: 2 each for the send, the group track, and the Master track; 1 each for the fader and the pan)**
    - a track's fader = the **channel fader**
    - a track's pan = the channel **pan** control
    - a send to a return track = an **aux send** (to an aux / effects return)
    - a group track = a **subgroup** (the console's submaster)
    - the Master track = the **master bus** (master fader)
14. **(6 points)**
    - For the one-shot vocal sample, warp is **off**. Its original timing is the point; warping it to the grid would stretch and distort it. *(3 points.)*
    - For the drum loop locked to tempo, warp is **on**, so it follows the set's tempo and stays in time as the project tempo changes. *(3 points.)*

## Part D

15. **(4 points)** Shortening a clip or adding a fade changes the clip's instructions (its start, end, and fades), not the audio file underneath. The file's samples stay exactly as recorded, so you can always pull the clip's edge back out or remove the fade. You can't ruin the source because every edit is layered on top of a file that's never altered. *(Full credit for tying "edits are on the clip" to "the file is untouched, so it's recoverable.")*
16. **(4 points)** A MIDI note carries pitch, timing, and velocity (how hard). It doesn't make any sound on its own; it triggers an instrument, and the instrument is what produces the audio. The chain is note, then instrument, then sound. *(2 for what the note carries, 2 for "the instrument makes the sound.")*
17. **(3 points)** Any two of: sample rate, bit depth, gain staging, EQ, compression, fades, multitrack arrangement. They transfer because they're properties of digital audio and audio production, not of any one program. The next tool will look different and work the same, so what students learned is portable rather than tied to Ableton's buttons. *(2 for two transferable concepts, 1 for the portability point.)*
18. **(3 points)** The sample rate already matches (48 kHz library into a 48 kHz set), so nothing resamples on import. The only format change is bit depth, and it happens at export, not import. You export the finished piece at **32-bit** (48 kHz, 32-bit). *(2 for "rate matches, nothing resamples," 1 for "export at 32-bit.")*
