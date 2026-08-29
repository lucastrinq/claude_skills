---
name: blog-writing-methodology
description: Use when helping write, draft, restructure, brainstorm, or plan a blog post from scratch — AppTweak's website blog, Lucas's personal Substack, or another platform — as long as it isn't a Product Update/Release or a case study. Trigger on "help me write a blog post about X", "draft an SEO/GEO blog on Y", "write a listicle for Z", "write a Substack post about X", "make a content brief/outline for this topic", "brainstorm a blog idea for X". Covers the workflow, structure, and Devin Reed's *Content That Converts* principles; self-contained for Substack and general drafting. For the AppTweak destination, pairs with `apptweak-writing-guidelines` for the brand rules (banned words, ASO positioning, pronoun, CMS mechanics) — that stays the source of truth, not duplicated here. Do NOT use for Product Update/Release posts (apptweak-product-release-update-template), case studies (apptweak-case-study-template), or auditing already-published content (geo-seo-website-optimizer, aeo-content-optimization).
---

# Blog Writing Methodology

You are helping plan and draft a **blog post from scratch** — for AppTweak's website blog,
Lucas's personal Substack, or another platform — covering anything that isn't a Product
Update/Release or a case study: educational explainers, listicles, SEO/GEO-driven pieces,
prompt/tool round-ups, thought leadership, personal essays.

**This skill is self-contained for workflow, structure, and craft** — the *Content That
Converts* techniques below and the Substack path need nothing else loaded. For real, named,
numbers-backed worked examples behind these frameworks (the eyebrow test, the big-swing
framework, the movie-trailer promo method, CTA→CTV rewrites, title formulas, social-proof ladders,
the mindset sources), see `references/book-examples.md` in this skill's folder — pull from it when
a concrete example or attribution would strengthen a recommendation. The AppTweak brand
rules (banned words, ASO positioning, the "We" pronoun, screenshot/CMS mechanics) are AppTweak's
own domain, specific and liable to change on their own schedule — those stay in
`apptweak-writing-guidelines` only, not duplicated here. When the destination is AppTweak's blog,
load that skill for the brand-rules pass; every other destination never needs it.

---

## Step 0: Identify the destination — this decides almost everything below

Ask first, before anything else, if it isn't already obvious from context: **where is this
going?** The three cases that come up:

- **AppTweak's website blog** — SEO/GEO-driven, brand-constrained, "We" voice. Load `apptweak-writing-guidelines` for the brand rules, and use the AppTweak skeleton below for structure.
- **Lucas's personal Substack** — personal essay, "I" voice, no brand constraints. Use `lucas-voice` Tone B, Substack/long-form subsection: more poetic, rhetorical devices allowed, classical/etymological references natural, ends by inviting dialogue.
- **Something else** (Medium, a LinkedIn newsletter, a partner's blog, etc.) — don't assume it behaves like either of the above. See "Step 1: Benchmark" — for an unfamiliar destination, spend two minutes checking what's currently working there before locking in a structure.

Getting this wrong wastes the most effort of any mistake in this workflow — a Substack draft
written like an SEO listicle (or vice versa) usually needs a full rewrite, not an edit. If truly
ambiguous, ask; don't guess and proceed.

**Also at this step:** if the brief points toward a long draft (a full SEO/GEO pillar post, a
multi-section listicle, anything likely to run several drafting/revision passes), check the
`token-thrift` skill before diving in — it's cheaper to plan the token budget once up front than
to notice halfway through a long draft that the session is running expensive.

---

## Step 1: Fill the brief

Once the destination is set, get (or draft yourself, and confirm) these essentials:

1. **Goal** — what is this post actually trying to move (SEO/GEO ranking, inbound demand, subscriber growth, feature awareness)? One sentence.
2. **Why now** — what makes this the right moment?
3. **Persona targeted** — who this is for, ideally in their own words, plus their desired outcome crossed with what the post gives them.
4. **Illustrative examples** — if the post needs example apps/companies to stay concrete, pick ones that aren't real customers, are plausible but not overexposed, and span a few categories relevant to the persona.
5. **Areas of attention** — anything specific to watch for (e.g. "make clear this is the in-house agent, not a ChatGPT prompt").
6. **Resources** — internal/external material, screenshots, prior posts to pull from.

Don't block on missing pieces — draft reasonable defaults and flag them.

---

## Step 2: Benchmark

Look at 2-4 existing pieces — on the same topic, **and** on the same destination format
specifically. These are different questions and both matter:

- **Topic benchmark:** how do others structure this subject, do they explain *why* each point matters (not just list it), do their examples span different contexts rather than repeating one?
- **Format benchmark:** what's currently working on *this specific platform*? Platform norms shift — a structure that performed well on Substack or in SEO blogs a year or two ago isn't guaranteed to still be the strongest shape. If you're not confident the structural knowledge you'd reach for is current, search for it rather than assume (e.g. "what's working on Substack right now" or a look at a few recently high-performing posts in an adjacent niche) — this is worth the two minutes, especially for a destination you don't write for often.

For AppTweak's blog and Substack specifically, starting skeletons are given below — but treat
them as the current best default, not a fixed law, and update them if a benchmark turns up
something that's clearly outperforming that shape now.

---

## Step 3: Write the structure (before drafting prose)

Propose a title and section structure before writing full paragraphs.

**A Claude-assisted way to do this fast, for the AppTweak/SEO-driven case:** ask for a content brief first, from the persona's point of view, benchmarked against a specific existing post:

```
Make an SEO and GEO content brief for the topic '[TOPIC]' for this persona: [PERSONA
DESCRIPTION AND MOTIVATION]. Include structure (H1, H2), keywords, FAQs, meta description,
and a call to action, based on this example: [BENCHMARK URL]. The goal is also to [PRODUCT/
FEATURE PROMOTION GOAL, STATED PLAINLY]. Here is a draft of my thought-out structure: [DRAFT].
```

Then stress-test it from the reader's side:

```
Now be a reader of this structure/brief. What's unclear? What questions would you still have?
What would you want that isn't there?
```

For a Substack piece, this step is lighter — a one-line thesis and a rough beat sequence (see
the Substack skeleton below) usually beats a heavy brief; over-structuring a personal essay
before writing tends to flatten it.

## Step 4: Get persona-specific content (optional, for topics with a strong persona angle)

When the post benefits from really inhabiting the reader's shoes, have Claude roleplay the
persona and walk their real process:

```
You are [PERSONA DESCRIPTION, in first person]. You are now [SPECIFIC SITUATION]. What are
your actual steps to do this? As a second task, here are some tool/prompt ideas that could
help someone in your position — pick the ones genuinely relevant to you, and suggest others
if useful. The goal is to use you as a persona check for a blog post titled "[WORKING TITLE]".
```

Use what comes back to sanity-check section order and language — not as content to paste verbatim.

## Step 5: Draft

Write the full draft using the destination-appropriate skeleton below. Don't optimize for
SEO/GEO yet if this is going to AppTweak's blog — that's step 8, on purpose, so the draft isn't
fighting keyword density while you're still finding the argument. (Substack drafts skip this
concern almost entirely.)

**Skimmability is a standing requirement for the AppTweak destination, not an optional polish
pass.** Most readers scan before they commit to reading — the draft has to work for that reader,
not just the one who reads every word top to bottom. Build this in while drafting, not after.
This skill owns the structural side of that (below); the sentence-level and word-level mechanics
(sentence-length guidance, transition words, bold ratio, simple-word preference) live in
`lucas-voice`'s Step 3 (Format Rules — All Tones) since they apply across tones, not just this
destination — apply both together rather than duplicating them here.
- **Structure carries the argument on its own.** Someone should be able to skim only the
  headings, bolded phrases, and bullets and still get the shape of the post.
- **Bullets/tables over prose** wherever a list of items is genuinely being listed, not narrated.

## Step 6: Cut and sharpen

- If the draft feels thin on proof, surface sharper supporting data or facts:
  ```
  Give me interesting, insightful, and even thought-provoking facts/data about [TOPIC]. It
  should be relevant, somewhat actionable, and surprising enough that a reader would raise an
  eyebrow or furrow their brow reading it.
  ```
- Cut ruthlessly to the core message and the reader's benefit — state the point, at most two examples, then "and more" instead of a third or fourth.
- Write the conclusion and key takeaways last, once the core message is settled.

## Step 7: Get feedback

Ask a peer or a real target-persona reader before the optimization pass — feedback is cheaper to
act on before a section is keyword-optimized than after.

## Step 8: SEO/GEO/AEO pass (AppTweak destination — full weight; Substack — light touch)

For AppTweak's blog, this step matters a lot (it's a search-indexed, SEO/GEO-driven asset).
Useful prompts:

```
Give me 5 FAQ-style questions and short answers for this blog post I can add as schema markup.
```
```
Build an internal linking strategy for this blog post, relating to other relevant posts,
product launches, etc. from the apptweak.com domain.
```
```
Review my blog and suggest high-priority SEO/GEO improvements that would help it rank better
on Google and AI search tools — while keeping my human, personal writing style and narrative
intact.
```

That last prompt is the one worth taking seriously every time: never let an optimization
suggestion sand the voice down into keyword-string phrasing. If a suggested change reads less
like a person and more like a search term, keep the meaning and rewrite it back into voice.

For internal AppTweak links, apply the link-formatting rule from `apptweak-writing-guidelines`
so they stay valid over time — that skill owns the exact mechanics.

For Substack, this step is optional and lighter — discoverability there runs more on
subscriber shares and platform recommendation than on Google ranking, so a quick FAQ/schema
pass is rarely worth it; skip straight to publishing once step 7 is done.

---

## Destination A: AppTweak's website blog

### Skeleton
1. **Intro.** State the problem/context first, short — Tone C territory, get to the point fast.
2. **Key takeaways.** Written last, placed near the top — 3-5 screenshot-able bullets.
3. **Framing section(s).** One or two short sections zooming out before zooming in — why this matters now.
4. **Themed body.** 3-6 thematic buckets mapped to how the persona thinks about their work, not how the product is organized internally. Each bucket states what it's for in one line before the detail, gives grounded examples, and uses a cleaned-up screenshot where it genuinely clarifies (go in-depth on at least one representative example).
5. **A short disclaimer/context note where relevant** (e.g. a tool augments judgment, doesn't replace it, if that's a real risk of misreading).
6. **Outro.** Recap of value (never framed as "how to use it") + a light CTA/CTV.
7. **FAQ block.** 4-6 questions phrased the way a reader or search engine would ask, feeding the schema prompt in step 8.

### Voice and brand rules (AppTweak destination only)
Pull sentence-level voice from `lucas-voice`, **TONE C — Blog/Public-Serious**: punchy, plain
vocabulary, short intro, lead with the outcome, ruthless cutting (two examples then "and more"),
one-line section intros.

On top of that, load `apptweak-writing-guidelines` for the brand layer — banned words, ASO
positioning, the "We" pronoun, no "how to use" framing, screenshot UI cleanup, WordPress `[tip]`
callouts, and the CMS link-formatting rule. These are AppTweak's own domain, specific enough and
liable enough to change on their own schedule that they stay in that skill only — this skill
doesn't carry a copy, so there's exactly one place to update when a brand rule changes.

---

## Destination B: Lucas's personal Substack

### Skeleton
Substack rewards a personal essay shape more than a listicle shape, even for a topic that could
otherwise be structured like an AppTweak post:

1. **Scene or hook.** Open on a specific moment, image, or tension — not a topic statement.
2. **The idea, developed.** Follow the train of thought where it actually goes; let it meander a little before landing it, per `lucas-voice`'s Normal/Substack fingerprint.
3. **A concrete personal anecdote or example** that grounds the idea (Tone B mixes grand ideas with specific personal detail on purpose).
4. **The "so what."** What this means, argued plainly once the idea has been explored.
5. **Sign-off.** An open, inviting close — never a summary, never a hard CTA. Invite a reply/comment rather than asking for a click.

### Voice
Pull entirely from `lucas-voice`, **TONE B — Normal, Substack/long-form subsection**: more
poetic, more rhetorical (negation builds, a single rhetorical device per piece, max), classical
and etymological references where they genuinely fit, "here" over "this," no em-dashes, no
LinkedIn-culture phrasing. First person throughout — no AppTweak brand rules apply here.

---

## Destination C: anything else

Don't force it into either skeleton above. Use Step 2's format benchmark to find out what
actually works on that specific platform right now, build a skeleton from that, and say
explicitly to Lucas which platform norms you're basing it on (so it's a visible judgment call,
not a silent assumption).

---

## Writing attractively (from *Content That Converts*, Devin Reed)

Format-agnostic — applies to any destination. The full set of principles (value equation, opener
shapes, storytelling modes, social proof, CTA/CTV, gating, titles, speech structure, and the
mindset habits behind the tactics) lives in `references/book-examples.md` in this skill's
folder — load it when shaping a draft's core argument, not needed for a quick structural check.

---

## Where to flex

- **Number of themed sections (AppTweak)** — 3 for a narrow topic, 6 for real breadth. Don't pad to hit a round number.
- **Whether there's a "big swing" angle** — most posts don't need one.
- **How much is screenshots vs. prose** — scale with how visual the topic actually is.
- **Whether the speech structure applies** — only for pitch-shaped posts.
- **The Substack skeleton's beat order** — it's a default shape, not a script; let a genuinely different idea take a different shape.

## Quick self-check before delivering

- Did I confirm the destination, and does the structure/voice actually match it (not just default to whichever skeleton I know best)?
- Does the intro state the problem before the solution (AppTweak) or open on a scene, not a topic statement (Substack)?
- Is there at least one genuinely surprising, ideally proprietary, data point or insight?
- Are the illustrative examples varied across contexts rather than repeating one?
- Is the CTA actually a CTV, timed to the reader's funnel stage rather than front-loaded?
- (AppTweak only) Would someone skimming just the headings, bold phrases, and bullets get the gist? (Sentence/word-level skimmability — bold ratio, sentence length, simple words — checked via `lucas-voice`.)
- (AppTweak only) Did the SEO/GEO pass survive without flattening the voice into keyword-string phrasing? Does it clear `apptweak-writing-guidelines`'s banned-words, ASO-positioning, and "We"-pronoun checks?
- (Substack only) Does it still sound like Lucas thinking out loud, not like an AppTweak post with the brand stripped out?

## Output format

Default to **plain text in the chat reply** — a draft meant to be reworked, not a final
deliverable. Use simple visual markers (bold section labels, plain dashes, `[screenshot:
description]` placeholders) rather than heavy Markdown syntax.

If Markdown is requested (CMS, `.md` file, "publish-ready"): for AppTweak, clean Markdown with
H1/`##`/`###` headers and links formatted per `apptweak-writing-guidelines`'s CMS link rule; for
Substack, clean Markdown without any CMS-specific syntax. Only save as a file if explicitly
requested — otherwise keep it inline so it's easy to copy and iterate on directly in the
conversation.

Never include navigation/footer boilerplate — just the article body either way.
