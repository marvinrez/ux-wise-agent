# Applied Psychology: Principles as Conditions, Not Laws

The system prompt lists the behavioural and cognitive principles this skill reasons from. A list of names does not tell the agent when a principle applies. This document does. For each principle it gives the mechanism, the conditions under which it holds, the conditions under which it does not, the question that tests whether it is in play, and, where relevant, the point at which it turns into manipulation.

Two rules govern every entry.

1. **A principle is a condition, not a verdict.** "Hick's law says this menu is too long" asserts that the principle applies. Whether it applies depends on how users use the menu, which the agent usually has not been told. Write it as a conditional, or ask.
2. **Name the principle with its scope, or do not use it.** The Grounding Gate's Standard check covers principles as much as WCAG numbers. A principle cited outside its scope is the same failure as a criterion cited with the wrong number. Some popular effects have weak or mixed replication. They are marked below and must not be presented as settled.

---

## Perception, Attention, and Movement

### Fitts's law

- **Mechanism:** the time to reach a target grows with its distance and shrinks with its size, on a logarithmic scale.
- **Applies when:** the user points at something with a cursor, a finger, or a stylus, especially for frequent or high-stakes targets on the primary path.
- **Does not apply when:** the delay is in deciding, not in moving. It says nothing about whether the user knows which target to pick.
- **Note:** with a mouse, targets on the edge of the screen cannot be overshot, which makes them effectively larger. This does not carry over to touch, where the finger also covers what it aims at.
- **Question:** how far does the user travel to the most frequent action, and how large is it next to the controls around it?

### The isolation effect (von Restorff)

- **Mechanism:** an item that differs from its neighbours is noticed and remembered more than they are.
- **Applies when:** one element must stand out: the primary action, a warning, a changed value.
- **Does not apply when:** several elements compete for the same distinction. Each extra highlighted item weakens the others.
- **Ethical line:** giving visual weight to the option that serves the business and making the user's likely choice visually quiet is misdirection, one of the patterns in Brignull's taxonomy of deceptive design.
- **Question:** how many elements on this screen are styled to stand out, and is the one the user most needs among them?

### Banner blindness

- **Mechanism:** users learn to skip regions that look like advertising, including real content placed there. First described by Benway and Lane.
- **Applies when:** content the user must read sits in a position or style associated with ads: a box at the top or side, a bright promotional treatment.
- **Question:** does anything the user must read look like something users have learned to ignore?

---

## Memory and Cognitive Load

### Working memory limits (Miller; Cowan)

- **Mechanism:** people can hold only a few items in mind at once. Miller's 1956 paper put the span near seven. Cowan's later work argues that core capacity is closer to four chunks.
- **Applies when:** the user must carry something across steps or screens: a code from an email, a price while comparing plans on another page, an earlier choice in a multi-step form.
- **Does not apply when:** the items are visible. A menu the user can see is recognition, not recall, so working memory is not the constraint and "no more than seven items" does not follow. Long visible lists have other costs, such as scanning time and findability, and those are what to reason about.
- **Misuse:** treating seven as a hard limit for navigation or option lists. This is the most common misreading of the principle.
- **Question:** what does the user have to hold in mind from one moment to the next, and could the interface show it instead?

### Recognition over recall

- **Mechanism:** picking an item out of a set takes less effort than producing it from memory.
- **Applies when:** the user must name, type, or remember something the system could show: previous values, recent items, available commands.
- **Does not apply when:** experts have learned the recall path and find it faster, as with keyboard shortcuts and command input. Offer both paths.
- **Question:** where does the user have to remember something the system already knows?

### Cognitive load (Sweller)

- **Mechanism:** the effort of a task splits into the effort the task itself demands (intrinsic load) and the effort added by how it is presented (extraneous load). Design can reduce the second. It cannot remove the first.
- **Applies when:** a task feels hard. The useful question is which kind of hard.
- **Misuse:** making a task look simpler by hiding steps it actually requires, which moves the load to a later and worse moment (see Tesler's law in `knowledge/arbitration.md`).
- **Question:** which part of this effort comes from the task, and which from the interface?

### Serial position (primacy and recency)

- **Mechanism:** when people try to remember a list, they recall the first and last items better than the middle ones.
- **Applies when:** the user must remember a sequence after seeing it: onboarding steps, terms, a list read aloud.
- **Does not apply when:** the list stays visible while the user acts on it. Position then affects scanning and attention, which is a different argument.
- **Question:** does the user need to remember this list later, or only act on it now?

---

## Decisions

### Hick-Hyman law

- **Mechanism:** the time to choose grows with the logarithm of the number of options (Hick). More precisely, it grows with the information in the choice, so options the user expects are chosen faster (Hyman).
- **Applies when:** the user knows the options and reacts by picking one: a small set of familiar actions.
- **Does not apply when:** the user is looking for a known item by name, which is scanning or search and depends on layout and labels. It also does not apply to complex judgments, which depend on how hard the options are to compare, not on how many there are.
- **Misuse:** citing it to cut any long list, including one that users search by name.
- **Question:** is the user choosing among options they know, or looking for one they can already name?

### Choice overload (contested)

- **Mechanism, as claimed:** more options can lower the chance of choosing at all, or lower satisfaction with the choice.
- **Status:** the original findings have not replicated consistently. A meta-analysis by Scheibehenne, Greifeneder, and Todd found a mean effect close to zero, with wide variation between studies. Present it as a possibility that depends on conditions (options that are hard to compare, no clear preference, no way to sort or filter), never as a rule.
- **Question:** can the user compare these options on what matters to them, or only count them?

### Satisficing (Simon)

- **Mechanism:** people often take the first option that looks good enough instead of comparing all of them.
- **Applies when:** the user scans a page or a list, especially under time pressure. The first plausible match tends to get the click.
- **Design consequence, as a condition:** if a wrong item looks plausible earlier on the page than the right one, users who satisfice will pick it. Labels and order then matter more than completeness.
- **Question:** what is the first thing on this screen that looks like it might be the answer, and is it?

### Defaults and status quo bias

- **Mechanism:** people tend to keep whatever is preselected. Johnson and Goldstein's research on organ donation defaults is the standard illustration of how large the effect can be.
- **Applies when:** the product preselects any choice: settings, plans, consent, add-ons.
- **Ethical line:** a default is a decision made on the user's behalf. A default that serves the business at the user's expense is a deceptive pattern. For consent specifically, GDPR Recital 32 states that pre-ticked boxes do not constitute consent.
- **Question:** if the user never touches this setting, does the outcome serve them?

### Loss aversion and framing (Kahneman and Tversky)

- **Mechanism:** a loss weighs more than a gain of the same size, so the same fact moves people more when framed as a loss.
- **Applies when:** copy or design describes what the user will lose or miss: expiring trials, downgrades, cancellations.
- **Ethical line:** a real loss stated at its real size is information. An invented or inflated loss (a fake countdown, false scarcity, a guilt-laden decline button) is manipulation. Brignull's taxonomy names confirmshaming and false scarcity.
- **Question:** is the loss described here real, current, and stated at its actual size?

### Anchoring (Tversky and Kahneman)

- **Mechanism:** the first number people see pulls their later estimates toward it.
- **Applies when:** prices, plan tiers, quantities, or estimates appear in sequence.
- **Ethical line:** an anchor that is a real reference point, such as the price actually charged before, informs. An invented "was" price misleads, and many jurisdictions regulate it.
- **Question:** what is the first number the user sees, and is it a real reference?

### Social proof (Cialdini)

- **Mechanism:** when unsure, people look to what others do.
- **Applies when:** the user is uncertain and the evidence of others' choices is relevant to them: people like them, in a situation like theirs.
- **Ethical line:** counts, ratings, and activity notices must be real and current. Invented activity ("12 people are viewing this") is deceptive.
- **Question:** is the social evidence real, current, and drawn from people comparable to this user?

---

## Motivation and Effort

### Goal gradient and endowed progress

- **Mechanism:** effort tends to rise as people get closer to a goal, and progress that appears to have already started can raise completion. The usual references are Kivetz, Urminsky, and Zheng on the goal gradient in reward programs, and Nunes and Drèze on endowed progress.
- **Applies when:** the task has a visible end the user wants: setup steps, profile completion, a reward goal.
- **Ethical line:** progress shown must be real progress. A bar that starts partly filled to imply work the user did not do, or that slows near the end to hold attention, is deceptive.
- **Question:** does the progress shown match the work actually done and the work left?

### Fogg Behavior Model

- **Mechanism:** a behaviour happens when motivation, ability, and a prompt are present at the same moment.
- **Applies when:** diagnosing why a user does not act. Is the gap motivation, ability (it is too hard), or the prompt (it came at the wrong time, or not at all)?
- **Misuse:** raising motivation or adding prompts to get an action the user would not choose on reflection. The test is whether the user, fully informed, would want to have done it.
- **Question:** which of the three is missing for this user at this moment?

### Peak-end rule (Kahneman)

- **Mechanism:** people judge a past experience largely by its most intense moment and by its end, and give little weight to how long it lasted.
- **Applies when:** the question is how users will remember or rate an experience: satisfaction surveys, return visits, recommendations.
- **Does not apply when:** the question is whether users can finish the task. Remembered experience and task success are measured differently.
- **Question:** what is the worst moment in this flow, and how does the flow end?

---

## Mental Models and Error

### Conceptual models and the two gulfs (Norman)

- **Mechanism:** users act on their own model of how the system works. The gulf of execution is the distance between what they want to do and what they can work out how to do. The gulf of evaluation is the distance between what happened and what they can tell happened.
- **Applies when:** capable users still get it wrong, which usually means their model differs from the system's.
- **Question:** what does the user believe will happen when they act here, and what does the interface show them afterward?

### Slips and mistakes (Norman; Reason)

- **Mechanism:** a slip is the right intention carried out wrongly, such as a mis-tap or the wrong item in a list. A mistake is the wrong intention carried out correctly: the user misunderstood what the option does.
- **Design consequence, as a condition:** if the errors are slips, the fix is spacing, confirmation, or undo. If they are mistakes, the fix is a clearer model: labels, previews, explanations. A confirmation added for a mistake only helps the user confirm the wrong thing.
- **Question:** when users get this wrong, did they mean to do something else, or did they mean to do this and misunderstand what it does?

### Jakob's law (Nielsen)

- **Mechanism:** users spend most of their time in other products and bring those conventions with them.
- **Applies when:** a pattern departs from what users meet elsewhere. The departure has a learning cost, and it has to buy something.
- **Does not apply when:** the convention itself fails users, or the product's job is different enough that following the convention would mislead.
- **Question:** where have users met this pattern before, and does this product's version behave the same way?

### Aesthetic-usability effect

- **Mechanism:** users tend to rate attractive interfaces as easier to use. First reported by Kurosu and Kashimura.
- **Applies when:** interpreting usability ratings and test feedback. A polished prototype collects kinder ratings.
- **Design consequence, as a condition:** if a decision rests on satisfaction ratings from a polished prototype, the ratings may overstate usability. Task success and time on task measure what ratings cannot.
- **Question:** is this finding about what users did, or about what they said?

---

## Automation and AI

### Automation bias and complacency

- **Mechanism:** when a system is usually right, people check its output less and accept its errors more. Parasuraman and Manzey reviewed the evidence across domains.
- **Applies when:** an AI or automated feature makes suggestions or decisions that the user is meant to review.
- **Question:** what does the user have to do to notice that a suggestion is wrong? See `knowledge/ai-ux-considerations.md`.

---

## Effects Not to Cite as Settled

Some widely repeated claims have weak, mixed, or misread support. Do not present them as rules. If one is relevant, state its status.

- **Choice overload:** mixed replication. See above.
- **"Seven plus or minus two" for menus:** a misreading of Miller. See above.
- **The three-click rule:** a rule of thumb without a research basis, and Nielsen Norman Group has argued against it. Reason about whether each step is clear, not about how many steps there are.
- **"Users don't scroll":** Nielsen Norman Group's eye-tracking research found that users do scroll, while giving more attention to what appears before they have to. Position matters. Scrolling is not a wall.
- **The Zeigarnik effect (better memory for unfinished tasks):** replication has been inconsistent. Do not use it to justify leaving tasks visibly open.
