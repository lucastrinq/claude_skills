---
name: pmm-audit-icp-4ps
description: "ICP & persona building (Jobs-to-be-Done) and 4Ps marketing mix audits, plus an orchestrator for a genuine multi-module 'full PMM audit' spanning ICP, competitive intel, win/loss, messaging, 4Ps, and launch together. Use when asked for: ICP definition, buyer persona, JTBD, 4Ps, pricing/channel/marketing-mix audit, or an explicit end-to-end/full product-marketing review touching several of these areas at once. Do NOT use for a single-area request that has its own dedicated skill — competitive analysis or battlecards (use competitive-intelligence directly), win/loss review (use win-loss-analyzer directly), messaging/positioning (use messaging-positioning directly), or launch planning (use product-launch-playbook directly). Loading this skill for those wastes a full skill-load only to redirect to the one that should've been loaded first. Do NOT use for purely technical product decisions, engineering roadmaps, or general business strategy unrelated to marketing."
---

# PMM Audit, ICP & 4Ps

This skill now owns two modules directly (ICP/Persona, 4Ps) and orchestrates the rest by
deferring to their own standalone skills. **Only load this skill for ICP/Persona, 4Ps, or a
request that genuinely spans multiple modules at once** — for a single-area request that maps
cleanly to Competitive Intelligence, Win/Loss, Messaging & Positioning, or Product Launch, go
straight to that skill instead. Routing a single-module request through here first costs a
full extra skill-load for no benefit, since this skill would just point back to it.

---

## Step 1: Read the Active Module Config

Before doing anything else, check which modules are currently active. The user controls this by saying things like **"activate Win/Loss"**, **"disable 4Ps"**, or **"show me my module config"**.

If no config has been set in this conversation, apply the **Default config** below.

### Module Registry

| # | Module | Default | Reference file |
|---|---|---|---|
| 1 | **ICP & Persona Builder** (JTBD-based) | ✅ Active | `references/icp-persona.md` |
| 2 | **Competitive Intelligence** | ✅ Active | → External: `competitive-intelligence` skill |
| 3 | **Win/Loss Analysis** | ✅ Active | → External: `win-loss-analyzer` skill |
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

This table matters once you're already here for ICP/4Ps or a genuine multi-module audit — it's
not a triggering guide. A single-area request (Competitive Intel, Win/Loss, Messaging,
Launch) shouldn't have loaded this skill in the first place; see the description at the top.
If one slips through anyway (e.g. the user explicitly asked for "the PMM skill"), route it to
the external skill directly rather than reproducing its logic here.

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
- **4Ps Marketing Mix** → `references/4ps.md` — Product/Price/Place/Promotion audit templates

### External Skills (already installed)
For these modules, defer fully to the existing skill — do not duplicate their logic:

- **Competitive Intelligence** → Apply the `competitive-intelligence` skill workflow (research protocol, mechanism method, battlecard output template — handles AppTweak and non-AppTweak competitors alike)
- **Win/Loss Analysis** → Apply the `win-loss-analyzer` skill workflow (data intake, pattern analysis, audience-specific reports)
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
