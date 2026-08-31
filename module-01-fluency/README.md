# Module 01 — Computer & Studio Fluency

**Week 1 · 1 session (100 min)**

---

## Module purpose

Most students arrive without Mac experience or studio fluency. Before any music-technology content makes sense, students need basic computer fluency, a clear file workflow, and confident hands on the gear at their station. This module is short but foundational. Everything downstream depends on it.

The single biggest thing the TA can do on Day 1 is establish that the lab is a low-stakes, supportive place to learn. Most students arrive nervous about technology. If they leave feeling like *they* did something — saved a file, plugged in gear, made a recording — they'll come back Monday ready to learn. If they leave feeling lost, the rest of the semester is harder.

Plan to circulate constantly. Don't lecture for more than 5 minutes at a stretch. Demo, then have them do it. Be willing to repeat instructions twice; some students will need to see something three times.

---

## Learning outcomes

By the end of this single session, students should be able to:

1. Locate, open, and navigate Finder; understand file paths, folders, and basic keyboard shortcuts
2. Set up a local working folder at `~/Documents/netid/` and connect to the class server with FileZilla
3. Save files using the course naming convention (lowercase, hyphens, no spaces, no special characters)
4. Identify the gear used today (USB hub, audio interface, mic, headphones, XLR cable) and connect them correctly
5. Set the three knobs on an audio interface (gain, main, headphone) in the correct order, starting from zero
6. Use a software level meter to set mic gain at a usable level
7. Record a short audio clip through the full signal chain and save it locally
8. Run through the full end-of-session routine: upload the local folder to the server, disconnect and quit FileZilla, sign out of browser accounts, quit apps, knobs to zero, unplug gear, return everything to the lab's gear storage, leave the station clean
9. Articulate the local-first / server-as-sync workflow that the course will use all semester

---

## Key concepts introduced

- **The local-first / server-as-sync workflow** — students work locally during sessions and use the class server to sync between machines. Download at start of session, upload at end. The server is the master copy; local is the working copy. Transfers happen in FileZilla, over SFTP.
- **The naming convention** — `lastname-projectname-version.ext`, all lowercase, hyphens not spaces, no special characters. Used for every file in the course.
- **The audio signal chain** — physical sound → microphone → cable → audio interface → digital audio. Students touch every link on Day 1; full treatment of each comes in Module 3.
- **Gain staging (light touch)** — input level should be strong but not clipping. Visual meter is the gauge. Full treatment in Module 3.
- **Close vs quit on macOS** — closing a window is not the same as quitting an app. Matters for audio software where multiple apps can conflict over a single interface.

---

## Deliverable

`week-01/[lastname]-hello.m4a` uploaded into the student's own folder on the server (auto-created, named by NetID). The local copy at `~/Documents/[netid]/week-01/` should also exist. Not graded — confirmation everyone made it through Day 1 with the workflow established.

---

## Listening assignment

None for Week 1. Module 1 is a setup module. The first listening assignment comes at the start of Module 2.

---

## Student-facing materials

- [`lessons/01-reading-first-day-setup.html`](https://csuebmusic.github.io/mus381/module-01-fluency/lessons/01-reading-first-day-setup.html) — distributed locally on each lab machine and via Canvas
- [`lessons/02-handout-session-routines.html`](https://csuebmusic.github.io/mus381/module-01-fluency/lessons/02-handout-session-routines.html) — printed and posted at every station; used at the start and end of every session for the rest of the semester

---

## Before class — preparation checklist

Do all of this **at least one day in advance** of the first session, ideally two:

- [ ] Confirm the server is reachable from every lab machine: connect with FileZilla to `sftp://134.154.190.239`, port 22, using your own NetID
- [ ] Confirm FileZilla is installed and launches on every station, and that **FileZilla → Settings… → Interface → Passwords** is set to **Do not save passwords**
- [ ] Confirm `Cmd + A` selects everything in FileZilla's file panes on the lab build; the download and upload steps in every handout depend on it
- [ ] Get the host key fingerprint from Inés and compare it against the unknown-host-key dialog at one station before class, so you know the prompt students accept is the right server
- [ ] Confirm `/public` exists with this term's folders in place: `/public/mus-381-fall-2026/project-01-pieces/`, `project-02-libraries/`, `final-pieces/`, plus `/public/sample-banks/project-01/`, `/public/module-02/orientation/`, and `/public/module-04/`
- [ ] Write the host address, port, and login (NetID and NetID password) on the whiteboard before class starts
- [ ] Place `01-first-day-setup.pdf` (exported from `lessons/01-reading-first-day-setup.html`) into `/Users/Shared/Downloads/` on every lab machine
- [ ] Print `02-session-routines.pdf` (exported from `lessons/02-handout-session-routines.html`) and post it at every station. This is the reference card students follow at the start and end of every session for the rest of the semester.
- [ ] **Wipe local `~/Documents/` on every lab machine** of any leftover student folders from previous semesters. Local folders accumulate over time; clean state every fall and spring.
- [ ] Walk through every station: confirm the USB hub is connected to the Mac mini behind the monitor and has open ports
- [ ] Walk through the lab's gear storage: inventory enough sets for the class — one audio interface, one pair of headphones, one dynamic mic, one mic stand, one XLR cable per student (or per pair, depending on enrollment). Confirm each audio interface is recognized when test-connected. Confirm headphones have the in-line slider all the way up
- [ ] Test-record end-to-end (take a gear set from storage, plug in at one station, test: mic → interface → QuickTime → local save → FileZilla upload, then stow the gear back) to confirm the full chain works
- [ ] Walk through the entire session yourself end-to-end on a lab machine the day before, as if you were a student. Time yourself. This will surface every broken thing.
- [ ] Have a backup plan if the server is down: students save locally only, you collect their work via USB drive at the end. **Do not cancel the session over a network issue.**
- [ ] Have at least one spare hub, one spare XLR cable, and one spare set of headphones available in case something fails during class

---

## What students walk in knowing

Assume:

- Most have **never used a Mac** in any meaningful way
- Most have **never connected to a file server**, and none will have used an SFTP client
- Most do not know what an **audio interface** is
- Some have used GarageBand or Audacity casually; very few have used a real DAW
- A small number will be quite advanced relative to the rest — they'll be bored if you go too slow, but they're useful as peer helpers

The right pacing: **slow enough that the slowest student keeps up, with side-tasks for the fast students.** When a fast student finishes early, ask them to help a neighbor. This is your secret weapon.

---

## Session — Wk 1 Wed: First day (100 min)

| Block | Time | Focus |
|---|---|---|
| 1 — Welcome & framing | 3:00–3:10 | Course overview, the room, where things live |
| 2 — Mac & Finder fundamentals | 3:10–3:35 | Finder, files, folders, screenshots, naming preview |
| 3 — Set up folders + connect to the server | 3:35–3:55 | Local-first / server-as-sync workflow established |
| 4 — Set up gear + make a recording | 3:55–4:30 | Full signal chain: mic → interface → QuickTime → local save |
| 5 — Exit routine | 4:30–4:40 | First full end-of-session: upload to the server, sign out, stow gear |

### Block 1 — Welcome (10 min)

- Introduce yourself briefly. Say you're a grad student in [program], working with Inés.
- **Walk them through the highlights of the syllabus.** Don't read it aloud, but do flag the parts that affect their semester:
  - **Projects.** One per module, four total. Project 1 (Module 2) is a 2-minute musique concrète piece due Wed Wk 5. The midterm (Module 3) is a sample library plus a terminology exam. The final (Module 4) is an Ableton piece due during finals week.
  - **Exams.** Midterm and a cumulative final exam during finals week. Tell them when (the calendar in the syllabus has the dates).
  - **Attendance.** This is a hands-on lab course. Most of the work happens in the room, with gear they don't have at home. Missing class is missing the work. Point them to the exact attendance policy in the syllabus.
  - **Late policy.** Spell out where it is in the syllabus and the headline (e.g., "X points per day late, communicate with the instructor in advance for extensions" — read the actual wording so you state it correctly). Don't dwell on it, but make sure they know it exists and where to find it.
- Tell them where to find the full syllabus (Canvas) and that the headlines you just gave are not a substitute for reading it themselves.
- The most important thing to communicate: **"You don't need to know any of this already. That's why we're here."**
- Tell them about the server in plain words: *"Everyone in this room is going to be working with big audio files all semester. The department runs a file server, and that's where your work lives between sessions. By the end of today you'll have connected to it and put your first recording on it. You reach it from inside this room, using your NetID."*

Aim for the syllabus walkthrough to take about 3 minutes. The point is to flag and locate, not to lecture. Students who want details have Canvas; what they need from you in class is *I know where this lives and that I'm responsible for it*.

### Block 2 — Mac & Finder (25 min)

This is the longest single block. Pace it carefully.

**Demo on the projector first, then have students do each step.** Don't try to teach all the shortcuts at once — introduce them as they come up:

- "Open Finder." (Some students don't know what Finder is. Show the smiley-face icon.)
- "Take a screenshot." (`Cmd+Shift+4`, drag a region.)
- "Now find that screenshot." (It goes to Desktop by default — this is where many students freeze. Walk them through opening Desktop in Finder.)
- "Rename it to `my-screenshot`." (Click once to select, press `return`, type, press `return` again.) This previews the naming convention they'll learn properly in Block 3, and gets them comfortable with Finder's rename behavior — students often try to double-click and end up opening the file instead.
- "Make a new folder called `test`." (Right-click → New Folder, OR `Cmd+Shift+N`.)
- "Drag the screenshot into the folder."
- "Now delete the folder." (Drag to Trash, or `Cmd+Delete`.)

That whole sequence in five minutes teaches: Finder, screenshots, Desktop location, renaming files, folder creation, drag-and-drop, deletion.

**Show file extensions.** This matters more than students realize. Walk them through Finder → Settings → Advanced → "Show all filename extensions." Some students will have the toggle already on; some won't. Make sure everyone leaves with extensions visible.

**Common confusion:** Students don't understand that "Documents," "Desktop," and "Downloads" are folders just like any other folder. Show them the same locations from inside Finder's sidebar — it's the same thing as the Desktop they see behind their windows.

**Practical exercise — local reading:** Have students find `01-first-day-setup.pdf` in `/Users/Shared/Downloads/` and open it. This proves they can navigate Finder. (You pre-loaded this earlier.)

### Block 3 — Set up folders and connect to the server (20 min)

This block establishes the workflow model for the entire semester. Students will hear "two folders, the local one is where you work, the server is how you transport between machines" and that becomes the mental model they carry forward. It's worth slowing down and being explicit about the *why*.

**Open with the conceptual frame.** Before any clicking, draw on the whiteboard:

```
~/Documents/netid/          <-->     your folder on the server
  (local working copy)               (master copy, syncs between machines)
```

Say something like: *"You'll keep two copies of your work. The local copy on whichever computer you're sitting at is where you actually do the work, and it's fast and reliable. The server holds the master copy. You download from it at the start of every session, and upload to it at the end. That way, if you sit at a different computer next time, your work is waiting for you."*

Add the constraint out loud, because it shapes how they plan: the server is reachable from inside the lab only. Work that doesn't get uploaded stays on that one machine until they are back in the room.

This is the most important conceptual moment of Day 1. Don't rush it.

**Then: the local folder, first.**

1. Finder → click **Documents** in the sidebar
2. `Cmd + Shift + N` → name it with their NetID (lowercase) → return
3. Open it, `Cmd + Shift + N` again → name it `week-01`

The local folder is named by NetID so the two FileZilla panes carry the same name and line up visually. Filenames still lead with last name, so submitted work stays identifiable.

Have students do this together with you on the projector. Drill the lowercase / no-spaces rule again here.

**Then: connect to the server.**

Open FileZilla on the projector first and name the parts before anyone types: Quickconnect bar across the top, message log under it, local machine on the left, server on the right, transfer queue along the bottom. Two panes, drag between them.

1. `Cmd + Space`, type FileZilla, return
2. Quickconnect bar: Host `sftp://134.154.190.239`, Username their NetID, Password their NetID password, Port `22`
3. Quickconnect
4. On the unknown host key prompt, tick **Always trust this host, add this key to the cache**, then OK. Without the tick the dialog returns on every connection, twice a session, all term

Then have them all do it together. **This is the moment most likely to break.** If it does:

- Common cause: the `sftp://` prefix left off the host. Without it FileZilla tries plain FTP on port 21 and the connection times out or is refused. This is the single most likely failure of the day.
- Common cause: port left at 21 or blank when the host has no prefix. Both fields have to agree: `sftp://` and 22.
- Common cause: NetID password typo, or a student typing a password for a different account. Campus password resets propagate to the server, so a recently changed password is the current one.
- Common cause: caps lock, or an autofilled username with a stray space.
- If one student cannot connect after two careful attempts, have them work locally for the session and sort it out after class. Do not let one login hold the room.

**Once everyone is connected**, have them look at the right pane. Their folder is created by the server on first login and named with their NetID. It should be empty. They'll upload their first work into it at end of class.

**Point out `/public` but don't dwell.** Click the `/` at the top of the server's directory tree, open `public`, show that class material and peer-review submissions live there, then navigate back. Module 2 is where they actually use it.

**Passwords.** FileZilla on the lab machines is set to leave passwords unsaved, so students type theirs each session. Keep them on the Quickconnect bar and off the Site Manager, which is where saved-site entries would otherwise accumulate on a shared machine.

**Disconnect.** Have students choose Server → Disconnect and quit FileZilla. Explicitly: *"You don't need FileZilla open during the session. We'll reconnect at the end of class to upload."*

**File naming convention.** Write the convention on the whiteboard:

```
lastname-projectname-version.ext
```

Examples (use your name and Inés's so it doesn't feel arbitrary):

```
thiebaut-hello.m4a
smith-soundpiece-v1.wav
```

Drill the rules: lowercase, hyphens, no spaces, no special characters. **Tell them why:** different operating systems and different software treat capitalization, spaces, and special characters inconsistently. A file named `My Project (final!).wav` will eventually break something.

**Sync discipline — preview the lesson.** Briefly tell them: *"Starting next session, every session will start with you downloading your work from the server, and end with you uploading it back. We'll go through the full routine at the end of class today. The most important rule: always upload before you leave. If you don't, your work is stranded on this computer, and the next time you sit at a different computer you'll be working from an older version."*

### Block 4 — Set up gear and make a recording (35 min) + Exit routine (10 min)

This is the day's main event. Students take gear from the lab's gear storage, plug in their full signal chain, set their levels, and produce one successful recording, then run the exit routine to upload to the server and stow the gear back. The pedagogical arc is one continuous activity from storage to upload.

The lab has different audio interface models (and different MIDI keyboard models later in the semester) in storage; the audio interfaces don't all look identical or have the same knob layout. The USB hub at each station is permanently connected to the Mac mini behind the monitor. Teach categories, not specific models.

**Time-keeping note.** Reserve the last 10 minutes for the exit routine; that leaves 35 minutes for everything from gear take-out through the recording. Rough internal budget: 5 min for take-out and back to stations, 25 min for plug-in through recording, 5 min slack for the things that always run over. Demo each step on the projector, then circulate while students do it themselves. Don't move to the next step until most of the room is caught up.

#### Step-by-step facilitation

**Take gear from the lab's gear storage.** This is the first time students do this part of the routine. Lead them to the storage area as a group; have each student take out one set: an audio interface, a pair of headphones, a dynamic mic with its stand, and an XLR cable. Walk back to stations together. Set the gear on the desk, no plugging in yet.

**Show the gear.** Once everyone's back at their stations, hold up each piece and say what it does in one sentence:

- *USB hub:* "Everything plugs into this. It's already at your station, connected to the computer behind your monitor. Don't unplug the hub itself, only the cables that go into it."
- *Audio interface:* "This converts analog audio (sound from a microphone, or sound to your headphones) into digital audio that the computer can work with, and back."
- *Microphone:* "This is a tabletop dynamic mic. It plugs into the audio interface using an XLR cable — the thick three-pin one."
- *Headphones:* "These go into the audio interface, never directly into the computer. The Mac's headphone jack is behind the monitor and you'd have to reach back there; the interface has a jack on the front or side."

**Knobs to zero first.** Before anything else, have students turn all three interface knobs (gain, main, headphone) all the way down. *Say why:* "If something is set wrong, you can get a sudden loud sound when you plug in. Starting at zero protects your ears and the gear. Build the habit now: knobs to zero before any plugging in or out, every time, in this class and anywhere else you touch audio gear."

**Plug everything in (in this order):**

1. Audio interface → USB hub
2. Mic → audio interface front-panel input (XLR)
3. Headphones → headphone jack on the audio interface

**The headphone slider gotcha.** The lab headphones have an in-line volume slider on the cable. Have students slide it all the way up *before* putting headphones on. This is a real Day 1 trap — students think the gear is broken when actually the slider is at zero. Calling it out early saves 10 minutes of confusion.

**Audio MIDI Setup.** `Cmd + Space`, type "Audio MIDI Setup." It opens. Students should see their audio interface listed.

**Naming gotcha.** The UM2 does not show up as "Behringer" or "UM2." It appears as **USB Audio CODEC**, and as two entries at that: CODEC 1 is the output, CODEC 2 the input. The PreSonus shows up as **AudioBox USB 96**. Students hunting for a brand name on a UM2 station get stuck here; point them to "USB Audio CODEC." The student reading covers this, but it's the most common Day 1 snag at this step.

If they don't:
- Common cause: USB cable not seated properly. Replug into the same hub port.
- Common cause: a flaky port on the hub. Try a different port on the same hub.
- Common cause: interface needs power switch (rare on USB-bus-powered units, common on larger ones).
- If a whole hub appears dead (multiple devices not recognized), have the student switch stations and flag the hub for replacement.

Right-click the interface → "Use this device for sound input" and "Use this device for sound output." This step is easy to forget and causes confusion later.

**Open QuickTime → New Audio Recording.** Walk students through opening QuickTime, choosing File → New Audio Recording, clicking the dropdown arrow next to the record button, and selecting their audio interface as the source.

**Bring up monitoring.** Have students put headphones on (slider already up — see above), then turn up the headphone knob to about noon (12 o'clock, knob pointing straight up), then the main knob to about noon. They probably won't hear anything yet because gain is still at zero. That's fine.

**The mix knob (only some interfaces).** Roughly half of the lab interfaces have an additional knob labeled "Mix" or "Direct/USB" — it controls the headphone balance between the live input signal and what the computer is sending back. The other half handle this internally and don't expose it to the user.

Before you teach the gain step, point this out:

> "Some of you have an extra knob labeled Mix or Direct-USB. If you do, set it to about 60% toward the direct/input side and 40% toward the computer side — about 11 o'clock if direct is on the left. This means you'll hear mostly yourself live, plus a little of any playback the computer sends. If your interface doesn't have this knob, don't worry — it handles this for you. We'll come back to this concept in Module 3."

Walk to the stations that have it and confirm they've set it correctly. This is a tiny piece of "your gear may differ" diversity — embrace it as a teaching moment rather than something to apologize for.

**Set the gain — this is the moment.** Have students talk into the mic at normal volume (suggest "count to twenty" or "say what you had for breakfast"). While talking, slowly turn up the gain knob. They watch the QuickTime level meter. Stop when the meter is regularly moving but not pinning the right edge.

This is the first time most students will see input level visually represented. Worth pausing here briefly:

> "What you just did is called *gain staging* — setting the input level so the signal is strong enough to be useful, but not so strong that it distorts. It's one of the most important skills in recording, and we'll come back to it properly in Module 3. For today, the rule is: meter moving = good, meter pinned all the way to the right = too hot, turn down."

Don't go deeper than that on Day 1. The temptation will be to teach digital headroom, dBFS, the relationship between input gain and noise floor — save it. Day 1 is the introduction; Module 3 is the proper treatment.

**Record + save.** Hit record, say name + one word, stop, listen back. Save as `lastname-hello.m4a` to `~/Documents/[netid]/week-01/` (local). The upload happens during the exit routine.

**Block 4 confusions — gear, signal chain, recording:**

- *"I can't hear anything in the headphones."* — Check in this order: (1) headphone slider on cable all the way up; (2) headphone knob on interface above zero; (3) audio interface set as system output in Audio MIDI Setup; (4) main/output knob above zero; (5) for stations with a mix knob, that it isn't pinned all the way to one side.
- *"I hear myself but no playback."* (only for stations with mix knob) — Mix knob is too far toward direct. Move toward the computer/USB side.
- *"I hear playback but not myself."* (only for stations with mix knob) — Mix knob is too far toward computer. Move toward the direct/input side.
- *"My meter isn't moving when I talk."* — Gain knob is at zero, or wrong input is selected in QuickTime, or mic XLR cable not seated properly.
- *"My meter is pinning red the whole time."* — Gain too high. Turn it down until peaks just stop hitting the right edge.
- *"My recording sounds quiet."* — Gain was too low when recording. Have them re-record with the gain higher.
- *"My recording sounds distorted/crunchy."* — Gain was too high (clipping). Re-record with the gain lower.
- *"I forgot to pick the audio interface in QuickTime."* — They recorded through the Mac mini's nonexistent built-in mic and got nothing, or got something through the wrong source. Have them re-record.

**If gear is genuinely broken.** Swap in a spare, or move the student to a working station. Every student leaves with a recording saved locally and uploaded to the server. Fix the failed gear after class.

**Before students leave**, connect on the projector and scroll through the student folders to confirm every student's file is there. This is a small ritual but makes the work feel real.

If a student's file isn't there in their local folder:
- Don't single them out publicly. Quietly help them after class or in office hours.
- Most often the issue is they saved to Desktop or Downloads. Walk them through Recents in Finder to find the file, then drag it into `~/Documents/[netid]/week-01/`.

**Teach the exit routine — last 10 minutes of class.** Before dismissing, walk students through the end-of-session routine on the projector. They have a printed copy at every station (the **Session Routines** reference card) and a version inside today's reading, but verbal reinforcement on Day 1 sets the habit. This is the first time they'll run the routine end-to-end, including the gear teardown.

Walk them through:

1. Save the recording in QuickTime if they haven't already (`Cmd + S`)
2. Open FileZilla and reconnect from the Quickconnect bar
3. Left pane to `~/Documents/[netid]/`; right pane stays in their own folder on the server
4. Click into the left pane, `Cmd + A`, drag across to the right pane
5. On the overwrite dialog, **Overwrite if source newer**, tick **Always use this action**, OK
6. Confirm the upload: the transfer queue empties, and the right pane shows `week-01/[lastname]-hello.m4a`
7. Server → Disconnect, then quit FileZilla (`Cmd + Q`)
8. Sign out of any browser accounts (Canvas, Google, etc.); quit the browser
9. Quit all apps with `Cmd + Q`
10. Turn the audio interface knobs (gain, main / output, headphone) back to zero
11. Unplug: headphones from the interface, the interface's USB from the hub, the mic's XLR from both ends. Coil cables loosely without kinks
12. Return everything to the lab's gear storage: interface, headphones, mic, mic stand, XLR cable
13. Chair in

Tell them this is the same routine they'll do every session for the rest of the semester. Today it'll take a few extra minutes because it's the first time; once habit, it's about 5 minutes total. The Session Routines card at every station summarizes the same steps for daily reference.

**Verify uploads on the projector.** Once everyone is done, connect on the projector and scroll the student folders. Confirm every student's folder holds their hello file. This is the same "small ritual" as before, but now it confirms upload happened, not just save.

**Common Day-1 confusions during the upload:**

- *Which pane is which.* The most common Day 1 disorientation. Say it the same way every time: left is this computer, right is the server. Point at the screen when you say it.
- *Dragging the folder instead of its contents.* A student who drags `~/Documents/[netid]/` itself into their server folder ends up with `netid/netid/week-01/`. Teach the pattern once and hold to it: click into the pane, `Cmd + A`, drag the selection.
- *Nothing appears to happen.* The transfer went into the queue at the bottom of the window and finished in under a second. Show them the queue and the **Successful transfers** tab so they know where to look for confirmation.
- *Overwrite dialog dismissed with the wrong option.* **Overwrite** and **Overwrite if source newer** both work at end of session; **Skip** silently uploads nothing. If a student reports an empty-looking upload, this is why.

---

## Common questions

- *"Do I need a Mac at home?"* — No. The lab has everything they need. The server keeps your work synced between lab machines.
- *"Can I connect to the server from home?"* — No. It's reachable from inside the lab only. Carry work out on a USB drive or personal cloud storage if you want it with you.
- *"Can I use my own headphones?"* — Yes. The lab provides them but personal headphones are fine.
- *"What if my audio interface isn't working?"* — Try: unplug from the hub, replug into a different hub port, check Audio MIDI Setup. If still broken, switch stations and report it.
- *"Can I take my files home on a USB drive?"* — Yes. Copy your folder from `~/Documents/` to a USB drive, personal cloud storage, or anywhere you can reach from home. The server itself is reachable from the lab only, so a copy you carry out is the way to work at home. Audacity is free and runs anywhere, so working at home on Module 2 material is fine. Ableton is lab-license-only, so Module 4 work mostly stays in the lab.
- *"What if I forget to upload at the end?"* — Your work is stranded on that machine. The next time you're at that exact same station, it'll still be in `~/Documents/[netid]/`, but if you're at a different station, you'll be working from an older version. Always upload.
- *"What if I forget to download at the start?"* — You'll be working from an older version. Sync regularly: download at start, upload at end. If you realize mid-session, save what you've done, then connect and check the server to see what you should have started with.
- *"Do I need to buy a textbook?"* — No. Course materials are in the GitHub repo and on Canvas.

---

## Common confusions

These show up across the whole day, not tied to any one block. Block-specific confusions live with their respective blocks above.

- **"I saved it but I can't find it."** — They saved to Desktop or Downloads instead of `~/Documents/[netid]/`. Walk them through Recents in Finder to find the file, then drag it.
- **"My screenshot didn't work."** — They held the wrong key combination. `Cmd + Shift + 4` to drag a region. The screenshot is saved to Desktop.
- **"I don't know my NetID."** — It's the front half of their campus email address, the same login as Canvas. Have them check Canvas in the browser.
- **"FileZilla says it can't connect."** — Check the `sftp://` prefix and port 22 first. That pair accounts for most of it. Password next.
- **"Local and server folders look different."** — Sync issue. Whichever has the newer modification date is the trusted version. Copy that one over the older one. Turn on View → Directory Comparison → Compare modification time to make the difference visible. If they can't tell which is newer, ask the TA before deleting anything.
- **"FileZilla asked me Overwrite, Skip, or Rename."** — At end of session the answer is **Overwrite if source newer**. Skip uploads nothing; Rename leaves two copies with confusing names.

---

## Pacing fallbacks

The day's clock is genuinely tight: Welcome 10 + Mac/Finder 25 + Folders/server 20 + Gear/recording 35 + Exit routine 10 = 100 min. That assumes Block 4 holds at 35 min for the gear and recording portion, with the last 10 min of class reserved for the exit routine. If gear setup or gain staging runs long, the exit routine is non-negotiable — cut something inside Block 4 instead.

If you're behind:

- Cut Block 2 short. Mac fundamentals continue informally throughout the semester. As long as students can find Finder and save a file, the rest can be picked up.
- Block 4 (gear + recording) is the heart of the day. Don't shortcut the order-of-operations (knobs to zero, slider up, plug in, monitor up, gain last). That sequence is the lesson.
- If absolutely necessary, accept a less-than-perfect gain setting and let students just get a recording. Module 3 will treat this properly.
- **Never skip the exit routine.** If everything else has run long, dismiss students one-by-one only after they've uploaded to the server. The whole semester's workflow depends on this habit forming on Day 1.

If you're ahead:

- Have students record a second clip and save it as `lastname-hello-v2.m4a`. Reinforces the versioning convention.
- Have them try adjusting the gain too low (recording too quiet) and too high (clipping) to hear the difference. Sets up Module 3.
- Open Audacity (which will be a focus next week) just to see the icon in Applications.

---

## After class

- [ ] Connect and check the student folders. Confirm every student has `week-01/[lastname]-hello.m4a` uploaded. Note any missing students for follow-up — these are students who didn't run the exit routine, which is the sync discipline we're trying to build from Day 1.
- [ ] Note any technical issues (broken stations, server or login trouble, gear that didn't work) in a running log so they get fixed before Monday.
- [ ] If the server or logins had problems, debrief with Inés about what happened and what to fix.
- [ ] Email any students whose files are missing — don't shame, just make sure they know how to do it before Monday.

---

## What to assess

Nothing in Module 1 is graded. The deliverable (`lastname-hello.m4a` uploaded to the server) is a check that everyone made it through Day 1 and ran the exit routine. The only thing to "assess" is whether each student's file is in the right place on the server — that's binary, no rubric needed.

If a student is missing the file by Monday's class, that's an early signal they may need extra support, particularly with the sync workflow. Reach out individually.

---

## What to bring starting Wk 2

- Headphones (lab provides, but students may bring their own if they prefer)
- Notebook or note-taking tool of choice
- Curiosity
