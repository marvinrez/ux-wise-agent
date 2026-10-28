# Deceptive Patterns: Named, Scoped, and Only Claimed About What Was Sent

Step 0 of `knowledge/arbitration.md` makes honesty a floor: an option that depends
on the user misunderstanding what is happening loses without being weighed. That
floor names a taxonomy the repository does not carry, and an agent cannot refuse
a pattern it cannot name. This file carries it.

It is reference material the agent reads, not output the agent quotes. The
difference matters because of `docs/boundaries.md`: producing a study with an
author and a percentage is forbidden, while naming a public framework accurately
is the second of the four origins in the Grounding Gate. So the agent may say
"this is the hidden-costs pattern in Brignull's taxonomy, and the FTC's 2022
staff report *Bringing Dark Patterns to Light* covers it." It may not say "68% of
users abandon carts over late fees." The first names a source. The second
invents a finding.

Three rules govern every entry.

1. **A pattern is a claim about an artifact, so it needs a supplied artifact.**
   Each entry below carries the line *To claim it you need*. Without that
   evidence the pattern is a question, exactly as an unsupplied state is a
   question in `knowledge/states-and-edge-cases.md`. "Your cancellation flow
   buries the exit" is invention unless the flow was sent. "If cancelling takes
   more steps than subscribing did, that asymmetry is the pattern" is reasoning.
2. **No entry carries a rating.** `knowledge/severity.md` rates for the people
   affected, needs frequency and persistence that are rarely supplied, and
   forbids one score for a screen. A catalogue that stamps a pattern "High"
   regardless of who meets it or how often contradicts that file. So no entry
   below prints a number. What an entry does carry is whether it breaks the
   honesty floor, and `knowledge/severity.md` turns a broken floor into a
   minimum of 3 by a convention of this skill. That is a floor, not a rating:
   it sets the bottom and leaves the number to the person with the artifact.
3. **Effect, not intent.** Nobody has to have meant it. The tests in the law
   are written around what a practice does. Article 6(1) of the Unfair
   Commercial Practices Directive (2005/29/EC, amended by Directives 2019/2161
   and 2024/825, so work from the consolidated text) reaches a presentation
   that "deceives or is likely to deceive the average consumer, even if the
   information is factually correct". Read the rest of that paragraph before
   relying on it: the practice must also cause, or be likely to cause, a
   transactional decision the consumer would not otherwise have taken. That
   condition is the limit, and quoting the first half alone makes the test sound
   wider than it is. California defines a dark pattern at Civil Code
   § 1798.140(l) as an interface "designed or manipulated with the substantial
   effect of subverting or impairing user autonomy, decisionmaking, or choice",
   completed by regulation, and the California Privacy Protection Agency's
   Enforcement Advisory No. 2024-02 reads that as a test of effect rather than
   of intent.
   The agent has a second reason to stay off intent, and this one holds wherever
   the product operates: nobody sends a motive. A screen, a flow and a policy
   are artifacts. The decision behind them is not one, so an agent that asserts
   it has left the gate. Describe the mechanism and what it does to the user.

## Why the catalogue is short

Every entry has to survive two bars, and shows on its own lines that it did.

The first is provenance, on the entry's `Named in`, `Law` or `Guidance` line:
a name that traces to a public taxonomy, a regulator or a court, or, where no
such name exists, a statement that the entry is derived here and from what. The
second is a stated test for what must have been supplied before the agent may
claim it, on the `To claim it you need` line. A pattern that cannot pass both is
one the agent could only use by fabricating, so it is not here.

The derived case is written out rather than left blank on purpose. An entry that
reads as established when nothing established it is the Evidence check failing
inside the file that polices it, and it costs more than the entry is worth.
Length is not the property that makes a catalogue useful under the gate, and an
entry kept for completeness is an entry the gate has to stop later.

---

## What is not a deceptive pattern

Calling ordinary design deceptive is its own failure, and it is the one this
file most needs to prevent. The agent loses its standing to name a real pattern
if it names three false ones first.

- **Friction with a reason.** A confirmation on an irreversible action, a
  cooling-off step before a large transfer, a second factor at sign-in. The test
  in `knowledge/arbitration.md` applies: friction proportional to the cost of a
  mistake is protection. Friction attached to the choice the business dislikes
  is not.
- **Persuasion with the facts intact.** A genuinely limited edition, a real
  deadline, an accurate count of what is left. Persuasion becomes manipulation
  when the claim stops being true or the user cannot check it.
- **A default that serves most people.** A default is not a trick. It becomes
  one when it is set against the interest of the person who did not change it,
  when changing it is harder than accepting it, or when it is presented as
  though no choice existed.
- **A paid product being paid.** An upsell, a price, a plan comparison. The
  pattern is in concealment or misdirection, never in commerce.
- **A design that is merely bad.** A confusing label, a buried setting, an
  unreadable error. Incompetence and deception produce similar screens and call
  for different conversations. Where the mechanism has no beneficiary, treat it
  as a usability problem and rate it with `knowledge/severity.md`.

When the agent cannot tell which of these it is looking at, that is a question
for the practitioner, not a finding.

---

## 1. Withheld from the decision

The information the choice depends on arrives after the choice.

**Hidden costs**
- What it does: fees, taxes, shipping, or service charges appear only at the last
  step, after the user has invested effort and formed a price expectation.
- To claim it you need: the sequence of steps with the price shown at each, or
  the final step beside an earlier one.
- Not this when: the charge genuinely cannot be computed earlier (a destination
  the user has not entered) and the interface says so where the price appears.
- Floor: yes. The decision was made on a price that was not the price.
- Named in: Brignull's taxonomy. A disclosure failure under Section 5 of the FTC
  Act in the US, and within the UK's headline-price rule in *Drip pricing* below.

**Drip pricing**
- What it does: the total grows across several screens, each increment small
  enough to pass, so the figure the user compared against is never the figure
  they pay.
- To claim it you need: at least two steps showing the total changing, or a
  written description of the increments.
- Not this when: every component is listed with the running total visible at the
  point each is added.
- Floor: yes, where the first figure is presented as the price.
- Named in: the vocabulary of the competition authorities, among them the UK's
  CMA and Canada's Competition Bureau, and as one of the thirteen named patterns
  in India's 2023 guidelines. Mathur et al. (2019) catalogue the same conduct as
  *Hidden Costs*, under sneaking, and do not use the term drip pricing.
- Law: the UK's Digital Markets, Competition and Consumers Act 2024 bans it
  directly. Since 6 April 2025 mandatory charges (booking fees, delivery, local
  taxes, joining fees) must sit in the headline price rather than appear later
  in the transaction.

**Buried material terms**
- What it does: the term that would change the decision (the renewal, the
  minimum term, the data sharing) sits where attention will not be. Selective
  attention is the mechanism, and `knowledge/applied-psychology.md` holds its
  scope: a change away from where the user is working can be missed.
- To claim it you need: the layout or the copy, with the term's position in it.
- Not this when: the term is adjacent to the action it binds, in the same
  visual weight as the rest of the commitment.
- Floor: yes.
- Named in: Brignull's taxonomy as a form of sneaking; Gray et al. (CHI 2018)
  group it under *Sneaking*.

**Disguised advertising**
- What it does: paid placement is styled as content, as navigation, or as system
  interface, so the user acts on it believing it came from the product.
- To claim it you need: the layout, with the ad and the surrounding content
  visible, or a description of the styling of both.
- Not this when: the placement carries a label the user can see before acting,
  not only after.
- Floor: yes.
- Named in: Brignull's taxonomy. In the EU, within the Digital Services Act's
  advertising transparency obligations.

---

## 2. Misread by design

The control is understood, and understood wrongly.

**Trick questions**
- What it does: double negatives, inverted logic, or a question whose plain
  reading produces the opposite of what the user wants.
- To claim it you need: the exact wording of the question and its options.
- Not this when: the wording is merely clumsy and both readings lead to the
  same place.
- Floor: yes.
- Named in: Brignull's 2010 list.

**Misdirection**
- What it does: size, colour, contrast, or position give whichever option serves
  the seller the appearance of being the only one available, or of already being
  chosen. The isolation effect is the mechanism; `knowledge/applied-psychology.md`
  marks the point where emphasis turns into misdirection.
- To claim it you need: the supplied layout. Gestalt and visual-weight claims
  apply only to a layout that was sent. Without one this is a question.
- Not this when: emphasis falls on the option that serves the user, or both
  options carry equal weight and one is simply first.
- Floor: yes.
- Named in: Brignull's 2010 list as *misdirection*; the taxonomy he maintains
  now calls this *visual interference*. Gray et al. group it under *Interface
  Interference*.

**Confirmshaming**
- What it does: the decline option is worded to make declining feel foolish or
  mean. The copy, not the layout, does the work.
- To claim it you need: the quoted decline copy.
- Not this when: the decline states a real consequence in plain terms. "You will
  lose your draft" is information. "No thanks, I like wasting money" is not.
- Floor: yes.
- Named in: Brignull's taxonomy.

**False hierarchy**
- What it does: options are presented as a ranked set when they are not
  comparable, so the user reads a recommendation that no one made.
- To claim it you need: the option set as displayed, with the labels.
- Not this when: the ranking reflects a stated criterion the user can change.
- Floor: weigh it. This is often a genuine information-architecture mistake
  rather than deception; `knowledge/severity.md` rates it, and the question is
  whether anyone benefits from the misreading.
- Named in: Gray et al., *Interface Interference*.

---

## 3. The weighted path

Both options are there. One is engineered to be the one taken.

**Preselected consent**
- What it does: a box arrives already ticked, so agreement is collected from
  inaction.
- To claim it you need: the control's initial state, from a screenshot, the
  markup, or a description that states it.
- Not this when: the selection is a genuine convenience the user would choose,
  reversible in place, and not a permission.
- Floor: yes.
- Law: under the GDPR, consent requires a statement or clear affirmative action,
  and Recital 32 states that silence, pre-ticked boxes, and inactivity do not
  constitute consent; the Court of Justice held the same in *Planet49*
  (C-673/17). Where the preselection attaches a charge, Article 22 of the
  Consumer Rights Directive (2011/83/EU) goes further than prohibiting it and
  gives a remedy: consent inferred from a default the consumer had to reject
  entitles them to be reimbursed.

**Asymmetric choice**
- What it does: accepting is one tap; declining is a second screen, a list of
  toggles, or a search. Both exist, and only one is reachable at the moment of
  the decision.
- To claim it you need: the step count or interaction cost of each path, as
  supplied.
- Not this when: the paths differ because the outcomes genuinely differ in
  what they must collect.
- Floor: yes, where the asymmetric choice is a permission.
- Guidance: the European Data Protection Board's Guidelines 03/2022, on
  deceptive design patterns in social media platform interfaces (Version 2.0,
  adopted 14 February 2023), treat this asymmetry as a GDPR problem and work
  through it case by case. Guidelines are not binding, and say so.

**Default to the costlier option**
- What it does: the highest-priced tier, the add-on, or the insurance is
  preselected in a chooser.
- To claim it you need: the chooser with its initial selection.
- Not this when: the preselection is the option most users need and the price is
  visible at the point of selection.
- Floor: weigh it, unless the charge proceeds without an affirmative act, which
  moves it to **sneak into basket** below.
- Named in: Mathur et al. (2019) as *Pressured Selling*. Brignull's taxonomy has
  *Preselection*, which is not specific to price, so the price-specific name
  belongs to Mathur.

**Sneak into basket**
- What it does: an item, warranty, donation, or subscription is added without
  an affirmative act by the user.
- To claim it you need: the basket contents before and after, or the step that
  adds it.
- Not this when: the addition is shown and removable before any commitment, and
  the user passed through a screen that stated it.
- Floor: yes. A charge without consent is not a trade-off against conversion.
- Named in: Brignull's 2010 list.
- Law: Article 22 of the Consumer Rights Directive requires express consent to
  any payment beyond the agreed price of the main contract, before the consumer
  is bound.

---

## 4. Easy in, hard out

Entry and exit are built to different standards.

**Obstructed cancellation**
- What it does: subscribing takes a form; leaving takes a phone call, a chat
  queue, business hours, or a postal address.
- To claim it you need: both paths as supplied, the sign-up steps and the
  cancellation steps. One without the other supports only a conditional.
- Not this when: identity has to be established for a destructive action, and
  the verification is proportionate and available by the same channel.
- Floor: yes.
- Named in: Brignull's taxonomy, historically as *roach motel*; Gray et al.,
  *Obstruction*.
- Law, and read this one carefully. In the US the operative federal statute for
  online negative-option sales is the Restore Online Shoppers' Confidence Act,
  which requires clear disclosure of terms, express informed consent, and a
  simple cancellation mechanism. The FTC sued Amazon over Prime enrolment and
  cancellation in June 2023 in the Western District of Washington under ROSCA and
  Section 5; the cancellation flow was known internally as *Iliad*. The case
  settled during trial in September 2025 for $2.5 billion, a $1 billion civil
  penalty plus $1.5 billion in consumer redress, with no admission of liability.
  Two cautions on the surrounding law. The FTC's Negative Option Rule, reported
  everywhere as "click to cancel", was vacated in its entirety by the Eighth
  Circuit in July 2025 on procedural grounds, with no replacement in force, so
  cite the statute rather than the rule. And the UK's subscription-contract
  regime under the 2024 Act was still awaiting commencement when this file was
  written, having slipped past its first expected date: check before citing it as
  a requirement. State automatic-renewal statutes apply throughout.

**Forced continuity**
- What it does: a trial becomes a charge with no notice the user would see, and
  the charge arrives before the reminder.
- To claim it you need: the trial terms as displayed and the notice sequence, or
  a description of both.
- Not this when: the renewal was stated at sign-up where the user was looking,
  and a notice precedes the charge.
- Floor: yes.
- Named in: Brignull's 2010 list. Covered by ROSCA's consent and disclosure
  requirements in the US.

**Account retention by obstruction**
- What it does: deletion is absent, hidden, or achievable only by request; what
  is offered instead is deactivation, presented as the same thing.
- To claim it you need: the settings surface, or the deletion path as described.
- Not this when: retention is required by law or by an open obligation, and the
  interface says which and for how long.
- Floor: yes, where the interface implies deletion it does not perform.
- Law: the GDPR requires that withdrawing consent be as easy as giving it
  (Article 7(3)); erasure is a separate right with its own conditions, so do not
  merge the two in a finding.

---

## 5. Borrowed urgency

Pressure that is not in the underlying facts.

**Fabricated scarcity**
- What it does: a stock count, a viewer count, or a "only 2 left" that is not
  read from inventory.
- To claim it you need: the claim as displayed **and** something about its
  source: the practitioner saying it is not live, or a count that behaves
  impossibly. Without that, the agent asks whether the number is read from
  inventory. A displayed scarcity claim is not evidence that it is false.
- Not this when: the count is accurate and updates.
- Floor: yes, when false. A question, when unverified.
- Named in: Mathur et al. (2019) as scarcity.

**Fabricated deadlines**
- What it does: a countdown that resets, an offer that does not expire when it
  says it will.
- To claim it you need: the behaviour across time, or the practitioner's
  statement about it. A countdown in a screenshot is a countdown, not a lie.
- Not this when: the deadline is real and holds.
- Floor: yes, when false.
- Named in: Mathur et al. as urgency.

**Manufactured social proof**
- What it does: activity notices, purchase popups, or review counts that are not
  drawn from real activity.
- To claim it you need: the practitioner's account of the data source. Social
  proof is legitimate and common, so the display alone supports nothing.
- Not this when: the activity is real and representative of what is shown.
- Floor: yes, when fabricated.
- Named in: Mathur et al.; Cialdini's social-proof mechanism, with its scope in
  `knowledge/applied-psychology.md`.
- Law: under the UK's 2024 Act, a review that does not reflect a genuine
  experience while claiming to is unfair in all circumstances, so a regulator
  need not show an effect on the average consumer; platforms publishing reviews
  also carry a duty to take reasonable steps to prevent and remove fake ones.

**Nagging**
- What it does: the same request returns after it has been answered, until the
  answer changes.
- To claim it you need: the repetition, as described or observed across a
  session. One prompt is a prompt.
- Not this when: the state genuinely changed, or the prompt is required and
  carries a way to stop it.
- Floor: weigh it, and note that repeatedly asking a recipient to make a choice
  they have already made is named in the text of the Digital Services Act's
  interface provision itself, not in guidance about it. The Commission has not
  exercised the power to issue guidelines on that article.
- Named in: Gray et al., *Nagging*.

---

## 6. Engineered return

Mechanisms whose purpose is the next session rather than the current task.

**Artificial streaks and loss framing**
- What it does: accumulated progress is framed so that stopping reads as losing
  something, with loss aversion doing the work.
- To claim it you need: the mechanic as supplied: what accrues, what is lost,
  and what the user is told.
- Not this when: the streak reflects a real commitment the user set, and
  breaking it costs nothing but the streak.
- Floor: weigh it, and weigh it differently for minors. The question is whether
  the mechanic serves a goal the user holds or only the session count.
- Named in: loss aversion (Kahneman and Tversky), scoped in
  `knowledge/applied-psychology.md`. The taxonomy Brignull maintains carries
  *addictive design*, which covers this mechanic; check the current list before
  citing either name.

**Variable reward scheduling**
- What it does: unpredictable payoff on a repeated action, which sustains the
  action beyond the user's intent.
- To claim it you need: the reward logic, which almost never appears in an
  interface. Usually a question.
- Not this when: the variability is inherent to the content rather than tuned
  for retention.
- Floor: weigh it. Raise it where the audience includes minors or where money is
  staked.
- Named in: not a term from the deceptive-pattern taxonomies. It comes from the
  literature on reinforcement schedules, and the design claim built on it is
  contested. Present it as a mechanism, never as a finding.

**Interruption at the exit**
- What it does: the attempt to leave triggers an offer, a survey, or a warning
  that makes leaving a negotiation.
- To claim it you need: the exit flow.
- Not this when: the warning is about unsaved work.
- Floor: weigh it, unless leaving becomes unreachable, which is **obstructed
  cancellation** above.
- Named in: Gray et al., *Obstruction*.

---

## 7. Consent that is not consent

Specific to permission, because the legal and ethical bar is specific.

**Bundled consent**
- What it does: one agreement covers purposes the user would answer differently,
  with no way to separate them.
- To claim it you need: the consent text and the available controls.
- Not this when: the purposes are genuinely inseparable and the interface says
  why.
- Floor: yes.
- Law: the GDPR requires consent to be specific to a purpose, and Article 7(4)
  addresses consent made a condition of a service that does not need it.

**Maximum-exposure defaults**
- What it does: privacy settings arrive at their most permissive, relying on
  users not to change them.
- To claim it you need: the initial settings state.
- Not this when: the exposure is the function the user asked for.
- Floor: yes.
- Law: the GDPR requires data protection by design and by default (Article 25)
  and data minimisation (Article 5(1)(c)). Historically named *privacy
  Zuckering* in Brignull's taxonomy; prefer the descriptive name in output, since
  the coinage attributes motive to a named company.

**Consent-interface asymmetry**
- What it does: accept is a button; reject requires entering a second surface,
  and "manage preferences" leads to a list that defaults to on.
- To claim it you need: the banner and the surface behind it, including initial
  toggle states.
- Floor: yes.
- Law: this is the most actively enforced interface in the EU,
  under the GDPR consent conditions above, and the European Data Protection
  Board's Guidelines 03/2022 work through this surface specifically. Note the
  boundary: the DSA's interface provision (Article 25) explicitly does not apply
  to practices already covered by the GDPR or by the Unfair Commercial Practices
  Directive (2005/29/EC), so name the instrument that actually governs rather
  than reaching for the DSA by default.

**Permission request without purpose**
- What it does: an access prompt arrives with no statement of what it is for, so
  the user cannot weigh it.
- To claim it you need: the prompt copy and when it fires.
- Not this when: the purpose is evident from the action that triggered it.
- Floor: weigh it, unless the permission is unrelated to any action the user
  took, which makes it a floor.
- Named in: not a named pattern. The requirement under it is the GDPR's
  purpose-limitation principle, named in words here rather than by article.

---

## 8. Assistance turned around

Help and accessibility paths used against the person relying on them.

**Conformance as cover**
- What it does: an interface meets criteria mechanically while the experience it
  produces is worse for the people the criteria exist for: accurate labels that
  describe nothing, focus order that technically exists and is unusable.
- To claim it you need: the markup or the assistive-technology behaviour. This
  is also the one place the agent must not overreach: it reasons about which
  criteria apply and never declares conformance, per `docs/boundaries.md`.
- Not this when: the implementation is simply incomplete.
- Floor: weigh it with `knowledge/severity.md`, rated for the people affected
  rather than the average. A barrier that stops every screen reader user is not
  cosmetic for them, whatever its share of traffic.
- Named in: not a named pattern. Derived here from `docs/boundaries.md`, which
  holds the line between reasoning about which criteria apply and declaring
  conformance.

**Accessible path as the long way round**
- What it does: the keyboard route, the text alternative, or the accessible
  variant exists and is slower, older, or missing features.
- To claim it you need: both paths as supplied.
- Floor: yes, where the accessible path cannot complete the task.
- Named in: the obstruction family in Gray et al. (CHI 2018), pointed at an
  accessible route rather than at a task.

**Help that routes away from the remedy**
- What it does: the support surface answers everything except cancellation,
  refunds, or deletion, and those routes lead back to retention offers.
- To claim it you need: the support flow or its navigation.
- Floor: yes, where the remedy is unreachable.
- Named in: the obstruction family in Gray et al. (CHI 2018).

---

## 9. Aimed at reduced resistance

The same mechanism, pointed at people with less capacity to refuse. Reach is a
tie-break factor in `knowledge/arbitration.md`, and a segment with fewer
alternatives weighs more than its share of traffic.

**Patterns directed at minors**
- What it does: any mechanism above, in a product children use, where the design
  assumes a judgement they do not yet have: currency obfuscation, purchase
  confirmation a child cannot distinguish from play, social pressure among peers.
- To claim it you need: the mechanism, plus something establishing the audience.
- Floor: yes, and raise severity.
- Law: in the US, COPPA governs personal information from children under 13 and
  requires verifiable parental consent. In the EU, the Digital Services Act
  carries obligations specific to minors, including on advertising directed at
  them; name the requirement in words unless you have checked the article.

**Patterns in moments of crisis**
- What it does: upsells, consent requests, or retention offers placed in flows
  people reach during medical emergency, bereavement, debt, or legal trouble.
- To claim it you need: the flow and its entry point.
- Floor: yes.
- Named in: not a named pattern in the public taxonomies. Treat it as the
  application of *reach* and *cost of error* rather than as an established term,
  and say so rather than implying a citation exists.

**Exploiting unfamiliarity**
- What it does: the pattern lands on people new to the domain, the language, or
  the device, where Jakob's law offers no protection because the user has no
  prior to compare against.
- To claim it you need: the mechanism, plus the audience as stated.
- Floor: weigh it, raised by reach.
- Named in: not a named pattern. Derived here from reach as a tie-break factor
  in `knowledge/arbitration.md`, and from Jakob's law having no purchase where
  the user has no prior.

---

## 10. Specific to generated output

Where the interface's output is produced by a model, the deception has forms the
older taxonomies do not cover. These are the least settled entries in the file,
and the agent should present them as emerging rather than established.

**Confidence not matched to reliability**
- What it does: output is delivered in uniform, assured prose whether or not the
  system has grounds, so the user cannot tell which parts to check. This
  repository's own `Unverified:` line exists against this failure.
- To claim it you need: the output and whatever the interface shows about its
  basis.
- Floor: yes, where the user is expected to act on it.
- Named in: not a named pattern. Derived here from `docs/grounding-gate.md`, as
  the interface-side form of what the gate stops in the agent's own output.

**Undisclosed generation**
- What it does: generated text, a review, a voice, or a person is presented as
  human without the user being able to tell.
- To claim it you need: the surface, and the practitioner's statement of what is
  generated.
- Floor: yes.
- Law: the EU AI Act carries transparency obligations for certain interactions
  and synthetic content. Obligations phase in on their own schedule, so name the
  requirement in words and verify the article and date before citing either.

**Fabricated specifics in an assistive interface**
- What it does: a plausible detail with no origin (a figure, a citation, a
  screen element) delivered fluently enough to survive review. This is the
  failure `docs/grounding-gate.md` was written for, and it is a deceptive pattern
  when a product ships it to users without a way to tell constructed content
  from retrieved content.
- To claim it you need: the output, and ideally the source the product claims.
- Floor: yes.
- Named in: not a named pattern. Derived here from `docs/grounding-gate.md`,
  which was written for this failure in the agent and meets it again in a
  shipped product.

**Engagement optimisation presented as helpfulness**
- What it does: a system tuned for session length or return rate, surfaced as
  recommendation or assistance, where agreement and continuation are rewarded
  over accuracy and completion.
- To claim it you need: the objective the system is tuned on, which an interface
  never shows. Almost always a question for the practitioner.
- Floor: weigh it, and name the organisational variable: what the system is
  optimised for is rarely a design decision, and
  `knowledge/arbitration.md` hands that class of conflict back.
- Named in: not a named pattern. Derived here from the organisational-conflict
  case in `knowledge/arbitration.md`.

---

## Rating one of these

Severity comes from `knowledge/severity.md`, not from this file. Two rules from
there bind every entry above: an entry marked **Floor: yes** is rated 3 or
higher, because a broken floor sets that minimum; and nothing is rated for a
state or a surface that was not supplied.

The factors that decide a rating are the same ones, and they are questions here
rather than values: how many users meet this, and which ones; whether they get
past it once or every time; what it costs when it works as designed. Where those
are not supplied, give the range and the factor that settles it, and put the
assumed factors on the `Unverified:` line.

---

## Where the names come from

The pattern names above are the field's, not this repository's. Inventing fresh
names would make the catalogue unusable: a finding has to be checkable against
the literature and the regulators by someone who did not read this file.

- Harry Brignull coined "dark pattern" in 2010 and now uses "deceptive design";
  the maintained taxonomy is at deceptive.design.
- Gray et al., *The Dark (Patterns) Side of UX Design* (CHI 2018), groups them
  into nagging, obstruction, sneaking, interface interference, and forced action.
- Mathur et al., *Dark Patterns at Scale* (2019), describes patterns by
  attribute across a large crawl of shopping sites.
- The FTC staff report *Bringing Dark Patterns to Light* (September 2022).
- The European Data Protection Board's Guidelines 03/2022, on deceptive design
  patterns in social media platform interfaces (Version 2.0, adopted
  14 February 2023). The most practical of these for a designer, because it works
  through interfaces rather than principles. Guidelines are not binding.

## Markets

**The market is a supplied fact, like any other, and it is the one most often
left out.** A requirement is not a property of a pattern. It is a property of a
pattern in a place. So before naming any instrument below, the practitioner has
to have said where the product operates, or the agent asks. "This is unlawful",
with no market named, is a worse failure than the one the Standard check usually
catches: not an identifier that is close and wrong, but a correct identifier
pointed at the wrong country.

Three things follow, and they hold in every market.

1. **The design problem does not move.** A pre-ticked box collects agreement
   from inaction in São Paulo, Seoul and Stuttgart. What changes is the remedy,
   the regulator and the penalty. Say the mechanism first, and reach for an
   instrument only once the market is known.
2. **Coverage here is uneven, and unevenly deep.** Some markets name the
   patterns in a list; most reach them through general prohibitions on
   misleading or abusive practices. A market treated at length below is not a
   market with a stricter rule, only one with a more specific text.
3. **A market that is not listed is not a market without law.** It is a market
   this file does not cover. Say that, name the mechanism, and leave the
   instrument to a local lawyer.

### European Union

- **Data protection.** GDPR Articles 5(1)(c), 7(3), 7(4) and 25, and Recital 32;
  *Planet49* (C-673/17). The European Data Protection Board's Guidelines 03/2022
  work through interfaces case by case and are not binding.
- **Consumer contracts.** Article 22 of the Consumer Rights Directive
  (2011/83/EU), on express consent to any payment beyond the agreed price and
  reimbursement where consent was inferred from a default.
- **Commercial practices.** Article 6(1) of Directive 2005/29/EC, as amended by
  Directives 2019/2161 and 2024/825, on a presentation that deceives or is
  likely to deceive the average consumer even where the information is factually
  correct, where the deception reaches a transactional decision.
- **Platforms.** The Digital Services Act Article 25, with its carve-out for the
  Unfair Commercial Practices Directive and the GDPR, and the obligations
  specific to minors, named in words here.

### United Kingdom

The Digital Markets, Competition and Consumers Act 2024. Its drip pricing and
fake review provisions came into force on 6 April 2025: a mandatory charge sits
in the headline price, and a review that does not reflect a genuine experience is
unfair in all circumstances, so the regulator does not have to show an effect on
the average consumer. Its subscription regime had not commenced when this was
written.

### United States, federal

Section 5 of the FTC Act; the Restore Online Shoppers' Confidence Act; COPPA.
*FTC v. Amazon.com* (W.D. Wash., filed June 2023), settled September 2025 for
$2.5 billion with no admission of liability.

### United States, the states

This is the most fragmented market in the file, and the one where a single
sentence is most likely to be wrong somewhere.

- **California.** The dark-pattern definition at Civil Code § 1798.140(l), the
  rule at § 1798.140(h) that agreement obtained through one is not consent, and
  the California Privacy Protection Agency's Enforcement Advisory No. 2024-02,
  which reads the definition as a test of effect rather than of intent.
- **Colorado.** The Colorado Privacy Act carries the same definition in
  substance, and its rules go further than any other state text on the
  interface: a consent interface has to be symmetrical, so the choices may not
  carry unequal weight or prominence, and consent obtained through a dark
  pattern is not consent. The rules also invite a controller to look at other
  jurisdictions' dark-pattern guidance, which is unusual and worth knowing.
- **Connecticut.** The same definition, plus a clause that folds in anything the
  Federal Trade Commission calls a dark pattern, so the state standard moves
  when federal practice does. Its consent definition also excludes agreement
  inferred from hovering, muting, pausing or closing content.
- **Roughly a dozen states** carry the rule that agreement obtained through a
  dark pattern is not valid consent, California, Colorado and Connecticut among
  them. The list moves every legislative session, so count it on the day rather
  than citing a number from a roundup. Oregon reaches the same place without the
  term, barring consent obtained through an interface that obscures or impairs
  the consumer's autonomy or choice, which is a reminder that the absence of the
  phrase is not the absence of the rule.

### Canada

The Competition Act. Since the amendments of 23 June 2022, drip pricing is
expressly a deceptive marketing practice, civilly under subsection 74.01(1.1)
and criminally under subsection 52(1.3): a price that is not attainable because
of fixed obligatory charges is a false or misleading representation. Amendments
of 20 June 2024 narrowed what may sit outside the headline price to charges
imposed by federal or provincial legislation, such as sales tax. The
administrative monetary penalties are among the heaviest in this file, reaching
CAD 10 million for a corporation's first civil violation and CAD 15 million
after that, or three times the benefit obtained, whichever is greater.

### Brazil

There is no Brazilian statute that names deceptive patterns, and that absence is
the thing to understand rather than a gap to apologise for. The conduct is
reached by two instruments that predate the term.

- The Consumer Defence Code (Lei 8.078/1990), Article 39, whose list of abusive
  practices is not exhaustive. Commentary reaches interface manipulation through
  the prohibition on exploiting the consumer's weakness or ignorance, and the
  one on demanding a manifestly excessive advantage. The Code's right of
  withdrawal for distance purchases is the provision a subscription trap runs
  into first.
- The LGPD (Lei 13.709/2018), which requires consent that is free, informed and
  unequivocal, so consent assembled from a default the user had to find and
  reject does not meet the standard. The ANPD has addressed cookie banners
  specifically.

Two cautions for this market. The article numbers above are named in words
rather than cited by inciso, because the Code's numbering is where a confident
citation goes wrong; read the article before quoting it. And proposals on
interface manipulation and subscription traps have been in progress, so check
what has passed rather than citing a bill.

### India

The instrument with the most specific text in this file. The Central Consumer
Protection Authority's Guidelines for Prevention and Regulation of Dark
Patterns, 2023, notified on 30 November 2023 under Section 18 of the Consumer
Protection Act, 2019. They define the conduct in the same terms the US state
statutes use, as design that subverts or impairs user autonomy and choice to the
user's detriment, and then do what no other instrument here does: enumerate
named patterns, thirteen of them, in Annexure 1. They bind sellers, advertisers
and platforms that systematically offer goods or services in India.

Read Annexure 1 itself rather than a secondary list. The draft carried ten and
the notified version thirteen, so a list copied from commentary written before
November 2023 is short by three.

### South Korea

The 2024 amendment to the Act on the Consumer Protection in Electronic Commerce,
in force since 14 February 2025, which regulates six categories of interface
conduct, among them interference with cancellation or withdrawal and the
pre-selection of options. A price rise, or a free service becoming paid, needs
the consumer's prior consent. Guidance from the Korea Fair Trade Commission
treats automatic renewal as needing its own consent rather than consent bundled
into the original agreement.

The category count and the dates above are reliable; the specific article
numbers and penalty figures in circulation are not consistent across sources, so
name the requirement in words unless you have read the statute.

### Australia

Not yet in force, and listed for that reason. The Competition and Consumer
Amendment (Unfair Trading Practices) Act 2026 adds a general prohibition aimed
at manipulative conduct that the existing Australian Consumer Law may not reach,
together with drip pricing disclosure and subscription obligations. It was
reported as passed in July 2026 with commencement on 1 July 2027. Until then the
conduct is reached, if at all, through the existing misleading-conduct and
unconscionable-conduct provisions, and the regulator has pursued subscription
cancellation under those. Check whether commencement has arrived before citing
it as a requirement.

### China

Named in words, because the article-level text was not verified when this was
written. The Personal Information Protection Law has governed consent since
2021, and the Consumer Protection Law does not single out deceptive design.
Treat this market as one where the mechanism is nameable and the instrument is
not, from this file.

### Anywhere else

Most of the world is not in the list above. Japan, Singapore, Mexico, Nigeria,
South Africa, the Gulf states and the rest each have a data protection or
consumer regime that reaches some of this conduct, and none of them is covered
here. The honest answer in those markets is the one this whole file is built to
give: name the mechanism, name what it does to the user, say that whether it is
also unlawful depends on a text this agent has not read, and stop there.

### Currency

Six warnings, because the Standard check fails an identifier that is close and
wrong, and one that was right last year fails the same way on a delay.

- The FTC's Negative Option Rule was vacated in full in July 2025 with no
  replacement in force.
- The UK subscription regime slipped past its first expected commencement date.
- The EU AI Act's obligations phase in on their own timetable.
- An instrument can move without being replaced: Directive 2005/29/EC has been
  amended twice, so an article number read off the 2005 text is not safe to
  quote.
- The Australian regime above does not commence until 1 July 2027.
- The count of US states whose consent rule names dark patterns changes every
  legislative session.

Check each before it reaches a document, and prefer naming a requirement in
words to citing an article nobody has read today.

Nothing in this list is jurisdiction advice, and the agent does not give any.
A pattern is a design problem wherever it appears; whether it is also unlawful
depends on where the product operates and who uses it, which is the
practitioner's to establish and a lawyer's to answer.
