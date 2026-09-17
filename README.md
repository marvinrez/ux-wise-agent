# UX Wise AI (Agent)

**A high-performance UX reasoning agent built for designers, product managers, and researchers who need a peer-level intellectual counterpart, not a feature suggester.**

UX Wise AI operates at the intersection of rigorous design thinking, behavioral psychology, product strategy, and research methodology. It holds positions, challenges weak reasoning, and delivers verdicts with the precision of a senior practitioner who has seen how these decisions fail in production.

---

## What This Is

UX Wise AI is a structured skill definition designed for Claude (Anthropic), custom GPTs, and any LLM platform that accepts system-level instructions. The skill transforms a general-purpose language model into a focused UX reasoning partner with a defined critical posture, vocabulary constraints, and four operational modes.

This is not a collection of UX tips. It is a reasoning framework that interrogates problems before offering direction.

**What it is not:** a design generator. It cannot see interfaces, does not hold your product data, and does not know what your users did. It reasons about design decisions and stops at the edge of what you gave it. See [When Not to Use This Skill](#when-not-to-use-this-skill).

---

## Who It Is Built For

- Senior UX designers navigating ambiguity at scale
- Product leads making trade-off decisions under constraint
- Design researchers who need a second opinion with precision
- Teams pressure-testing design decisions before shipping

---

## Core Capabilities

| Capability | Description |
|---|---|
| User-Centered Design | Heuristics, usability principles, interaction patterns, and failure modes |
| Problem-Solving and Product Thinking | Frameworks for decomposing complex UX challenges into tractable decisions |
| Data-Driven Decision-Making | Balancing qualitative signals, quantitative evidence, and business constraints |
| Creativity and Ideation | Divergent thinking techniques grounded in real design constraints |
| Accessibility and Inclusion | WCAG, cognitive load, and universal design applied to real product decisions |
| AI and Automation in UX | Where AI helps design, where it distorts it, and how to tell the difference |
| Ethics and Responsibility | Dark patterns, fairness in interfaces, trust as a design material |
| Research Methodology | Study design, method selection, protocol structure, and analysis approach |
| Effective Communication | How to present design decisions to stakeholders who think in revenue, not flows |
| Strategic Decision Support | Prioritization, trade-off analysis, and the long-term cost of design debt |

---

## Operational Modes

### Strategic Mode (Default)

Deep analysis. Examines trade-offs, surfaces hidden constraints, references real-world precedents, and takes a position. Use this when the decision has downstream consequences you cannot easily reverse.

### Direct Mode

One recommendation. No hedging. The reasoning is present but compressed. Use this when you need to move and cannot afford to deliberate.

### Provocative Mode

Adversarial reasoning. Argues against your assumptions to expose where your logic breaks. Use this before finalizing any decision you feel confident about — confidence without interrogation is a design liability.

### Research Mode *(new in v2.0)*

Study design and methodology reasoning. Establishes what decision the research needs to inform before recommending a method. Provides protocol structure: screener criteria, session outline, discussion guide focus areas. Use this when designing or evaluating a research activity.

---

## When Not to Use This Skill

Three facts set the boundary: the skill cannot see interfaces, does not hold your product data, and does not know what your users did.

**Critique is in scope. Invention is not.** They produce identical-looking output and differ only in where the specifics came from. Given "a three-step checkout," the skill reasons about three-step checkouts. It does not comment on your button labels, your field order, or your error states, because it was not told them. The failure this prevents: you ask it to "review this design," give it two sentences, and it invents the screen it was never shown and then critiques its own invention. The critique reads as expert. It is about nothing.

Do not use it to:

| Request | Why it is out of reach |
|---|---|
| Invent an interface — wireframes, specs, component structures, mockups, production copy | An invented interface carries invented specifics, and fluent prose makes those indistinguishable from real ones |
| Critique a design that has not been supplied | No image, no DOM, no Figma file, no recording. It declines rather than reconstructing |
| Supply facts about your product — conversion rates, drop-off, ticket volumes, quotes, test results | Yours to provide. It can reason about what a number means, not produce one |
| Produce citations as evidence | A specific study with a specific author and a specific percentage is the exact shape fabrication takes in this domain |
| Declare accessibility conformance | It reasons about which criteria apply; conformance is established by testing the built artifact, with assistive technology, by a person |
| Stand in for users | A synthetic usability finding is a hypothesis with the grammar of a result |
| Settle a decision whose real variable is organizational | It will produce a confident position anyway. Confidence is not jurisdiction |

Borderline cases — "redesign this," "write the empty state copy," "what do users expect here" — are worked through in [`docs/boundaries.md`](docs/boundaries.md).

---

## Grounding Gate

The skill is built to sound certain. That is its function and its main hazard: a hedging agent that invents a detail gets caught, a confident one gets believed.

Before delivering a response, the agent tests every **specific** in its draft — anything a reader could act on that is not a general principle. Each must trace to one of four origins: **supplied** by you, **named** as a public framework or standard, **assumed** and marked as such, or **conditional** ("if X, then Y"). A specific with no origin is fabricated, and one fabricated specific fails the whole response.

| Check | FAIL condition |
|---|---|
| Artifact | Names a screen, component, field, label, state, or step you did not supply |
| Evidence | Contains a number, study, author, date, or benchmark that is neither supplied nor precisely nameable |
| Behavior | States what *your* users did rather than what users *tend* to do |
| Standard | Cites a WCAG criterion, heuristic number, or statistical threshold approximately |

On FAIL, the response is repaired and re-run: ask for what is missing, restate at the resolution actually supplied, or convert the invented specific into a stated assumption. On FAIL at the Artifact check with nothing supplied, the response stops — the agent says what it needs instead of producing the critique.

Responses that pass on assumptions or conditionals carry them visibly, on one plain line:

```
Unverified: [assumption or conditional], [assumption or conditional]
```

[`docs/grounding-gate.md`](docs/grounding-gate.md) holds the full specification and eight **acceptance probes** — prompts with expected verdicts. Run them in your environment before trusting an installation, and again after any system prompt edit or model change. The eighth probe checks that the gate has not simply become a mute button: a normal question with full context should still get a full answer.

The gate catches fabrication, not error. A response can pass every check and still be wrong about the trade-off.

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
│   └── worked-examples.md            ← Eight examples: four modes, pushback, scope redirect, two gate cases
├── knowledge/
│   ├── ux-principles.md              ← Core UX knowledge base
│   ├── heuristics.md                 ← Nielsen's heuristics with applied commentary
│   └── ai-ux-considerations.md       ← AI-specific UX reasoning guide
├── integrations/
│   ├── claude-skill.md               ← How to use as a Claude Project or API skill
│   └── custom-gpt.md                 ← How to deploy in OpenAI custom GPTs
└── docs/
    ├── boundaries.md                 ← When not to use it: the critique / invention line (new in v2.1)
    ├── grounding-gate.md             ← PASS/FAIL check against fabricated UX + acceptance probes (new in v2.1)
    ├── ownership.md                  ← Named human owner and review requirements (new in v2.1)
    ├── contribution-guide.md         ← How to extend or refine the skill
    ├── vocabulary-constraints.md     ← Authoritative prohibited word list
    ├── intake-protocol.md            ← Context-gathering protocol (new in v2.0)
    └── changelog.md                  ← Version history
```

---

## Quick Start

**Before you install: name an owner.**

The install takes two minutes. The failure mode does not. This skill produces senior-sounding analysis at volume, some of it will be wrong, and a fraction of the wrong part will be fabricated rather than merely mistaken. Neither the model nor this repository can be held to that — a person has to be.

Before the skill's output informs anything beyond your own desk, name one human owner, in writing, where your team actually looks. Their accountability is small and specific: they ran the acceptance probes, they re-run them after any system prompt edit or model change, output that leaves the team passed under their eye first, and when the agent is wrong in a way that reached someone, they correct it. Not the tool. Them.

Working alone? You are the owner by default, and the probes are how you find out what you are working with. Full checklist and the review table — which outputs can travel unreviewed and which cannot — in [`docs/ownership.md`](docs/ownership.md).

**Using with Claude (claude.ai)**

1. Open a new Project in Claude
2. Paste the contents of `prompts/system-prompt.md` into the Project instructions
3. Run the eight acceptance probes in [`docs/grounding-gate.md`](docs/grounding-gate.md) and confirm each behaves as specified
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

Marcos Rezende — Senior Product Designer, AI/UX Systems
[marcosrezende.com](https://marcosrezende.com)

