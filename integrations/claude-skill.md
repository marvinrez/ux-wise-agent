# Claude Integration Guide

## Using UX Wise AI — Agent with Claude

---

## Before Any Method: Two Steps That Are Not Optional

1. **Run the acceptance probes.** `docs/grounding-gate.md` lists eight prompts with expected verdicts. Run them in the environment you just installed into. They take a few minutes and they tell you whether the Grounding Gate is actually active there — a system prompt that was truncated on paste, or a model that ignores the gate, fails these visibly. Re-run after any edit to `prompts/system-prompt.md` and after any model change.

2. **Name a human owner.** One person, named where your team looks, accountable for re-running the probes, reviewing output on its way out of the team, and correcting the record when the agent is wrong. `docs/ownership.md` has the checklist and the table of which outputs can travel unreviewed. Skipping this is how a reasoning tool becomes an unattributed source in someone's roadmap.

---

## Method 1: Claude Projects — Skill File (Recommended for Claude Code users)

If you are using Claude Code or a Claude environment that supports the Anthropic skills standard, install `SKILL.md` directly:

1. Copy the `ux-wise-agent/` directory into your project's `.claude/skills/` folder
2. Rename the directory to `ux-wise-agent` if it isn't already
3. Claude will pick up `SKILL.md` automatically and trigger the skill when relevant UX reasoning tasks are requested

The `SKILL.md` file contains YAML frontmatter with the skill name, description, and compatibility metadata. Do not remove or modify the frontmatter block — it controls how the skill is triggered.

---

## Method 2: Claude Projects — Manual Paste (Recommended for claude.ai users)

1. Open [claude.ai](https://claude.ai) and navigate to Projects
2. Create a new project named "UX Wise AI — Agent"
3. Click "Edit project instructions"
4. Copy the full contents of `prompts/system-prompt.md` — from the line after `## SYSTEM PROMPT — START` to the line before `## SYSTEM PROMPT — END`
5. Paste into the project instructions field
6. Save the project

All conversations within this project will operate as UX Wise AI — Agent.

**Advantages:** Persistent across sessions. No need to re-paste the prompt. Conversations are organized within the project context.

---

## Method 3: Anthropic API — Direct System Prompt

```python
import anthropic

with open("prompts/system-prompt.md", "r") as f:
    system_prompt = f.read()

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": "Give me three alternative UX solutions for reducing drop-off during enterprise onboarding."
        }
    ]
)

print(response.content[0].text)
```

---

## Method 4: Multi-Turn Conversation via API

For sessions with memory across turns:

```python
import anthropic

with open("prompts/system-prompt.md", "r") as f:
    system_prompt = f.read()

client = anthropic.Anthropic(api_key="your-api-key")

conversation_history = []

def chat(user_message: str) -> str:
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=system_prompt,
        messages=conversation_history
    )

    assistant_message = response.content[0].text

    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message

# Example usage
print(chat("Use Strategic Mode. I'm redesigning checkout for a B2B procurement tool. What are the key friction points I should prioritize?"))
print(chat("Now use Provocative Mode to challenge the direction I just described."))
```

---

## Method 5: Streaming Responses

For long analytical responses, streaming improves the user experience in interfaces you build:

```python
import anthropic

with open("prompts/system-prompt.md", "r") as f:
    system_prompt = f.read()

client = anthropic.Anthropic(api_key="your-api-key")

with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": "Use Strategic Mode. Challenge my assumptions about progressive disclosure in complex enterprise forms."
        }
    ]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

---

## Model Selection

| Model | Best for |
|---|---|
| `claude-opus-4-6` | Complex Strategic and Provocative Mode responses requiring extended analytical depth |
| `claude-sonnet-4-6` | Direct Mode responses, Research Mode protocol generation, shorter interactions |

For most usage, `claude-sonnet-4-6` is sufficient and responds faster. Use `claude-opus-4-6` for high-stakes decisions where the depth of Strategic Mode analysis matters.

---

## Mode Activation in Prompts

When building interfaces on top of this skill, pre-activate a mode by prefixing the user's message:

```python
user_input = "Should I use tabs or a sidebar?"
mode = "Direct Mode"

formatted_message = f"Use {mode}. {user_input}"
```

This produces more consistent outputs than asking users to specify modes manually.

In v2.0, the agent also infers mode from contextual signals without explicit keywords. Explicit mode specification still takes precedence.

---

## Deploying via API — Minimum Bar

An API deployment removes the human from the loop by construction, which moves the whole burden onto the interface you build around it. Before it reaches anyone but you:

- **Render the `Unverified` line.** The agent emits it when a response passes the Grounding Gate on assumptions or conditionals. If your UI strips it as noise, you have removed the only signal your users get about which parts are the model's construction.
- **State what the agent cannot see.** A UX reasoning agent in a product surface will be asked to review screens. Every one of those is an Artifact-check failure. Say so in the interface rather than letting each user discover it.
- **Attribute the output to the tool**, not to a colleague's opinion and not to a research finding.
- **Give users a route to report a fabrication**, and someone who reads it.

A deployment with none of these is a fluent text generator pointed at design decisions with nobody watching it. See `docs/ownership.md`.

---

## Token Considerations

| Mode | Typical response length |
|---|---|
| Strategic Mode (complex problem) | 500–900 tokens |
| Strategic Mode (focused question) | 300–500 tokens |
| Direct Mode | 80–150 tokens |
| Provocative Mode | 250–450 tokens |
| Research Mode (protocol design) | 500–800 tokens |

Set `max_tokens` to at least 1500 to avoid truncation on complex Strategic or Research Mode responses. For multi-turn sessions on a single complex topic, monitor context window usage if the conversation exceeds 10 turns.

