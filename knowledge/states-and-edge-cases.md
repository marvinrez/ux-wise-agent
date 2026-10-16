# States and Edge Cases: What to Ask About a Design You Have Not Seen in Full

Most of a product is not the screen in the mockup. It is the same screen with no data, with too much data, mid-request, after a failure, for a user without permission, at 200% text size, on the hundredth visit. A review that looks only at the populated, successful state misses the places where users actually get stuck.

The agent cannot inspect those states unless they are supplied. That sets the rule for this whole document:

**A state the practitioner did not supply is a question, never a finding.**

"Your empty state has no call to action" is invention unless the empty state was shown. "What does this screen show the first time, before there is any data? If it shows a blank table, a new user has no next step" is reasoning. A screenshot supplies one state. The others are still questions.

---

## Using This Document

1. List the states the practitioner supplied, by name.
2. For the rest, ask the questions below. Ask only the ones that could change the decision at hand. A full sweep in answer to a small question fails the proportional-depth standard.
3. Rank the open questions by what a bad answer would cost (see `knowledge/severity.md`, and Step 4 of `knowledge/arbitration.md`).
4. In the response, keep what was reviewed apart from what was asked: `Reviewed: [states supplied]. Not supplied: [states]`.

---

## The State Inventory

Every screen and most components pass through some of these states. For each one the questions are the same: does it exist, what does it show, and how does the user leave it?

| State | Variants worth asking about | Question |
|---|---|---|
| Populated | a typical amount of data; one item; the most the product allows | What does this look like with one item, and with the most the product permits? |
| Empty | first use; no results for a search or filter; everything cleared or completed; no permission to see the contents | When there is nothing to show, does the user learn why and what to do next? |
| Loading | first load; refresh; loading more; background sync | Does the user know something is happening, and can they keep working in the meantime? |
| Partial | some items loaded and some failed; a long task partly done | If part of the request fails, can the user see what succeeded and what did not? |
| Error | input the user can fix; system failure; network failure; permission denied; timeout | Does each error say what happened, whose problem it is, and what to do next, with the user's input still in place? |
| Success | confirmation of a finished action; a result that arrives later | How does the user know it worked, and what can they do next? |
| Disabled | not available yet; not available to this role; not available on this plan | Does the user learn why it is unavailable and how to make it available? |
| Read-only or locked | someone else is editing; the record is archived; approval is pending | Is it clear that the user cannot edit, and why? |
| Stale or offline | data out of date; connection lost; changes queued | Can the user tell the data is out of date, and what happens to changes made offline? |

---

## Transitions

States are half of the picture. Users also get lost moving between them.

- **Entry and exit.** For each supplied state, how does the user arrive, and how do they leave? A state with no exit is a trap.
- **Preservation.** When a request fails, is everything the user typed still there? Losing input on an error turns a recoverable problem into an abandoned task.
- **Interruption.** What happens if the user leaves mid-flow (closes the tab, follows a notification, loses the connection) and comes back later?
- **Order.** Can the user reach a later step without passing through the earlier ones (a deep link, a bookmark, the back button)? What does the later step show when its inputs are missing?

---

## Edge Case Questions by Category

Ask these as questions, or write them as conditionals. None of them is a statement about the product until the practitioner answers.

### Data

- What happens at zero, at one, and at the maximum the product allows? What happens one past the maximum?
- What does the layout do with the longest realistic value: a long name, a long translated label, an unbroken string such as an email address or a URL?
- Do names and text with diacritics, non-Latin scripts, right-to-left scripts, or emoji display and sort correctly?
- What shows when an optional field was never filled in?
- Are numbers, currency, dates, and units formatted for the user's locale?

### Time

- What does the user see while waiting? Nielsen's response-time limits are the reference: about 0.1 second feels instantaneous, about 1 second keeps the user's flow of thought although the delay is noticed, and about 10 seconds is the limit for keeping attention on the task. If a supplied operation can pass one of these limits, ask what the user sees at that point.
- What happens when a session expires mid-task? WCAG 2.2.1 Timing Adjustable (Level A) requires that users can turn off, adjust, or extend most time limits.
- Are times shown in the user's time zone? What happens across a daylight-saving change, or with a date in the past where only future dates make sense?

### Repeated and Concurrent Actions

- What happens if the user submits twice, or taps the same control several times quickly?
- If two people edit the same record, whose change survives, and does the other person find out?
- Is there an undo, and how long does it stay available?
- Inside a multi-step flow, what do the back button and refresh do?

### Access and Roles

- Does every role see the same screen? What does a user without permission see: the control disabled with a reason, the control hidden, or an error after trying?
- What happens if access is removed while the user is mid-task?
- What does the screen look like when a feature is turned off for this account or plan?

### Environment

- Does the layout still work with text enlarged to 200% (WCAG 1.4.4 Resize Text, Level AA) and in a viewport 320 CSS pixels wide (WCAG 1.4.10 Reflow, Level AA)?
- Can every control be reached and operated with a keyboard alone, with focus visible at all times?
- Are status changes (saved, failed, finished loading) announced to screen readers without moving focus? WCAG 4.1.3 Status Messages (Level AA) covers this.
- Are touch targets at least 24 by 24 CSS pixels, or spaced so that smaller targets do not crowd each other? WCAG 2.5.8 Target Size (Minimum), Level AA, added in WCAG 2.2, sets this with listed exceptions.
- If the interface animates in response to the user, does it respect the operating system's reduced-motion setting?
- What happens on a slow connection and a low-end device, rather than on the team's own hardware?

### Lifecycle

- What does the first visit look like, and what does the hundredth? Guidance that helps once becomes noise on every later visit.
- What does a user returning after months away see? Has anything they relied on moved?
- What happens to existing users and their data when this ships: migration, defaults for settings they never chose, notice of the change?
- How does a user leave: cancel, delete the account, export their data? Is leaving as clear as joining?
- Does the process ask users to type something they already entered earlier in the same process? WCAG 3.3.7 Redundant Entry (Level A, added in WCAG 2.2) covers this.

---

## How the Gate Applies

- **Artifact check.** Describing the contents of a state ("the error says...", "the empty state shows...") fails unless that state was supplied.
- **Behavior check.** "Users will get stuck here" fails. "If the empty state offers no next step, a first-time user has nowhere to go" passes as a conditional.
- **Standard check.** The criteria cited above are WCAG 2.2 success criteria, as published by the W3C in October 2023. Re-check numbers and levels when a new version of WCAG is published. When unsure of a number, cite the requirement in words.
- **Proportion.** Forty questions in reply to a two-sentence description is not rigour. Ask the three that could change the decision, and offer the rest on request.
