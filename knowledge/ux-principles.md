# UX Principles: Knowledge Base

This document provides the core UX knowledge the agent draws from. It is not a tutorial. It is a reference that records how each principle is applied in practice and where practitioners typically misapply it.

**Source of the ten heuristics below:** they are Jakob Nielsen's, from *Enhancing the explanatory power of usability heuristics* (CHI 1994), maintained since by the Nielsen Norman Group. Each **Principle** line here is this file's own statement of the heuristic, not a quotation. `knowledge/heuristics.md` carries the longer applied reference; this file carries the commentary.

---

## Nielsen's 10 Usability Heuristics: Applied Commentary

### 1. Visibility of System Status

**Principle:** The user can tell what the system is doing, from the system, without having to guess or wait in silence.

**Where it is misapplied:** Loading spinners that appear without context. Progress indicators with no connection to real progress (the bar that jumps to 90% and stalls). Status messages that describe the system's internal state rather than the user's task state ("Processing request" vs. "Saving your changes — done in a moment").

**The underlying question:** After any user action, can the user confirm that the system received it and is acting on it? If the honest answer is "no," the heuristic is being violated.

---

### 2. Match Between System and the Real World

**Principle:** The vocabulary on screen is the one the user already has, not the one the database or the team uses.

**Where it is misapplied:** Error messages written by developers for developers. Feature names derived from the product's internal architecture rather than the user's mental model. Navigation labels that describe the technology stack ("API Manager") rather than the user's task ("Connect your tools").

**The underlying question:** If a user read this label, message, or instruction without any product context, would it tell them anything useful about what they should do?

---

### 3. User Control and Freedom

**Principle:** Getting out of a wrong turn costs one visible action, not a sequence the user has to complete first.

**Where it is misapplied:** Multi-step flows with no back button. Confirmation dialogs that confirm destructive actions but do not offer an undo. Settings changes that take effect immediately without an obvious reset path. The absence of this heuristic is often intentional — it is where dark patterns begin.

**The underlying question:** What happens when the user makes the wrong choice? Can they recover without contacting support?

---

### 4. Consistency and Standards

**Principle:** The same thing is named and behaves the same way in every place it appears.

**Where it is misapplied:** Design systems that are maintained in Figma but diverge in code. Terminology that changes across product areas because different teams owned them at different times. Icon usage that is internally inconsistent — the same icon meaning two different things in two different contexts.

**The underlying question:** If a user learned this interaction pattern in section A of the product, does it work the same way in section B?

---

### 5. Error Prevention

**Principle:** The best error message is the one that was never needed, because the condition that caused it was designed out.

**Where it is misapplied:** Allowing invalid input to be submitted before validation fires. Date pickers that allow impossible date ranges. Bulk action confirmations that describe the action in abstract terms rather than showing the user what will actually be affected. "Are you sure?" dialogs that do not show what "are you sure" refers to.

**The underlying question:** What is the most common mistake users make at this point? Is the interface designed to make that mistake impossible, or just to explain it after it happens?

---

### 6. Recognition Over Recall

**Principle:** Nothing the user needs is held only in their head between one step and the next.

**Where it is misapplied:** Command interfaces with no discoverability for new users. Keyboard shortcut-only features with no menu equivalents. Contextual actions that appear only on hover, making them invisible on touch devices. Search bars with no suggested queries or recent history for returning users.

**The underlying question:** Does the user need to remember something from a previous session, a previous step, or a prior mental state in order to proceed? If yes, that is a recall requirement — consider whether the interface can surface that information instead.

---

### 7. Flexibility and Efficiency of Use

**Principle:** The frequent path can be made faster by the person who walks it daily, without that speed getting in the beginner's way.

**Where it is misapplied:** Products that force all users through the same flow regardless of their expertise or frequency of use. Onboarding flows that cannot be skipped by returning users. No keyboard navigation in a product used primarily by power users.

**The underlying question:** Who are the daily users of this feature? Does the interface serve their actual usage pattern, or the hypothetical first-time user pattern?

---

### 8. Aesthetic and Minimalist Design

**Principle:** Everything on screen competes with everything else for attention, so an element that is not needed now is taking visibility from one that is.

**Where it is misapplied:** Dashboard widgets that display every available metric regardless of user role. Modals with three paragraphs of legal text before the action button. Navigation menus with 15 items because stakeholders requested parity with the sitemap.

**The underlying question:** If you removed this element, would a user completing their primary task notice its absence? If not, it is a candidate for removal or deprioritization.

---

### 9. Help Users Recognize, Diagnose, and Recover from Errors

**Principle:** An error names what happened, where, and what to do about it, in words the user already understands.

**Where it is misapplied:** Error code displays ("Error 403") with no plain language translation. "Something went wrong" messages with no recovery path. Form validation that marks the field red but does not specify what was wrong with the input. Backend error messages surfaced directly to users without translation.

**The underlying question:** After reading this error message, does the user know (a) what happened, (b) whether it is their fault or the system's, and (c) what to do next?

---

### 10. Help and Documentation

**Principle:** Help is reachable from where the task is, searchable, scoped to what the user is doing, and short enough to be read in the middle of the work.

**Where it is misapplied:** Feature-organized help centers that require users to know the product's taxonomy before they can search it. Help articles written in feature-release language ("New in v2.4: the enhanced dashboard") rather than task language ("How to view your team's performance data"). Contextual help that links to a help center home page rather than the relevant article.

**The underlying question:** If a user types their actual problem into the help search, does it return the article that solves it?

---

## Laws and Psychological Principles

### Fitts's Law
The time to acquire a target is a function of the distance to and size of the target. Practical application: primary action buttons should be large and positioned where the cursor or finger naturally rests. The worst-performing button placement is far from the user's natural resting position and small.

### Miller's Law
Working memory holds only a few items at once. Miller put the span near seven (plus or minus two); later work by Cowan argues that core capacity is closer to four chunks. Practical application: the limit constrains what users must remember across steps or screens, such as a code, a price, or an earlier choice. It does not set a maximum for a menu the user can see, because a visible menu is recognition, not recall. The principle that matters is that working memory is finite and chunking helps. Scope and common misreadings: `knowledge/applied-psychology.md`.

### Hick's Law
The time to make a decision increases logarithmically with the number of choices available, when the user knows the options and picks among them. Practical application: reducing the number of options does not always mean reducing functionality; it means reducing the decision cost. Progressive disclosure is one application of Hick's Law: fewer visible options at the start, with the ability to reveal more. It does not apply when the user is looking for an item they can already name; that is search, and it depends on labels and layout.

### Cognitive Load Theory (Sweller)
Three types of load affect learning and task completion: intrinsic (the inherent complexity of the task), extraneous (the load added by poor design), and germane (the load used to build understanding). Good UX design reduces extraneous load — it does not make the task simpler than it is, but it does not add complexity that is not inherent to the task.

### Fogg Behavior Model
Behavior = Motivation × Ability × Prompt. A user will take an action if they are sufficiently motivated, have the ability to do it, and receive a prompt at the right moment. Misapplication: using this model to design manipulative systems that exploit motivation without considering whether the action is in the user's interest.

### Peak-End Rule (Kahneman)
Users judge an experience based primarily on how they felt at the most intense point and at the end — not on the average of all moments. Practical application: invest disproportionately in the experience at key moments (error recovery, task completion, first success) rather than optimizing every screen equally.
