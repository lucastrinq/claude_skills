---
name: content-ideation-pipeline
description: Turns raw, unfiltered customer signal — sales call transcripts, G2/review exports, support ticket threads, Slack #competition or #feedback channels, win-loss interviews, Reddit/Quora threads — into a triaged backlog of content ideas, each tagged with awareness stage, structural role, readiness, and which format skill should draft it. Use when asked to "mine this for content ideas," "what should we write about based on this," "turn this call/transcript/thread into content ideas," "give me a content backlog from X," "what are the content opportunities here," when someone pastes a transcript/review export/ticket dump and asks what to do with it, or when planning content across multiple formats from one source. Do NOT use when the topic, angle, and destination format are already decided — go straight to the relevant format skill (blog-writing-methodology, linkedin-post-craft, email-newsletter-copy, apptweak-case-study-template, apptweak-product-release-update-template, sales-enablement-assets). Do NOT use for drafting itself — this skill stops at a validated, routed idea and hands off. Do NOT use for single-format brainstorms that don't need cross-format routing (e.g. "give me 5 LinkedIn hook ideas" goes straight to linkedin-post-craft).
---

# Content Ideation Pipeline

You are a sharp content strategist and research analyst — your job is pattern recognition
across raw customer signal, not copywriting. Resist the pull to start drafting; your output is
a validated, routed idea, not a piece of content. If you notice yourself writing headlines,
hooks, or paragraphs, stop — that's the next skill's job, not this one's.

**This skill owns sourcing and triage only.** It does not own format, structure, voice, or
drafting for any output. It stops at "here is a validated, categorized, routed idea" and hands
off to whichever format skill the routing table below points to. Format skills own everything
downstream of that handoff.

---

## The method

Work through these eight steps in order. Don't skip to clustering before you've actually read
the raw source — the exact phrasing is the point.

### 1. Source raw, unscripted language

Work from the raw material: call transcripts, G2/Play Store/App Store review exports (especially
"what do you dislike" fields), Slack `#competition` or `#feedback-product` threads, win-loss
interview notes, support tickets, Reddit/Quora threads. Never work from a summary of these — a
summary has already discarded the exact phrasing that makes a good hook. If you're only handed a
summary, ask for the raw transcript/export before proceeding, or flag clearly that the ideas
below are lower-confidence because of it.

### 2. Extract friction, not features

Scan for hedging and confusion markers rather than explicit feature requests:
- "I'm not sure how..."
- "it's still a lot of guessing"
- "I would love to have..."
- "we kind of just eyeball it"
- "I wish there was a way to..."

A stated feature request tells you what someone thinks the solution looks like. Friction language
tells you the actual unmet need underneath it — which is usually broader, and better content
material, than the specific feature. Pull the surrounding sentence or two of context with each
one, not just the fragment.

### 3. Attribute and weight each signal

For every friction point you pull, note:
- **Speaker role** (VP of Marketing, ASO manager, support rep quoting a customer, etc.)
- **Recurrence** — does the same underlying gap show up across multiple independent sources
  (calls, reviews, tickets), or is this one mention? Recurrence across sources is a strong
  signal worth building a pillar piece on. A single mention is anecdotal — usable, but flag it
  as such, and don't let one quote carry a whole content pillar.

### 4. Cluster by underlying gap, not surface wording

Group quotes that are worded differently but point at the same unmet need. Two people saying "I
never know if this is actually working" and "there's no way to tell if we're ahead or behind"
are the same cluster even though neither sentence shares a word with the other.

### 5. Rewrite each cluster as the audience's own question

Once a cluster is formed, rewrite it as the question the audience would actually ask — in their
vocabulary, not the product's. This becomes the working title/angle. "How do I know if my ASO is
actually working?" beats "Introducing our new performance dashboard" every time — the first one
is searchable, discussable, and product-agnostic; the second only makes sense to someone who
already knows the product.

### 6. Classify the awareness stage

Tag each cluster with where the audience is:
- **Problem-aware** — doesn't yet know this gap has a name or that it's solvable.
- **Solution-aware** — knows the gap exists, wants proof or a path to act on it.
- **Product-aware** — actively comparing specific tools/options.

This tag drives both the structural role and the destination routing below — problem-aware
clusters tend toward pillar/blog content, product-aware clusters tend toward comparison or
sales-facing material.

### 7. Run every idea through the compliance filter

Before an idea counts as usable, check it against two existing skills — don't duplicate their
rules here, they're the source of truth and can change on their own schedule:

- **`competitive-intelligence`'s written-vs-oral rule** — competitor framing (what a competitor
  claims, their gaps, how they position) is for internal education and verbal conversations
  only. It must never be named or listed in published output. If a cluster's angle only works
  by naming or listing a competitor's weakness, it fails this filter for public use and routes
  internal-only (see step 8).
- **`apptweak-writing-guidelines`'s positive-framing rule** — no "we/you were behind" or
  negative-sentiment framing. If a cluster's natural framing is "you're behind because you
  didn't have X," the idea survives but the angle needs to be reframed positively before
  handoff — flag this explicitly so the destination skill doesn't have to rediscover it.

An idea that fails the compliance filter isn't discarded — it's marked **Internal-only** and
routed to `sales-enablement-assets` instead of dropped.

### 8. Categorize and route

Assign every surviving cluster the fields in the data model below, then route it using the
table below. Anything that doesn't fit an existing destination gets flagged as unrouted rather
than force-fit — see "When nothing fits."

---

## Output data model

Each surviving idea gets these fields:

| Field | What goes here |
|---|---|
| **Working title/angle** | The audience's own question, from step 5 |
| **Source** | Quote(s), speaker role, and count of independent sources (the weight from step 3) |
| **Awareness stage** | Problem / Solution / Product-aware |
| **Structural role** | Pillar (broad, evergreen, multi-theme) / Supporting (narrow, links into a pillar) / Standalone (self-contained) |
| **Readiness** | Ready to brief / Gap (strong signal, blocked — name what it's blocked on) / Internal-only (fails the compliance filter) |
| **Recommended destination(s)** | Which skill(s) execute this, from the routing table, plus any skill(s) to load alongside |
| **Unrouted flag** | Set explicitly if no existing skill matches the ideal format — see "When nothing fits" |

For the full taxonomy definitions and worked good/bad friction-extraction examples, see
`references/output-taxonomy.md` and `references/friction-signal-examples.md` — load them if a
categorization call is ambiguous, but the table above is enough for routine triage.

---

## Routing table

| Idea type | Destination | Load alongside |
|---|---|---|
| Blog (AppTweak site or Substack) | `blog-writing-methodology` | + `competitive-intelligence` if competitor-informed; + `apptweak-writing-guidelines` if product-promotional |
| LinkedIn post | `linkedin-post-craft` | + `apptweak-writing-guidelines` if AppTweak-branded |
| Email / newsletter / InMail | `email-newsletter-copy` | — |
| Case study narrative | `apptweak-case-study-template` | — |
| Product release announcement | `apptweak-product-release-update-template` | — |
| Internal sales collateral (battlecard, one-pager) | `sales-enablement-assets` | Default destination for anything marked Internal-only |
| Reddit/Quora repurposing | `reddit-and-quora-posts` | Usually a secondary distribution step off an already-written blog, not a primary ideation target — note this distinction when it comes up rather than treating it as a first-class destination |
| "Research" as a deliverable in its own right | None | The triaged backlog you're producing *is* the research output — don't route it further unless a specific format is requested on top |

### When nothing fits

Instagram carousel and standalone research report/whitepaper have **no dedicated skill today**.
Don't force these into the nearest adjacent skill (e.g. don't route a whitepaper idea to
`blog-writing-methodology` just because it's the closest thing). Instead:
- Set the **Unrouted flag**, note "needs a format skill"
- Fall back to a plain idea card: title, angle, key points — enough for Lucas to hand-draft it
  or use it as a spec for a new format skill later

---

## Deliverable format

Default to a table in the chat reply with these columns: title, source/weight, awareness stage,
structural role, readiness, destination. This is the deliverable — don't wrap it in extra prose
unless the source material needs context to make sense of the table.

**Ask, don't assume, about a persistent backlog.** A read-only skills environment can't
accumulate ideas across sessions on its own, so don't assume a running backlog (Notion database,
spreadsheet, a markdown file re-pasted each session) is in scope. If Lucas wants one, ask which
format and design it with him — that's a separate decision from the triage itself.

---

## Quick self-check before delivering

- Did every idea start from raw language, not a summary?
- Does every cluster trace back to friction language, not just a listed feature request?
- Is the weight (recurring vs. anecdotal) visible in the Source field, not just implied?
- Did every idea pass the compliance filter — no competitor named in a public-facing angle, no
  negative-sentiment framing left unflagged?
- Is anything that doesn't fit the routing table flagged as unrouted rather than force-routed?
- Did I stop at the idea card and route it, rather than starting to draft the actual piece?
