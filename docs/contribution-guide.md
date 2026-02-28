# Contribution Guide

---

## Who This Is For

This guide is for practitioners who want to extend, refine, or fork the UX Wise AI — Agent skill. Contributions are welcome if they meet the reasoning and quality standards the skill is built on.

---

## What Can Be Extended

**Prompts**

The system prompt can be updated to add capabilities, refine mode specifications, or adjust the tone policy. Any change to the system prompt should be tested against the three worked examples in `examples/worked-examples.md` — if the change causes the agent to produce lower-quality responses to those prompts, the change needs revision.

**Knowledge Files**

New knowledge documents can be added to the `knowledge/` directory. Knowledge files must meet the following standard:

- They document how a principle or framework is applied, not just what it is
- They identify common misapplications — where practitioners get it wrong
- They do not reproduce copyrighted material verbatim
- They reference primary sources by author and concept, not by URL (URLs decay)

**Examples**

New worked examples should demonstrate a realistic practitioner question and a response that meets the full quality standard of the relevant mode. Examples that are too simple do not demonstrate what the skill is capable of. Examples that are too idealized do not reflect how practitioners actually ask questions.

**Integrations**

Integration guides for new platforms are welcome. They should include:

- Platform-specific configuration steps with specificity (no vague instructions)
- Known limitations on that platform
- Any capability adjustments required for the platform (features that do not translate)

---

## Quality Standards for Contributions

Every contribution must meet these standards before it is merged:

**No prohibited vocabulary.** Run any new text against the prohibited word list in `docs/vocabulary-constraints.md`. The list exists for a reason — additions that import prohibited language undermine the skill's core quality signal.

**No hedged positions.** If a knowledge document or prompt addition takes a position, it should take it clearly. "Some practitioners prefer X while others prefer Y" is not analysis — it is the absence of analysis. Take the position and explain it.

**No generic examples.** Examples should reference specific product contexts, specific user populations, or specific design decisions. Generic examples ("imagine a user who wants to do something") do not demonstrate the reasoning quality the skill is designed to produce.

**Grounded claims.** Every claim in a knowledge document should be traceable to a named researcher, a documented study, or a well-established professional standard. "Studies show" without attribution is not acceptable.

---

## How to Submit

1. Fork the repository
2. Create a branch named for the specific change (e.g., `add-research-methodology-knowledge`, `refine-provocative-mode-specification`)
3. Make your changes
4. Test against the worked examples in `examples/worked-examples.md` if you changed the system prompt
5. Open a pull request with a description that explains what changed and why

---

## What Will Not Be Accepted

- Changes that soften the skill's critical posture to make it more agreeable
- Additions that import corporate or consulting vocabulary from the prohibited list
- New modes or personas that duplicate the existing three without clear differentiation
- Knowledge content that is tutorial-level rather than practitioner-level
- Examples that do not reflect realistic practitioner questions
