# Changelog

---

## v2.0.0 — Current Release

**Release date:** 2026

**What changed:**

**New: Research Mode**
Added a fourth operational mode for study design and methodology reasoning. Research Mode establishes the decision a study needs to inform before recommending a method, provides protocol structure (screener criteria, session outline, discussion guide focus areas), and names the limits of what the research can answer. Trigger signals include "design a usability test for...", "what research method should I use", "help me write a discussion guide", and "how many participants do I need?"

**New: Context Intake Protocol**
The agent now has a defined approach for handling missing context. Rather than asking multiple clarifying questions, it makes one key assumption explicit, states it at the top of the response, and proceeds. This preserves response quality while respecting practitioner time. Full specification in `docs/intake-protocol.md`.

**New: Mode auto-inference**
Mode selection is now driven by contextual signals, not only by explicit mode keywords. The system prompt documents inference signals for each mode: time pressure and stated certainty direct to Direct Mode; expressed confidence without evidence directs to Provocative Mode; research activity language directs to Research Mode. Strategic Mode remains the default for open exploration.

**New: Pushback handling specification**
The system prompt now defines explicitly how the agent should respond when a practitioner disagrees. The agent examines whether the counterargument introduces new evidence or reasoning. If it does, it updates and explains what changed. If it does not, it holds the position and names why. Capitulating to preference rather than reasoning is named as a skill failure.

**New: Scope redirect protocol**
The agent now has explicit language for redirecting requests outside its scope (wireframes, specs, production copy) without being unhelpful. The redirect always offers the analytical foundation that should precede the out-of-scope deliverable.

**Fixed: SKILL.md format**
`skill.md` has been renamed to `SKILL.md` and updated with proper YAML frontmatter (`name`, `description`, `compatibility`, `version`) to comply with the Anthropic skills standard and enable correct triggering in Claude Code and Claude Projects.

**Fixed: Vocabulary constraint duplication**
The prohibited word list previously appeared in both `prompts/system-prompt.md` and `docs/vocabulary-constraints.md`. The system prompt now contains a summary with reference to the authoritative file. This eliminates maintenance drift between the two copies.

**Fixed: API model string**
The example API code in `SKILL.md` and `README.md` now references `claude-sonnet-4-6`, replacing the outdated model string from v1.0.

**Updated: Worked examples**
`examples/worked-examples.md` now includes six examples covering all four modes plus two edge cases: a pushback scenario (agent holds position) and a scope redirect. v1.0 had three examples covering the original three modes.

**New: `docs/intake-protocol.md`**
Full specification of the context intake behavior, including rules, context dimensions that matter most, and what the protocol does not do.

**New: `prompts/research-mode.md`**
Full behavioral specification for Research Mode, including trigger conditions, five-step protocol, method selection framework, protocol structure for qualitative and quantitative research, and a worked example.

---

## v1.0.0 — Initial Release

**Release date:** 2025

**What this version established:**

- Three operational modes: Strategic, Direct, Provocative
- Ten core capability areas with application-level knowledge documentation
- Vocabulary constraint policy with prohibited word list and reasoning
- Formatting rules covering structure, tone, and presentation
- Full system prompt for Claude and compatible LLM platforms
- Integration guides for Claude (Projects and API) and OpenAI Custom GPTs
- Knowledge base covering Nielsen's heuristics with applied commentary, behavioral psychology laws, and AI/UX considerations
- Three worked examples demonstrating each mode in a realistic UX scenario
- Contribution guide for extending or refining the skill

**Design decisions in v1.0:**

The skill was intentionally positioned above entry-level and intermediate UX practice. It does not define basic terms, does not provide tutorial-style explanations for established concepts, and does not soften positions to avoid disagreement. This is a deliberate choice — the target practitioner is senior, and the value of the skill diminishes if it hedges to accommodate a broader audience.

The three-mode structure reflects a theory about when different types of analysis are most valuable. Strategic Mode is the default because most UX decisions have downstream consequences that benefit from deliberation. Direct Mode exists because there are situations where deliberation is a liability. Provocative Mode exists because the most expensive design mistakes are the ones that felt certain.

