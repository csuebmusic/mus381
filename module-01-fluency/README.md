# Module 01 · computer & studio fluency

**Wk 1 · 1 session (Wed Aug 19, 100 min)**

---

## module purpose

Module 1 is one session. Students learn basic Mac and Finder use, set up the course file workflow (a local folder plus their folder on the class server), connect the gear at their station, make one recording, and run the full end-of-session routine for the first time.

Most students start the course without Mac experience or studio experience, and many are nervous about the technology. Make the lab feel low-stakes. Every student should leave having saved a file, plugged in gear, made a recording, and uploaded it.

Circulate constantly. Don't lecture for more than 5 minutes at a stretch: demo a step, then have students do it. Repeat instructions; some students need to see a step three times.

---

## learning outcomes

By the end of this session, students should be able to:

1. Locate, open, and navigate Finder; understand file paths, folders, and basic keyboard shortcuts
2. Set up a local working folder at `~/Documents/[netid]/` and connect to the class server with FileZilla
3. Save files using the course naming convention (lowercase, hyphens, no spaces, no special characters)
4. Identify the gear used today (USB hub, audio interface, mic, headphones, XLR cable) and connect it correctly
5. Set the three interface knobs (gain, main / output, headphone) in the correct order, starting from zero
6. Select the audio interface in Audio MIDI Setup and confirm its Format reads 48,000 Hz
7. Use a software level meter to set mic gain at a usable level
8. Record a short audio clip through the full signal chain and save it locally
9. Run the full end-of-session routine: upload the local folder to the server, disconnect and quit FileZilla, sign out of browser accounts, quit apps, knobs to zero, unplug gear, return everything to the lab's gear storage, chair in
10. Explain the local-first, server-as-sync workflow the course uses all semester

---

## concepts introduced

Students work locally during a session and use the class server to sync between machines: download at the start of a session, upload at the end. The server copy is the master copy; the local copy is the working copy. Transfers happen in FileZilla, over SFTP.

The naming convention is `lastname-projectname-version.ext`: all lowercase, hyphens instead of spaces, no special characters. It applies to every file in the course.

The audio signal chain is physical sound → microphone → cable → audio interface → digital audio. Students touch every link on Day 1; Module 3 covers each one in depth.

Gain staging gets a light touch: the input level should be strong but not clipping, and the visual meter is the gauge. Module 3 covers it in depth.

Closing a window on macOS isn't the same as quitting the app. Two audio apps left running at once can conflict over the same audio interface.

---

## deliverable

`week-01/lastname-hello.m4a`, uploaded into the student's own folder on the server (created by the server on first login, named with the student's NetID). The local copy at `~/Documents/[netid]/week-01/` should also exist. It isn't graded; it confirms each student made it through Day 1 with the workflow set up.

---

## listening assignment

None for Wk 1. The first listening assignment is Module 2's, due Mon Sep 14 (Wk 5).

---

## student-facing materials

- [your first day](https://csuebmusic.github.io/mus381/module-01-fluency/lessons/01-reading-first-day-setup.html) (`lessons/01-reading-first-day-setup.html`) is the Day 1 reading. A PDF export goes on each lab machine (see the checklist below) and on Canvas.
- [session routines](https://csuebmusic.github.io/mus381/module-01-fluency/lessons/02-handout-session-routines.html) (`lessons/02-handout-session-routines.html`) is the reference card, printed and posted at every station. Students follow it at the start and end of every session for the rest of the semester.

---

## before class: preparation checklist

Do all of this at least one day before the first session, ideally two.

- [ ] Confirm the server is reachable from every lab machine: connect with FileZilla to `sftp://134.154.190.239`, port 22, using your own NetID.
- [ ] Confirm FileZilla is installed and launches on every station, and that **FileZilla → Settings… → Interface → Passwords** is set to **Do not save passwords**.
- [ ] Confirm `Cmd + A` selects everything in FileZilla's file panes on the lab build. The download and upload steps on every page use it.
- [ ] Get the host key fingerprint from Inés and compare it against the unknown-host-key dialog at one station before class.
- [ ] Confirm `/public` exists with this term's folders in place: `/public/mus-381-fall-2026/project-01-pieces/`, `project-02-libraries/`, `final-pieces/`, plus `/public/sample-banks/project-01/`, `/public/module-02/orientation/`, and `/public/module-04/`.
- [ ] Write the host address, port, and login (NetID and NetID password) on the whiteboard before class starts.
- [ ] Print `02-session-routines.pdf` (exported from `lessons/02-handout-session-routines.html`) and post it at every station.
- [ ] Wipe local `~/Documents/` on every lab machine of leftover student folders from previous semesters. Do this every fall and spring.
- [ ] Walk through every station: confirm the USB hub is connected to the Mac mini behind the monitor and has open ports.
- [ ] Walk through the lab's gear storage and inventory enough sets for the class: one audio interface, one pair of headphones, one dynamic mic, one mic stand, and one XLR cable per student (or per pair, depending on enrollment). Confirm each audio interface is recognized when test-connected. Confirm the headphones' in-line slider is all the way up.
- [ ] Test-record end to end: take a gear set from storage, plug in at one station, and run mic → interface → Audio MIDI Setup (Format at 48,000 Hz) → QuickTime → local save → FileZilla upload, then stow the gear.
- [ ] The day before, walk through the entire session yourself on a lab machine as if you were a student, and time yourself. This finds anything broken.
- [ ] Have a backup plan if the server is down: students save locally only, and you collect their work on a USB drive at the end. Don't cancel the session over a network issue.
- [ ] Have at least one spare hub, one spare XLR cable, and one spare pair of headphones ready in case something fails during class.

---

## what students walk in knowing

Assume:

- Most have never used a Mac in any meaningful way.
- Most have never connected to a file server, and none will have used an SFTP client.
- Most don't know what an audio interface is.
- Some have used GarageBand or Audacity casually; very few have used a full DAW.
- A few will be far ahead of the rest. They'll be bored if you go too slow, and they're useful as peer helpers.

Pace the session so the slowest student keeps up, and give the fast students side tasks. When a fast student finishes early, ask them to help a neighbor.

---

## session · Wk 1 Wed: first day (100 min)

| Block | Time | Focus |
|---|---|---|
| 1 · welcome | 3:00–3:10 | Course overview, the room, where things are |
| 2 · Mac & Finder | 3:10–3:35 | Finder, files, folders, screenshots, file extensions (reading Part 1) |
| 3 · folders + server | 3:35–3:55 | Local folder, FileZilla connection, naming rules (reading Parts 2 and 3) |
| 4 · gear + recording | 3:55–4:30 | Full signal chain: mic → interface → QuickTime → local save (reading Part 4) |
| 5 · exit routine | 4:30–4:40 | First full end of session: upload to the server, sign out, stow gear |

### Block 1 · welcome (10 min)

- Introduce yourself briefly: you're the course instructor, a grad student in [program], and Inés Thiebaut supervises the course.
- Walk them through the highlights of the syllabus. Don't read it aloud; flag the parts that affect their semester.
  - There are three projects. Project 1 (Module 2) is a musique concrète piece of 90 seconds to 2 minutes, due Wed Sep 16 (Wk 5). The midterm (Module 3) is a sample library plus an in-class terminology exam, due Wed Oct 14 (Wk 9). The final project (Module 4) is a piece built in Ableton Live, with drafts due Wed Nov 18 (Wk 14) and Wed Dec 2 (Wk 15), completed during finals.
  - The final exam is a cumulative in-class exam during finals week (date and time TBD in the syllabus).
  - The grade weights are Project 1 20%, midterm 20%, final project 25%, final exam 20%, and listening and peer responses 15%.
  - This is a hands-on lab course, and most of the work happens in the room with gear they don't have at home. Students who have to miss a session email you ahead of time.
  - Late assignments lose 2% per day late, up to a maximum deduction of 50%.
  - Generative AI isn't allowed for any graded work.
- Tell them the full syllabus is on the course website and on Canvas, and that your headlines don't replace reading it.
- Tell them: *"You don't need to know any of this already. That's why we're here."*
- Tell them about the server in plain words: *"Everyone in this room is going to be working with big audio files all semester. The department runs a file server, and that's where your work is kept between sessions. By the end of today you'll have connected to it and put your first recording on it. You reach it from inside this room, using your NetID."*

Keep the syllabus walkthrough to about 3 minutes: name each policy and say where it is in the syllabus.

### Block 2 · Mac & Finder (25 min)

This is the longest single block. Pace it carefully.

Demo each step on the projector first, then have students do it. Introduce shortcuts as they come up. The sequence follows reading Part 1:

- "Open Finder." (Some students don't know what Finder is. Show the blue and white smiley-face icon in the Dock.)
- "Make a new folder on the Desktop called `test`." (Click **Desktop** in the Finder sidebar, then File → New Folder, or `Cmd + Shift + N`.)
- "Take a screenshot." (`Cmd + Shift + 4`, drag a region.)
- "Now find that screenshot." (It saves to the Desktop by default. Many students freeze here; walk them through opening Desktop in Finder.)
- "Rename it to `my-screenshot`." (Click once to select, press `return`, type, press `return` again.) This previews the naming rules in Block 3. Students often double-click and open the file instead of renaming it.
- "Drag the screenshot into the `test` folder."
- "Now delete the folder." (Select it and press `Cmd + Delete`.)

That sequence takes about five minutes and covers Finder, folder creation, screenshots, the Desktop location, renaming, drag and drop, and deletion.

Show file extensions. Walk them through Finder → Settings → Advanced → **Show all filename extensions**. Some students will have it on already. Make sure everyone leaves with extensions visible. With extensions showing, students can tell a `.wav` from an `.mp3` at a glance.

Point out two callouts in Part 1. The lab Desktop gets cleared periodically, and students save work in `~/Documents/[netid]/`, never on the Desktop or in Downloads. Clicking the red dot closes a window but leaves the app running; `Cmd + Q` quits.

Students don't realize that Documents, Desktop, and Downloads are folders like any other. Show the same locations in Finder's sidebar, and show that the Desktop in the sidebar is the Desktop behind their windows.

### Block 3 · set up folders and connect to the server (20 min)

Students leave this block with the two-copy model they use all semester: they work in the local folder and move their work between machines through the server. Slow down and say why there are two copies.

Before any clicking, draw this on the whiteboard:

```
~/Documents/netid/          <-->     your folder on the server
  (local working copy)               (master copy, syncs between machines)
```

Say something like: *"You'll keep two copies of your work. The local copy on whichever computer you're sitting at is where you edit, and it's fast and reliable. The server holds the master copy. You download from it at the start of every session, and upload to it at the end. That way, if you sit at a different computer next time, your work is waiting for you."*

Say the constraint out loud: the server is reachable from inside the lab only. Work that doesn't get uploaded stays on that one machine until they're back in the room, and anything they want at home goes on a USB drive or their own cloud storage.

Make the local folder first:

1. Finder → click **Documents** in the sidebar
2. `Cmd + Shift + N` → name it with their NetID (lowercase) → return
3. Open it, `Cmd + Shift + N` again → name it `week-01`

The local folder and the server folder have the same name (the NetID), and the two FileZilla panes match. Filenames still start with the student's last name.

Have students do this along with you on the projector. Repeat the lowercase, no-spaces rule here.

Then connect to the server.

Open FileZilla on the projector first and name the parts before anyone types: the Quickconnect bar across the top, the message log under it, this computer on the left, the server on the right, the transfer queue along the bottom. Two panes; you drag between them.

1. `Cmd + Space`, type FileZilla, return
2. Quickconnect bar: Host `sftp://134.154.190.239`, Username their NetID, Password their NetID password, Port `22`
3. Quickconnect
4. On the unknown host key prompt, tick **Always trust this host, add this key to the cache**, then OK. Without the tick the dialog comes back on every connection.

Then have them all do it together. Expect connection problems here:

- The `sftp://` prefix was left off the host. Without it FileZilla tries plain FTP on port 21, and the connection times out or is refused. Check this first.
- The port was left at 21 or blank. Both fields have to agree: `sftp://` and 22.
- The NetID password has a typo, or the student typed a password for a different account. Campus password resets reach the server, so a recently changed password is the current one.
- Caps lock is on, or an autofilled username has a stray space.
- If one student can't connect after two careful attempts, have them work locally for the session and sort it out after class. Don't hold the room for one login.

Once everyone is connected, have them look at the right pane. Their folder was created by the server on first login and is named with their NetID. It's empty. They'll upload their first work into it at the end of class.

Point out `/public` briefly. Click the `/` at the top of the server's directory tree, open `public`, show that class material and peer-review submissions are there, then go back. Students start using it in Module 2.

The reading also links the FileZilla project's guide and names the four sections that apply. Students don't need it in class.

FileZilla on the lab machines doesn't save passwords. Students type theirs each session, in the Quickconnect bar, not the Site Manager.

Have students choose Server → Disconnect and quit FileZilla. Say: *"You don't need FileZilla open during the session. We'll reconnect at the end of class to upload."*

Then the naming rules (reading Part 3). Write the convention on the whiteboard:

```
lastname-projectname-version.ext
```

The reading's examples:

```
thiebaut-hello.m4a
smith-soundpiece-v1.wav
garcia-fieldrec-traffic.wav
```

Add one with your own last name. Go over the rules: lowercase, hyphens instead of spaces, no special characters, descriptive names, and versions saved as v1, v2 rather than overwriting. Tell them that different operating systems and software treat capitals, spaces, and special characters differently, and a file named `My Project (final!).wav` can open on one machine and fail on the next.

Preview sync discipline. Tell them: *"Starting next session, every session will start with you downloading your work from the server, and end with you uploading it back. We'll go through the full routine at the end of class today. The rule: always upload before you leave. If you don't, your work is stuck on this computer, and the next time you sit at a different computer you'll be working from an older version."*

### Block 4 · set up gear and make a recording (35 min)

Students take gear from the lab's gear storage, plug in the full signal chain, set their levels, and make one recording. Block 5 then runs the exit routine to upload it and stow the gear.

Storage has two audio interface models with different layouts: the Behringer U-Phoria UM2 and the PreSonus AudioBox USB 96. (MIDI keyboards come in Module 4.) The USB hub at each station is permanently connected to the Mac mini behind the monitor. Teach the categories (gain, main / output, headphone, mix) rather than one model's layout.

Reserve the last 10 minutes of class for Block 5. That leaves 35 minutes for everything from gear take-out through the recording: about 5 minutes for take-out and back to stations, 25 for plug-in through recording, and 5 of slack. Demo each step on the projector, then circulate while students do it. Don't move to the next step until most of the room has caught up.

#### step by step

Take gear from the lab's gear storage. Lead students to the storage area as a group; each student takes one set: an audio interface, a pair of headphones, a dynamic mic with its stand, and an XLR cable. Walk back to stations together. Set the gear on the desk, no plugging in yet.

Show the gear. Once everyone's back at their stations, hold up each piece and say what it does in one sentence:

- Hold up the USB hub: "Everything plugs into this. It's already at your station, connected to the computer behind your monitor. Don't unplug the hub itself, only the cables plugged into it."
- Hold up the audio interface: "This converts analog audio (sound from a microphone, or sound to your headphones) into digital audio that the computer can work with, and back."
- Hold up the microphone: "This is a tabletop dynamic mic. It plugs into the audio interface with an XLR cable, the thick three-pin one."
- Hold up the headphones: "These plug into the audio interface, never directly into the computer. The interface's headphone jack is on the front or the back, depending on the model. Look for the headphones icon."

Start with knobs to zero (reading Step 1). Have students turn all three interface knobs (gain, main / output, headphone) all the way down. Tell them: "If something is set wrong, you can get a sudden loud sound when you plug in. Starting at zero protects your ears and the gear. Knobs to zero before any plugging in or out, every time, in this class and anywhere else you use audio gear."

Plug everything in, in this order (Step 2):

1. Audio interface USB → USB hub
2. Mic → audio interface front-panel input (XLR)
3. Headphones → headphone jack on the audio interface

At Step 3, the lab headphones have an in-line volume slider on the cable. Have students slide it all the way up before putting the headphones on. Students who skip this think the gear is broken.

At Step 4, students open Audio MIDI Setup (`Cmd + Space`, type "Audio MIDI Setup," return). Students should see their audio interface in the list on the left.

The UM2 doesn't show up as "Behringer" or "UM2." It appears as **USB Audio CODEC**, and as two entries: **USB Audio CODEC 2** is the input, **USB Audio CODEC 1** the output. The PreSonus shows up as a single entry, **AudioBox USB 96**. Students hunting for a brand name on a UM2 station get stuck here; point them to "USB Audio CODEC." The reading covers this, and it's still the usual snag at this step.

If the interface isn't listed:

- The USB cable may not be seated. Replug it into the same hub port.
- The hub port may be flaky. Try a different port on the same hub (this is the reading's fix).
- The interface may need its power switch on (rare on USB-bus-powered units, common on larger ones).
- If a whole hub seems dead (several devices not recognized), have the student switch stations and flag the hub for replacement.

Right-click the interface → **Use this device for sound input**, then right-click again → **Use this device for sound output**. On the UM2, set CODEC 2 as input and CODEC 1 as output. Students forget this step, and it causes confusion later.

With the interface selected, have students check that the **Format** line reads **48,000 Hz**. If it shows another rate, they pick a 48,000 Hz option from the Format dropdown. On the UM2 they check both entries. The reading has a clip showing where to look, and tells students they'll learn what the numbers mean in Module 2. Then quit Audio MIDI Setup (`Cmd + Q`).

Open QuickTime → New Audio Recording (Step 5). Walk students through opening QuickTime Player, choosing File → New Audio Recording, clicking the small arrow to the right of the record button, and selecting their audio interface as the source.

Bring up monitoring (Step 6). Have students put the headphones on (slider already up), turn the headphone knob up to about noon (12 o'clock, knob pointing straight up), then the main / output knob to about noon. They probably won't hear anything yet because the gain is still at zero.

Step 7 sets the mix knob or the Direct Monitor button. About half of the lab interfaces have an extra knob labeled Mixer, Mix, or Direct/USB (the AudioBox's is labeled Mixer). It sets the headphone balance between the live input and the computer's playback. The UM2 has a **Direct Monitor** button instead, which has to be pressed in for students to hear their mic.

Before the gain step, point this out:

> "Some of you have an extra knob labeled Mixer, Mix, or Direct/USB. If you do, set it to about 60% toward the direct/input side and 40% toward the computer side, about 11 o'clock if direct is on the left. You'll hear mostly yourself live, plus a little of any playback the computer sends. If you have a Direct Monitor button instead, press it in. We'll come back to this in Module 3."

Walk to the stations and confirm each knob is set, or each Direct Monitor button is pressed in.

Set the gain (Step 8). Have students talk into the mic at normal volume ("count to twenty" or "say what you had for breakfast"). While talking, they slowly turn up the gain knob and watch QuickTime's level meter. They stop when the meter moves regularly but never hits the right edge, roughly half to two-thirds across. They should now hear themselves in the headphones and can adjust the headphone knob.

Most students are seeing input level on a meter for the first time. Pause briefly:

> "What you just did is called *gain staging*: setting the input level so the signal is strong enough to be useful, but not so strong that it distorts. Module 3 covers it in depth. For today, a moving meter is good, and a meter pinned all the way to the right is too hot: turn it down."

Don't go deeper on Day 1. Digital headroom, dBFS, and the relationship between input gain and noise floor are Module 3 material.

Record and save (Steps 9 and 10). Students click record, say their name and one word about why they're taking this class, stop, and listen back. Then File → Save, name it `lastname-hello`, and save it in `~/Documents/[netid]/week-01/` (local). The upload happens in Block 5.

#### Block 4 confusions: gear, signal chain, recording

- When a student can't hear anything in the headphones, check in this order: (1) the headphone slider on the cable is all the way up; (2) the headphone knob on the interface is above zero; (3) the interface is set as the system output in Audio MIDI Setup (CODEC 1 on the UM2); (4) the main / output knob is above zero; (5) on a UM2, the Direct Monitor button is pressed in; on stations with a mix knob, it isn't turned all the way to one side.
- When a student on a mix-knob station hears themselves but no playback, the knob is too far toward direct. Move it toward the computer/USB side.
- When a student on a mix-knob station hears playback but not themselves, the knob is too far toward the computer. Move it toward the direct/input side.
- When the meter doesn't move during talking, the gain knob is at zero, the wrong input is selected in QuickTime, or the mic's XLR cable isn't seated.
- When the meter is pinned at the right edge the whole time, the gain is too high. Turn it down until peaks stop hitting the right edge.
- When the recording sounds quiet, the gain was too low. Have them re-record with the gain higher.
- When the recording sounds distorted or crunchy, the gain was too high (clipping). Re-record with the gain lower.

If gear is broken, swap in a spare or move the student to a working station. Every student leaves with a recording saved locally and uploaded to the server. Fix the failed gear after class.

Before Block 5, circulate and confirm each student's file is in `~/Documents/[netid]/week-01/`. If a student's file isn't there:

- Don't single them out publicly.
- Most often they saved to Desktop or Downloads. Walk them through Recents in Finder to find the file, then drag it into `~/Documents/[netid]/week-01/`.

### Block 5 · exit routine (10 min)

Walk students through the end-of-session routine on the projector. The Session Routines reference card at every station has the same steps, and the reading ends with them ("before you leave today"). This is the first time students run the routine end to end, including the gear teardown.

1. Save the recording in QuickTime if they haven't already (`Cmd + S`)
2. Open FileZilla and reconnect from the Quickconnect bar
3. Left pane to `~/Documents/[netid]/`; right pane stays in their own folder on the server
4. Click into the left pane, `Cmd + A`, drag across to the right pane
5. On the overwrite dialog, choose **Overwrite if source newer**, tick **Always use this action** and **Apply to current queue only**, then OK
6. Confirm the upload: the transfer queue empties, the file appears under **Successful transfers**, and the right pane shows `week-01/lastname-hello.m4a`
7. Server → Disconnect, then quit FileZilla (`Cmd + Q`)
8. Sign out of any browser accounts (Canvas, Google, Microsoft, etc.); quit the browser
9. Quit all apps with `Cmd + Q`; any app with a dot under its Dock icon is still running
10. Turn the interface knobs (gain, main / output, headphone) back to zero
11. Unplug: headphones from the interface, the interface's USB from the hub, the mic's XLR from both ends. Coil cables loosely without kinks
12. Return everything to the lab's gear storage: interface, headphones, mic, mic stand, XLR cable
13. Chair in

Tell them this is the routine for every session for the rest of the semester. Today it takes a few extra minutes; once it's a habit, it takes about 5 minutes.

Once everyone is done, connect on the projector and scroll the student folders. Confirm every student's folder holds `week-01/lastname-hello.m4a`.

#### Block 5 confusions: the upload

- Students mix up which pane is which. Say it the same way every time: left is this computer, right is the server. Point at the screen when you say it.
- A student who drags `~/Documents/[netid]/` itself into their server folder ends up with `netid/netid/week-01/`. Teach the pattern once and hold to it: click into the pane, `Cmd + A`, drag the selection.
- When nothing appears to happen, the transfer ran in the queue at the bottom of the window and finished in under a second. Show them the queue and the **Successful transfers** tab.
- When an upload looks empty, the student probably chose **Skip** on the overwrite dialog, which uploads nothing. **Overwrite** and **Overwrite if source newer** both work at the end of a session.

---

## common questions

- *"Do I need a Mac at home?"* No. The lab has everything they need, and the server keeps their work synced between lab machines.
- *"Can I connect to the server from home?"* No. It's reachable from inside the lab only. They can take work out on a USB drive or personal cloud storage.
- *"Can I use my own headphones?"* Yes. The lab provides them, and personal wired headphones are fine.
- *"What if my audio interface isn't working?"* Unplug it from the hub, plug it into a different hub port, and check Audio MIDI Setup. If it still doesn't work, switch stations and report it.
- *"Can I take my files home on a USB drive?"* Yes. Copy the folder from `~/Documents/` to a USB drive or personal cloud storage. Audacity is free and runs anywhere, so working at home on Module 2 material is fine. Ableton Live is lab-license-only, so Module 4 work mostly stays in the lab.
- *"What if I forget to upload at the end?"* The work stays on that machine. At that same station it'll still be in `~/Documents/[netid]/`, but at a different station they'll be working from an older version. Always upload.
- *"What if I forget to download at the start?"* They'll be working from an older version. If they notice mid-session, they save what they've done, then connect and check the server to see what they should have started with.
- *"Do I need to buy a textbook?"* No. Course materials are free on the course website (csuebmusic.github.io/mus381) and on Canvas.

---

## common confusions across the day

Block-specific confusions are with their blocks above.

- A student who says "I saved it but I can't find it" saved to Desktop or Downloads instead of `~/Documents/[netid]/`. Walk them through Recents in Finder to find the file, then drag it into place.
- A screenshot that didn't work means the wrong key combination: `Cmd + Shift + 4`, then drag a region. The screenshot saves to the Desktop.
- When FileZilla can't connect, check the `sftp://` prefix and port 22 first, then the password.
- When the local and server folders look different, it's a sync issue. The copy with the newer modification date is the one to keep; copy it over the older one. To see the difference, choose View → Directory Comparison → Compare modification time, then View → Directory Comparison → Enable. If a student can't tell which is newer, they ask you before deleting anything.
- When FileZilla asks Overwrite, Skip, or Rename at the end of a session, the answer is **Overwrite if source newer**. Skip uploads nothing; Rename leaves two copies with confusing names.

---

## pacing fallbacks

The day's timing is welcome 10 + Mac & Finder 25 + folders and server 20 + gear and recording 35 + exit routine 10 = 100 min. If gear setup or gain staging runs long, cut something inside Block 4 and keep the full 10 minutes for the exit routine.

If you're behind:

- Cut Block 2 short. Students pick up Mac fundamentals through the semester. They need to find Finder and save a file today.
- Keep the gear order intact: knobs to zero, plug in, slider up, monitoring up, gain last.
- If necessary, accept a less-than-ideal gain setting so students get a recording. Module 3 covers gain properly.
- Never skip the exit routine. If everything else ran long, dismiss students one by one only after each has uploaded to the server.

If you're ahead:

- Have students record a second clip and save it as `lastname-hello-v2.m4a`, using the versioning rule.
- Have them record once with the gain too low (too quiet) and once too high (clipping) to hear the difference. This sets up Module 3.
- Open Audacity, next week's tool, just to find the icon in Applications.

---

## after class

- [ ] Connect and check the student folders. Confirm every student has `week-01/lastname-hello.m4a` uploaded. Note missing students for follow-up; they didn't run the exit routine.
- [ ] Log any technical issues (broken stations, server or login trouble, gear that didn't work) so they're fixed before Mon Aug 24.
- [ ] If the server or logins had problems, debrief with Inés about what happened and what to fix.
- [ ] Email any students whose files are missing. Keep it friendly, and make sure they know how to upload before Monday.

---

## what to assess

Nothing in Module 1 is graded. The deliverable (`lastname-hello.m4a` uploaded to the server) checks that each student made it through Day 1 and ran the exit routine. The only check is whether each student's file is in the right place on the server: yes or no, no rubric.

A student whose file is still missing by Monday's class may need extra support, especially with the sync workflow. Reach out individually.

---

## what students bring starting Wk 2

- Headphones (the lab provides them; students may bring their own wired pair)
- A notebook or note-taking tool
