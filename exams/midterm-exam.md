# Terminology exam: Module 3 midterm

TA-facing. Contains the exam and the answer key. The exam section can be copied as the student handout; keep the answer key for grading.

## Administration

- **When:** Wed Wk 9, the second part of the session, after the sample libraries are submitted and verified (Part 1, roughly the first 30 minutes). Students have the rest of the 100-minute period, roughly an hour.
- **Format:** Individual, in class, closed-book, no devices.
- **Scope:** Cumulative, Modules 1 through 3. Everything on it comes from the midterm review packet (`lessons/09-handout-midterm-review.html`), which students were given as the study guide. Do not test terms or ideas the guide does not cover.
- **Total:** 50 points. Rescale to the gradebook weight as needed; the syllabus sets the midterm at 20%.

### How this exam maps to the guide

The guide tells students to expect three kinds of thinking, and this exam is built on them, with a fourth part drawn from the guide's "Test yourself" self-check.

- **Part A: Define in plain language.** The guide's first thinking type.
- **Part B: Identify from a description.** The guide's second thinking type, including the signal-level-and-cable matching the guide flags as "one of the most testable ideas in this module."
- **Part C: Trace a signal flow.** The guide's third thinking type. Part C1 is the voice-to-WAV trace from the self-check.
- **Part D: Short answer.** The why/how questions the self-check primed (noise floor, balanced cable, clipping, the prep pipeline).

Every question is a sibling of something in the guide, written fresh so it is not a verbatim copy of the self-check. If a future version is needed, keep it inside the guide's ten term clusters and these four parts so students still get what they studied for.

---

# MUS 381: Midterm Terminology Exam

Name: ___________________________     Date: ___________

Closed book. No devices. 50 points total.

## Part A: Define in plain language (18 points, 2 each)

Give a one or two sentence definition for each term.

1. The session workflow
2. Sample rate
3. Nyquist theorem
4. Crossfade
5. Transient
6. Transducer
7. Cardioid
8. Unity gain
9. Timbre (use the words *fundamental* and *partial* in your answer)

## Part B: Identify from a description (12 points)

10. **(6 points)** You are handed three things: a synth, an electric guitar, and a vocal mic. For each one, name the signal level it puts out and the cable that carries it.

11. **(2 points)** A microphone captures fine detail and needs a 48-volt supply before it will work at all. What type of microphone is it, and what is that supply called?

12. **(2 points)** An audio interface holds two converters. One runs while you record, the other while you play back. Name each by its abbreviation and say which direction it runs.

13. **(2 points)** On the mixer, a bus groups several channels into a sub-mix with its own fader before that mix goes into the master. What is this called? Give the term our Toft console uses.

## Part C: Trace a signal flow (12 points)

14. **(10 points)** Trace the signal flow from a singer's voice to a WAV file on the computer. Name every stage, and the cable or conversion between stages.

15. **(2 points)** Now continue the path the other way: how does that WAV file get back out to the singer's headphones? Name the conversion involved and the direction it runs.

## Part D: Short answer (8 points, 2 each)

16. Why does a 16-bit recording have a higher noise floor than a 24-bit one? What sets that floor?
17. Explain how a balanced cable rejects noise. What property of its two signal copies makes this work?
18. A recording clips. Can you fix it in editing? Why or why not?
19. Name the three steps of the sample prep pipeline, in order, and say what each one fixes.

---

# Answer key

Award full credit when the student conveys the idea, even if the wording differs from the guide. Spelling of terms is not graded; using the right idea is.

## Part A (2 points each)

1. **The session workflow.** Download your folder from the server at the start of a session, work locally on the Mac, upload it back to the server at the end. Keeps the master copy current and protects work if a lab Mac is wiped. *(Full credit for the download/work-local/upload pattern.)*
2. **Sample rate.** How many samples are taken per second, in Hz or kHz. Common rates are 44.1 kHz (CD) and 48 kHz (the course standard). *(1 point for "samples per second," 1 for the unit or naming a standard rate.)*
3. **Nyquist theorem.** You must sample at twice the highest frequency you want to capture. This is why 44.1 kHz covers human hearing. *(Full credit for the "twice the highest frequency" idea.)*
4. **Crossfade.** An overlapping fade-out and fade-in: one sound fades out as another fades in, so the seam blends instead of jumping.
5. **Transient.** The brief, sharp burst at the start of a note or hit, before the body settles (a drum strike, a string pluck, a spoken consonant). Carries much of a sound's character.
6. **Transducer.** A device that converts one kind of energy into another. A microphone turns air pressure into voltage; a speaker does the reverse.
7. **Cardioid.** A polar pattern most sensitive in front, less at the sides, rejecting sound from behind. The pattern of most dynamic mics, including the lab's.
8. **Unity gain.** The fader or knob position where signal passes through unchanged, marked 0 dB. Above it boosts, below it reduces.
9. **Timbre.** The quality that lets you tell a violin from a flute at the same pitch. Set by which **partials** are present and how strong each is, built on the **fundamental** (the lowest partial, heard as the pitch). *(Both words must be used correctly for full credit.)*

## Part B

10. **(6 points, 2 per item: 1 for the level, 1 for the cable.)**
    - **Synth:** line level; carried on TRS or XLR (balanced), or RCA (unbalanced consumer).
    - **Electric guitar:** instrument level; carried on TS (unbalanced).
    - **Vocal mic:** mic level; carried on XLR (balanced).
11. **(2 points)** A **condenser** microphone. The supply is **phantom power** (+48V). *(1 point each.)*
12. **(2 points)** **ADC** (analog-to-digital, runs while recording) and **DAC** (digital-to-analog, runs while playing back). *(1 point per converter, named with its direction.)*
13. **(2 points)** A **subgroup**, which our Toft console labels a **submaster**. *(Either term earns full credit; "submaster" is the console's label.)*

## Part C

14. **(10 points)** A complete trace names each stage and what connects them. Award up to 10 across the stages below (roughly 1.5 each; full credit for naming the stages and the conversions in order):
    1. The voice: acoustic pressure in the air.
    2. The **microphone**, a transducer, turns that pressure into a weak **mic-level** signal.
    3. A balanced **XLR cable** carries the signal to the interface.
    4. Inside the **audio interface**, the **preamp** lifts the mic-level signal toward line level (set with the gain knob).
    5. The **ADC** converts the analog signal into digital **samples**, at the set **sample rate** and **bit depth**.
    6. A **USB cable** carries the digital data (the stream of numbers, not analog audio) to the computer.
    7. The **computer** stores those samples as a **WAV file**.
15. **(2 points)** The computer sends the samples to the **DAC**, which converts them from digital back to an **analog** signal for the headphones. Direction: **digital to analog**. *(1 point for naming the DAC, 1 for the digital-to-analog direction.)*

## Part D (2 points each)

16. **Noise floor, 16-bit vs 24-bit.** Bit depth sets the noise floor, roughly 6 dB of range per bit (so 16-bit gives about 96 dB). Fewer bits means coarser quantization, so the quantization noise sits louder relative to the signal. 24-bit has more bits, a lower floor, and more headroom for quiet detail. *(Full credit for tying the floor to bit depth and quantization.)*
17. **Balanced cable.** It carries two opposite-polarity copies of the signal. Noise picked up along the run lands on both copies the same way (in phase). At the far end one copy is flipped and summed with the other: the signal doubles and the noise cancels. **Phase** (the opposite polarity of the two copies) is the property that makes it work.
18. **Clipping.** No, it cannot be fixed in editing. Clipping happens at capture when the signal exceeds the digital ceiling (0 dBFS) and the peaks are flattened off. That information is gone, so there is nothing to restore. Prevent it with gain and headroom while recording. *(Full credit for "unrecoverable because the peaks were lost at capture.")*
19. **Sample prep pipeline, in order:**
    1. **Denoise**, using a captured silence sample, to remove background hiss and hum.
    2. **Trim** the silence at the start and end, to tighten the sample.
    3. **Peak-normalize** to a consistent ceiling, so every sample in the library sits at a uniform level.
    *(1 point for the correct order, 1 for what the steps fix. Full credit needs all three in order.)*
