# Server file retention and archival policy — MUS 381

**Status:** Current.
**Owner:** Inés Thiebaut (course PI and lab manager).
**Last updated:** August 2026.

## Purpose

To define what happens to MUS 381 student working files on the class server over time: when they stay, when they are removed, and who removes them.

## Scope

This policy applies to:

- Student working folders on the class server, one per student, created by the server on first login and named with the student's NetID
- Project deliverables and final exports stored in those folders
- The contents of `/public`: the shared sample bank, class listening folders, and any TA or instructor working files for MUS 381

This policy does **not** apply to:

- Grade records, course rosters, or other registrar-managed data
- Student-owned files stored on personal devices or personal cloud accounts
- Files stored elsewhere on CSUEB systems outside the class server

## The server

An SFTP server at `sftp://134.154.190.239`, port 22, reachable from inside the lab only. Students authenticate with their NetID and NetID password. Total capacity is 4 TB.

## Storage states

Files exist in one of two states:

1. **On the server** — read-write, in the student's own folder or in `/public`. This is the normal state and has no expiry.
2. **Deleted** — permanently removed. Cannot be recovered.

There is no separate archive tier and no automatic deletion. Nothing leaves the server except by a deliberate action taken by the instructor.

## Lifecycle

Student folders remain on the server after the semester ends. They stay through winter and summer breaks, through a repeat of MUS 381 in a later term, and through continuation into Sound Design or other downstream courses.

Once a year, in summer, the instructor reviews the student folders and clears folders belonging to students who have left CSUEB or who are not continuing with coursework that uses the lab. "Not continuing" means: not enrolled in MUS 381 again, not enrolled in Sound Design or another course that uses the lab server, and not in a graduate program with continued lab access.

`/public` is cleared of the prior term's `mus-381-fall-YYYY/` folder at the same review. The sample bank and module asset folders under `/public` are semester-stable and stay.

## Notification

Students are notified twice:

- **At enrollment in MUS 381**, the syllabus and Day 1 orientation mention file retention and point to this document.
- **Before any deletion**, students receive an email from the instructor at least four weeks before the review date. The notice includes the date, instructions for downloading their files, and a contact path for questions or requests for extension.

## Responsibilities

**Instructor (course PI):**

- Owns this policy.
- Confirms the "not continuing" student list each summer.
- Sends the notification email.
- Performs the deletions.
- Handles requests for extension.
- Updates this policy as the course evolves.

**Teaching assistant:**

- Builds the term's `/public` folders before the semester starts.
- Verifies student uploads through the term.
- Drafts the notification email for the instructor's signature.

**IT:**

- Provides and maintains the server, accounts, and capacity.
- Handles NetID authentication and password resets.

## Student rights

Students may, at any time before deletion:

- Download their own files from their folder on the server, from inside the lab.
- Request an extension if they need more time, are returning from leave, or have an ongoing project that would benefit from continued access.
- Request that their files be deleted earlier than the default lifecycle would dictate.

Requests go to the instructor by email.

## Exceptions

The annual review skips a folder in cases including but not limited to:

- A student takes a leave of absence and intends to return.
- A student's MUS 381 work is part of an ongoing research project, performance, or portfolio.
- A student is using their final project as part of a graduate school or job application.
- The instructor or another faculty member identifies pedagogical or archival value in retaining a piece of student work as a reference example (with the student's written permission).

Extensions run in one-year increments. The instructor reviews active extensions each summer.
