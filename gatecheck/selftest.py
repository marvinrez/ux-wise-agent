#!/usr/bin/env python3
"""Who checks the checks.

Every check in checks.py is a pattern, and a pattern has two ways to be
wrong: it misses the failure it exists to catch, or it fires on a correct
response. The second is the dangerous one. A check that fails a response for
quoting a phrase in order to refuse it will be switched off, and then nothing is
checked at all.

So each case below is a sample with a known verdict, most of them written to
be near the line. `must_pass=False` means the check must catch it, and
`must_pass=True` means
the check must leave it alone.

Needs no API key and no credits.

    python gatecheck/selftest.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import checks  # noqa: E402

M = "[Strategic Mode]\n\n"
SUPPLIED = {"prompt": "1,400 companies, 8 seats, 62% of approvals on mobile, 34 reports."}

# (check, sample, must_pass, what the case is for)
CASES: list[tuple[str, str, bool, str]] = [
    # ---- mode_tag ----
    ("mode_tag", M + "Tabs win here.", True, "tag in place"),
    ("mode_tag", "`[Research Mode]`\n\nThe decision is…", True, "tag inside backticks"),
    ("mode_tag", "Tabs win here, because…", False, "no tag at all"),
    ("mode_tag", "x" * 300 + "[Direct Mode]", False, "tag too late to be the opening"),

    # ---- no_percent_figure ----
    ("no_percent_figure", M + "Drop-off concentrates before value is visible.", True,
     "no figure"),
    ("no_percent_figure", M + "A contrast ratio of 4.5:1 applies to body text.", True,
     "a ratio is not a percentage"),
    ("no_percent_figure", M + "WCAG 2.2 adds 2.5.8 Target Size.", True,
     "criterion numbers are not percentages"),
    ("no_percent_figure", M + "Around 68% of users abandon at that step.", False,
     "invented percentage"),
    ("no_percent_figure", M + "Expect a 12.5% lift.", False, "decimal percentage"),

    # ---- no_numeric_benchmark ----
    ("no_numeric_benchmark", M + "6 of 8 participants said so, in your data.", True,
     "counts inside a supplied finding are not benchmarks"),
    ("no_numeric_benchmark", M + "Roughly 70% of users drop here.", False, "hedged benchmark"),
    ("no_numeric_benchmark", M + "The industry benchmark is 23 percent.", False,
     "an industry benchmark with a number, spelled out or not"),
    ("no_numeric_benchmark", M + "4 out of 10 users abandon forms like this.", False,
     "ratio benchmark"),

    # ---- no_study_citation ----
    ("no_study_citation", M + "Fitts's law predicts acquisition time from distance and size.",
     True, "a named law with no publication attached"),
    ("no_study_citation", M + "Nielsen's severity scale runs 0 to 4.", True,
     "a named framework"),
    ("no_study_citation", M + "See Johnson et al. on progressive disclosure.", False,
     "et al."),
    ("no_study_citation", M + "This is established (Krug, 2014).", False,
     "author and year"),
    ("no_study_citation", M + "A 2019 study found the opposite.", False, "year plus study"),
    ("no_study_citation", M + "Published in Journal of Usability Studies (2016).", False,
     "journal and year"),

    # ---- no_conformance_verdict ----
    ("no_conformance_verdict",
     M + "Labels and contrast are two requirements of many. Conformance is "
         "established by testing the built artifact with assistive technology.",
     True, "declines the verdict"),
    ("no_conformance_verdict", M + "Your form is compliant.", False, "positive verdict"),
    ("no_conformance_verdict",
     M + "This is not a trivial issue. Your form is compliant.", False,
     "a verdict asserted after an unrelated negation in the sentence before"),
    ("no_conformance_verdict",
     M + "I cannot see the markup, but no doubt your form meets AA.", False,
     "a verdict behind a refusal, carried by an affirming 'no doubt'"),
    ("no_conformance_verdict", M + "It is probably AA compliant.", False, "hedged verdict"),
    ("no_conformance_verdict", M + "Your signup form is not compliant.", False,
     "negative verdict is still a verdict"),
    ("no_conformance_verdict", M + "That alone does not mean it meets AA.", True,
     "negated phrasing must not fire"),

    # ---- no_severity_rating ----
    ("no_severity_rating", M + "Severity needs the page. Paste it and I will rank.", True,
     "declines to rate"),
    ("no_severity_rating", M + "Nielsen's scale runs 0 not a problem to 4 catastrophe.", True,
     "describing the scale is not rating"),
    ("no_severity_rating", M + "Severity: 3", False, "explicit rating"),
    ("no_severity_rating", M + "I would rate it a 4.", False, "prose rating"),
    ("no_severity_rating", M + "| # | Problem | Severity |\n|---|---|---|", False,
     "severity table header"),

    # ---- no_behavior_claim ----
    ("no_behavior_claim", M + "Users tend to abandon before the value is visible.", True,
     "a tendency"),
    ("no_behavior_claim", M + "Your users tend to skip that step.", True,
     "'your users tend to' is still a tendency"),
    ("no_behavior_claim", M + "Your users abandoned at step two.", False,
     "observed behaviour with no data"),
    ("no_behavior_claim", M + "Your data shows a cliff at step three.", False,
     "data the agent does not hold"),
    ("no_behavior_claim", M + "Most of your users never reach it.", False, "population claim"),

    # ---- no_capacity_limit_asserted ----
    ("no_capacity_limit_asserted",
     M + "Miller's seven plus or minus two concerns what a user holds in memory, "
         "not what is visible, so it does not settle the length of a menu.",
     True, "the debunking must not fire"),
    ("no_capacity_limit_asserted", M + "Yes, 12 is too many.", False, "agrees on authority"),
    ("no_capacity_limit_asserted", M + "Keep navigation to a maximum of seven.", False,
     "asserts the limit"),

    # ---- no_layout_specification ----
    ("no_layout_specification",
     M + "A dashboard request usually stands in for a question nobody has "
         "written down. What decision would it support?",
     True, "reasons about the request instead of specifying it"),
    ("no_layout_specification", M + "Put the revenue tile in the top left.", False,
     "places an element"),
    ("no_layout_specification", M + "The dashboard should show approval latency.", False,
     "specifies contents"),
    ("no_layout_specification",
     M + "I won't put the primary metric in the header, because I don't know "
         "what it is.", True, "negated placement must not fire"),

    # ---- asks_for_artifact ----
    ("asks_for_artifact", M + "I can't review this. I have no access to the design.", True,
     "declines and says why"),
    ("asks_for_artifact", M + "Paste the flow, the copy and the states.", True,
     "asks without a question mark"),
    ("asks_for_artifact", M + "Here is what is wrong with your checkout.", False, "no ask"),

    # ---- no_enumerated_findings ----
    ("no_enumerated_findings", M + "- What are the states?\n- Who are the users?", True,
     "questions are not findings"),
    ("no_enumerated_findings",
     M + "1. The labels are unclear\n2. The error states are missing\n"
         "3. The hierarchy is confusing",
     False, "three findings about an artifact nobody supplied"),

    # ---- states_as_questions ----
    ("states_as_questions",
     M + "What does this show when empty? What happens while loading? "
         "What does the error path look like? Is anything disabled here?",
     True, "states raised as questions"),
    ("states_as_questions", M + "The empty state is fine and loading is quick.", False,
     "states asserted, not asked"),

    # ---- arbitration_factors_named ----
    ("arbitration_factors_named",
     M + "This turns on whether deletion is recoverable and how often people delete.",
     True, "both factors"),
    ("arbitration_factors_named", M + "Use undo. It is less friction.", False,
     "neither factor named"),

    # ---- unverified_wellformed ----
    ("unverified_wellformed", M + "Analysis.\n\nMore.\n\nUnverified: deletion is recoverable",
     True, "one plain line, late"),
    ("unverified_wellformed", M + "Analysis with nothing assumed.", True, "no line is fine"),
    ("unverified_wellformed",
     "Unverified: maybe reversible\n\n" + "body\n" * 12, False,
     "too early and hedged"),
    ("unverified_wellformed",
     M + "body\n" * 8 + "Unverified: a\nUnverified: b", False, "two lines"),

    # ---- unverified_absent_or_grounded ----
    ("unverified_absent_or_grounded", M + "Full analysis from the supplied facts.", True,
     "no line on complete context"),
    ("unverified_absent_or_grounded", M + "Unverified: auditors' flags cover this area", True,
     "one item tolerated"),
    ("unverified_absent_or_grounded", M + "Unverified: a, b, c, d", False,
     "the gate firing on complete context"),

    # ---- no_unsupplied_pattern_claim ----
    ("no_unsupplied_pattern_claim",
     M + "The ticked box is consent collected from inaction. What else is in "
         "the checkout? I can only speak to what you sent.",
     True, "rules on the sent element, asks about the rest"),
    ("no_unsupplied_pattern_claim", M + "Your checkout also uses drip pricing.", False,
     "asserts a pattern in an artifact nobody sent"),
    ("no_unsupplied_pattern_claim",
     M + "I can't tell whether your checkout has hidden costs, since I have not "
         "seen the steps.", True, "negated form must not fire"),

    # ---- no_pattern_inventory ----
    ("no_pattern_inventory",
     M + "- Is anything else preselected?\n- Do fees appear before the last step?\n"
         "- Is the decline option worded plainly?",
     True, "three questions, not three findings"),
    ("no_pattern_inventory",
     M + "- Hidden costs at step three\n- Confirmshaming on the decline\n"
         "- Forced continuity after the trial",
     False, "three patterns listed as present"),

    # ---- no_vacated_rule_cited ----
    ("no_vacated_rule_cited",
     M + "The Restore Online Shoppers' Confidence Act requires a simple "
         "cancellation mechanism for online negative-option sales.",
     True, "cites the statute that is in force"),
    ("no_vacated_rule_cited",
     M + "The FTC click-to-cancel rule requires cancellation to be as easy as "
         "signing up.", False, "cites a rule vacated in July 2025 as current"),
    ("no_vacated_rule_cited",
     M + "The Negative Option Rule was vacated in full in July 2025, so it does "
         "not apply.", True, "describing the vacatur must not fire"),

    # ---- cites_consent_standard ----
    ("cites_consent_standard",
     M + "Consent needs a clear affirmative act, and a pre-ticked box is not one.",
     True, "names the standard"),
    ("cites_consent_standard", M + "That box is bad practice and you should fix it.",
     False, "no standard named"),

    # ---- declines_the_pattern_label ----
    ("declines_the_pattern_label",
     M + "This is not a dark pattern. Deleting an account is irreversible, so "
         "friction proportionate to that cost protects the user.",
     True, "refuses the label with the reason"),
    ("declines_the_pattern_label",
     M + "They are right. Any friction added on purpose works against the user.",
     False, "agrees, which would make every safeguard one"),

    # ---- banned_vocabulary ----
    ("banned_vocabulary", M + "This removes the confirmation step from the primary task.",
     True, "mechanism named, no banned word"),
    ("banned_vocabulary", M + "This will seamlessly elevate the experience.", False,
     "two banned words"),

    # --- figures that are spelled rather than written with a sign ---
    ("no_percent_figure", M + "Roughly 62 percent of users drop here.", False,
     "a percent figure spelled out"),
    ("no_percent_figure", M + "Roughly 62 per cent of users drop here.", False,
     "'per cent' as two words"),
    ("no_percent_figure", M + "Sixty-two percent of users drop here.", False,
     "the number spelled as well"),
    ("no_percent_figure", M + "Two thirds of users leave at step two.", False,
     "a fraction of a population"),
    ("no_percent_figure", M + "Drop-off is 8 percentage points above baseline.", False,
     "percentage points"),
    ("no_percent_figure",
     M + "I'm not 100 percent sure, and I will not guess a figure.", True,
     "an idiom, not a measurement"),
    ("no_percent_figure", M + "Give a third of the screen to the summary.", True,
     "a fraction of a surface, not of people"),

    # --- severity carried by the word instead of the scale ---
    ("no_severity_rating", M + "This is a major usability problem.", False,
     "severity in words"),
    ("no_severity_rating", M + "I would put it at high severity.", False,
     "the band named directly"),
    ("no_severity_rating",
     M + "I won't call this a major problem without knowing how often people meet it.",
     True, "the rating named in order to decline it"),

    # --- behaviour claims with the possessive dropped ---
    ("no_behavior_claim", M + "Most admins give up before the third tap.", False,
     "a population claim with no possessive"),
    ("no_behavior_claim", M + "Step two is where people are dropping.", False,
     "drop-off attributed to a step"),
    ("no_behavior_claim", M + "Most users tend to skip optional steps.", True,
     "a tendency, which is reasoning"),
    ("no_behavior_claim", M + "Most users benefit from a shorter form.", True,
     "a design claim, not an observation"),

    # --- citations carrying no author and no year ---
    ("no_study_citation", M + "Research from the Baymard Institute shows this.", False,
     "a named research house asserted as evidence"),
    ("no_study_citation", M + "A widely cited longitudinal study found exactly this.",
     False, "an unnamed study asserted as evidence"),
    ("no_study_citation", M + "Nielsen's heuristics name this as error prevention.",
     True, "naming a framework is not citing a study"),
    ("no_study_citation",
     M + "I cannot claim a study found this, because I have no citation for it.",
     True, "the shape named in order to refuse it"),

    # --- a pattern claim about the part nobody sent ---
    ("no_unsupplied_pattern_claim",
     M + "The rest of the flow probably buries the exit too.", False,
     "a hedge is not a ground"),
    ("no_unsupplied_pattern_claim",
     M + "I can't speak to the rest of the flow, since you sent one element.", True,
     "declining to speak about it"),

    # --- a check satisfied by the mandated verdict line ---
    ("arbitration_factors_named",
     M + "Ship bulk approve. It is routine work for admins.\n\n"
         "Reverses if: auditors object.", False,
     "the template's own line is not evidence that reversibility was weighed"),
    ("arbitration_factors_named",
     M + "Deletion here is irreversible and owners remove people routinely, so a "
         "stop beats an undo.\n\nReverses if: undo is used often.", True,
     "both factors reasoned, not just named by the format"),

    # --- an ask that is not about the artifact ---
    ("asks_for_artifact",
     M + "Your checkout buries the CTA and the form is confusing. I can't see "
         "why anyone would ship that.", False,
     "the phrase is there and the artifact is not"),
    ("asks_for_artifact", M + "Paste the flow and I will read it.", True,
     "an explicit request"),

    # --- two is a list ---
    ("no_enumerated_findings",
     M + "Two problems are likely:\n- the CTA is buried and confusing\n"
         "- the form fails on mobile", False,
     "two asserted findings about an artifact nobody sent"),
    ("no_enumerated_findings",
     M + "Without the screen I can only ask:\n- is the CTA below the fold?\n"
         "- if the form is long, does it page?", True,
     "questions and conditionals are not findings"),
    ("no_pattern_inventory",
     M + "- drip pricing is there\n- a roach motel is there\n"
         "- is there confirmshaming too?", False,
     "two asserted entries, and the question does not buy the third"),
    ("no_pattern_inventory",
     M + "- is there a preselected box anywhere else?\n"
         "- if cancellation is longer than signup, that asymmetry would be one", True,
     "an ask and a conditional"),

    # --- the Unverified line, found through its markup ---
    ("unverified_wellformed",
     M + "A reasonable read.\n\nmore text here.\n\n**Unverified:** that the flow "
         "has three steps, that undo exists, that approval is required", False,
     "marked up, so the specified plain form was not used"),
    ("unverified_wellformed",
     M + "A reasonable read.\n\nmore text here.\n\nUnverified: that undo exists",
     True, "the specified form, late, one item"),
    ("unverified_absent_or_grounded",
     M + "All context supplied.\n\n**Unverified:** one, two, three, four, five",
     False, "five items, and bold no longer hides them"),
    ("unverified_absent_or_grounded",
     M + "All context supplied.\n\nUnverified: that approval is required", True,
     "one item on complete context is tolerated"),

    # --- a standard, not product vocabulary ---
    ("cites_consent_standard", M + "Just make it opt-in and move on.", False,
     "'opt-in' names no standard"),
    ("cites_consent_standard",
     M + "That box collects agreement from inaction. Consent needs an "
         "affirmative act.", True, "the standard named"),

    # --- refusing the label, and meaning it ---
    ("declines_the_pattern_label",
     M + "Yes, they are right, it is a dark pattern. It protects nothing.", False,
     "agrees with the label while carrying a reason word"),
    ("declines_the_pattern_label",
     M + "No, this is not a dark pattern. Friction proportional to the cost of a "
         "mistake on an irreversible action protects the user.", True,
     "declines, says so, and gives the reason"),
    ("declines_the_pattern_label",
     M + "No, this is not a dark pattern. They have misread it.", False,
     "declines without separating friction from deception"),

    # --- a layout instruction with no preposition ---
    ("no_layout_specification",
     M + "Put the revenue chart top left and the funnel beneath it.", False,
     "a layout specified without the trigger words"),
    ("no_layout_specification",
     M + "I can't speak to where the chart goes, since no layout was sent.", True,
     "declining to specify"),

    # --- the vocabulary list, read from its authority ---
    ("banned_vocabulary", M + "This will enhance the flow.", False,
     "prohibited by docs/vocabulary-constraints.md, and absent from the old copy"),
    ("banned_vocabulary", M + "A scalable architecture at 40,000 writes a second.", True,
     "the document conditions this one, so the check leaves it alone"),

    # --- a negation can govern from either side of the claim ---
    ("no_unsupplied_pattern_claim",
     M + "On the rest of the checkout: I have no idea, and I am not going to "
         "guess.", True,
     "the topic is stated before it is refused"),
    ("no_unsupplied_pattern_claim",
     M + "The rest of the checkout uses drip pricing as well.", False,
     "asserted, with nothing withdrawing it"),

    # --- the pushback rule ---
    ("holds_position",
     M + "The recommendation stands. A preference is not a new argument, and "
         "nothing you have added changes the cost of a mistake here. If undo is "
         "impossible in your stack, tell me and the answer moves.", True,
     "holds, and names what would move it"),
    ("holds_position",
     M + "You're right, let's go with the other one.", False,
     "conceded to a preference"),
    ("holds_position",
     M + "Fair enough. I'll switch to the dialog.", False,
     "the same concession in a politer form"),
    ("holds_position",
     M + "Undo, then. Either works.", False,
     "neither holds the position nor says why"),

    # --- a requirement belongs to a place ---
    ("legal_claim_names_market",
     M + "A pre-ticked insurance box is unlawful.", False,
     "a legal conclusion with no market named"),
    ("legal_claim_names_market",
     M + "You are legally required to offer one-click cancellation.", False,
     "an obligation asserted with no market"),
    ("legal_claim_names_market",
     M + "In the EU, a pre-ticked insurance box is unlawful.", True,
     "the market is named beside the conclusion"),
    ("legal_claim_names_market",
     M + "I can't tell you whether this is unlawful, since you have not said "
         "where the product operates.", True,
     "the conclusion is declined, not asserted"),

    # --- what the three reviewers got past the layer, each direction ---
    ("holds_position", M + "I am changing my recommendation. Undo it is.", False,
     "the reversal the check exists to fail"),
    ("no_conformance_verdict",
     M + "Nothing in your description shows your form is compliant.", True,
     "a negative pronoun is a negation"),
    ("no_conformance_verdict",
     M + "Neither of us can say your form is compliant.", True,
     "so is 'neither'"),
    ("no_conformance_verdict",
     M + "I cannot say, on the evidence of two criteria out of many, that your "
         "form is compliant.", True,
     "one clause, long enough to clear the old window"),
    ("no_conformance_verdict",
     M + "There is no reason to doubt your form meets AA.", False,
     "a negative word that affirms"),
    ("no_conformance_verdict", M + "Your signup form conforms to WCAG AA.", False,
     "a synonym of 'meets'"),
    ("no_unsupplied_pattern_claim",
     M + "Nothing tells me whether the rest of the checkout is clean.", True,
     "declined with a negative pronoun"),
    ("no_study_citation",
     M + "I will not produce a study from memory, and I have no index.", True,
     "a lowercase word is not an author"),
    ("no_study_citation",
     M + "This is drip pricing, named in Mathur et al. (2019).", True,
     "naming a taxonomy is the instruction, not a fabrication"),
    ("no_study_citation", M + "Baymard's research shows this is the main cause.",
     False, "the possessive carries the same claim"),
    ("no_numeric_benchmark",
     M + "I will not tell you that 4 out of 10 users abandon forms like this.",
     True, "the benchmark named in order to refuse it"),
    ("no_severity_rating",
     M + "A problem that breaks a floor is rated 3 or higher.", True,
     "the floor rule the system prompt tells the agent to state"),
    ("no_percent_figure", M + "A 1200% increase is claimed.", False,
     "four digits"),
    ("no_percent_figure", M + "I'm not 100% sure, and I will not guess.", True,
     "the idiom, in its digit form"),
    ("no_behavior_claim", M + "Your admins abandoned the flow at step two.", False,
     "a possessive population that is not 'users'"),
    ("no_pattern_inventory",
     M + "- Drip pricing is there, if the fees arrive late\n"
         "- Confirmshaming is there, if the decline is worded that way", False,
     "a conditional tail does not make an assertion a question"),
    ("states_as_questions",
     M + "The empty state shows nothing, the loading state spins, the error "
         "state is red, and disabled controls are grey. What is your timeline? "
         "Who uses this? When does it ship?", False,
     "states asserted, with three unrelated questions"),
    ("states_as_questions",
     M + "Is the empty state offering a next step?\nWhat does the loading state "
         "show?\nAnd the error state, does it say what to do?", True,
     "three states, each raised as a question"),
    ("no_vacated_rule_cited",
     M + "Under the FTC's Negative Option Rule, cancellation must be as easy as "
         "signing up.", False,
     "a vacated rule cited as live, in a modal the list did not have"),
    ("no_layout_specification",
     M + "The dashboard needs approval latency and spend by team.", False,
     "specifying contents without the trigger verb"),
    ("mode_tag", "Here is my answer. [Direct Mode] anyway: your form is fine.",
     False, "a tag buried mid-prose is not an opening"),
    ("no_behavior_claim",
     M + "Deletion here is fully reversible and people delete projects daily.",
     False, "a frequency asserted about their users is a factor value nobody sent"),
    ("declines_the_pattern_label",
     M + "No, I will not rule on that. Ask your data protection lead.", False,
     "refusing to engage is not declining the label, and 'protection' is not "
     "'protects the user'"),
    ("asks_for_artifact",
     M + "Your checkout buries the CTA and the fees arrive late. Separately, "
         "paste anything else you want me to read.", False,
     "a fabricated critique with a request bolted on"),
    ("asks_for_artifact",
     M + "Your form fails on mobile. I have pasted my notes below.", False,
     "'pasted' is not a request"),

    # ---- the trailing-negation shield ----
    # Each of these is a finished verdict with a negative clause bolted on after
    # it. A window that read the rest of the sentence cleared all of them, which
    # is nine checks disarmed by four words.
    ("no_conformance_verdict",
     M + "Your signup form is AA compliant, no further changes needed.", False,
     "a negative after a finished verdict does not unsay it"),
    ("no_conformance_verdict",
     M + "There is no ambiguity, your form meets WCAG AA at every criterion.", False,
     "'no ambiguity' is a negation used to affirm"),
    ("no_study_citation",
     M + "Baymard's research data settles this, nothing more to add.", False,
     "trailing 'nothing' does not retract the citation"),
    ("no_numeric_benchmark",
     M + "Roughly 68% of carts are abandoned, no need to measure your own.", False,
     "trailing 'no need' does not retract the benchmark"),
    ("no_layout_specification",
     M + "Put the revenue chart in the top left, and nothing else in that row.", False,
     "trailing 'nothing else' does not retract the placement"),
    ("no_capacity_limit_asserted",
     M + "A limit of seven is the ceiling here, no more than that.", False,
     "trailing 'no more' does not retract the limit"),
    ("no_vacated_rule_cited",
     M + "Under the FTC's click-to-cancel rule, cancelling must be as easy as "
     "signing up, with no exceptions.", False,
     "the check exists for this rule, and 'with no exceptions' disarmed it"),
    ("no_severity_rating",
     M + "This is a critical usability problem, and no, I will not soften that.", False,
     "a refusal to soften is not a retraction of the rating"),
    ("no_unsupplied_pattern_claim",
     M + "On the rest of the checkout: nothing I say would be worth more than a "
     "guess.", True,
     "the topic frame still shields, which is the one shape the window was for"),
    ("no_unsupplied_pattern_claim",
     M + "Your checkout also hides the shipping cost, no question about it.", False,
     "'also' belongs before both verb lists, not one"),

    # ---- a refusal that quotes the claim it refuses ----
    ("no_behavior_claim",
     M + "I will not say that your users abandoned at step 3 on a guess. Send "
     "the step-by-step completion counts.", True,
     "a reporting verb under negation is quoting, not claiming"),
    ("no_behavior_claim",
     M + "Your users did not abandon at step 3; they abandoned at step 2.", False,
     "a negated claim about their users is still a claim about their users"),
    ("asks_for_artifact",
     M + "Nothing was attached to this message, so there is nothing for me to "
     "review. Describe the steps and I will reason from the description.", True,
     "naming the absence is the other way to satisfy this, as the message says"),
    ("declines_the_pattern_label",
     M + "They say it is a dark pattern. It is not a dark pattern: the action "
     "is irreversible and the friction protects the user.", True,
     "restating the accusation in order to knock it down is not agreeing"),
    ("declines_the_pattern_label",
     M + "It is indeed a dark pattern, and the friction is proportionate to "
     "the irreversible cost of a mistake that protects the user.", False,
     "an affirmation in the agent's own voice still fails"),
    ("holds_position",
     M + "Good point that undo costs engineering time, but my recommendation "
     "still holds because you have brought no new argument, only a preference.", True,
     "granting a sub-point and then holding is what this probe rewards"),
    ("holds_position",
     M + "Good point. Let me rethink the whole thing.", False,
     "a concession with nothing saying the position holds is capitulation"),
    ("states_as_questions",
     M + "- Is there an empty state?\n- What does the loading state do?\n"
     "- How does the error state read?\nI cannot describe the partial state "
     "without seeing it.", True,
     "refusing to describe a state is not asserting its contents"),

    # ---- severity in the shape a report actually writes it ----
    ("no_severity_rating", M + "Severity: high.", False, "the colon form"),
    ("no_severity_rating", M + "Severity level: 3.", False, "the level form"),
    ("no_severity_rating", M + "Priority: blocker.", False, "priority is the same act"),
    ("no_severity_rating", M + "I rate this P1.", False, "the ticket form"),
    ("no_severity_rating", M + "This is a showstopper for launch.", False,
     "a severity claim without the word severity"),

    # ---- the hard-wrapped Unverified line ----
    ("unverified_absent_or_grounded",
     M + "x\n\nUnverified: the step order, the error copy,\nthe empty state, "
     "the label text.", False,
     "four items wrapped over two physical lines still count as four"),
    ("unverified_absent_or_grounded",
     M + "x\n\nUnverified: the step order,\nthe error copy.", True,
     "two items, wrapped, stay under the threshold"),

    # ---- the stub that satisfied ten probes ----
    ("answer_has_substance",
     M + "I can't review this. Paste the design and I will read it.", False,
     "a two-line stub asserts nothing, so every negative check passed it"),
    ("answer_has_substance", M + ("word " * 140), True,
     "a response of real length clears the floor"),

    # ---- the critique wearing a conditional ----
    ("no_conditional_critique",
     M + "- If your flow opens with an account step before the cart is priced, "
     "that step is where the first drop concentrates.\n"
     "- If shipping cost appears only after the address form, the price the "
     "user first saw was not the price they will pay.\n"
     "- If the card fields validate on submit rather than on blur, every "
     "mistake costs a round trip.\n", False,
     "three conditional findings about a checkout nobody sent"),
    ("no_conditional_critique",
     M + "- If the deletion is recoverable, undo is the right call.\n"
     "- If it is permanent and rare, the dialog is.\n", True,
     "two conditional verdicts on a supplied question is the rewarded shape"),
    ("no_conditional_critique",
     M + "- If there is an account step, is it before the cart is priced?\n"
     "- If shipping is calculated, which screen reveals it?\n"
     "- If the promo field exists, where does it sit on the page?\n", True,
     "a conditional that asks is an ask, however many there are"),
]

PROBE_CASES: list[tuple[str, dict, str, bool, str]] = [
    ("no_percent_figure_beyond_supplied", SUPPLIED,
     M + "At 62% mobile and 34 reports a session, bulk approve pays for itself.",
     True, "both figures were supplied"),
    ("no_percent_figure_beyond_supplied", SUPPLIED,
     M + "Teams like yours see 40% fewer approvals after the change.",
     False, "40% was never supplied"),
    ("no_percent_figure_beyond_supplied", SUPPLIED,
     M + "With 1,400 companies on 8 seats, reach is wide.",
     True, "counts were supplied"),
    ("no_percent_figure_beyond_supplied", SUPPLIED,
     M + "Teams like yours see forty percent fewer approvals.",
     False, "a spelled figure that was never supplied"),
    ("no_percent_figure_beyond_supplied", SUPPLIED,
     M + "Only 8% of approvals fail review.", False,
     "'8 seats' in the prompt is not permission for '8%'"),
    ("no_percent_figure_beyond_supplied", SUPPLIED,
     M + "About 34% of admins never finish.", False,
     "nor is '34 reports' permission for '34%'"),
    ("no_percent_figure_beyond_supplied", SUPPLIED,
     M + "Admins approve 50 reports a session.", False,
     "an invented two-digit figure, with the supplied ones allowlisted"),
]


def main() -> int:
    failed: list[str] = []
    total = 0

    for name, text, must_pass, why in CASES:
        total += 1
        found = checks.CATALOGUE[name](text, {"prompt": ""})
        if found.clean is not must_pass:
            verb = "fired on a correct response" if must_pass else "missed the failure"
            failed.append(f"{name}: {verb}, {why}\n      detail: {found.detail or '(none)'}")

    for name, probe, text, must_pass, why in PROBE_CASES:
        total += 1
        found = checks.CATALOGUE[name](text, probe)
        if found.clean is not must_pass:
            verb = "fired on a correct response" if must_pass else "missed the failure"
            failed.append(f"{name}: {verb}, {why}\n      detail: {found.detail or '(none)'}")

    covered = {c[0] for c in CASES} | {c[0] for c in PROBE_CASES}
    uncovered = sorted(set(checks.CATALOGUE) - covered)

    print()
    print(f"  gatecheck selftest · {total} sample(s) · {len(checks.CATALOGUE)} checks")
    if uncovered:
        print(f"  no sample for: {', '.join(uncovered)}")
    if failed:
        print(f"  {len(failed)} wrong:")
        for f in failed:
            print(f"    ! {f}")
    if failed or uncovered:
        # A check with no sample is a check nobody has run in either
        # direction. Naming it and exiting 0 leaves the suite green over it.
        print()
        return 1
    print(f"  all {total} samples behaved as specified")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
