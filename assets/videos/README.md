# Videos

Short Audacity screen recordings used as inline demos inside readings and lab handouts. Each clip shows one operation in Audacity.

## Directory layout

```
videos/
├── module-02-week-03/    Editing vocabulary (Lecture 2)
│   ├── cut.mp4
│   ├── trim.mp4
│   ├── splice.mp4
│   ├── fades.mp4
│   ├── crossfade.mp4
│   └── reverse.mp4
├── module-03-week-06/    Recording lab (Lab 1)
│   ├── audio-setup-dropdown.mp4    Audio Setup menu walkthrough (Step 2)
│   ├── meter-monitoring.mp4        Live input meter once silent monitoring is disabled (Step 3)
│   └── test-recording.mp4          End-to-end record / stop / playback (Step 5)
└── …
```

The Module 2 editing-vocabulary set has six videos. The loop term has no video; the reading defines it in prose and points ahead to Module 4 (Ableton).

The Module 3 set is the recording lab's three clips of the Audacity interface and live input. They use the same encoding and embedding as the Module 2 set, and the recording specs below apply except for the shared source audio and the 5-to-12-second length.

## Recording specs

Each clip in the editing-vocabulary set:

- uses the same source audio as the rest of the set, one voice recording or another sound with a clear envelope
- is silent, with no audio track (record video only, or strip the audio in post)
- runs 5 to 12 seconds and shows the source, the operation, and the result
- captures the Audacity track view with at least the timeline, transport, and Edit menu visible, without the rest of the macOS window or the dock
- shows the cursor
- holds the source for about 1 second before the operation and the result for about 1 second after

## Encoding

Recordings come in as `.mov` (QuickTime). Re-encode to `.mp4` (H.264) before placing in this folder:

```bash
ffmpeg -i input.mov \
  -vf "scale=1280:-2,fps=30" \
  -c:v libx264 -crf 23 -preset slow \
  -movflags +faststart \
  -an \
  output.mp4
```

Notes on the flags:
- `scale=1280:-2` resizes to 1280px wide preserving aspect ratio, with height rounded to an even number (required by H.264)
- `fps=30` drops 60 fps screen recordings to 30 and halves the file size, with no visible loss for screen content
- `crf 23` sets the quality; lower (18–20) for higher quality, higher (26–28) for smaller files
- `preset slow` spends more CPU during encoding for better compression
- `+faststart` moves the MP4 metadata to the front so the video can start playing before fully loaded
- `-an` strips any audio track

For typical Audacity screen recordings at 1518×1160 source, this produces files at 200–400 KB per clip.

## Embedding

In the reading HTML, each clip embeds inside the `.vocab` definition list as a `<figure class="vocab-video">` containing a `<video>` plus a row of speed-control buttons (0.5×, 1×, 2×). The buttons are wired up by a small script at the bottom of the reading. See `module-02-audio-editing-mixing/lessons/04-reading-editing-envelope.html` for the canonical pattern.
