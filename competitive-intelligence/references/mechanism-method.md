# Deriving competitive arguments from facts (the mechanism method)

> Owns the step between "we did the research" (Research protocol in SKILL.md) and "we have an
> argument" (the output template). Run this whenever building a *new* structural argument
> against a competitor — not needed to reuse an already-verified positioning anchor as-is.

Raw platform research produces a feature list. A feature list is not a pitch — it's a
checklist that a competitor's next release can quietly invalidate. The method below turns raw
research into arguments that survive a few product release cycles, because they're rooted in
how a competitor's product is *built*, not what it currently *has*.

This is the process to use whenever:
- A prospect-facing pitch or sales collateral needs a new competitive argument, not just a
  feature comparison
- Positioning against a competitor needs refreshing because the existing anchor feels thin,
  dated, or too feature-based
- Someone asks "why is this actually different," not just "what's different"

## The method

### 1. Map mechanisms, not features

For each platform (AppTweak and the competitor), answer the same handful of questions:
- What's the unit of analysis? (brand? domain? app ID?)
- What has to be input by the customer vs. what ships pre-built?
- Where does the underlying data come from?

Skip marketing copy — the target is how the tool actually works. Usually found in docs,
pricing pages, or a live demo, not the homepage.

### 2. Lay the answers side by side

Put both platforms' answers to the same questions into one table, one row per question.
Differences become visually obvious once aligned this way, instead of buried across two
separate paragraphs of prose.

### 3. Keep structural deltas, drop feature gaps

- **Feature gap** ("they don't have X yet") — can disappear with a competitor's next release.
  A weak, short-lived argument. Don't build a positioning pillar on one.
- **Structural delta** — comes from how the product is architected and can't be patched
  without rebuilding it. This is what makes a durable argument.

Only structural deltas graduate to the next step. A feature gap can still be useful as a
tactical, disposable talking point (see the existing "Where they win" / structural gaps
sections in the competitor anchors) — but it doesn't earn a "3 reasons" or "reframe" slot on
its own.

### 4. Trace each delta to a blind spot

For each structural difference, ask: what does this force the tool to do, or stop it from
doing? Follow that forward until it lands on something a buyer would actually notice or
feel — not an abstract technical detail, but a real limitation in their day-to-day use.

### 5. Attach a concrete example

An abstract mechanism difference doesn't land in a pitch. Pair it with either:
- A **real proof point** (a screenshot, an actual score comparison) if one exists, or
- A simple, realistic **illustrative example** a rep can say out loud if it doesn't

### 6. Write claim → mechanism → consequence → example

Keep the final argument to that shape:
1. One bolded, one-line claim
2. A sentence on the mechanism that produces it
3. A sentence on why it matters to the buyer
4. The example

## Strength classification — use this every time

Not all structurally valid arguments are equally strong. Sort every finished argument into one
of two buckets, and carry that label into the output (don't blend them silently):

- **Directly provable** — you can show it. A screenshot, a side-by-side score, a documented
  fact. Safe to state with full confidence.
- **Mechanism-inferred** — you reason to it from how the tool works, illustrated with a
  plausible example, but not something you can screenshot. Still legitimate, but flag it
  internally as inferred. If a prospect pushes back with "how do you know that," the honest
  answer is "here's how their tool is built, and here's what that implies" — not a fabricated
  data point. Check G2 reviews or the competitor's own docs for anything that would upgrade an
  inferred argument to an evidenced one (e.g. a review literally saying "I didn't know what
  prompts to add").

When populating the output template's "3 reasons" or "Reframes" sections with an argument built
this way, keep the strength tag attached in internal notes even if it doesn't appear in the
prospect-facing framing — the rep needs to know which kind of claim they're making before
someone asks them to prove it.

## Worked example: AppTweak vs. Profound

**Argument 1 — Granularity**

| Question | Profound | AppTweak |
|---|---|---|
| Unit of analysis | Domain / brand | App ID |
| Input required | A domain | Nothing — the app is already mapped |
| Data source | Web crawlers + licensed GenAI data | AppDNA (200+ subcategories, real app-store data) |

**Structural delta:** domain-level vs. app-ID-level analysis. Not fixable by a Profound feature
release — it's what the tool measures at its core.

**Blind spot:** any app without a strong standalone website, or any brand running multiple
apps, gets flattened into one aggregated number.

**Example:** Rho (app invisible in AppTweak's data, brand well-scored in Profound), Zoho (one
aggregated brand score in Profound vs. per-app scoring in AppTweak), Adobe (20+ apps tied back
to one domain).

**Strength: Directly provable.** You can screenshot both platforms' scores side by side.

---

**Argument 2 — Discovery**

| Question | Profound | AppTweak |
|---|---|---|
| Prompt source | Customer defines and inputs prompts | Fixed set, pre-built from intents + AppDNA |
| What this requires of the user | Guessing which prompts matter | Nothing |

**Structural delta:** user-sourced prompts vs. system-generated prompts.

**Blind spot:** when a human defines prompts, they default to the general phrasing already in
their head ("best running app"), not the specific way real users query LLMs ("best app to
train for a half marathon") — so a user-defined system will systematically under-sample the
long tail.

**Example:** "best running app" vs. "best app to train for a half marathon."

**Strength: Mechanism-inferred, not directly provable.** It's reasoned from how the tool
works, not measured with a screenshot. Flag this distinction if a prospect pushes back — and
check G2 reviews or Profound's own docs for anything confirming "users struggle to know what
prompts to add," which would upgrade it from inferred to evidenced.
