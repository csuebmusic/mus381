# Build conventions

Naming, chrome, dates, and the visual system for this repo. For Inés and Claude; the TA doesn't need this file.

Prose and register rules are in Inés's profile instructions. Per-asset specs are in [`assets/asset-recipes.md`](../../assets/asset-recipes.md). Page skeletons are in [`templates/`](./templates/README.md); copy one as the starting point for a new page.

Each rule is stated once. What a page, `assets/style.css`, a template, or the Session Routines card states is owned by that file, and this file points to it.

---

## naming

### base rule

Lowercase, hyphens instead of spaces, no special characters (`&`, `!`, `@`, `#`, `$`, `%`, `(`, `)`, quotes, apostrophes). Module 1's first-day reading teaches students the same rule.

### placeholders

In patterns, `XX`, `YY`, and `NN` are zero-padded two-digit numbers: `module-XX-week-YY/` is `module-02-week-03/`. `[bracketed words]` are free text, such as a shortname. `lastname` and `netid` are written bare.

### module folders

Module folders are `module-XX-shortname/`, with a few hyphenated words as the shortname. A module folder holds:

```
README.md     the module: purpose, learning outcomes, live page links, session-by-session teaching notes
lessons/      student-facing material in encounter order: readings, interactive tools, lab handouts
listening/    listening assignments
projects/     project prompts and project-specific TA notes
```

A module adds a subfolder when it has something to put in it.

### lesson files

`NN-type-shortname.html`, numbered by encounter order and restarting at `01` in each module. The type is `reading`, `tool`, or `handout`: `01-reading-digital-audio.html`, `02-tool-digital-audio-explorer.html`.

### listening files

`historical.html` for the historical listening. Peer listening is `peer-[shortname].html`, named for what students listen to: `peer-project-01.html`, `peer-midterm.html`.

### project files

A numbered project's prompt is `project-NN-shortname.html` and its TA and prep notes are `project-NN-shortname-notes.md`. Project numbers are global across the semester; Project 2 is the midterm. The final project's prompt is `final-project.html`.

### assets

```
assets/images/module-XX-week-YY/[shortname].[ext]
assets/audio/module-XX-week-YY/[shortname].wav     build-script output
assets/audio/source/[shortname].[ext]              recordings used as build-script input
assets/videos/module-XX-week-YY/[shortname].mp4
```

The week in the folder name is the week the asset was first made for; any week can use it. Files in `audio/source/` can't be regenerated. Video specs are in [`assets/videos/README.md`](../../assets/videos/README.md).

### build scripts

`build/generate-[purpose].py`, with a `-week-YY` suffix when there's one script per week of generated assets.

### paths in student materials

A student's private paths are written relative to their own folder on the server (`project-01/`, `sample-library/`), never as absolute paths. Shared material is under `/public`. The local mirror is `~/Documents/netid/`, named to match the server folder.

Every document, student-facing and internal, writes the placeholder bare: `~/Documents/netid/`.

A semester date appears in a path only in the `mus-381-fall-YYYY/` folder under `/public`.

### sample library files

`sample-library/[category]/[category]-[descriptor]-[variant].wav`. The category is the kind of sound and matches its folder (`paper`, `metal`). The descriptor names the sound in a word or two (`crumble`, `clang`). The variant distinguishes sibling takes of one descriptor (`slow`, `close`, `corner`) and is left off when a descriptor has one take.

### student filenames

Last name first, then a token: `lastname-project01.wav`, `lastname-listening-02.docx`, `lastname-final.wav`. The project token has no internal hyphen (`project01`); a project folder does (`project-01/`). Versions add `-vN`, unpadded: `-v1`, `-v10`. In listening filenames `NN` is the module number, and peer listening adds `peer`: `lastname-peer-listening-03.docx`.

---

## chrome

### role line

`Module XX · Role`, with the module zero-padded and the role number unpadded: `Module 02 · Lab 1`. A document used across modules leads with its context type: `Lab · Reference card`.

The header `<span class="meta">` and the matching footer span hold the role line.

| Document type | Role line |
|---|---|
| Reading (Monday lecture) | `Module XX · Lecture N` |
| Reading that supplements a lecture | `Module XX · Lecture N (supplement)` |
| Lab handout, principal document for one lab session | `Module XX · Lab N` |
| Module-tied handout not paired with one lab session | `Module XX · Handout N` |
| Interactive tool | `Module XX · Tool N` |
| Listening assignment | `Module XX · Listening` |
| Peer listening assignment | `Module XX · Peer listening` |
| Numbered project prompt | `Module XX · Project N` |
| Final project prompt | `Module XX · Final project` |
| Handout used all semester | `Lab · Reference card` |

Counts restart in each module, except project numbers, which are global. Lecture N counts Monday lectures, Lab N counts Wednesday lab sessions, Handout N counts module-tied handouts not paired with one lab (none at present), and Tool N counts interactive tools.

### separators

A middle dot (`·`, U+00B7) separates title metadata in `<title>` elements and in metadata-style headings: `Step 1 · Turn the knobs down`. En dashes (U+2013) stay in typographic compounds (`musique concrète–style`) and number ranges.

### title block

The module tag (`<div class="module-tag">`) holds the module's thematic label, the same on every document in the module: `Module 02 · Digital audio, editing & mixing`. The subtitle is one sentence describing the document, with no dates.

### headings

Every heading, the `<h1>`, and the page title in `<title>` are lowercase, except proper nouns, product names, acronyms, and chrome tokens (`MUS 381`, `Module 03`, `Lab 4`, `Project 1`): `<title>MUS 381 · recording into Audacity</title>`, `<h1>recording into Audacity</h1>`.

### labeled items

No list item or paragraph uses the bold-label pattern (`<strong>Term:</strong> explanation`). A labeled item is a sentence; bold may mark a control or term name inside it. Step lists are ordered lists, and each step opens with a sentence.

### lede

The first `<p>` after the title block is exactly one paragraph, `<p class="lede">`. A second intro paragraph is merged into it or moved past the first `<hr>`.

### today's gear callout

Every document students use during a lab session has the template's Today's gear callout immediately after the lede, before the first `<h2>` or `<hr>`, with the gear list for its file type:

| File type | Gear list |
|---|---|
| Reading (Monday lecture) | audio interface, headphones |
| Interactive tool | audio interface, headphones |
| Module 2 lab handout | audio interface, headphones |
| Module 3 lab handout | audio interface, headphones, dynamic mic (with stand and XLR cable) |
| Module 4 sampling handout (`03-handout-sampling-in-practice.html`) | audio interface, headphones, MIDI keyboard |
| Other Module 4 lab handouts | audio interface, headphones |

The Session Routines card, the Day 1 reading, listening pages, and project prompts have no Today's gear callout. Body prose doesn't repeat the gear list.

### end of session

Readings and tools end with the template's End of session callout, immediately before the footer. Lab handouts have an `<h2>end of session</h2>` block instead, with that session's upload steps, closing with the template's sentence that continues into the Session Routines card's routine. When the card's routine changes, update the card first, then that sentence in every lab handout. Module 3's Lab 4 (handout 08) has no end-of-session block. The documents without a Today's gear callout have no End of session callout.

### links

Every link that leaves a student-facing page opens in a new tab, written `target="_blank" rel="noopener noreferrer"`, for external links and for links to other pages in the repo. In-page links to `#section` anchors stay in the same tab.

### Markdown files

Internal Markdown docs identify themselves in the H1:

| Document type | H1 line |
|---|---|
| Module README (spec and TA notes) | `# Module XX · [module title]`, title in lowercase |
| Operational doc | `# [Document title]`, with no module reference |

A metadata line under the H1 is bold and dateless: `**Weeks 2–5** (7 sessions)`. Calendar date ranges are in `syllabus.html`.

The new-tab rule applies to HTML only. GitHub strips `target` from Markdown links.

---

## dates

Calendar dates appear only in `syllabus.html` and on Canvas. Every other document uses week references: `Mon Wk 2` or `Wed Wk 5` for a session, `Wk 3` when the day doesn't matter.

Dates that are content stay: historical citations (`Schaeffer (1948)`), `**Last updated:**` lines on operational docs, year labels in timeline diagrams, the `mus-381-fall-YYYY/` path, and filename illustrations (`Screenshot 2026-08-19 at 3.21.45 PM.png`). A date that would change next semester is schedule and becomes a week reference.

---

## visual system

### aesthetic

Modern minimal with mechanical-retro influences: warm cream backgrounds, warm-grey text, a rust accent, generous whitespace, and small uppercase mono headers. Every student-facing page has the same look.

### color and type

Colors are CSS variables, defined with their purposes in `assets/style.css`. Component CSS and SVG reference variables by name and never hardcode hex. A new color is added to the variable list before it's used.

In diagrams, `--accent` marks devices, and each cable type has its own `--cable-*` variable, used for that cable in every diagram. A new cable type gets a new `--cable-*` variable. Level meters use `--meter-good`, `--meter-hot`, and `--meter-clip`. The gain-reduction gradient runs from `--gr-light` to `--gr-heavy`, with `--meter-hot` as the midpoint of a three-stop gradient.

Body text is `--serif` (DM Sans). The wordmark, header and footer chrome, labels, captions, and code are `--mono` (DM Mono).

### SVG diagrams

Diagrams are inline in the HTML. CSS variables don't resolve in an SVG loaded through `<img src>`.

A build script writes its diagram to `assets/images/module-XX-week-YY/`, and the page has that SVG's content pasted inline. The file on disk is for regeneration and review.

Every SVG has `role="img"` and an `aria-label`, uses `var(--…)` for stroke and fill, writes text in the literal stack `DM Mono, monospace`, and uses a `viewBox` instead of a fixed width and height.

### signal-flow diagrams

Devices are rounded rectangles outlined in `--accent` and filled with `--bg-alt`, equal in size where possible. Cables are thinner segments stroked in their `--cable-*` color, each with a small DM Mono label in the same color and an arrowhead at the receiving device. A DM Mono caps label in `--accent` above the diagram names it (`BASIC RECORDING CHAIN`). Under each device, an `--ink-soft` DM Mono caption names the signal leaving it (`acoustic`, `analog electrical`, `digital`). The reference example is the chain diagram in section 1 of `module-03-recording/lessons/01-reading-recording-chain.html`.

### images and screenshots

Images are `<img loading="lazy">` inside a `<figure>` with a `<figcaption>`. A photo attribution is a `.photo-attribution` line under the caption.

An annotated figure is a `figure.annotated` (or `figure.screenshot` for software) with an `.annotation-key` block below the image. Screenshots made in-house carry numbered orange filled circles with white numbers on the regions they identify, with no leader lines; a re-captured screenshot gets fresh markers in that style. The reference example is `assets/images/module-02-week-02/audacity-interface-empty.png`. Figures from outside sources keep their source's markers, and only the `.annotation-key` is in the course voice, as in `assets/images/module-03-week-06/dynamic-microphone-cross-section.png`.

### callout and pause blocks

A `.callout` is a short operational aside, such as a lab heads-up or a reminder, of a few sentences at most. It has tight padding, an `--accent` left border, and a DM Mono caps `.callout-label`.

A `.pause` explains a principle the prose depends on before the prose continues. It has a dashed border, a background tint, a `.pause-label` reading `PAUSE`, and an `<h4>` title followed by paragraphs and an optional figure. The reference example is the phase-summation pause in section 4 of `module-03-recording/lessons/01-reading-recording-chain.html`.

### audio format standards

| Module | Sample rate | Bit depth | Software |
|---|---|---|---|
| 1 | QuickTime default | QuickTime default | QuickTime |
| 2 | 48 kHz | 24-bit | Audacity |
| 3 | 48 kHz | 24-bit | Audacity |
| 4 | 48 kHz | 32-bit at export | Ableton Live |

Each module's first reading introduces its format. Write the depth as `32-bit`, never `32-bit float`, and give the rate first: `48 kHz, 24-bit`.

Build scripts write project and library audio in the module's format. Demo clips embedded in readings, handouts, and lectures keep the rate and depth they were rendered at.

### page structure

A page is `<header class="handout-header">`, then `<div class="title-block">`, then `<p class="lede">`, then the first `<hr>`, the body, and `<footer class="handout-footer">`. The page width is set on `body` in `style.css`. A tool that needs more room overrides the width on its own block.
