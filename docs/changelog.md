# Changelog

---

## v2.2.1 (Current Release)

**Release date:** 2026

**Fixed: `SKILL.md` frontmatter now passes the skill upload validator**
The claude.ai skill uploader accepts only `name`, `description`, `license`, `allowed-tools`, `metadata`, and `compatibility` in the frontmatter, and limits the description to 1,024 characters. v2.2.0 had a top-level `version` key and a 1,195-character description, so it could not be uploaded. The version now sits under `metadata`, and the description was rewritten at 1,024 characters or fewer with the same triggers and the same exclusions.

---

## v2.2.0

**Release date:** 2026

This release turns four things the skill named but never made operational into rules: how to settle a trade-off, which states to ask about, when a psychological principle applies, and how bad a problem is. Each is written as conditions and questions, and the Grounding Gate governs all four.

**New: Arbitration (`knowledge/arbitration.md`)**
Strategic Mode required naming trade-offs but gave no rule for settling one when both sides trace to sound principles. The arbiter checks floors first (irrecoverable loss, applicable accessibility criteria, legal requirements, honesty), names what each side protects, classifies the conflict (organizational conflicts are handed back), looks for a design that keeps both, and only then applies a fixed tie-break order: reversibility and cost of error, frequency and proficiency, reach, strength of evidence, cost of reversing later. Every verdict states what would reverse it. Includes a decision record and recurring conflicts written as conditions.

**New: States and edge cases (`knowledge/states-and-edge-cases.md`)**
A state inventory, transitions, and edge case questions by category: data, time, repeated and concurrent actions, access, environment, lifecycle. The governing rule: a state the practitioner did not supply is a question, never a finding.

**New: Applied psychology (`knowledge/applied-psychology.md`)**
The principles the system prompt names, each with its mechanism, when it applies, when it does not, the question that tests it, and where it becomes manipulation. Contested or misread claims (choice overload, "seven plus or minus two" for menus, the three-click rule, "users don't scroll", the Zeigarnik effect) are flagged as not settled. Also covers Gestalt grouping (proximity, similarity, common region, Prägnanz, uniform connectedness), applied only to supplied layouts; selective attention and change blindness; the paradox of the active user; flow; and Postel's law. Pareto, Parkinson, and Occam sit in a separate section as product heuristics, not psychology.

**New: Severity (`knowledge/severity.md`)**
Nielsen's 0 to 4 scale, bound to supplied artifacts. Frequency and persistence are supplied or assumed, ratings are for the people affected rather than the average, a broken floor sets a minimum of 3, and no overall score is given for a product or a screen.

**Changed: system prompt, Strategic Mode, gate**
The system prompt carries a compact version of all four rules, so a paste-only install gets them. The gate names arbitration factors, severity factors, state contents, and principle scope as specifics that need an origin. Strategic Mode applies the arbiter when both sides are defensible, and its output ends with a "Reverses if" line.

**New: Acceptance probes 9 to 12**
Arbitration without context, severity without an artifact, a misapplied principle stated with confidence, and edge cases from a single screenshot.

**Fixed: probe 5 verdict**
Probe 5 expected "FAIL-stop on Check 4", but the specification stops a response only on Check 1 with nothing supplied. It now reads "FAIL on Check 4, repaired".

**Fixed: Miller and Hick in `knowledge/ux-principles.md`**
The Miller entry treated seven as a cap on visible menus, which contradicts recognition over recall in the same file. Both entries now state their scope.

**Fixed: `SKILL.md` collision and loading**
The lowercase `skill.md` (v1.0) mapped to the same path as `SKILL.md` on case-insensitive filesystems, and a clone on macOS checked out the v1.0 file, which has no frontmatter. It has been removed. `SKILL.md` now tells Claude Code to read the system prompt before the first response, because the skill file only summarizes it.

**New: Worked example 9**
An arbitration case where the verdict splits on one fact the practitioner did not supply.

---

## v2.1.0

**Release date:** 2026

This release closes three gaps that shared a single root: the skill claimed authority without a boundary, a verification step, or a named human.

**New: Scope boundary — `docs/boundaries.md`**
v2.0 had a scope limit covering what the skill *produces* (no wireframes, specs, or copy). It had nothing covering what the skill *knows*. The new boundary document draws the critique / invention line: the agent may reason one level above what it was given and zero levels below. Given "a three-step checkout," it reasons about three-step checkouts; it does not comment on button labels or error states it was never shown. The document lists what is in scope, what is out, and works through the borderline requests — "redesign this," "write the empty state copy," "is this accessible." The failure it prevents: a fluent, expert-sounding critique of an interface the agent invented because none was supplied.

**Changed: Skill description no longer says "always activate"**
The v2.0 frontmatter instructed unconditional activation for complex UX decisions. It now names what the skill must not be activated for — inventing interfaces, critiquing designs that have not been supplied, producing metrics or citations, declaring accessibility conformance.

**New: Grounding Gate — `docs/grounding-gate.md`**
A PASS/FAIL check the agent runs against its own draft, and that a human can run against the skill. Every specific in a response must trace to one of four origins: supplied by the practitioner, named as a public framework or standard, stated as an assumption, or written as a conditional. A specific with no origin is fabricated, and one fabricated specific fails the response. Four checks cover the ways fabrication enters this domain — Artifact (invented screens and elements), Evidence (invented numbers and studies), Behavior (claiming what *their* users did), Standard (approximate criterion numbers, which survive review because nobody checks a number that looks right).

FAIL means repair and re-run, not refuse. The single exception is an Artifact failure with nothing supplied, where the response stops and asks for the design.

**New: Visible `Unverified` line**
Responses that pass the gate on assumptions or conditionals now list them on one plain line at the end. It exists for auditability — the practitioner and their reviewer can see which load-bearing parts are the agent's construction. It is explicitly not a disclaimer: a claim that should not have been made gets repaired, not labelled.

**New: Acceptance probes**
Eight prompts with expected verdicts, for verifying that the gate is active in a given installation and after any system prompt edit or model change. Probe 8 is a normal question with full context, checking that the gate has not become a mute button — a skill that refuses everything is not safer, it is useless.

**New: Ownership requirement — `docs/ownership.md`**
The install is two minutes and the failure mode is not. Before the skill's output informs anything beyond one person's desk, a named human owner is required: one person who ran the probes, re-runs them after changes, reviews output on its way out of the team, and corrects the record when the agent is wrong. The document includes a table of which output classes can travel unreviewed and which cannot, an install checklist, and a minimum bar for API deployments, where no human sits in the loop by construction.

**New: Worked examples 7 and 8**
Example 7 shows the gate stopping a response — a critique requested with no artifact supplied. Example 8 shows the more common case: a draft that named an invented step, repaired into a conditional, delivered in full with the assumption surfaced. The analysis loses nothing and stops claiming to know what it does not.

**Updated: `prompts/system-prompt.md`, `SKILL.md`, `README.md`, `integrations/claude-skill.md`**
Boundary and gate embedded in the system prompt. Install paths in all three surfaces now include running the probes and naming the owner.

---

## v2.0.0

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

