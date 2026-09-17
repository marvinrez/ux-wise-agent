# Boundaries — When to Use This Skill and When Not To

This skill reasons about design decisions. It does not see interfaces, it does not hold your product data, and it does not know what your users did last quarter. Those three facts set the boundary.

The failure this document prevents: a practitioner asks the agent to "review this design," provides a two-sentence description, and the agent invents the screen it was not shown — the fields, the labels, the hierarchy, the empty state — and then critiques its own invention. The critique reads as expert. It is about nothing.

---

## Use This Skill For

| Request | Why it fits |
|---|---|
| "Should I use tabs or a sidebar for this navigation?" | A pattern trade-off decided by principle and context, not by inspection |
| "Challenge my assumption that mobile-first is right here" | Adversarial reasoning against a stated premise |
| "What research method answers whether users understand this pricing model?" | Method selection from a decision |
| "How do I present this accessibility debt to a VP who thinks in revenue?" | Framing and communication strategy |
| "Here is the flow [pasted, described in full, or attached]. Where does it break?" | Critique of an artifact the practitioner supplied |
| "We ran this test and got this result. What can it actually prove?" | Interpretation of evidence the practitioner supplied |

The pattern: the reasoning is the deliverable, and every specific in the answer comes from a principle, from the practitioner, or from a source that can be named.

---

## Do Not Use This Skill For

**Inventing an interface.** The skill does not produce wireframes, screen specifications, component structures, visual mockups, or production copy. This is not a modesty clause — it is a correctness constraint. An invented interface carries invented specifics, and invented specifics are indistinguishable from real ones in fluent prose.

**Critiquing an interface the agent cannot see.** "Review this design" with no design attached is the single highest-risk request in this skill's surface. The agent has no image, no DOM, no Figma file, no screen recording. What it can critique is a description, and only to the depth of the description supplied. If the description says "a three-step checkout," the agent may reason about three-step checkouts. It may not comment on the button labels, the field order, or the error states, because it was not told them.

**Producing facts about your product.** Conversion rates, drop-off numbers, support ticket volumes, user quotes, session counts, and A/B results are yours. The agent has none of them. It can reason about what a number would mean if you supplied it; it cannot supply it.

**Citing research as evidence for a decision that needs your evidence.** The agent reasons from documented patterns and named frameworks. It is not a literature search tool, it does not have a citation index, and a specific study title with a specific author and a specific percentage is the shape hallucination takes most often in this domain. Treat any such citation as a lead to verify, never as a source.

**Settling a decision that belongs to a person.** Prioritization under political constraint, hiring, vendor selection, and anything where the real variable is organizational rather than behavioral. The agent will produce a confident position because that is what it is built to do. Confidence is not jurisdiction.

**Standing in for users.** The agent is not a participant, not a panel, and not a substitute for a study. A synthetic usability finding is a hypothesis with the grammar of a result.

---

## The Critique / Invention Line

Critique and invention look the same in output. They differ only in where the specifics came from.

| The agent is critiquing | The agent is inventing |
|---|---|
| Reasoning about a flow the practitioner described, at the resolution they described it | Naming screens, fields, labels, or states the practitioner never mentioned |
| "Three steps before the value is visible is long for a trial signup, because…" | "Your step two asks for company size, which is premature because…" (nobody said step two asks that) |
| "Whatever your error copy says, error recovery in this pattern usually fails because…" | "Your error message 'Something went wrong' is unhelpful because…" (nobody quoted the error) |
| Applying a documented failure mode to the described situation | Reporting a failure mode as observed in the practitioner's product |

The rule: **the agent may reason one level above what it was given, and zero levels below.** It can generalize from a description. It cannot fill in the description.

When the agent needs a detail it was not given, the correct move is to ask for it or to mark the gap, not to supply it. See `docs/grounding-gate.md` for the check that enforces this and `docs/ownership.md` for who is accountable when it fails.

---

## Requests That Sit on the Line

**"Redesign this."** Out of scope as stated. In scope if reframed: the agent can reason about what the redesign has to solve, what the constraints rule out, and how to tell whether the redesign worked. The artifact is yours to make.

**"Write the empty state copy."** Out of scope as a first output. The skill's scope limit stands: copy that does not come from an established user need and communicative intent is filler. In scope after the need is established, and then only as options a writer edits.

**"What do users expect here?"** In scope as a claim about documented patterns, with the pattern named. Out of scope as a claim about your users. Those are different sentences and the agent is required to write the one it can support.

**"Is this accessible?"** In scope for reasoning about the criteria that apply to the pattern described. Out of scope as a verdict — a conformance claim requires testing the built artifact against the standard, with assistive technology, by a person.
