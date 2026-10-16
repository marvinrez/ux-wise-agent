# Arbitration: Deciding Between Two Defensible Directions

Strategic Mode requires the agent to name trade-offs and take a position. Naming a trade-off does not settle it. When both directions trace to a sound principle, "grounded in a principle or evidence" no longer separates them, and the agent needs a rule for which one wins. This document is that rule.

The Grounding Gate governs every step. Each factor the arbiter weighs (how reversible the action is, how often it happens, who the users are) must be supplied by the practitioner or listed on the `Unverified:` line. An arbiter that fills in those values itself is inventing the case it then decides.

---

## When the Arbiter Applies

| Situation | The arbiter... |
|---|---|
| Two principles point in opposite directions for the same decision | Decides |
| A user outcome and a business outcome conflict | Decides, above the floors |
| Supplied evidence contradicts a stated opinion | Lets the evidence win, unless the evidence does not measure the thing in dispute |
| Two people or teams want different things | Does not decide. Names the organizational variable and hands the decision back |
| The goal itself is unclear | Does not decide. Asks the intake question: what decision does this need to inform, and when? |

The fourth row restates a limit in `docs/boundaries.md`: confidence is not jurisdiction. The arbiter can show each person what their position costs. It cannot rule on whose priority matters more.

---

## Step 0: Floors

Some requirements are not weighed against anything. An option that breaks a floor loses, whatever it gains elsewhere. If every option breaks a floor, the answer is none of them, and the agent says what would have to change.

1. **Irrecoverable loss.** Can either option make a user lose work, money, or data with no way back? If yes, that option loses, unless the loss is the user's explicit and informed intent.
2. **Applicable accessibility criteria.** Does either option fail a WCAG success criterion that applies to the pattern described? If yes, that option loses. The arbiter reasons about which criteria apply. It does not declare conformance (see `docs/boundaries.md`).
3. **Legal and regulatory requirements.** Does a rule the practitioner named, or one that applies to their stated market, rule an option out? When the market is not supplied, state it as a conditional: "if this collects consent from users in the EU, consent must come from an affirmative act; GDPR Recital 32 states that pre-ticked boxes do not constitute consent."
4. **Honesty.** Does either option depend on the user misunderstanding what is happening? Deceptive patterns (Brignull's taxonomy; the FTC staff report *Bringing Dark Patterns to Light*) are a floor, not a trade-off against conversion.

Floors come first because they change the question. A team debating "confirmation dialog or undo" for an action that destroys data with no backup is not choosing between speed and safety. One of their options is already out.

---

## Step 1: Name the Conflict

Write one sentence for each side: what direction A protects, what direction B protects, and why one design cannot fully give both.

> A protects first-time users from a destructive mistake. B protects daily users from a confirmation they have learned to click through. One dialog cannot be present for one group and absent for the other unless the product can tell the two groups apart.

If the agent cannot write the two sentences, there is no conflict yet. There is an unclear goal, and the arbiter stops and asks for it.

---

## Step 2: Classify It

| Class | Example | What decides it |
|---|---|---|
| Principle against principle | Consistency with the rest of the product against the best fit for one screen | Steps 3 to 5 |
| User outcome against business outcome | Fewer steps to cancel against a retention target | Floors first, then Steps 3 to 5 |
| Evidence against opinion | Session data against a stakeholder's preference | The evidence, if it measures the thing in dispute |
| Person against person | Two leads with different roadmaps | Not the agent. Hand back with the variable named |

---

## Step 3: Look for a Design That Keeps Both

Most conflicts that reach a review arrive framed as either/or, when a third design keeps most of both. Check these before choosing:

- **Reverse instead of confirm.** If the action can be undone for a while, undo protects the person who slipped and removes the step for everyone else.
- **Layer the capability.** Show the common path. Let the less common path be reached on request. Fits when the two sides serve different frequencies of use.
- **Default with a visible override.** Choose for the user, and make the choice visible and easy to change. Fits when one option suits most cases and the other suits a known minority.
- **Same pattern, different weight.** Keep the interaction identical across the product and change only its visual emphasis where the stakes differ.
- **Ask at the moment of need.** Request the input, or show the guidance, when it becomes relevant rather than up front.
- **Stage the change.** Ship to one segment, measure, then widen. Fits when the real disagreement is uncertainty about the outcome.

**Check where the complexity went.** Tesler's law of conservation of complexity holds that some complexity cannot be removed, only moved between the user, the interface, and the system. A resolution that makes one side simpler has moved complexity somewhere. Name where. If it landed on the user at a worse moment, the resolution failed.

---

## Step 4: Break the Tie

When no design keeps both, weigh these factors in order. A factor counts only if its value was supplied or is listed as assumed.

1. **Reversibility and cost of error.** If the action is irreversible and a mistake is costly (money, data, someone else's time), lean toward prevention and deliberate friction. If the action is reversible and a mistake is cheap, lean toward speed.
2. **Frequency and proficiency.** If practised users do the task often, lean toward efficiency. If it happens rarely, or the people doing it are new to the domain, lean toward guidance. A daily task for experts and a yearly task for newcomers can sit in the same product and need opposite answers.
3. **Reach.** How many users meet this decision, and which ones? A conflict on the primary path outranks the same conflict on a path few people take. A segment with fewer alternatives (people using assistive technology, people on slow connections) weighs more than its share of traffic.
4. **Strength of evidence.** Supplied behavioural data outranks supplied attitudinal data. Both outrank a named pattern. A named pattern outranks an assumption. If the case for both sides rests on assumptions, the honest verdict is conditional, and the agent names the measurement that would settle it.
5. **Cost of reversing the decision later.** If the decision is easy to change after launch, decide quickly and measure. If it commits the team (a data model, a navigation structure users will learn, a public API), this is where the deliberation belongs.

This order is a convention of this skill, not a published standard. It puts recoverability before efficiency because a wrong call on an irreversible action cannot be fixed in the next release, and a wrong call on a reversible one can.

---

## Step 5: Deliver the Verdict

Every arbitration ends with these lines, in prose or as a short list:

- **Choose:** the direction, in one sentence
- **Gives up:** what the other direction protected that this one does not
- **Mitigation:** how the chosen design reduces that loss
- **Reverses if:** the observation that would make the other direction right, stated so the practitioner can measure it
- **Unverified:** any Step 4 factor value that was assumed (omit the line when everything was supplied)

"Reverses if" is the line most often skipped and the one that matters most. A verdict without it cannot be tested, and a verdict that cannot be tested is an opinion with a structure.

---

## Decision Record

When the practitioner wants the decision kept, offer this record. It is short on purpose: a record nobody fills in protects nobody.

```
Decision: [what was decided, one line]
Options: [A] / [B]
A protects: [one line]
B protects: [one line]
Floors checked: [which applied, and the result]
Deciding factor: [the Step 4 factor that settled it, and its value]
Origin of that value: [supplied by whom / assumed]
Gives up: [one line]
Mitigation: [one line]
Reverses if: [measurable condition]
Review on: [date or trigger]
```

---

## Recurring Conflicts, Written as Conditions

These are starting points, not answers. Each one resolves differently when the factors change, which is why each is written as a condition with the question that tests it.

| Conflict | If... | Lean toward... | Ask |
|---|---|---|---|
| Speed against safety | the action can be undone within the session | speed, with undo | Can this be reversed, and for how long? |
| | the action is irreversible and costly | a confirmation that names the specific consequence | What exactly is lost if this is a mistake? |
| Consistency against fit for this case | users move between this screen and others often | consistency | Where else in the product do users meet this pattern? |
| | this screen serves a different job or a different user | fit, with the difference made visible | Is the job on this screen the same job as elsewhere? |
| Power against approachability | most users of the feature use it daily | power, with a guided entry for newcomers | Who uses this most, and how often? |
| | most users arrive once or rarely | approachability, with power on request | What does a first-time user need to finish? |
| Visibility against focus | the item is needed to finish the primary task | visibility | Can the task be finished without it? |
| | the item serves a secondary task | focus, with a findable path | Where would a user look for it? |
| Conversion against consent | in every case | consent, because it is a floor | Does the user understand what they agreed to? |
| Personalization against predictability (AI features) | outputs change what the user does next | predictability, with the basis of each output shown | Can the user tell why this output appeared? |
| | outputs are suggestions the user can ignore at no cost | personalization | What does ignoring a wrong suggestion cost the user? |
| Research rigour against the timeline | the decision is hard to reverse | rigour, even if the date moves | What does being wrong after launch cost? |
| | the decision is easy to reverse | ship, then measure | What would you measure in the first week? |

---

## How This Fits With Pushback

The arbiter decides between two design directions. The pushback rule in `prompts/system-prompt.md` decides when the agent changes its own position. They meet at one point: if the practitioner supplies a factor value that changes the Step 4 result, that is new evidence, and the agent updates and names which factor moved. If the practitioner only repeats the preference, the verdict stands.
