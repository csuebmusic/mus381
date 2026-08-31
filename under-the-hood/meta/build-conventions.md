# Build conventions

Naming, chrome, dates, and the visual system for this repo.

> **For Inés and Claude only.** The TA does not need to read this. These are scaffolding for building the course, not part of teaching it.

Prose and register rules live in Inés's profile instructions, not here.

Per-asset specs (what each hand-produced audio file or image is, and how to recreate or substitute it) live in [`assets/asset-recipes.md`](../../assets/asset-recipes.md). Page skeletons live in [`templates/`](./templates/README.md); copy one as the starting point for a new page.

Internal docs (module READMEs, TA notes, this file) record state and rules rather than deliberation: the decision, the rule, the current status, the open question. Process belongs in chat with Inés and nowhere else.


---

## Naming

> **Scope:** the whole repo, including student-facing material on the class server. File paths show up in handouts, in transfer instructions, and on the projector.

### The base rule

Lowercase. Hyphens, not spaces. No special characters (no `&`, `!`, `@`, `#`, `$`, `%`, `(`, `)`, quotes, apostrophes).

This is the same convention taught to students on Day 1 (see Module 1's first-day handout). The repo follows the rule students follow.

### Placeholder syntax used in this file

When a pattern uses `XX`, `YY`, or `NN`, those are placeholders for a zero-padded two-digit number that gets substituted at use-time. Examples:

- `module-XX-shortname/` → `module-01-fluency/`, `module-02-audio-editing-mixing/`
- `module-XX-week-YY/` → `module-02-week-03/`
- `project-NN-shortname.html` → `project-01-musique-concrete.html`
- `lastname-projectNN.wav` → `lastname-project01.wav`

Note: `XX` and `NN` are interchangeable as "zero-padded number" placeholders; the letter choice in this file just helps disambiguate when multiple numbers appear in one pattern (e.g. `module-XX-week-YY/` makes it clear which number is the module and which is the week). They're not meaningful tokens to the filesystem.

`[bracketed-words]` are placeholders for arbitrary user-supplied content (a last name, a descriptive shortname, etc.) and are not zero-padded numbers.

### Folder structure

#### Top level

```
README.md
syllabus.html
module-01-fluency/
module-02-audio-editing-mixing/
module-03-recording/
module-04-the-daw/
exams/
assets/
under-the-hood/
  build/
  meta/
  policies/
```

Module folders are `module-XX-shortname/` where XX is zero-padded (`01`, `02`, etc.) and shortname is a few hyphenated words capturing the module's content. The shortname is meant to make the folder readable in `cd` and `ls` output; it's not load-bearing for any reference.

#### Per-module

```
module-XX-name/
  README.md          The module: purpose, learning outcomes, session-by-session teaching notes
  lessons/           Student-facing material in encounter order: readings, interactive tools, lab handouts
  listening/         Listening assignments (historical + peer where applicable)
  projects/          Project prompts and project-specific TA notes
```

Not every module uses every subfolder; they're added as needed.

### Lesson files

Lesson files inside `module-XX-name/lessons/` are numbered by encounter order within the module, with the document type in the filename:

```
01-reading-digital-audio.html
02-tool-digital-audio-explorer.html
03-handout-audacity-orientation.html
04-reading-editing-envelope.html
05-handout-editing-techniques.html
06-handout-mixing-in-audacity.html
07-reading-dynamics.html
08-tool-mixing-dynamics.html
09-reading-audacity-dynamics.html
```

The number is a sort key, not a global ID; it resets at the start of each module. The type word (`reading`, `tool`, `handout`) lets the TA glance at the folder and see the shape of the module without opening anything.

### Listening files

Listening files inside `module-XX-name/listening/` use descriptive shortnames:

```
historical.html
peer-project-01.html
```

The peer-listening filename includes the project number it pairs with (so Module 3 will have `peer-midterm.html` or similar, not `peer-project-02.html` if the midterm isn't formally a "Project 2").

### Project files

Project files inside `module-XX-name/projects/` use `project-NN-shortname.html` for the prompt and `project-NN-shortname-notes.md` for the TA/prep notes:

```
project-01-musique-concrete.html
project-01-sample-bank-notes.md
```

Project numbers are zero-padded and global (Project 1, Project 2 = midterm, Project 3 = final, etc.) — this matches the chrome convention.

### Assets

#### Images

```
assets/images/module-XX-week-YY/[descriptive-shortname].[ext]
```

Week numbers are zero-padded. Examples: `module-02-week-02/audacity-settings.png`, `module-02-week-05/wide-vs-narrow.svg`.

Some images sit in week-keyed folders even though they're conceptually module-wide (e.g. Audacity screenshots used across multiple weeks). The week is the week the image was *first generated for*, not a constraint on where it can be used.

#### Audio

```
assets/audio/module-XX-week-YY/[descriptive-shortname].wav   <- build-script output
assets/audio/source/[descriptive-shortname].[ext]            <- inputs to build scripts
```

Examples: `module-02-week-02/sr-8k-16bit.wav`, `module-02-week-05/range-wide.wav`, `source/voice-tape-demo.aif`.

The `source/` folder holds real recordings used as inputs to build scripts. Files there are commit-tracked but not regenerable: losing them means losing material.

#### Videos

```
assets/videos/module-XX-week-YY/[descriptive-shortname].[ext]
```

Short Audacity screen recordings inlined in readings. Specs in `assets/videos/README.md`.

### Build scripts

```
build/generate-[purpose].py
build/generate-[purpose]-week-YY.py
```

The week suffix is used when there's a script per week of generated assets (e.g. `generate-audio-demos-week-03.py`). For single-purpose scripts that produce one set of assets, the week suffix is dropped (e.g. `generate-audio-demos.py`).

### Server paths (referenced in handouts)

The class server is an SFTP server at `sftp://134.154.190.239`, port 22. Students authenticate with their NetID and NetID password, using FileZilla. It is reachable from inside the lab only.

A student's login arrives at the root of their own folder, created by the server on first login and named with their NetID. Student-facing materials therefore name private paths **relative to that folder**, never as absolute paths:

```
project-NN/                                  Per-project working folders
sample-library/                              Per-student sample library (Module 3 onward)
final/                                       Final project folder
```

Shared material lives under `/public`, reached by clicking the `/` at the top of FileZilla's remote directory tree:

```
/public/sample-banks/project-01/             Project 1 sample bank
/public/module-XX/[purpose]/                 Module-specific shared assets (e.g. orientation samples)
/public/mus-381-fall-2026/                   Per-semester shared resources
/public/mus-381-fall-2026/project-NN-pieces/ Class listening folders for Projects 1 and 3
/public/mus-381-fall-2026/project-02-libraries/ Peer-listening folder for the Module 3 libraries
/public/mus-381-fall-2026/final-pieces/      Final piece listening folder
```

Students create their own subfolders inside `/public` when a submission has more than one file. The top-level structure is built for them before the term.

The local mirror is `~/Documents/[netid]/`, matching the server-side folder name so FileZilla's two panes line up. Filenames still lead with last name.

Student-facing pages write the placeholder bare, as `~/Documents/netid/`. Internal docs bracket it, as `~/Documents/[netid]/`.

The `mus-381-fall-YYYY/` prefix is the only place a semester date appears in a path. Every other path is semester-stable.

### Sample library files

Starting in Module 3 Wk 6, every student builds and maintains a personal sample library at `sample-library/` inside their own folder on the server. Filenames inside the library follow a category-descriptor-variant pattern:

```
[category]-[descriptor]-[variant].wav
```

- **category** — the high-level kind of sound; matches the folder it lives in. Examples: `paper`, `metal`, `water`, `voice`, `field`.
- **descriptor** — what the sound is, in a word or two. Examples: `crumble`, `rip`, `clang`, `drip`, `hum`.
- **variant** — what distinguishes this take from sibling takes of the same descriptor. Examples: `slow`, `fast`, `close`, `far`, `dry`, `wet`.

Lowercase, hyphens between words, no spaces, no special characters. Same base rule as everywhere in the repo.

Worked examples:

```
sample-library/
  paper/
    paper-crumble-slow.wav            Module 3 Wk 6 starter library
    paper-crumble-fast.wav
    paper-rip-slow.wav
    paper-rip-fast.wav
  metal/
    metal-pan-strike-soft.wav         Hypothetical Wk 7 additions
    metal-pan-strike-hard.wav
    metal-wire-scrape-slow.wav
```

The variant slot is optional when there's only one take of a descriptor (`metal-fork-drop.wav` is fine if there's no sibling); add it when sibling variants exist. If a student records a third or fourth variant of a descriptor and the slow/fast axis runs out, use a noun-shaped variant instead (`paper-crumble-slow.wav`, `paper-crumble-fast.wav`, `paper-crumble-corner.wav`, `paper-crumble-edge.wav`). The rule isn't a fixed taxonomy; it's a discipline of meaningful distinctions.

The category is also the folder. `paper-crumble-slow.wav` lives in `paper/`. The redundancy is intentional: the file is identifiable on its own (without the folder context) and the folder is browsable on its own (without renaming files when reorganizing).

All samples in the library are mono, 48 kHz, 24-bit WAV, prepped through the denoise / trim / normalize pipeline (see the Module 3 Wk 6 lab handout).

### Student submission filenames

The filenames students use when submitting work follow the same lowercase-hyphen rule, with last name first:

```
lastname-projectNN.wav                  Audio deliverables (e.g. lastname-project01.wav)
lastname-projectNN-vN.wav               Versioned working copies (lastname-project01-v3.wav)
lastname-listening-NN.docx              Historical listening writeups (NN = module number)
lastname-peer-listening-NN.docx         Peer listening writeups (NN = module number, same as the historical listening)
lastname-orientation.wav                Module 1 / 2 orientation deliverables
lastname-hello.m4a                      Module 1 Day 1 recording
```

Project numbers are zero-padded and global (`project01`, `project02`), matching the chrome and project-file conventions. Version numbers are not padded (`v1`, `v2`, `v10`).

#### Hyphen rule for project references

The token `project01` in filenames does **not** take an internal hyphen, but the same project referenced as a folder name does:

- Filename: `lastname-project01.wav`
- Folder name: `project-01/`, `project-01-pieces/`, `sample-banks/project-01/`

Treat the filename's hyphen as the separator between last name and project token; inside the project token, no further hyphen. In folder names, the hyphen reads as a visual break between the word `project` and the number, since folder names tend to be longer and read better with the hyphen.

This means `~/Documents/[netid]/project-01/lastname-project01.wav` is the canonical full local path for a student's Project 1 working file: hyphenated folder, unhyphenated filename.

#### Listening filename NN meaning

The `NN` in listening filenames is the module number, for both assignment types:

- **Historical listening (one per module):** `lastname-listening-02.docx` is the Module 2 historical writeup, `lastname-listening-03.docx` is Module 3, and so on.
- **Peer listening (where a module has one):** the same module number as that module's historical listening, with `peer` as the distinguisher. `lastname-peer-listening-02.docx` is the Module 2 peer listening (on the Project 1 pieces); `lastname-peer-listening-03.docx` is the Module 3 peer listening (on the midterm sample libraries). The specific files a student responds to are named in the assignment, so the project anchor lives there rather than in the number.

The two assignments are different enough (one is per-module, one is per-project) that giving them different placeholder meanings reads more clearly than forcing both onto the same axis.


---

## Chrome

> **Scope:** all documents. The patterns differ between HTML (student-facing) and Markdown (internal), but every document is covered.

### The pattern

`Module XX · Role` — module-tagged context first, role within the module second. Modules are zero-padded (`Module 01`, `Module 02`); roles are not (`Lecture 1`, `Project 1`, `Handout 1`).

For documents that aren't tied to a single module (e.g. a lab reference card used all semester), the leading word is the context type (`Lab`), followed by the document's role.

### HTML files (student-facing)

The header `<span class="meta">` and the matching footer span both contain the role line for the document. They identify the document without dating it.

| Document type | Header / footer right span |
|---|---|
| Reading (Monday lecture) | `Module XX · Lecture N` |
| Reading (supplement to a lecture) | `Module XX · Lecture N (supplement)` |
| Lab handout (paired with a specific lab session) | `Module XX · Lab N` |
| Generic module-tied handout | `Module XX · Handout N` |
| Interactive tool | `Module XX · Tool N` |
| Listening assignment | `Module XX · Listening` |
| Peer listening assignment | `Module XX · Peer listening` |
| Project prompt | `Module XX · Project N` |
| Module-agnostic handout (used all semester) | `Lab · Reference card` |

#### Numbering rules

All within-module counts reset at the module boundary. Most numbers are within-module; project numbers are the exception (global, since projects build on each other across the semester).

- **Lecture numbers** count Monday lectures within a module. Mon Wk 2 in Module 2 is Lecture 1, Mon Wk 3 is Lecture 2, etc.
- **Supplement readings** take the parent lecture's number with `(supplement)` appended. Example: `Lecture 3 (supplement)` for a reading that backs up Lecture 3.
- **Lab numbers** count Wednesday lab sessions within a module. Module 2 has three lab sessions and three Lab-numbered handouts (Lab 1 → Lab 2 → Lab 3). Used when a module has multiple labs and the number serves as session-navigation help.
- **Handout numbers** count handouts within a module when the document is module-tied but not paired with a single lab session. No document currently uses this pattern; the slot is reserved for future module-tied handouts that aren't paired with a specific Wednesday lab.
- **Tool numbers** count interactive tools within a module. Module 2's digital audio explorer is Tool 1; its dynamics tool is Tool 2.
- **Project numbers** count globally across the semester. Project 1 (Module 2), Project 2 (Module 3 midterm), etc.

#### When to choose Lab N vs Handout N for a module-tied handout

If the module has multiple labs (Wednesday sessions) and the handout is the principal document for a specific one of them, use `Lab N`, where N is which lab in the module. This matches Module 2's pattern and helps the TA and students quickly navigate to "the handout for Wednesday two."

If the handout isn't tied to a specific lab session (e.g. a "general orientation" handout used across multiple weeks of the module), use `Handout N`, where N counts handouts within the module.

The distinction is about whether the number provides session-navigation value. If yes → Lab. If no → Handout.

#### Separators

Middle dot (`·`, U+00B7) separates title metadata in `<title>` elements and in metadata-style headings: `Step 1 · Turn the knobs down`.

En dashes (`–`, U+2013) stay where they form a typographic compound, as in `musique concrète–style found sounds`, and in number ranges.

#### Title block

The title block's module tag (`<div class="module-tag">`) holds the module's *thematic* label (e.g. `Module 02 · Digital audio, editing & mixing`), shared across all documents in a module.

The title block's subtitle is a one-sentence description of the document's content. **Subtitles do not contain dates.**

#### Intro paragraph

The intro paragraph (the first `<p>` after the title block) is **exactly one paragraph at lede size** (`<p class="lede">`).

If the intro wants to be two paragraphs, merge them into one, or push the second past the first `<hr>` so it belongs to the body.

#### Today's gear callout

Every student-facing HTML document that students use during a lab session opens with a **Today's gear** callout, placed immediately after the lede paragraph and before the first `<h2>` or `<hr>`. The callout names what students need to take from the lab's gear storage for today's session.

Three gear tiers, mapped across file type and module:

| File type | Gear list |
|---|---|
| Reading (Mon lecture) | audio interface, headphones |
| Interactive tool | audio interface, headphones |
| Module 2 lab handout | audio interface, headphones |
| Module 3 lab handout | audio interface, headphones, dynamic mic (with stand and XLR cable) |
| Module 4 lab handout | audio interface, headphones, MIDI keyboard |

The Module 3 recording-lab variant uses the inline "(with stand and XLR cable)" parenthetical rather than listing the stand and cable as separate items, since the mic-stand-cable triplet is a unit (you can't use any one of them without the other two).

The MIDI-keyboard tier applies only to the sampling handout (`03-handout-sampling-in-practice.html`), the one Module 4 session where students play the keyboard (Simpler and Drum Rack). The other three Module 4 lab documents are exceptions to the row and run on the reading/tool tier (audio interface, headphones only): audio editing (`02-handout-audio-editing.html`) imports and edits clips, mixing (`04-handout-mixing-in-practice.html`) mixes an already-committed session, and the Adobe Audition follow-along (`05-handout-transferable-concepts.html`) has no instruments and no MIDI. None of the three touches the keyboard.

The callout markup is always the same:

```html
<div class="callout">
  <div class="callout-label">Today's gear</div>
  <p>Take from the lab's gear storage: <strong>[gear list]</strong>. Plug in and run through the start-of-session steps on the <strong>Session Routines</strong> card before continuing here.</p>
</div>
```

Files that don't get the callout:
- The Session Routines card itself (it's the card the callout references)
- The Day 1 reading (`01-reading-first-day-setup.html`), since it teaches the take-out cycle from scratch with its own walkthrough
- Listening pages and project prompts (consulted at home, across sessions; gear context is the day's lab handout, not these files)

Once the callout is present, the body prose should not redundantly list the gear. A lab handout's "Before you start" callout can hold pedagogical context (first-time framing, what's new about today's session), but should not re-list interface/headphones/mic. Templates for new pages live in `templates/`.

#### End of session callout

Readings and interactive tools close with a small **End of session** callout, placed at the very end of the body content, immediately before the `<footer>`. It mirrors the Today's gear callout at the top: a structural cue students see at the moment they're about to tab away from the page.

The readings and tools have no other end-of-session prompt. Without it, a Monday-reading student can close the tab and walk out without doing the upload and gear teardown. The card at the station holds the canonical routine; this callout is the salience cue that points back to it.

The callout markup is always the same:

```html
<div class="callout">
  <div class="callout-label">End of session</div>
  <p>Before leaving the station, run the end-of-session routine on the <strong>Session Routines</strong> card. Upload first, gear teardown second.</p>
</div>
```

Files that get this callout:
- Readings (Mon lectures)
- Interactive tools

Files that don't:
- Lab handouts (Wed): they already have an `<h2>End of session</h2>` block with the session-specific "what to upload today" steps plus the same "continue with the rest of the card's routine" tail. That block does the same job in heading-and-prose form; adding the callout would double up.
- The Session Routines card itself, the Day 1 reading, listening pages, and project prompts: same exception list as Today's gear, for the same reasons.

#### Lab handout end-of-session tail (canonical sentence)

Every lab handout's End of session block closes with the same sentence pointing back to the Session Routines card:

```
Then continue with the rest of the card's end-of-session routine: disconnect and quit FileZilla, sign out of browser accounts, quit all apps, knobs back to zero, unplug everything (including the mic's XLR from both ends), stow the gear back in the lab's gear storage, chair in.
```

The Session Routines card is the canonical source for what's in this list. The sentence is repeated in lab handouts as a salience cue, not as the authoritative procedure. **If the routine changes (a step added, removed, or reordered on the card), update the card first, then sweep every lab handout for the same edit.** Otherwise the cue and the card will drift, and students who follow the cue will skip whatever the card added.

Lab handouts that currently use this sentence:
- Module 2 Labs 1, 2, 3
- Module 3 Labs 1, 2, 3 (handouts 02, 05, 07)

Module 3's Lab 4 (handout 08, the self-guided studio walkthrough) does not use the tail. It is worked through on the student's own time in MB2508, not a standard MB2525 lab session with shared-gear teardown and an upload, so the routines-card cue does not apply.

#### Links

Every link that navigates away from a student-facing page opens in a new tab, written `target="_blank" rel="noopener noreferrer"`. This holds for both external links (the Ableton manual, Adobe's guides) and cross-document links to another lesson in the repo, so a student who follows a link keeps the page they were reading open behind it.

In-page links are the exception: a table of contents pointing to `#section` anchors within the same document stays in the same tab, since a new tab for a same-page jump would only duplicate the page. The rule is new tab if the link leaves the page, same tab if it scrolls within it.

### Markdown files (internal)

Markdown docs (module specs, TA notes, this folder) use the H1 to identify themselves:

| Document type | H1 line |
|---|---|
| Module spec / TA notes (merged) | `# Module XX — [Module title]` |
| Operational doc (server archival policy, sample bank prep, this folder's files) | `# [Document title]` (no module reference) |

The repository README (`README.md` at the repo root) is student-facing and takes no em dashes. The em-dash H1 form in the table above applies to internal Markdown only.

If a metadata line is useful immediately under the H1, put it as bold text and keep it dateless. For example: `**Weeks 2–5** (7 sessions)`. Calendar date ranges belong in `syllabus.html`.

Links in these files cannot be forced to open in a new tab. GitHub strips the `target` attribute when it renders Markdown, whether the link is written in Markdown syntax or as a raw HTML anchor, so the new-tab rule above applies to the student-facing HTML only. On GitHub a reader opens a link in a new tab with a middle-click or cmd/ctrl-click. This is a platform limitation, not a gap to fix.


---

## Dates

> **Scope:** the whole repo, every document type.

### The rule

Calendar dates (`Aug 24`, `Sep 16`, etc.) appear **only** in the syllabus (`syllabus.html`).

Re-running this course in a future semester should require editing only that file (and Canvas, externally). Every other reference to time uses a stable positional label that doesn't change between semesters.

### Week references

For everything except the syllabus, use week references:

- **`Day Wk N`** for a specific session: `Mon Wk 2`, `Wed Wk 5`. This is the default and matches the existing TA-notes phrasing.
- **`Wk N`** when day-of-week doesn't matter: `By Wk 3`, `Starting Wk 2`.
- Add role-words ("the lab session," "lecture day") only when the *role* is what's being emphasized, not when position alone identifies the session.

#### Examples

- "Project 1 is due Wed Wk 5." (was: "Wed Sep 16")
- "We'll discuss the pieces at the start of class on Mon Wk 6." (was: "Mon Sep 21")
- "Bank uploaded by Wk 3 Wed." (was: "Wed Sep 2")
- "(no Mon Wk 4 session, Labor Day)" (was: "Sep 7, Labor Day")

### Exceptions: when a date is content, not schedule

Some dates describe historical facts or external metadata and don't change between semesters. These stay:

- **Historical citations and bibliography:** `Schaeffer (1948)`, `Hosken (2nd ed., 2015)`, `June 1981` magazine reference. Historical facts.
- **Doc-revision metadata:** `**Last updated:** April 2026` at the top of operational docs. Helps the reader know how stale the doc is.
- **Year labels in timeline diagrams:** `1948`, `~2000`, `today (2026)`. Historical landmarks in a diagram about the history of recording.
- **File path embeds:** `mus-381-fall-2026/`. The semester is part of the path under `/public` on the class server.
- **Filename illustrations:** `Screenshot 2026-08-19 at 3.21.45 PM.png`. Demonstrating the macOS default screenshot format.

### The content-vs-schedule test

If you're unsure whether a date is schedule (move it) or content (keep it), the test is: **would this number need to change next semester?**

- Yes → it's schedule, replace it with a week reference.
- No → it's content, keep it.


---

## Visual system

> **Scope:** all student-facing HTML, the build scripts that generate audio assets, and any new visual elements (diagrams, screenshots, palette extensions).

### Aesthetic

Modern minimal with mechanical-retro influences. Warm cream backgrounds, warm-grey text, rust accent. Functional, technical-manual feel, but not cold. Generous whitespace; small uppercase mono headers; serif-feeling DM Sans body text; DM Mono for labels and code.

The aesthetic is consistent across every student-facing surface (readings, handouts, listening assignments, project prompts, interactive tools) so the course feels like one continuous body of work rather than a stack of unrelated documents.

### Palette

All colors live in CSS variables. **Never hardcode hex values in component CSS.** Reference variables by name; if a color doesn't exist for what you need, add it to the variable list first and use the name everywhere.

The variable definitions in `assets/style.css`:

| Variable | Hex | Purpose |
|---|---|---|
| `--bg` | `#f5f1e8` | Page background, warm cream |
| `--bg-alt` | `#ede6d6` | Slightly darker cream for callouts, audio comparison blocks, figure backgrounds |
| `--ink` | `#2a2620` | Body text, dark warm grey |
| `--ink-soft` | `#5c544a` | Secondary text, captions, sublabels |
| `--ink-faint` | `#8a8175` | Tertiary text, photo attributions |
| `--rule` | `#c9bfa8` | Borders, dividers, rules |
| `--rule-soft` | `#ddd3bd` | Subtle grid lines in diagrams |
| `--accent` | `#a85c2e` | Rust accent, used for module tags, callout titles, link borders, key highlights |
| `--accent-soft` | `#d89169` | Lighter rust for hover states, secondary accents |
| `--warn-bg` | `#f0e3d2` | Background for warning callouts |
| `--warn-ink` | `#6b3e1a` | Text for warning callouts |
| `--meter-good` | `#5c8c4e` | Level-meter green zone: signal safely below ceiling |
| `--meter-hot` | `#c08a2e` | Level-meter amber zone: signal approaching ceiling |
| `--meter-clip` | `#a83030` | Level-meter red zone: signal at or over ceiling |
| `--gr-light` | `#d9b042` | Gain-reduction gradient, light end (small reduction, yellow) |
| `--gr-heavy` | `#b5552f` | Gain-reduction gradient, heavy end (large reduction, rust) |
| `--cable-xlr` | `#3a6b7a` | XLR cable, mic-level balanced; teal-slate |
| `--cable-usb` | `#525a5e` | USB cable, digital data; neutral graphite |
| `--cable-ts` | `#a8862e` | TS cable, instrument-level unbalanced; warm ochre |
| `--cable-trs` | `#6b5e8c` | TRS cable, balanced line / stereo; muted plum |

#### Meter color taxonomy

`--meter-good`, `--meter-hot`, `--meter-clip` are the canonical level-meter triplet. They follow the audio-industry green / amber / red convention but are warmed slightly to sit with the cream palette. Used in both static SVG meter diagrams (e.g. the gain-staging figure in `06-handout-mixing-in-audacity.html`) and live CSS meter widgets (e.g. the input / output / GR meters in the dynamics tool).

`--gr-light` and `--gr-heavy` are the two endpoints of the gain-reduction gradient. CSS gradient interpolation handles the middle; if a sharper transition is needed (e.g. a 3-stop gradient with a deliberate midpoint), `--meter-hot` works as the intermediate color since it sits naturally between yellow and rust.

#### Cable color taxonomy

Each cable type used in the course gets a distinct desaturated hue, kept separate from `--accent` (reserved for devices) and from each other. The convention is consistent everywhere a cable appears in a diagram, so a student who learns "XLR is teal" in the Wk 6 Mon reading can recognize XLR by color in the Wk 7 Mon expansion, the Wk 8 Mon mixer diagram, and any later signal-flow visual.

| Variable | Cable | Carries | Where it first appears |
|---|---|---|---|
| `--cable-xlr` | XLR | Mic-level (or line-level), balanced, three-conductor | Module 3 Wk 6 Mon reading (basic recording chain) |
| `--cable-usb` | USB | Digital data | Module 3 Wk 6 Mon reading (interface to computer) |
| `--cable-ts` | TS | Instrument-level, unbalanced, two-conductor | Module 3 Wk 7 Mon reading (widening the flow) |
| `--cable-trs` | TRS | Balanced line / unbalanced stereo, three-conductor | Module 3 Wk 7 Mon reading |

If a new cable type is needed later (optical, MIDI, etc.), add a `--cable-*` variable here first, then use the name everywhere.

### Typography

| Variable | Stack | Purpose |
|---|---|---|
| `--serif` | `'DM Sans', -apple-system, system-ui, sans-serif` | Body text (despite the variable name, DM Sans is a humanist sans, not a serif) |
| `--mono` | `'DM Mono', 'SF Mono', Menlo, monospace` | Headers, labels, captions, code, key combos |

Fonts are loaded from Google Fonts via the `@import` at the top of `style.css`. The course wordmark, the document-chrome header / footer, and all label-style elements use `--mono`; everything else uses `--serif`.

### SVG diagrams

Diagrams are **written inline** in the HTML. CSS variables only resolve when the SVG is embedded directly; loading SVG via `<img src="...">` strips the variable resolution and breaks the palette.

For diagrams generated by build scripts (e.g. the wide-vs-narrow waveform in Module 2 Week 5), the script writes the SVG to `assets/images/module-XX-week-YY/` as the source of truth, and the reading **inlines that SVG content directly** by pasting it into the page. The image on disk exists for regeneration and review; the version that ships in the HTML is the inlined copy.

SVG conventions:

- Always include `role="img"` and `aria-label` for accessibility
- Use `var(--ink)`, `var(--accent)`, etc., for stroke and fill colors, never hex
- Use `DM Mono, monospace` for any text inside the SVG (this is the convention; the variable doesn't resolve inside SVG `font-family` attributes in some browsers, so the literal stack is fine)
- `viewBox` rather than fixed width/height so diagrams scale

#### Signal-flow diagrams

Signal-flow diagrams show how audio moves through equipment: from a source, through cables and devices, to a destination. They appear throughout Module 3 (basic recording chain, widened flow, mixer routing) and need to read consistently across readings.

The visual hierarchy distinguishes **devices** from **cables**:

- **Devices** (mic, audio interface, computer, mixer, etc.) are drawn as rounded rectangles outlined in `--accent`, filled with `--bg-alt`. Equal size where possible. They're the nodes of the flow.
- **Cables** (XLR, USB, TS, TRS) are drawn as smaller, lower-weight labeled segments connecting two devices. Stroked in the cable's color from the `--cable-*` family. Each cable gets a small inline label (e.g. "XLR", "USB") in DM Mono, positioned above or below the segment, colored to match the cable.
- **Direction** is shown with an arrowhead at the receiving-device end of each cable segment, in the cable's color.

The device-cable-device-cable-device chain reads visually as anchor-line-anchor-line-anchor, with color doing the work of distinguishing cable types at a glance.

A separate inline label above the whole diagram, in `--accent` DM Mono caps with letter-spacing, names what the diagram is (`BASIC RECORDING CHAIN`, `SIGNAL FLOW`, etc.). Beneath each device, an `--ink-soft` DM Mono caption names what category of signal is leaving that device (`acoustic`, `analog electrical`, `digital`).

The canonical example is the chain diagram in `module-03-recording/lessons/01-reading-recording-chain.html`, section 1.

### Images and screenshots

Screenshots of software (Audacity, etc.) and photographs are loaded as `<img>` with `loading="lazy"`. They sit inside `<figure>` blocks with a `<figcaption>` styled in DM Mono uppercase.

Photo attributions, when present, go inside the figure as a small italic line under the figcaption (see Module 2 listening for examples). The attribution uses `--ink-faint` and the `.photo-attribution` class.

When a figure needs numbered annotations, the HTML pattern is the same regardless of source: a `<figure class="annotated">` (or `figure.screenshot` for software screenshots specifically) containing the image, a brief `<figcaption>`, and an `.annotation-key` block below the image listing the numbered items.

For screenshots that the course produces in-house (e.g. an Audacity capture taken from a lab machine), the markers drawn directly onto the PNG follow a fixed style: orange filled circles with white numbers, placed on the region they identify, no leader lines. The canonical example is `audacity-interface-empty.png` in `assets/images/module-02-week-02/`. If the screenshot is ever re-captured, the new version needs fresh annotations drawn on in the same style.

For figures that come from outside sources (e.g. a third-party cross-section diagram of a microphone, a manufacturer-produced schematic), the markers on the image stay in whatever style the source uses; only the `.annotation-key` block beneath is rewritten in the course voice. A canonical example is `dynamic-microphone-cross-section.png` in `assets/images/module-03-week-06/`.

### Callout and pause blocks

Two block types interrupt the main prose flow with framed content.

**`.callout`** — a small framed aside for operational notes: lab heads-ups, "don't yank the cable," brief reminders. Tight padding, left border in `--accent`. A `.callout-label` in DM Mono caps names the kind of interruption (e.g. `LAB NOTE`, `WEDNESDAY: DON'T YANK THE CABLE`). Short. Doesn't take more than a few sentences.

**`.pause`** — a longer aside that interrupts the main flow to explain a deeper principle. Dashed border on all sides, more generous padding, full background tint. A `.pause-label` in DM Mono caps reads `PAUSE`. Inside, an `<h4>` titles what's being explained, followed by paragraphs, optionally a figure. Used when the prose has just made a claim that depends on a principle worth taking a moment to ground (e.g. the balanced-cable cancellation depends on how waveforms sum, so a pause box explains phase summation before the prose moves on).

The visual cue:
- Callout = "heads-up, then keep reading"
- Pause = "stop, learn this, then resume"

The canonical pause example is the phase-summation explainer in `module-03-recording/lessons/01-reading-recording-chain.html`, section 4.

### Per-module audio format standards

Each module has a default audio format that students use throughout. The standard is introduced in the module's first reading and reinforced consistently in handouts and project prompts.

| Module | Sample rate | Bit depth | DAW | Notes |
|---|---|---|---|---|
| 1 | n/a | n/a | QuickTime | Day 1 hello recording uses whatever default QuickTime sets |
| 2 | 48 kHz | 24-bit | Audacity | Course-wide rate |
| 3 | 48 kHz | 24-bit | Audacity | Matches Module 2 and the 48/24 phone field recordings |
| 4 | 48 kHz | 32-bit | Ableton | Same rate as Modules 2–3; bit depth steps to 32 at export |

Write the depth as `32-bit` in student-facing material, never `32-bit float`. Write the pair rate first: `48 kHz, 24-bit`.

Build scripts target the per-module standard (48/24 for Modules 2–3, 48/32 for Module 4) for audio a student works with as a project or library file. Demo clips embedded in readings, handouts, and lectures are exempt: the existing sets (Wk 2 rate/depth degradation, Wk 3 tape-speed and editing, Wk 5 dynamics) stay at the rate they were rendered, and the Wk 2 demos in particular keep the specific rates and depths they teach.

### Page width and structure

Student-facing HTML pages are constrained to `max-width: 720px` (see `body` in `style.css`). This is the readable-prose width and shouldn't be widened for any reason short of an interactive tool that needs more horizontal room. If a tool needs more width, scope the override to the tool block; don't widen the body.

Header lives in `<header class="handout-header">` at the top. Title block lives in `<div class="title-block">` immediately after. The lede paragraph is `<p class="lede">` immediately after the title block. Footer is `<footer class="handout-footer">` at the bottom. The first horizontal rule `<hr>` after the lede separates intro from body content.

This structural skeleton is consistent across every student-facing document; deviating without reason breaks the visual rhythm of the course.
