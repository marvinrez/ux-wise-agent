# Contribution Guide

---

## Who This Is For

This guide is for practitioners who want to extend, refine, or fork the UX Wise AI — Agent skill. Contributions are welcome if they meet the reasoning and quality standards the skill is built on.

---

## What Can Be Extended

### System Prompt and Mode Specifications

The system prompt (`prompts/system-prompt.md`) and individual mode files (`prompts/strategic-mode.md`, `prompts/direct-mode.md`, `prompts/provocative-mode.md`, `prompts/research-mode.md`) can be updated to add capabilities, refine mode behaviors, or adjust the tone policy.

Any change to the system prompt must be tested against all six worked examples in `examples/worked-examples.md`. If the change causes the agent to produce lower-quality responses to those prompts, the change needs revision.

**Adding a new mode:** New modes must be structurally distinct from the existing four — not a variation of tone, but a different reasoning posture applied to a different type of practitioner need. The mode must have:
- A clear trigger condition
- A behavioral specification (what the agent does differently in this mode)
- A defined output structure
- At least one worked example in `examples/worked-examples.md`
- A corresponding prompt layer file in `prompts/`

### Knowledge Files

New knowledge documents can be added to the `knowledge/` directory. Knowledge files must meet the following standard:

- They document how a principle or framework is **applied**, not just what it is
- They identify common misapplications — where practitioners get it wrong
- They do not reproduce copyrighted material verbatim
- They reference primary sources by author and concept, not by URL (URLs decay)
- They are written at senior practitioner level — no definitions of basic terms

### Examples

New worked examples should demonstrate a realistic practitioner question and a response that meets the full quality standard of the relevant mode. The `examples/worked-examples.md` file accepts additions in the following categories:

- A standard example for an existing mode (anchor it to a specific product type or industry)
- An edge case example (vague question, pushback scenario, out-of-scope redirect, multi-mode pivot)
- A Research Mode example demonstrating a specific method type (qualitative, quantitative, IA testing)

Examples that are too simple do not demonstrate what the skill is capable of. Examples that are too idealized do not reflect how practitioners actually ask questions.

### Integrations

Integration guides for new platforms are welcome. Add them to `integrations/`. They must include:

- Platform-specific configuration steps (no vague instructions)
- Known limitations or capability gaps on that platform
- Any adjustments required for the platform (e.g., context window constraints, system prompt field limitations)

### Vocabulary Constraints

New prohibited words or phrases can be added to `docs/vocabulary-constraints.md`. Each addition must include:

- The word or phrase
- The category it belongs to
- Why it fails the accountability or substitution test
- The replacement standard

Do not add words to the prohibited list that are precise and useful in the right context. The goal is to prohibit vague language, not to reduce the vocabulary available for accurate description.

---

## Quality Standards for All Contributions

**No prohibited vocabulary.** Run any new text against `docs/vocabulary-constraints.md` before submitting. The vocabulary constraints apply to documentation, examples, and knowledge files — not only to the system prompt.

**No hedged positions.** If a knowledge document or worked example takes a position, take it clearly. "Some practitioners prefer X while others prefer Y" is not analysis — it is the absence of analysis. Take the position and explain it.

**No generic examples.** Examples must reference specific product contexts, specific user populations, or specific design decisions. Generic examples ("imagine a user who wants to accomplish something") do not demonstrate the reasoning quality this skill is designed to produce.

**Grounded claims.** Every substantive claim in a knowledge document must be traceable to a named researcher, a documented study, or a well-established professional standard. "Studies show" without attribution does not meet the standard.

**No tutorial content.** This skill is built for senior practitioners. Do not add content that defines basic UX terms or explains foundational concepts. If a concept is in any introductory UX textbook, it does not need to be defined here — it needs to be applied.

---

## What Will Not Be Accepted

- Changes that soften the skill's critical posture to make it more agreeable
- Additions that import corporate or consulting vocabulary from the prohibited list
- New modes that duplicate the existing four without clear structural differentiation
- Knowledge content that is tutorial-level rather than practitioner-level
- Examples that do not reflect realistic practitioner questions
- API examples using deprecated model strings (always use the current models listed in `integrations/claude-skill.md`)

---

## How to Submit

1. Fork the repository
2. Create a branch named for the specific change
   - Format: `add-[thing]` for new content, `fix-[thing]` for corrections, `refine-[thing]` for improvements
   - Examples: `add-research-methodology-knowledge`, `fix-vocabulary-constraints`, `refine-provocative-mode-spec`
3. Make your changes
4. Test against `examples/worked-examples.md` if you changed the system prompt or any mode file
5. Open a pull request with a description that explains what changed and why the change improves the skill

---

## File Map for Contributors

| File | Purpose | Touches what |
|---|---|---|
| `SKILL.md` | Anthropic skills-format master definition | Skill metadata, mode overview, quick start |
| `prompts/system-prompt.md` | LLM system prompt | Identity, modes, reasoning standards, vocabulary summary, formatting |
| `prompts/[mode]-mode.md` | Behavioral spec for each mode | Mode triggers, step-by-step protocol, output structure, example |
| `docs/boundaries.md` | Scope boundary spec | What the skill must not be used for; the critique / invention line |
| `docs/grounding-gate.md` | Anti-fabrication check and acceptance probes | Any change to the gate requires re-running all eight probes |
| `docs/ownership.md` | Accountability and review requirements | Who answers for the output; install checklist |
| `docs/vocabulary-constraints.md` | Authoritative prohibited word list | All contributions must pass this |
| `docs/intake-protocol.md` | Context-gathering behavior spec | How the agent handles missing context |
| `examples/worked-examples.md` | Worked examples for all modes | Test cases for system prompt changes |
| `knowledge/` | Domain knowledge base | Applied frameworks, heuristics, AI/UX guidance |
| `integrations/` | Platform setup guides | Claude, OpenAI, API usage |

