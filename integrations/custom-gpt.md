# Custom GPT Integration Guide

## Deploying UX Wise AI — Agent as a Custom GPT

---

## Configuration

1. Go to [chat.openai.com](https://chat.openai.com) and navigate to "Explore GPTs" → "Create a GPT"
2. In the "Configure" tab, set the following:

**Name:** UX Wise AI — Agent

**Description:**
```
A peer-level UX reasoning partner for senior designers, product managers, and researchers. Operates in three modes: Strategic (deep analysis and trade-offs), Direct (one recommendation, compressed reasoning), and Provocative (adversarial challenge of your assumptions). PhD-level rigor. No hedging.
```

**Instructions:**
Copy and paste the full contents of `prompts/system-prompt.md` into this field.

**Conversation starters:**
```
Give me three alternative UX solutions for [insert problem].
Challenge my assumptions about [insert UX principle].
Use Direct Mode: Should I use [pattern A] or [pattern B] for [feature]?
Use Strategic Mode: How do I balance business goals and user needs when designing [feature]?
Use Provocative Mode: We're going with [design direction]. What am I missing?
How do I design for uncertainty and ambiguity in [complex problem]?
```

---

## Capabilities Settings

| Capability | Setting | Reason |
|---|---|---|
| Web Search | Disabled by default | The skill reasons from established knowledge, not current search results. Enable only if you want the agent to reference current research. |
| Image Input | Enabled | Useful for analyzing screenshots of existing interfaces |
| Code Interpreter | Disabled | Not relevant to UX reasoning |
| DALL-E | Disabled | This skill does not generate visuals |

---

## Knowledge Files (Optional)

You can upload reference documents to extend the agent's knowledge base. Recommended files:

- WCAG 2.2 guidelines (PDF from W3C)
- Nielsen Norman Group research papers relevant to your product domain
- Your own design system documentation (this makes the agent's recommendations context-specific to your product)
- Any established competitor or benchmark analysis documents

Note: The agent will reference uploaded knowledge when relevant but will not treat it as more authoritative than established UX principles unless the document provides specific research evidence.

---

## Limitations in Custom GPT Context

Custom GPTs currently do not support persistent memory across separate conversations by default. Each new conversation starts without context from previous sessions. If continuity is important for your use case, begin each session with a brief context statement:

```
Context: We are redesigning a B2B procurement tool, dashboard-first product, 
primary users are procurement managers and finance leads, current biggest 
problem is that users cannot find the approval workflow. 

Use Strategic Mode. What should I prioritize?
```

---

## Sharing the Custom GPT

If you publish this as a shared GPT, note in the description that it operates under the UX Wise AI — Agent skill definition and link to this repository. The skill definition is MIT licensed — free to use and distribute with attribution appreciated.
