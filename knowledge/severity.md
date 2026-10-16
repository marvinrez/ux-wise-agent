# Severity: Ranking Problems in What Was Supplied

A critique that lists ten problems at the same volume leaves the practitioner to do the ranking. This document gives the agent a scale and the rules for using it inside the Grounding Gate.

---

## Scope

Rate severity only for:

- a problem in an artifact the practitioner supplied (a flow, copy, a screenshot, a recording, a written description), at the resolution supplied
- a problem the practitioner described and asked to have ranked

Do not rate a state that was not supplied (see `knowledge/states-and-edge-cases.md`). An unsupplied state gets a question. If the answer could turn out to be severe, say so as a conditional.

Do not compute one overall score for a product or a screen. A total built from a description hides which parts were seen and which were assumed, and it reads as a measurement when it is a judgment.

---

## The Scale

This is Nielsen's severity scale for usability problems, in this skill's words.

| Rating | Name | What it means | Priority |
|---|---|---|---|
| 0 | Not a usability problem | A preference or a disagreement, not something users will run into | None |
| 1 | Cosmetic | Users notice it, but it does not slow or stop anyone | Fix when there is time |
| 2 | Minor | Users are slowed or frustrated, and they recover | Low priority |
| 3 | Major | Users fail the task, or recover only with real effort | High priority |
| 4 | Catastrophe | Users cannot complete the task | Fix before release |

---

## The Factors

Nielsen bases severity on three factors, and adds market impact for the product as a whole:

- **Frequency:** how often the problem occurs among the users who reach that point
- **Impact:** how hard it is to get past when it occurs
- **Persistence:** whether users get past it once and move on, or meet it again every time

These factors need data the agent usually does not have. Impact can often be reasoned from the artifact. Frequency and persistence usually cannot: they come from analytics, support tickets, or testing. When they are not supplied:

- rate on impact alone and say so, or
- give the range and the factor that decides it: "3 if most users reach this step, 2 if it sits on a path few take. Your funnel data settles which."

Each assumed factor goes on the `Unverified:` line.

---

## Rules

1. **Rate for the people affected, not for the average.** A problem that blocks every screen reader user is a 4 for those users, even when they are a small share of traffic. Averaged across everyone, accessibility failures look cosmetic.
2. **Floors set a minimum.** A problem that breaks a floor in `knowledge/arbitration.md` (irrecoverable loss, an applicable accessibility criterion, a legal requirement, deception) is rated 3 or higher. This minimum is a convention of this skill.
3. **Rank, then group.** Present the highest ratings first. Group problems that share a cause. One fix for the cause outranks several fixes for its symptoms.
4. **Rate the problem, not the fix.** Severity says how bad the problem is for users. Effort to fix goes in its own column, so a cheap fix for a 2 is never mistaken for a 4.
5. **One rater is not enough for a real audit.** Nielsen found that severity ratings from a single evaluator are unreliable and recommended combining ratings from several evaluators. When the ratings will drive a roadmap, say so.

---

## Output

| # | Problem | Where (as supplied) | Severity | Deciding factor | Origin of that factor | Effort to fix |
|---|---|---|---|---|---|---|
| 1 | [problem] | [the supplied step, screen, or quote] | 3 (2 if [condition]) | [frequency / impact / persistence] | [supplied / assumed] | [low / medium / high, or unknown] |

The "Where" column must point to something the practitioner supplied. If it cannot, the row does not belong in this table. It belongs in the questions.

---

## How the Gate Applies

- **Artifact check:** the "Where" rule above.
- **Evidence check:** "affects 30% of users" fails unless that figure was supplied. Frequency stays a range or a condition.
- **Behavior check:** "users abandon here" fails without data. "If users reach this step without X, they cannot continue" passes.
- **Standard check:** the rating names and numbers follow the table above exactly.
