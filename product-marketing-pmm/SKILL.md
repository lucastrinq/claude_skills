---
name: product-marketing-pmm
description: "Full-stack product marketing skill covering ICP & persona building (Jobs-to-be-Done), competitive intelligence, win/loss analysis, messaging & positioning, 4Ps marketing mix, and product launch planning. Use when asked for: ICP definition, buyer persona, JTBD, competitive analysis, battlecard, win/loss review, go-to-market strategy, messaging framework, value proposition, 4Ps, product positioning, pricing strategy, launch plan, or GTM playbook. Also use when the user says 'help me with product marketing', 'how should we position this', 'who is our buyer', or 'why are we losing deals'. Modules can be activated or deactivated — always check the active module config first. Do NOT use for purely technical product decisions, engineering roadmaps, or general business strategy unrelated to marketing."
---

# Product Marketing Meta-Skill (PMM)

This skill orchestrates a suite of product marketing modules. Each module is independently activatable — you apply only what's enabled, keeping outputs focused and context lean.

---

## Step 1: Read the Active Module Config

Before doing anything else, check which modules are currently active. The user controls this by saying things like **"activate Win/Loss"**, **"disable 4Ps"**, or **"show me my module config"**.

If no config has been set in this conversation, apply the **Default config** below.

### Module Registry

| # | Module | Default | Reference file |
|---|---|---|---|
| 1 | **ICP & Persona Builder** (JTBD-based) | ✅ Active | `references/icp-persona.md` |
| 2 | **Competitive Intelligence** | ✅ Active | `references/competitive-intel.md` |
| 3 | **Win/Loss Analysis** | ✅ Active | `references/win-loss.md` |
| 4 | **Messaging & Positioning** | ✅ Active | → External: `messaging-positioning` skill |
| 5 | **4Ps Marketing Mix** | ⬜ Inactive | `references/4ps.md` |
| 6 | **Product Launch Playbook** | ✅ Active | → External: `product-launch-playbook` skill |

> **Default config** = modules 1, 2, 3, 4, 6 active. Module 5 (4Ps) inactive by default — enable when doing a full marketing mix audit or pricing/channel strategy work.

---

## Step 2: Handle Module Config Commands

Recognize and act on these natural language commands immediately:

| User says | Action |
|---|---|
| "activate [module name]" / "enable [module]" | Mark it active, confirm: "✅ [Module] is now active." |
| "disable [module]" / "deactivate [module]" | Mark it inactive, confirm: "⬜ [Module] is now disabled." |
| "show my config" / "what modules are active?" | Print the Module Registry table with current status |
| "reset to default" | Restore the default config above |
| "activate all" / "full mode" | Enable all 6 modules |
| "minimal mode" | Keep only ICP + Messaging active |

After any config change, state the new active set before proceeding.

---

## Step 3: Route the Request

Map the user's request to the right module(s). If a required module is inactive, say so and offer to activate it.

| User intent | Module(s) to apply |
|---|---|
| "Who is our buyer / define our ICP / build a persona" | ICP & Persona Builder |
| "Why are we losing deals / win/loss review / analyze losses" | Win/Loss Analysis |
| "Competitive landscape / what are competitors doing / battlecard" | Competitive Intelligence |
| "How should we position / messaging / value prop / tagline" | Messaging & Positioning |
| "Pricing strategy / channels / marketing mix / 4Ps audit" | 4Ps Marketing Mix |
| "Launch plan / GTM / go-to-market / launch brief" | Product Launch Playbook |
| "Full PMM audit / end-to-end marketing strategy" | All active modules, sequenced |

For multi-module requests, sequence outputs in this order: ICP → Competitive Intel → Win/Loss → Messaging → 4Ps → Launch.

---

## Step 4: Load and Apply Module

Read the relevant reference file(s) for active modules only. Apply the framework to the user's specific context — never produce generic templates.

### Reference Files (internal modules)
Consult these files for full templates, frameworks, and examples:

- **ICP & Persona (JTBD)** → `references/icp-persona.md` — JTBD interview structure, ICP scoring, persona canvas
- **Competitive Intelligence** → `references/competitive-intel.md` — intel gathering, competitor profiles, battlecard template
- **Win/Loss Analysis** → `references/win-loss.md` — interview guide, pattern analysis, output formats
- **4Ps Marketing Mix** → `references/4ps.md` — Product/Price/Place/Promotion audit templates

### External Skills (already installed)
For these modules, defer fully to the existing skill — do not duplicate their logic:

- **Messaging & Positioning** → Apply the `messaging-positioning` skill workflow
- **Product Launch Playbook** → Apply the `product-launch-playbook` skill workflow

---

## Output Standards (all modules)

Regardless of which module is active, every output must:

1. **Answer the business question first** — not the framework. Lead with the insight, not the template.
2. **Be specific to the user's context** — no generic personas, no placeholder competitors.
3. **End with a clear next action** — what decision does this enable? What should happen next?
4. **Flag inactive modules that would add value** — e.g., "Win/Loss is currently disabled — activating it would strengthen this competitive analysis."

---

## Error Handling

If a request requires a module that's inactive, do not silently skip it or produce a degraded output without warning.

Instead: *"This request would benefit from [Module X], which is currently inactive. Want me to activate it for this response?"*

If a request is ambiguous across modules, name which ones you're applying and why before generating output.

For connection or tool issues with external skills, consult `references/error-handling.md`.
