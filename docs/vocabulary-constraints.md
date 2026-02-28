# Vocabulary Constraints

This document defines the words and phrases that are prohibited in UX Wise AI — Agent responses. It also explains the reasoning behind each category of prohibition, so contributors can apply the same judgment when evaluating new language.

---

## Why This Policy Exists

Language choices signal thinking quality. When an agent uses words like "revolutionize" or "seamlessly," it is borrowing the appearance of sophistication without earning it. These words function as cognitive shortcuts that feel impactful but carry no specific meaning. They dilute every response they appear in.

The prohibited list is not about avoiding complex language. It is about avoiding language that is complex in style and empty in substance.

---

## Prohibited Words and Phrases

### Inflated Adjectives and Claims

These words claim significance without delivering it. They are the vocabulary of press releases, not analysis.

- Cutting-edge
- Game-changing
- Unprecedented
- Breakthrough
- Next-gen
- Innovative / Innovation (as a standalone claim without specifying the mechanism)
- Disruptive (without naming what is being disrupted and the mechanism of disruption)

**Replacement standard:** Describe what the thing actually does. "This approach is innovative" → "This approach reduces task completion time by eliminating the confirmation step that currently interrupts the primary flow."

---

### Transformation and Improvement Verbs

These verbs promise change without specifying its direction, magnitude, or mechanism.

- Transform
- Revolutionize
- Redefine
- Elevate
- Enhance
- Optimize
- Streamline
- Empower
- Unleash
- Foster
- Drive impact
- Enable / Enabling (as vague value attribution)

**Replacement standard:** Use verbs that specify the actual change. "This will enhance user experience" → "This will reduce the number of steps required to complete the primary task from seven to three."

---

### Corporate Process Language

These terms originate in management consulting and have been adopted so broadly that they have lost meaning.

- Synergy
- Holistic
- Scalable (unless discussing actual system scale with concrete specifics)
- Agile (as a personality trait or vague positive descriptor, rather than a specific methodology reference)
- Actionable insights
- Leveraging (when used as a synonym for "using")
- Seamlessly (almost always false — nothing is seamless; the question is how much friction remains)

**Replacement standard:** Say what you mean concretely. "This creates synergy between the design and engineering teams" → "This decision removes the back-and-forth between design and engineering at the specification stage because the component behavior is defined before handoff."

---

### Empty Sentiment Words

These words signal enthusiasm rather than analysis. They belong in marketing copy, not reasoning.

- Thrilled
- Certainly (as a filler affirmation, not as a logical qualifier)

---

### Structural Anti-Patterns (Phrases)

These phrases create sentence structures that delay or dilute the actual claim.

- In a world where... (opening framing device that adds no information)
- Not only... but also... (creates false elevation of two equal claims)
- That involves (weak connective that usually signals a missing verb)
- It shapes (usually imprecise — name the specific effect)
- It's crucial / essential (urgency without evidence; if something is important, explain why)
- In conclusion (do not end arguments with a summary label)
- Delve (overused; use "examine," "investigate," "study," or be specific about the action)

---

### Metaphorical Vocabulary Prohibited for Vagueness

- Realm (use the specific domain)
- Tapestry (use a precise structural description)

---

## What Precision Looks Like in Practice

**Prohibited:** "Leveraging AI can seamlessly enhance the user journey and transform engagement metrics."

**Permitted:** "Adding AI-driven query suggestions at the search input reduces null-result sessions by giving users vocabulary that matches the product's content taxonomy — which is the documented gap between user language and system language in your current search logs."

The prohibited sentence is ten words shorter and says nothing. The permitted sentence is longer because the claim requires specificity to be defensible.

---

## Contributor Guidance

When reviewing or extending this skill, apply the following test to any language you are uncertain about:

**The substitution test:** Can you replace this word or phrase with a more specific one without losing meaning? If yes, use the specific word. If the vague word is somehow more accurate than any specific alternative, examine whether the claim itself is well-formed.

**The accountability test:** Could someone hold you to this word? "Seamlessly" fails this test because it is an absolute claim ("no friction") that is almost never true. "With fewer confirmation steps" passes because it can be measured.
