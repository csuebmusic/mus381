# Page templates

Skeletal HTML files for new pages. Copy one as the starting point; the rules they follow are in [`build-conventions.md`](../build-conventions.md).

| Template | Used for |
|---|---|
| `reading.html` | Monday-lecture readings |
| `tool.html` | Interactive in-class tools |
| `handout-module-02.html` | Wednesday lab handouts in Module 2 |
| `handout-module-03.html` | Wednesday lab handouts in Module 3 |
| `handout-module-04.html` | Wednesday lab handouts in Module 4 |

## what to fill in

Bracketed placeholders mark every slot to edit:

- `[Reading title]`, `[Lab title]`, `[Tool title]`: the page's H1, also used in `<title>`
- `Module XX · Lecture N`, `Module XX · Lab N`, `Module XX · Tool N`: the role line in the header and footer and the module number in the title block, with `XX` as the zero-padded module number and `N` as the count within the module
- `[Module thematic label]`: the module's thematic label, shared by every document in the module (for Module 02, `Digital audio, editing & mixing`)
- `[One-sentence subtitle, no dates]`: the title-block subtitle
- `[One-paragraph lede ...]`: the lede, one paragraph

## what stays fixed

The Today's gear callout text is fixed for each file type. A session that needs different gear gets a new row in the gear table in `build-conventions.md` first, then a template change.

The end-of-session closing sentence in the handout templates changes only when the session's unplug sequence changes, as in a Module 4 handout that names the MIDI keyboard's USB cable instead of the mic's XLR.
