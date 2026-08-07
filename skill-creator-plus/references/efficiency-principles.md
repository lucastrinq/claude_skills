# AI Resource Efficiency — Principles & Best Practices

## Why It Matters

Every turn in a conversation reprocesses the entire context window — all previous messages, skill files, and instructions. The two biggest energy drivers are:
- **Context length** — how many tokens are processed each turn
- **Number of turns** — how many times that processing happens

Skill files are a small fixed cost. Long multi-turn conversations compound significantly.

---

## Best Practices (apply in every skill)

1. **Start fresh conversations often** — the single highest-impact habit. When a topic is done, close the chat.
2. **Front-load context** — one well-structured message beats five clarifying exchanges.
3. **Be specific from the start** — vague prompts generate answers you iterate on; precise prompts reduce rounds.
4. **Batch requests** — combine related asks into one message rather than chaining follow-ups.
5. **Request only what you need** — a bullet list costs less than a full breakdown when that's all you need.
6. **Don't extend conversations unnecessarily** — sentimental continuity has a real compute cost.

---

## How to Apply This in a Skill

Add this pointer in any skill where resource usage is relevant:

> "Before proceeding, check `efficiency-principles.md`: can this be achieved in fewer turns with a more structured input? If the conversation is already long, flag to the user that starting fresh would reduce their footprint."

And gate expensive operations with:

> "Only proceed with [resource-intensive step] if the task genuinely requires it. If a simpler approach would achieve the same result, prefer that."
