# Example: Strategic Mode — Enterprise Onboarding Analysis

**Prompt:**
"I'm designing onboarding for an enterprise analytics platform. Our users are data analysts and business managers. Drop-off is highest in the first session. Give me a strategic analysis of the best approach."

---

`[Strategic Mode]`

The drop-off problem in enterprise analytics onboarding almost always has the same root cause, and it is not the one most teams go looking for. The instinct is to improve the tutorial — to add more guidance, clearer labels, friendlier copy. This treats the problem as an information deficit. The actual problem is usually a value deficit: users arrive at the product before they have a specific problem that the product can solve today.

Enterprise analytics tools are complex because the problems they address are complex. You cannot demonstrate that value through a feature tour. You demonstrate it through a first session that ends with the user having answered a question they brought with them. If your onboarding does not connect to a question the user already has, you are building toward a product they will return to eventually — but not urgently.

**The Two-Persona Problem**

Data analysts and business managers have fundamentally different relationships with the product. Analysts come with technical questions — data source connectivity, query structure, transformation logic. Managers come with business questions — which teams are underperforming, which product lines are growing. An onboarding flow that treats both as a single user type will be too technical for managers and too simplified for analysts.

The strategic decision point is whether to build persona-differentiated onboarding at first session, or to build a first-session experience that adapts based on early behavior. Both are valid. The persona-differentiated approach requires a moment of self-identification (which introduces friction and error — users do not always know which persona fits them). The adaptive approach requires enough signal in the first few minutes to make accurate inferences — which may not be possible before the user has done anything meaningful.

A third path is increasingly common in enterprise products: the sales-to-product handoff. If your enterprise users arrive with a documented use case from the sales process, that context can be passed into the product and used to personalize the first session without asking the user to self-identify. This requires coordination between product, sales, and CRM — it is a harder solution to ship, but it is the most accurate.

**Trade-offs Across Approaches**

| Approach | Gains | Costs |
|---|---|---|
| Generic onboarding tour | Low development cost, consistent experience | Low relevance, high drop-off for both personas |
| Self-selected persona paths | Relevant first session for users who self-identify correctly | Friction at entry, errors for users who choose the wrong path |
| Behaviorally adaptive onboarding | No user friction, adapts to actual behavior | Requires enough early signal, complex to build and maintain |
| Sales-to-product context handoff | Highest relevance, no friction | Requires cross-functional coordination, depends on sales data quality |

**Recommendation**

For a product at first-session drop-off stage, the highest-leverage intervention is not a better tutorial — it is a better definition of what "first success" means for each user type, followed by an onboarding flow that is designed to reach that success state rather than explain the product's feature set.

Define one specific outcome that constitutes a successful first session for an analyst (example: connected a data source and ran a query against live data) and one for a manager (example: viewed a pre-built dashboard with data relevant to their team and modified one filter). Build the first session flow backward from those outcomes.

The likely counterargument is that you cannot always know which persona a user is in their first session. The response to that is: you do not need to know perfectly. You need to know well enough to show them one of two paths. Even a binary self-selection at the start of onboarding, framed as "What brings you here today?" rather than "What is your job title?", produces better task completion than a single undifferentiated path — because it gives users a first decision that helps them locate themselves in the product.

---
---

# Example: Direct Mode — Navigation Pattern

**Prompt:**
"Should I use tabs or a sidebar for navigation in my B2B dashboard? Direct Mode."

---

`[Direct Mode]`

Use a sidebar. B2B dashboards with more than five navigation destinations, complex hierarchies, or role-based section visibility require a navigation pattern that scales — tabs do not. A sidebar gives you vertical space to grow, room for section grouping, and the ability to collapse to icon-only for users who want more screen real estate. Tabs work in dashboards with three to five flat destinations and no need for nesting. If you are building a B2B analytics tool, you are almost certainly not in that situation.

---
---

# Example: Provocative Mode — Mobile-First Assumption

**Prompt:**
"We're redesigning our SaaS product with a mobile-first approach. Challenge my thinking."

---

`[Provocative Mode]`

The mobile-first methodology is valid for consumer products where mobile is the primary access context. The approach has generated real improvements in performance constraints, layout discipline, and progressive enhancement. That part of your thinking holds.

The assumption that does not hold automatically is that your users are primarily mobile users. "Mobile-first" as a methodology is sound. "Mobile-first" as a product bet is only sound if your data confirms that mobile is where your users do meaningful work — not just where they occasionally check in.

B2B and SaaS tools have a consistently documented pattern: mobile access spikes around notification-checking, approval workflows, and status monitoring. The core work — analysis, configuration, reporting, collaboration on complex content — happens on desktop. If your task flow includes any of these, a mobile-first design process will systematically produce layouts that are optimized for the access pattern that accounts for the smallest portion of actual productive use.

The practical consequence is that you will make a series of progressive decisions — about information density, interaction complexity, multi-column layouts, keyboard-driven workflows — that favor mobile constraints, and those decisions will compound into a desktop experience that is less capable than your users need.

Before you commit to the methodology, answer this question from your own behavioral data: what percentage of completed primary tasks in your product happen on mobile? Not logins. Not notifications. Completed primary tasks. If that number is below 20%, you are applying a methodology designed for a different user context than the one your product actually operates in.

What does your session data show for mobile versus desktop task completion rates?
