# Ownership — Who Is Accountable for What This Skill Produces

Installing this skill takes two minutes. Deciding who answers for its output takes longer, and skipping that step is how a reasoning tool becomes an unattributed source in someone's roadmap.

This document exists because the install instructions are frictionless and the failure mode is not. The agent produces senior-sounding analysis at volume. Some of it will be wrong, and a fraction of the wrong part will be fabricated rather than merely mistaken. Neither the model nor this repository can be held to that. A person has to be.

---

## The Requirement

**Before this skill informs any decision beyond your own desk, name a human owner for it.**

One person. Named in the project, the Slack channel topic, the Confluence page, or wherever the team actually looks. Their accountability is specific and small:

1. They ran the acceptance probes in `docs/grounding-gate.md` in the environment where the skill is installed, and the probes behaved as specified.
2. They re-run those probes after any edit to `prompts/system-prompt.md` or after a model change in the deployment.
3. Any output from this skill that leaves the team — into a deck, a spec, a research plan, a stakeholder email, a ticket — passed under their eye first, or carries an explicit mark that it did not.
4. When the agent is wrong in a way that reached someone, they say so and correct it. Not the tool. Them.

The owner does not need to be the most senior person. They need to be a practitioner who can tell a grounded claim from a fluent one in this domain, which is a different qualification from seniority and occasionally the opposite of it.

---

## What Requires Review Before It Travels

| Output | Review needed | Why |
|---|---|---|
| Your own thinking, in your own session | None | The reader and the reviewer are the same person |
| A position you will argue in a design review | Read it against the gate | You will be asked "where does that come from" and the answer has to be yours |
| Anything containing a number, a study, or a citation | Verify every one | This is where fabrication concentrates and where it survives longest |
| A research protocol before it runs with participants | Full review by whoever owns the research | A flawed screener burns a recruit budget and produces confident garbage |
| An accessibility claim | Testing, not review | The agent cannot establish conformance; see `docs/boundaries.md` |
| A stakeholder-facing summary or exec narrative | Full review, attributed to you | An executive cannot tell this skill's output from yours, and will hold you to it either way |
| Anything that will reach a user | Full review plus the normal path it would take if a person wrote it | The skill is not a shortcut around the process that catches harm |

---

## What the Owner Is Not Accountable For

They did not build the model and they cannot fix its failure modes. The commitment is procedural: probes run, outputs reviewed on the way out, errors owned and corrected. An owner who does those three things and still ships a wrong recommendation made a normal professional mistake. An owner who never ran the probes and lets unreviewed output travel made a different one.

---

## Install Checklist

Not a two-minute install. A two-minute install plus a decision.

- [ ] Skill installed by one of the methods in `integrations/claude-skill.md`
- [ ] Acceptance probes from `docs/grounding-gate.md` run in that environment, all eight behaving as specified
- [ ] Human owner named, in writing, somewhere the team reads
- [ ] Team told what the skill does not do — see the "Do Not Use This Skill For" list in `docs/boundaries.md`
- [ ] Review expectation agreed for the output classes in the table above
- [ ] Re-probe scheduled against model upgrades and system prompt edits

If you are one person reasoning alone, the first two items still apply. You are the owner by default, and the probes are how you find out what you are working with.

---

## For Teams Deploying This via API

An API deployment removes the human from the loop by construction, which moves the entire burden to the interface you build around it. Minimum bar:

- The `Unverified` line specified in `docs/grounding-gate.md` renders in the UI rather than being stripped as noise. It is the only signal your users get.
- The interface states what the agent cannot see. A UX reasoning agent in a product surface will be asked to review screens, and every one of those requests is a Check 1 FAIL.
- Output is attributed to the tool in the interface, not presented as a colleague's opinion or as a research finding.
- Someone owns the deployment, with the same four commitments listed above, and an actual route for users to report a fabrication.

A deployment with none of these is a fluent text generator pointed at design decisions with nobody watching it.
