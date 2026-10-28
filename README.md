# UX Wise AI (Agent)

**A high-performance UX reasoning agent built for designers, product managers, and researchers who need a peer-level intellectual counterpart, not a feature suggester.**

UX Wise AI operates at the intersection of rigorous design thinking, behavioral psychology, product strategy, and research methodology. It holds positions, challenges weak reasoning, and delivers verdicts with the precision of a senior practitioner who has seen how these decisions fail in production.

---

## What This Is

UX Wise AI is a structured skill definition designed for Claude (Anthropic), custom GPTs, and any LLM platform that accepts system-level instructions. The skill turns a general-purpose language model into a focused UX reasoning partner with a defined critical posture, vocabulary constraints, and four operational modes.

This is not a collection of UX tips. It is a reasoning framework that interrogates problems before offering direction.

**What it is not:** a design generator. It cannot see interfaces, does not hold your product data, and does not know what your users did. It reasons about design decisions and stops at the edge of what you gave it. See [When Not to Use This Skill](#when-not-to-use-this-skill).

---

## Who It Is Built For

- Senior UX designers navigating ambiguity at scale
- Product leads making trade-off decisions under constraint
- Design researchers who need a second opinion with precision
- Teams pressure-testing design decisions before shipping

---

## Knowledge Areas

| Capability | Description |
|---|---|
| User-Centered Design | Heuristics, usability principles, interaction patterns, and failure modes |
| Problem-Solving and Product Thinking | Frameworks for decomposing complex UX challenges into tractable decisions |
| Behavioral Psychology | Principles with their scope attached, and the contested ones named as contested |
| Accessibility and Inclusion | WCAG, cognitive load, and universal design applied to real product decisions |
| AI and Automation in UX | Where AI helps design, where it distorts it, and how to tell the difference |
| Ethics and Responsibility | Dark patterns, fairness in interfaces, trust as a design material |
| Research Methodology | Study design, method selection, protocol structure, and analysis approach |
| Communication and Influence | How to present design decisions to stakeholders who think in revenue, not flows |

---

## Operational Modes

### Strategic Mode (Default)

Deep analysis. Examines trade-offs, surfaces hidden constraints, references real-world precedents, and takes a position. Use this when the decision has downstream consequences you cannot easily reverse.

### Direct Mode

One recommendation. No hedging. The reasoning is present but compressed. Use this when you need to move and cannot afford to deliberate.

### Provocative Mode

Adversarial reasoning. Argues against your assumptions to expose where your logic breaks. Use this before finalizing any decision you feel confident about. Confidence without interrogation is a design liability.

### Research Mode *(new in v2.0)*

Study design and methodology reasoning. Establishes what decision the research needs to inform before recommending a method. Provides protocol structure: screener criteria, session outline, discussion guide focus areas. Use this when designing or evaluating a research activity.

---

## When Not to Use This Skill

Three facts set the boundary: the skill cannot see interfaces, does not hold your product data, and does not know what your users did.

**Critique is in scope. Invention is not.** They produce identical-looking output and differ only in where the specifics came from. Given "a three-step checkout," the skill reasons about three-step checkouts. It does not comment on your button labels, your field order, or your error states, because it was not told them. The failure this prevents: you ask it to "review this design," give it two sentences, and it invents the screen it was never shown and then critiques its own invention. The critique reads as expert. It is about nothing.

Do not use it to:

| Request | Why it is out of reach |
|---|---|
| Invent an interface: wireframes, specs, component structures, mockups, production copy | An invented interface carries invented specifics, and fluent prose makes those indistinguishable from real ones |
| Critique a design that has not been supplied | No image, no DOM, no Figma file, no recording. It declines rather than reconstructing |
| Supply facts about your product: conversion rates, drop-off, ticket volumes, quotes, test results | Yours to provide. It can reason about what a number means, not produce one |
| Produce citations as evidence | A specific study with a specific author and a specific percentage is the exact shape fabrication takes in this domain |
| Declare accessibility conformance | It reasons about which criteria apply; conformance is established by testing the built artifact, with assistive technology, by a person |
| Stand in for users | A synthetic usability finding is a hypothesis with the grammar of a result |
| Settle a decision whose real variable is organizational | It will produce a confident position anyway. Confidence is not jurisdiction |

Borderline cases ("redesign this," "write the empty state copy," "what do users expect here") are worked through in [`docs/boundaries.md`](docs/boundaries.md).

---

## Grounding Gate

The skill is built to sound certain. That is its function and its main hazard: a hedging agent that invents a detail gets caught, a confident one gets believed.

Before delivering a response, the agent tests every **specific** in its draft, meaning anything a reader could act on that is not a general principle. Each must trace to one of four origins: **supplied** by you, **named** as a public framework or standard, **assumed** and marked as such, or **conditional** ("if X, then Y"). A specific with no origin is fabricated, and one fabricated specific fails the whole response.

| Check | FAIL condition |
|---|---|
| Artifact | Names a screen, component, field, label, state, or step you did not supply |
| Evidence | Contains a number, study, author, date, or benchmark that is neither supplied nor precisely nameable |
| Behavior | States what *your* users did rather than what users *tend* to do |
| Standard | Cites a WCAG criterion, heuristic number, or statistical threshold approximately |

On FAIL, the response is repaired and re-run: ask for what is missing, restate at the resolution actually supplied, or convert the invented specific into a stated assumption. On FAIL at the Artifact check with nothing supplied, the response stops, and the agent says what it needs instead of producing the critique.

Responses that pass on assumptions or conditionals carry them visibly, on one plain line:

```
Unverified: [assumption or conditional], [assumption or conditional]
```

[`docs/grounding-gate.md`](docs/grounding-gate.md) holds the full specification and twelve **acceptance probes**: prompts with expected verdicts. [`gatecheck/`](gatecheck/README.md) carries those twelve plus three more as a suite that runs and returns an exit code. Run them in your environment before trusting an installation, and again after any system prompt edit or model change. The eighth probe checks that the gate has not simply become a mute button: a normal question with full context should still get a full answer.

The gate catches fabrication, not error. A response can pass every check and still be wrong about the trade-off.

---

## Reasoning Rules *(new in v2.2)*

Naming a trade-off does not settle it, and a principle cited outside its scope is a fabricated specific with a respectable name. Five references give the agent rules for both, and the Grounding Gate governs every one of them. Each is written as conditions and questions, so applying it never requires a detail you did not supply.

| Reference | What it decides |
|---|---|
| [`knowledge/arbitration.md`](knowledge/arbitration.md) | Which of two defensible directions wins: floors that are never traded, a design that keeps both, then a fixed tie-break order, and a verdict that states what would reverse it |
| [`knowledge/states-and-edge-cases.md`](knowledge/states-and-edge-cases.md) | Which states and edge cases to ask about. A state you did not supply is a question, never a finding |
| [`knowledge/applied-psychology.md`](knowledge/applied-psychology.md) | When a psychological or Gestalt principle applies, when it does not, where it becomes manipulation, and which popular claims are contested. Pareto, Parkinson, and Occam are kept apart as product heuristics |
| [`knowledge/severity.md`](knowledge/severity.md) | How bad a problem in a supplied artifact is, on Nielsen's 0 to 4 scale, rated for the people affected |
| [`knowledge/deceptive-patterns.md`](knowledge/deceptive-patterns.md) | Which patterns are deceptive, what must have been supplied before one can be claimed, which break the honesty floor, what is not one, and which market a requirement belongs to |

---

## Repository Structure

```
ux-wise-agent/
├── SKILL.md                          ← Master skill definition (Anthropic skills format)
├── README.md                         ← This file
├── prompts/
│   ├── system-prompt.md              ← Full system prompt for Claude and compatible LLMs
│   ├── starter-prompts.md            ← Curated prompt library
│   ├── strategic-mode.md             ← Strategic Mode prompt layer
│   ├── direct-mode.md                ← Direct Mode prompt layer
│   ├── provocative-mode.md           ← Provocative Mode prompt layer
│   └── research-mode.md              ← Research Mode prompt layer (new in v2.0)
├── examples/
│   └── worked-examples.md            ← Nine examples: four modes, pushback, scope redirect, two gate cases, one arbitration
├── .claude-plugin/
│   ├── plugin.json                   ← Plugin manifest for Claude Code (new in v2.3)
│   └── marketplace.json              ← Makes this repository its own marketplace (new in v2.3)
├── knowledge/
│   ├── arbitration.md                ← Deciding between two defensible directions (new in v2.2)
│   ├── deceptive-patterns.md         ← Deceptive patterns, each bound to a supplied artifact (new in v2.3)
│   ├── states-and-edge-cases.md      ← States and edge cases to ask about, as questions (new in v2.2)
│   ├── applied-psychology.md         ← Principles with their scope; contested claims flagged (new in v2.2)
│   ├── severity.md                   ← Severity scale for problems in supplied artifacts (new in v2.2)
│   ├── ux-principles.md              ← Core UX knowledge base
│   ├── heuristics.md                 ← Nielsen's heuristics with applied commentary
│   └── ai-ux-considerations.md       ← AI-specific UX reasoning guide
├── gatecheck/                        ← The acceptance probes as a runnable suite (new in v2.3)
│   ├── probes.toml                   ← The fifteen probes, declaratively
│   ├── checks.py                     ← The deterministic patterns, and the catalogue that names them
│   ├── run_probes.py                 ← Scaffold, read, report, exit code
│   ├── selftest.py                   ← Samples with known outcomes, both directions per pattern
│   ├── check_packaging.py            ← Both manifests parse, and their version is SKILL.md's
│   ├── fixtures/                     ← Pictures a probe sends. P12 needs one here
│   ├── runlog/                       ← One file per probe. These are the record
│   └── README.md                     ← What the two layers decide, and what the suite cannot supply
├── integrations/
│   ├── claude-skill.md               ← How to use as a Claude Project or API skill
│   └── custom-gpt.md                 ← How to deploy in OpenAI custom GPTs
├── LICENSE                           ← MIT
├── .gitignore
└── docs/
    ├── boundaries.md                 ← When not to use it: the critique / invention line (new in v2.1)
    ├── grounding-gate.md             ← PASS/FAIL check against fabricated UX + acceptance probes (new in v2.1)
    ├── ownership.md                  ← Named human owner and review requirements (new in v2.1)
    ├── contribution-guide.md         ← How to extend or refine the skill
    ├── vocabulary-constraints.md     ← Authoritative prohibited word list
    ├── intake-protocol.md            ← Context-gathering protocol (new in v2.0)
    └── changelog.md                  ← Version history
```

`.github/workflows/gatecheck.yml` runs the suite on every pull request, on
pushes to `main`, and on demand. It needs no key
and no secret, because nothing in `gatecheck/` calls a model.

---

## Quick Start

**Before you install: name an owner.**

The install takes two minutes. The failure mode does not. This skill produces senior-sounding analysis at volume, some of it will be wrong, and a fraction of the wrong part will be fabricated rather than merely mistaken. Neither the model nor this repository can be held to that. A person has to be.

Before the skill's output informs anything beyond your own desk, name one human owner, in writing, where your team actually looks. Their accountability is small and specific: they ran the acceptance probes, they re-run them after any system prompt edit or model change, output that leaves the team passed under their eye first, and when the agent is wrong in a way that reached someone, they correct it. Not the tool. Them.

Working alone? You are the owner by default, and the probes are how you find out what you are working with. Full checklist and the review table (which outputs can travel unreviewed and which cannot) in [`docs/ownership.md`](docs/ownership.md).

**Which path.** Installing as a plugin if you work in Claude Code, because the
skill then activates on its own description and the files travel with it. Paste
the system prompt if you work on claude.ai or through the API, because there is
nothing to install there. The two are the same rules; what differs is who loads
them.

**Using with Claude Code (plugin)**

```
/plugin install ux-wise-agent --marketplace marvinrez/ux-wise-agent
```

The repository is its own marketplace, so that line registers it and installs the
skill in one step. On Claude Code before 2.1.275, add the marketplace first with
`/plugin marketplace add marvinrez/ux-wise-agent` and then install. To load a
local checkout without installing anything, start Claude Code with
`claude --plugin-dir /path/to/ux-wise-agent`.

Once installed the skill activates on its own description.
`prompts/system-prompt.md` is still the operating rules, so read it before the
first response in a session. Then run the suite in
[`gatecheck/`](gatecheck/README.md), which is the twelve acceptance probes in
[`docs/grounding-gate.md`](docs/grounding-gate.md) plus two for the
deceptive-pattern catalogue and one for the pushback rule, and name the owner.

**Using with Claude (claude.ai)**

1. Open a new Project in Claude
2. Paste the contents of `prompts/system-prompt.md` into the Project instructions
3. Run the acceptance probes and confirm each behaves as specified. Twelve are specified in [`docs/grounding-gate.md`](docs/grounding-gate.md) and three more live in [`gatecheck/probes.toml`](gatecheck/probes.toml); with the repository checked out, `python gatecheck/run_probes.py --scaffold` sets all fifteen up to paste into
4. Name the owner where your team will see it
5. Start with a starter prompt or go straight to your problem

**Using via Anthropic API**

```python
import anthropic

with open("prompts/system-prompt.md", "r") as f:
    system_prompt = f.read()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    system=system_prompt,
    messages=[
        {"role": "user", "content": "Give me three alternative UX solutions for reducing drop-off in enterprise onboarding."}
    ]
)
print(message.content[0].text)
```

---

## Starter Prompts

```
Give me three alternative UX solutions for [insert problem or scenario].

How do I balance business goals and user needs when designing [insert feature]?

What are the best UX patterns for [insert feature]?

Challenge my assumptions about [insert UX principle or direction].

How do I design for uncertainty and ambiguity in [insert complex problem]?

What research method should I use to understand [insert user behavior or decision]?

Design a usability test for [insert feature or flow].

How do I present [insert design decision] to stakeholders who will push back on it?
```

---

## Design Principles of This Skill

**Positions, not suggestions.** The agent takes a stance. It explains why one direction is stronger than another. It does not offer five equally valid options and ask you to choose.

**Evidence before opinion.** Every claim is anchored to a principle, a behavioral pattern, or a documented failure mode. Opinions without grounding are not offered.

**Clarity under complexity.** The harder the problem, the more important the structure. This agent does not retreat into abstraction when problems get complicated.

**No performative safety.** The agent does not hedge every recommendation with "it depends." It accounts for context and then commits.

**Certainty only where it is earned.** Committing to a position and inventing a detail are different acts, and fluent prose hides the difference. The Grounding Gate is the line between them: reason hard, stop at the edge of what you were given, and mark what is assumed.

---

## Vocabulary Constraints

This skill enforces a strict vocabulary policy. Words that signal vague, corporate, or inflated thinking are prohibited. See `docs/vocabulary-constraints.md` for the full list and reasoning.

---

## License

MIT License. Free to use, modify, and distribute. Attribution to UX Wise AI is appreciated but not required.

---

## Author

Marcos Rezende, Senior Product Designer, AI/UX Systems
[marcosrezende.com](https://marcosrezende.com)

