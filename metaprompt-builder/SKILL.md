---
name: metaprompt-builder
description: "On-demand prompt amplifier. Builds a high-quality, structured metaprompt to maximize depth, context, and output quality for a specific task — before or during a conversation. Use when the user says 'help me build a prompt for X', 'make this prompt better', 'I need a strong prompt to do Y', 'write me a metaprompt', 'I need more depth in this', 'take this seriously', 'I want the best possible prompt for Z', or any signal that they want rigorous, structured thinking before executing a task. Also trigger when the user flags complexity, stakes, or nuance — even without explicitly saying 'prompt'. Do NOT use when the goal is a reusable skill or system (use skill-creator-plus instead), when the user wants a direct answer right now rather than a prompt to use, for simple one-off questions that need no amplification, or for routine low-stakes tasks where prompt quality does not materially change the outcome. Be resource-conscious — trigger only when the depth, stakes, or reusability of the task genuinely justify it."
---

# Metaprompt Builder

This skill turns a task, idea, or rough prompt into a precise, structured metaprompt that maximizes the quality of what comes next. It works before a conversation starts or mid-conversation when a reframe is needed.

---

## Step 1 — Assess & Interview

Before building anything, assess what you already know:

**If the request is already detailed** (clear goal, context, constraints, desired output): skip or minimise the interview. Use judgment — err on the side of asking at least one confirming question if anything is ambiguous.

**If the request is thin or complex**: interview the user first. Adapt the style to complexity:
- Simple tasks → batch all questions at once, numbered, concise
- Complex/deep tasks → conversational, 2–3 questions at a time, go deeper based on answers

**Core things to surface in the interview:**
1. What is the goal or desired outcome?
2. Who is the audience for the final output (just you, a team, clients)?
3. What context or background is relevant?
4. Are there constraints (length, tone, format, data sources)?
5. What does a great output look and feel like?
6. Is there an example, inspiration, or reference to draw from?
7. Which of the 3 construction paths fits best? (see below)

**Never start building until you have enough to fill the structure properly.** Incomplete input = incomplete metaprompt.

---

## Step 2 — Choose Construction Path

Three options depending on what the user has:

| Path | When to use | How |
|---|---|---|
| **1 — Instructions Prompt** | User has a clear goal and enough context | Build directly using the 8-part structure |
| **2 — Example Breakdown** | User has a great example of the output they want | Ask AI to deconstruct it step-by-step, then turn that into Path 1 |
| **3 — Expert Source** | User has a reliable reference or domain source | Extract a guide from it (Path 2 logic), then build Path 1 |

Default to **Path 1** unless the user signals they have an example or source to work from.

---

## Step 3 — Build the Metaprompt

Scale the output structure to task complexity:

**Lean (simple tasks):** Role + Instructions + Output Format
**Full (complex/deep tasks):** All 8 parts below

For the full structure, consult `references/metaprompt-template.md` for the complete template, field-by-field guidance, and the original metaprompt to preserve verbatim.

### The 8-Part Structure at a Glance

1. **Role / Persona** — Who the AI is. Be specific. Name the expert (e.g. "Expert Copywriter with 15 years in B2B SaaS", not just "a writer").
2. **Context** — The situation, background, and why this matters.
3. **Requirements & Constraints** — What must be true. What must not happen.
4. **Inspirations & Examples** — References, examples, tone benchmarks.
5. **Mental Model & Feel** — The expert persona's thinking style. How it should reason, not just what it should produce.
6. **Core Intent (The Why)** — The deeper purpose behind the task. This is what prevents a technically correct but soulless output.
7. **Instructions** — Step-by-step what to do. Decompose into subtasks if complex. Assign sub-experts if needed.
8. **Output Format** — Exactly how the final result should look.

---

## Step 4 — Expert Personas

When the task benefits from specialist reasoning, actively name and assign the right persona(s). Don't leave it vague.

Consult `references/expert-personas.md` for a curated list of expert persona patterns by task type (creative, analytical, technical, strategic, etc.) and how to write them with precision.

Key rule: **use "fresh eyes"** — never assign the same expert to both create and validate a solution. If verification matters, assign a second independent expert to review.

---

## Step 5 — Anti-Hallucination Handling

**Always bake in** a "never guess, disclaim uncertainty" instruction — in every prompt, regardless of task type.

**Exception — subjective/aesthetic fields** (UI feel, tone, creative direction, visual judgment): replace the hard disclaimer with a transparency flag:
- In the prompt itself: instruct the AI to signal when it's making a judgment call vs. stating a fact
- In your explanation to the user: note *"this field involves interpretation — this is my read on it, adjust if it doesn't match your intent"*
- If unsure whether a field is subjective: ask the user before assuming

Baseline anti-hallucination instruction to include in every generated prompt:
> "If you are uncertain about any fact, figure, or claim, do not guess. State clearly that you are uncertain and either ask for clarification or provide a clearly labelled estimate with your reasoning."

---

## Step 6 — Deliver

Output format:
1. **The metaprompt** — plain text, clean, copy-paste ready
2. **Brief explanation** — 3–5 bullet points covering the key structural choices made (why this persona, why this structure depth, any judgment calls on subjective fields, etc.)

Then offer one optional refinement round:
> "Want me to adjust anything — the persona, the depth, a specific section?"

Do not push for more iteration after that unless the user initiates it.

---

## Resource Efficiency

This skill has a real compute cost. Before triggering, apply the test in `references/efficiency-principles.md`. In short:
- If the conversation is already long, suggest the user start a fresh chat first
- If a direct answer would serve just as well as a built prompt, skip the skill
- Prefer one precise turn over two approximate ones

## When NOT to Use This Skill

Be deliberate. This skill is for tasks where prompt quality materially changes the outcome. Skip it for:
- Quick factual questions or simple requests you'd naturally dash off
- Tasks with no reuse value and low stakes
- Anything already well-specified enough that amplification adds noise, not signal
- Routine back-and-forth in an ongoing conversation

**Good trigger test:** "Would a poorly structured prompt here produce a meaningfully worse result?" If no — skip it.

## Non-Negotiables

- Never build the prompt before understanding the task well enough to fill every section properly
- Always name expert personas specifically — no vague "an expert" or "a professional"
- Always include the anti-hallucination baseline, adapted for subjective fields
- Scale the structure to complexity — a lean prompt for a simple task is better than a bloated one
- This skill produces a *prompt to be used*, not a direct answer — keep that distinction clear throughout

---

## Reference Files

- `references/metaprompt-template.md` — Full 8-part template with field guidance, the original metaprompt verbatim, and annotated examples
- `references/expert-personas.md` — Curated expert persona patterns by domain, with writing guidance
- `references/efficiency-principles.md` — Resource efficiency best practices; consult when deciding whether to trigger this skill or when the conversation is running long
