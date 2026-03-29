# UX Wise AI (Agent)

**A high-performance UX reasoning agent built for designers, product managers, and researchers who need a peer-level intellectual counterpart, not a feature suggester.**

UX Wise AI operates at the intersection of rigorous design thinking, behavioral psychology, product strategy, and research methodology. It holds positions, challenges weak reasoning, and delivers verdicts with the precision of a senior practitioner who has seen how these decisions fail in production.

---

## What This Is

UX Wise AI is a structured skill definition designed for Claude (Anthropic), custom GPTs, and any LLM platform that accepts system-level instructions. The skill transforms a general-purpose language model into a focused UX reasoning partner with a defined critical posture, vocabulary constraints, and four operational modes.

This is not a collection of UX tips. It is a reasoning framework that interrogates problems before offering direction.

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
│   └── worked-examples.md            ← Six examples across all four modes
├── knowledge/
│   ├── ux-principles.md              ← Core UX knowledge base
│   ├── heuristics.md                 ← Nielsen's heuristics with applied commentary
│   └── ai-ux-considerations.md       ← AI-specific UX reasoning guide
├── integrations/
│   ├── claude-skill.md               ← How to use as a Claude Project or API skill
│   └── custom-gpt.md                 ← How to deploy in OpenAI custom GPTs
└── docs/
    ├── contribution-guide.md         ← How to extend or refine the skill
    ├── vocabulary-constraints.md     ← Authoritative prohibited word list
    ├── intake-protocol.md            ← Context-gathering protocol (new in v2.0)
    └── changelog.md                  ← Version history
```

---

## Quick Start

**Using with Claude (claude.ai)**

1. Open a new Project in Claude
2. Paste the contents of `prompts/system-prompt.md` into the Project instructions
3. Start with a starter prompt or go straight to your problem

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

