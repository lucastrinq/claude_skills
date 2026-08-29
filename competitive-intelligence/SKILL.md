---
name: competitive-intelligence
description: "Competitive intelligence and battlecard system — AppTweak competitors by default, and any other company's competitors when the user says this is for outside-AppTweak work. Load this skill whenever anyone asks how AppTweak (or another product the user names) compares to a competitor, asks for a battlecard, asks for pre-call prep, wants to handle an objection, wants to turn competitor research into a pitch/positioning argument, or uses phrases like 'AppTweak vs X', '[my other project] vs X', 'how do we compare to X', 'what should I say about X', 'quick on X', 'what does X do well', 'how do I handle X objection', 'we're losing to X', 'what are X's weaknesses', or any variant of competitive positioning questions. Also load for questions about the AI Visibility competitive landscape. If a competitor is not listed in this skill, say so honestly, research immediately from web and G2, and flag as preliminary if high-stakes verification is needed."
---

# Competitive Intelligence System

> Built and maintained by Georgia Shepherd, Senior PMM, for AppTweak.
> Extended by Lucas as his single, living tool for competitive research and battlecards —
> AppTweak deals and outside-AppTweak work alike. Update this file (not a separate copy) when
> the method improves, so both contexts stay current together.
> Last updated: May 2026.
> Questions or new intel? Ping the team.

---

## Which context is this?

This skill runs in one of two contexts. Determine which applies before running the research
protocol — it changes which sources are mandatory and whether the positioning anchors apply.

**AppTweak context (default)** — the competitor is one of AppTweak's, or the user doesn't say
otherwise. Run the full protocol below as written: Slack, G2, apptweak.com pages, the
positioning anchors, and AppTweak's global positioning all apply.

**Outside-AppTweak context** — the user says this is for another company/product, or the
company in question clearly isn't AppTweak (e.g. a side project, a friend's startup, unrelated
consulting work). In this context:
- Skip every AppTweak-only source: Slack #competition, apptweak.com/alternative-to pages, the
  positioning anchors, and the "AppTweak vs. Everyone" global positioning section below — none
  of that applies to a different product
- Run the generic research protocol instead: web search, G2/Capterra/Trustpilot reviews, the
  competitor's and your own pricing/product pages, recent launches (blog/changelog)
- The **mechanism method** (below, and in
  [references/mechanism-method.md](references/mechanism-method.md)) and the **output
  template**'s shape both still apply — that's the portable part of this skill, built to work
  for any product
- The "written vs. oral output" rule in Rules is AppTweak's specific brand policy — outside
  that context, ask the user what their own company's policy is, or default to the same
  caution (no raw competitor gap-lists in written prospect-facing copy) unless told otherwise
- There's no positioning-anchor file to fall back on — research fresh each time unless the
  user asks to start keeping one for that company too

---

## How this skill works

**Live research is the source of truth — always, for every query.** The first thing Claude does upon loading this skill is run the live research protocol (Slack #competition, G2, and where applicable web/pricing). The positioning anchors below are stable verified context to anchor the response — they are not a substitute for live checks.

This means:
- **Claude never answers from anchors alone.** Slack and G2 always come first.
- The skill handles competitors not listed here — research first, then apply the template
- Strengths and reframes stay accurate even as products evolve
- This file only needs updating when AppTweak's own positioning changes, or when a positioning anchor is confirmed wrong

**Raw research isn't the deliverable — the argument is.** The point of this skill isn't just
"find facts about a competitor" — it's turning those facts into gaps that hold up, then
building the pitch and sales collateral from them. Whenever live research surfaces something
new (not just reusing an already-verified anchor as-is), run it through the mechanism method
in [references/mechanism-method.md](references/mechanism-method.md) before it goes in the
output: map how each platform actually works, keep only the differences that come from
architecture (a feature gap can vanish in a competitor's next release — a structural one
can't), trace each one to a blind spot the buyer would actually feel, and back it with a proof
point or a concrete illustrative example. See the Output template below for where this feeds
in, and the reference file for the full method plus a worked AppTweak vs. Profound example.

---

## Modes

Modes apply in both contexts. In outside-AppTweak context, run the generic protocol steps
(see below) instead of the AppTweak-only steps — the mode logic itself doesn't change.

**Full mode** — "AppTweak vs [competitor]", "battlecard for [competitor]", "help me prep for a call"
→ Run all steps of the research protocol. Output the full template.

**Quick mode** — "quick on [competitor]", "I'm on a call with a [competitor] prospect"
→ Run all steps of the research protocol — mandatory even in Quick mode. Output: one-liner + 3 reasons + top 2 reframes only. Flag any live intel that changes the answer.

**Research mode** — "refresh [competitor]", "what's new with [competitor]"
→ Run all steps with extra depth. Surface findings as a draft — flag for team review before treating as sales-ready.

**Unknown competitor** — not in the anchors below (always true in outside-AppTweak context, since anchors are AppTweak-only)
→ Run all steps of the research protocol. Output the full template. Note that the output is based on live research and flag anything that needs internal verification before use in a high-stakes deal.

---

## Research protocol

> ⛔ **HARD GATE: Do not write any competitive output until all mandatory live checks below are complete.** In AppTweak context, the positioning anchors are stable context only — they are never sufficient on their own. Slack and G2 are fast-moving; anything posted in the last 90 days could invalidate an anchor.

### In outside-AppTweak context, use this instead of Steps 1–3 below

Run the generic version of the same three checks:
- **Recent chatter/reviews** — web search for `[competitor] reviews`, G2/Capterra/Trustpilot for the competitor and (if it exists) the user's own product; focus on "what do you dislike" fields
- **Web + pricing** — `[competitor] pricing`, `[competitor] vs [user's product]`, `[competitor] new features [current year]`, the competitor's blog/changelog for recent launches
- **The user's own product** — ask for or search out equivalent positioning material (a comparison page, docs, pricing) so the mechanism-method table in the next section has both sides to compare

Skip Slack #competition and apptweak.com pages entirely — they don't exist for a company
outside AppTweak. Then continue to "Turning findings into arguments" below.

### Mandatory for ALL modes (Full, Quick, Research, Unknown) — AppTweak context

**Step 1 — Slack #competition (always first)**
Search Slack before anything else. Recent deal intel, lost deal notes, and feature updates live here and are not in the positioning anchors.
- Run: `[competitor] in:#competition` sorted by date descending
- Also run: `[competitor] in:#product-updates`, `[competitor] in:#marketing-updates`, and `[competitor] in:#feedback-product` — the last channel surfaces competitor mentions in the context of client feedback about AppTweak's own tool
- Read any threads from the last 90 days in full
- If a message references a LinkedIn post, product update, or external link — fetch it

**Step 2 — G2 reviews**
Both AppTweak's and competitors' G2 reviews are often incentivised — treat all ratings and praise as directional only, not as objective truth. Look for themes across 5+ reviews; single mentions aren't signal.
- Fetch: `g2.com/products/[competitor]/reviews` — sort by most recent. Focus on **"What do you dislike?" / "What's missing?"** fields for the most unfiltered signal.
- Fetch: `g2.com/compare/apptweak-vs-[competitor]` — head-to-head comparison page with feature scores and AI-generated summaries from real user reviews. If this URL 404s, try the reversed order: `g2.com/compare/[competitor]-vs-apptweak`
- **Prioritise areas where AppTweak wins** — use these to strengthen the "3 reasons" and reframes in the output.
- Where G2 signals a genuine competitor strength or an AppTweak weakness, **include it as internal context for the team only** — flag it clearly, don't surface it in the prospect-facing framing. The goal is to keep the rep informed and prepared, not to hand them reasons to doubt.
- Flag any finding that contradicts a positioning anchor with 🔍

**Step 3 — Web + pricing (mandatory for ALL modes)**
- Web search: `[competitor] app store optimization`, `[competitor] Apple Ads`, `[competitor] vs AppTweak`, `[competitor] new features [current year]`
- Fetch: `[competitor].com/pricing` — pricing pages often have the clearest feature-by-feature breakdowns
- Fetch: `apptweak.com/en/alternative-to-[competitor]` if it exists — **this is a primary internal source of truth for feature-by-feature comparisons and AppTweak's official positioning against each competitor.** These pages include a feature comparison table showing what AppTweak has that the competitor doesn't. They are updated quarterly, so treat them as the baseline for feature gaps — but live Slack and G2 signals take priority if more recent. Always fetch this page; do not rely on memory of the positioning anchors alone.
- Check competitor's blog or product release page for recent launches (e.g. `[competitor].com/blog`, `[competitor].com/changelog`, LinkedIn newsletter)
- For AI Visibility competitors: fetch https://apptweak.atlassian.net/wiki/x/DIBE9pwG

### What to do with findings
- Anything from Slack or G2 that contradicts a positioning anchor → **update the anchor in your response, flag with 🔍, note the source**
- Anything from Slack or G2 that adds new intel not in the anchors → **include it, flag with 🔍 if unverified**
- If Slack or G2 search returns no recent results → state that explicitly ("No #competition mentions in last 90 days")
- Never skip a step and assume the anchors are current

Use findings to populate the output template below.

### Turning findings into arguments (mechanism method)

Before writing "3 reasons" or "Reframes" for a *new* argument (not just reusing a
verified positioning anchor), run the raw research through
[references/mechanism-method.md](references/mechanism-method.md):

1. Map the mechanism, not the feature — unit of analysis, what the customer has to input,
   where the data comes from, for both platforms
2. Lay both platforms' answers side by side in a table, one row per question
3. Keep only the differences that come from architecture (structural deltas); drop pure
   feature gaps — those can vanish with the competitor's next release
4. Trace each structural delta to a blind spot the buyer would actually notice or feel
5. Attach a proof point if one exists, or a simple illustrative example if it doesn't
6. Write it as: one bolded claim → one sentence of mechanism → one sentence of consequence →
   the example

Tag every argument built this way as **directly provable** (you can show it — a screenshot, a
side-by-side score) or **mechanism-inferred** (reasoned from how the tool works, illustrated
with an example, not something you can screenshot). Keep that tag in internal notes even when
it doesn't appear in the prospect-facing framing — the rep needs to know which kind of claim
they're making before a prospect asks "how do you know that."

---

## Output template

Use this structure for every competitor response. Populate from live research + positioning anchors.

```
> ⚠️ Everything below is for internal use and verbal conversations only.
> For written prospect-facing output (emails, follow-ups, shared docs) — see the written output rule in Rules.

### [Competitor]
**Category:** [what they do / how they overlap with AppTweak]

**Where they win**
[Honest, specific, and brief. Name the real scenario where this competitor is the right
call. This builds credibility — but keep it contained and matter-of-fact. The goal is
for the rep to feel informed and prepared, not unsettled. One or two sentences is enough;
this isn't the section that lingers.]

**Trap-setting questions**
[2 questions that surface the gaps naturally — let the prospect reach the conclusion]

**3 reasons clients choose AppTweak**
[Specific, not generic. Name the feature, the gap, the real sales moment. Reference
AppTweak's global positioning below. Tie in a relevant case study where possible. For any
reason built fresh from research rather than reused from an anchor, run it through the
mechanism method above first — prefer a structural delta over a feature gap.]

**Reframes for their genuine strengths**
[Address the specific things prospects will cite from "When they win." Don't dismiss —
reframe. Format: "[Their genuine strength/claim]" → [reframe]]

*(Internal note, not shown in prospect-facing framing: tag new mechanism-derived arguments
above as directly provable or mechanism-inferred — see mechanism-method.md.)*

**Objections**
[Process and commercial pushback: switching cost, already set up, pricing, contract length.
Separate from feature reframes. Format: "[Objection]" → [response]]

**One-liner**
[One sentence. Honest. Confident. Human.]
```

---

## AppTweak vs. Everyone — the global positioning

Use this as the foundation for any competitive conversation. These points are stable.

**Unique to AppTweak:**
- **AI Visibility** — the only AI visibility tool built from mobile app and game market data (AppDNA/GameDNA + 1,000+ intents/topics + 10,000 weekly prompts to ChatGPT). Web tools exist; mobile-specific methodology doesn't exist elsewhere.
- **Atlas AI** — proprietary intelligence layer trained on 10+ years of app store data. Not a generic LLM wrapper — understands semantic connections between apps, keywords, intent, and performance.
- **AI Agents** — the only platform with ASO Agent, Ad Agent, Reporting Agent, and Reviews Agent. Other tools have one or none.
- **Creative intelligence** — the only platform with CSL Explorer (organic creative intelligence for Custom Store Listings), AI Screenshot Search, and screenshot + CPP/CSL translations. On A/B test tracking: AppTweak is the only platform that shows the % split per variant — some competitors show that A/B tests are running, but none combine A/B test tracking with PPO (Product Page Optimization / app store-native testing) in the same platform. No competitor has this breadth of creative research capability.
- **Incrementality** — proving what ASO and Apple Ads initiatives actually drive growth, not just reporting on it.
- **Exact Match Discovery Experiments** — keyword opportunity discovery through controlled testing.
- **10M+ keyword database** — largest and most accurate in the industry, with unique metrics: keyword installs, maximum reach (impressions), keyword relevancy score.

**How AppTweak positions overall:**
- **All-in-one** — ASO, Apple Ads, and AI Visibility as the three primary growth levers, plus Market Intelligence, App Reviews, and Advanced Reporting — all in a single platform built on the same data foundation. Not a bundle of acquired tools.
- **Actionable** — AI Agents close the loop from insight to action.
- **Intelligence-first** — built to find what you don't know yet, not just track what you already have.
- **Trusted partnership** — in-house consultants, long-term relationships, industry's recognised ASO leader since 2012.

**Concrete proof points to make ASO + Apple Ads tangible** (use these to move from abstract claims to specific capability):
- **Exact Match Discovery Experiments** — powered by Atlas AI, these prefill test campaigns with keyword opportunities the team hasn't thought of yet. The proof of intelligence-first: it's not just automating what you have, it's finding what you're missing.
- **Incrementality** — measures the actual uplift from ASO and Apple Ads initiatives, separating organic growth from paid. The proof of ROI: leadership gets a number, not a story.
- **Creative research** — CPP Explorer, CSL Explorer, A/B test % split variants, AI Screenshot Search, and screenshot + CPP/CSL translations. The proof of creative intelligence depth: understanding what's working for competitors across both organic and paid, before running anything yourself.
- **Atlas AI** — the connective tissue. Trained on 10+ years of app store data, it powers keyword discovery, recommendations, and agents in a way no generic LLM can replicate.

**When a competitor is positioned as cheaper — ROI reframe (applies to any competitor):**
The conversation needs to shift from cost to return. AppTweak generates ROI through concrete, measurable mechanisms most competitors can't match: (1) **Keyword discovery at scale** — Atlas AI and Exact Match Discovery Experiments find untapped high-volume keywords that drive incremental installs a monitoring-only tool never surfaces; (2) **Apple Ads efficiency** — the Ad Agent and organic-to-paid intelligence reduce wasted spend and improve ROAS (SoundCloud: -39% CPI, +58% ASA conversion rate); (3) **Incrementality** — AppTweak proves which initiatives actually drove growth, turning a budget conversation with leadership into a renewals conversation; (4) **Time saved** — King reduced recurring ASO tasks by 62%, which has a real headcount cost. Frame the question as: "What is it worth to find the keyword opportunities you're currently missing, and prove the installs they drove?"

**When a competitor offers direct store publishing — security reframe (applies to any competitor):**
AppTweak deliberately does not publish directly to the app stores. This is a security choice, not a gap — AppTweak is ISO 27001 certified and built for enterprise-grade security. Direct publishing from a third-party tool introduces risk that large teams and regulated categories (fintech, health, games with young audiences) actively want to avoid. Enterprises with review workflows and internal sign-off processes prefer this separation. Position it as a feature: AppTweak gives you the intelligence and the optimised metadata; your team controls what goes live and when.

---

## Positioning anchors

These are the stable, internally verified facts per competitor — internal pricing, known structural gaps, and deal context that live research won't surface. Everything else comes from the research protocol above.

For full product details or comparison pages, refer to apptweak.com/en/alternative-to-[competitor].

---

### Mobile Action
**Overlap:** Core ASO + Apple Ads + Market Intelligence
**Where they win:** Cross-network paid creative intelligence — Meta, Google UAC, TikTok, ironSource in one place. AppTweak doesn't match this. If understanding what competitors run across all paid channels is the primary brief, Mobile Action is a legitimate call. The all-in-one pitch (ASO + Apple Ads + ad intelligence) also appeals to teams that want breadth over depth.
**Pricing:** Not published. Treat any internal figures as directional.
**Deal context:** Often positioned as "Sensor Tower + AppTweak + SplitMetrics in one." Challenge: three capabilities at moderate depth, not one at full depth.
**Key link:** apptweak.com/en/alternative-to-mobile-action · g2.com/products/mobileaction/reviews

---

### SplitMetrics
**Overlap:** Apple Ads automation (Acquire) + A/B testing (Optimize). Acquired AppRadar Nov 2023 for ASO — not built from scratch.
**Where they win:** Acquire's bid management and automation mechanics are practitioner-praised. If pure Apple Ads automation on a mature keyword list is the entire brief — especially for teams on MMPs outside AppsFlyer, Adjust, Branch, or Singular — Acquire is a legitimate call. Optimize is genuinely capable for CPP/store page A/B testing if testing in isolation (not creative intelligence) is the need.
**Structural gaps:** No keyword discovery — automates what you already have. No organic-to-paid intelligence. Three products, three logins. No incrementality. No AI Visibility.
**Pricing (directional ⚠️):** Acquire: % of ad spend. Under $50k/mo = 3.5%, $50–100k = 3.3%, $100–300k = 2.5%, $300–500k = 1.8%, $500k–1M = 1.5%. Min $800/month. Sometimes offers AppRadar free at $50–100k/mo+ spend.
**Unverified intel 🔍:** Smart bidding flagged for large unpredictable spend jumps — only raise if prospect brings it up first. Needs Gong verification.
**Key links:** apptweak.com/en/alternative-to-splitmetrics · g2.com/products/splitmetrics-acquire/reviews

---

### AppRadar
**Overlap:** ASO tracking. Part of SplitMetrics ecosystem since Nov 2023. Target: indie developers and small teams.
**Where they win:** Price and publishing. AppRadar is meaningfully cheaper than AppTweak for small teams and indie developers. Direct-to-store metadata publishing (App Store + Google Play) from within the platform is a genuine workflow advantage at this scale. If budget is hard-constrained and publishing convenience matters more than discovery depth, AppRadar is a reasonable starting point. *(📎 Confirm publishing is still a current feature before using this. For the publishing and price objections, see global positioning reframes above.)*
**Structural gaps:** No keyword installs, no Exact Match Discovery Experiments, no Atlas AI, no CSL Explorer, no Market Intelligence, no Apple Ads, no AI Agents, no AI Visibility. Note: App Radar added Max Reach in Feb 2025 — AppTweak also has Max Reach, plus keyword installs and relevancy scores which App Radar does not have. For the full feature-by-feature breakdown, always fetch apptweak.com/en/alternative-to-appradar.
**Pricing (directional ⚠️):** Scale plan ~€2,990/year (15 apps, 3,000 keywords, 5 seats).
**Key links:** apptweak.com/en/alternative-to-appradar · g2.com/products/app-radar/reviews

---

### Sensor Tower
**Overlap:** Enterprise market intelligence. Not always either/or — often "AppTweak AND Sensor Tower."
**Where they win:** Panel-based engagement data (MAU, DAU, session frequency, time spent) — expanded after data.ai/App Annie acquisition. For strategy teams and analysts doing investor-grade competitive benchmarking, this is data AppTweak doesn't match on methodology or depth. Established enterprise brand with analyst relationships and category-level market sizing. If the primary brief is market intelligence with no execution layer needed, Sensor Tower is the right call.
**Structural gaps:** No ASO execution, no Apple Ads management, no AI Agents, no AI Visibility, no reviews. Enterprise-only pricing, no transparent self-serve tier.
**Privacy note (use carefully ⚠️):** Panel-based data is estimated from an opted-in subset. For teams in regulated categories (health, finance, children's apps), GDPR posture on panel construction is worth surfacing — get a compliance check before using in a live deal. Only raise if prospect is in a regulated category or has raised compliance themselves.
**Deal context:** Establish what they're buying Sensor Tower for before positioning. Often additive, not competitive.
**Key links:** apptweak.com/en/alternative-to-sensor-tower · g2.com/products/sensor-tower/reviews

---

### AppFollow
**Overlap:** App reviews management + basic ASO monitoring.
**Where they win:** Review automation depth — reply workflows, routing, tagging — is more mature than AppTweak's ARM. Covers Amazon and Microsoft Store in addition to App Store and Google Play. Helpdesk integrations (Zendesk, Intercom, Jira) are frequently cited. For support teams whose primary job is review response at volume, especially those publishing on Amazon or Microsoft Store, AppFollow is the honest choice. *(📎 Confirm current AppTweak ARM store coverage before any prospect conversation.)*
**Two separate conversations:**
- *Reviews-only:* Be honest. AppFollow is more advanced on pure review management. AppTweak's ARM is strong but reviews is not AppTweak's core product.
- *Full platform:* AppTweak wins clearly. AppFollow has no Apple Ads, no meaningful keyword intelligence, no market intelligence, no AI Agents, no incrementality, no AI Visibility.
**Our ICP is the full platform buyer.** The question to ask: "Do you want best-in-class reviews in isolation, or reviews connected to ASO, Apple Ads, market intelligence, and AI Visibility?"
**Key links:** apptweak.com/en/alternative-to-appfollow · g2.com/products/appfollow/reviews

---

### Gummicube + ASO agencies
**Overlap:** ASO agency with proprietary tooling (DATACUBE). Positioning applies broadly to any ASO agency comparison.
**Where they win:** Capacity and confidence. Teams without headcount to run ASO, or newer to ASO and wanting expert-led execution — an agency solves both immediately without a hiring cycle. Gummicube's DATACUBE positioning as iOS-native data appeals to teams with doubts about third-party data accuracy. If full outsourcing with no intention to build internal capability is the brief, an agency is the right call. *(🔍 Verify current DATACUBE positioning before use.)*
**Structural gaps:** Agency clients have limited visibility into what's being done and why. Institutional knowledge leaves when the engagement ends. DATACUBE methodology is not independently verified or transparently published.
**Proof point:** Sykes Holiday Cottages — +45% visibility, highest rankings YTD after moving from agency to in-house with AppTweak.
**Key links:** apptweak.com/en/alternative-to-gummicube · apptweak.com/en/case-studies/sykes-holiday-cottages

---

### SimilarWeb
**Overlap:** Web analytics + app market intelligence. ASO in beta. AI Visibility (web-based).
**Where they win:** Combined web + app intelligence in one platform — strongest web intelligence on the market. For teams running both a web product and a mobile app, the unified cross-platform view (web traffic + audience demographics + app market data) is a genuine differentiator no other tool in this list matches. The 42matters acquisition added credible app download/revenue estimates. If cross-platform market intelligence is the primary need with no ASO execution requirement, SimilarWeb is the stronger choice.
**Structural gaps:** AppTweak is mobile-first — different scope, not a weakness. ASO suite in beta, limited country coverage as of early 2026 (full launch expected Q3 2026 — verify current status). No Apple Ads management, no AI Agents, no App Reviews Manager.
**On AI Visibility:** SimilarWeb's AI Visibility starts from your domain and web content. AppTweak starts from 1,200+ user intents from real app store data, sends 10,000 prompts weekly to ChatGPT, and matches results to real app IDs. Different question, different methodology.
**Pricing (directional ⚠️):** Per-country dataset. ~$12k/year (India), ~$18k (SEA), ~$27k (SEA + India + US), ~$47k (worldwide).
**Key links:** g2.com/products/similarweb/reviews

---

### Newton AI
**Overlap:** Managed Apple Ads + ASO in APAC. Not a self-serve tool competitor.
**Where they win:** CPCU (Cost Per Converted User) billing — client pays per converted user, not a flat fee. Performance risk sits with Newton. For teams with budget uncertainty or leadership requiring guaranteed ROI before committing, this model is genuinely differentiated. Only Apple Ads Partner in APAC (4th globally) — relevant for India and SEA where Apple Ads is growing and local expertise is scarce. *(🔍 Verify current partner status before use.)*
**Structural gaps:** Managed service — strategy and optimisation logic sit with Newton, not the client. Knowledge leaves when engagement ends. Newton uses platforms like AppTweak as data inputs — they are an execution service, not an intelligence platform.
**Deal context:** Same outsourcing-vs-ownership framing as Gummicube. AppTweak can be the intelligence layer regardless of who manages execution.

---

### Asapty 🔍
**Overlap:** Apple Ads automation and management. Direct competitor on Apple Ads, particularly in AMER deals.
**Where they win:** Solid Apple Ads automation fundamentals — custom automation rules, MMP integrations, SKAG workflow, Share of Voice tracking, and cross-country reporting are all present. For teams whose entire brief is Apple Ads campaign management with no need for keyword discovery intelligence, organic data, or creative tools, Asapty covers the core mechanics. Also offers managed Apple Ads services for teams that want execution support.
*🔍 Verify genuine practitioner praise via Slack #competition and LinkedIn — the above is based on internal comparison data. Live research needed for "why people choose them" in their own words.*
**Structural gaps (from internal comparison, April 2026):**
- Keyword discovery: partial only — can't build keyword lists beyond seed keywords or app name at full depth
- AI Discovery Experiments: absent
- Organic keyword metrics in paid workflow (rank, max reach, organic installs): absent
- Smart bidding: partial — no continuous AI-driven adjustment
- CPP Explorer, CPP Scheduling: absent
- In-product AI Agent: absent
- Campaign benchmarks: absent
- Incrementality modeling: absent
**Key question to ask:** "When you're building your keyword strategy, where does discovery come from? Are you finding new terms or mostly managing what you already have?" — surfaces the keyword intelligence gap quickly.
**Key links:** 🔍 Search G2 and Slack #competition for current practitioner feedback before high-stakes use.

---

## AI Visibility — team education

> For full objection handling, product FAQs, and methodology comparisons, always fetch: https://apptweak.atlassian.net/wiki/x/DIBE9pwG

**The core distinction:**
Web AI visibility tools measure how your brand or domain appears in AI answers, starting from your own content. AppTweak measures whether your app is recommended when users ask AI for an app to download, starting from the full landscape of real user needs in the mobile market.

**How to explain it simply:** "Other tools read your website and show you where your brand appears in AI. AppTweak looks at what users are actually asking AI for when they want to download an app, then shows where your app stands across all of those questions — including the ones you didn't think to look for."

**No AI visibility tool has real LLM search volume data.** AI tools like ChatGPT don't expose actual query volumes through public APIs. Any tool claiming to show "how many people search for X in AI" is estimating from a proprietary panel, not actual LLM query statistics. The honest answer: no tool has it. What AppTweak focuses on is showing where your app is actually being recommended — which competitors are winning which intents — and that's what you can act on.

**The "3 reasons" framing for all AI Visibility competitors** (frame as AppTweak AND the web tool, not instead of):

We start from the market, not your brand. Web tools read your website and measure where you appear for topics associated with your content. AppTweak runs 10,000 prompts per week built from 1,200+ user intents from real app store data — you see the full competitive landscape first, including intents where competitors are winning that your current tool would never show you.

Our prompt library is purpose-built for app discovery. Every AppTweak prompt is framed as "what is the best app to [intent]" — not brand queries, not web queries. This measures actual app recommendation dynamics. No web-based tool generates this data because they're not asking the question users ask when they're about to download an app.

From visibility gap to growth action. Web tools show you a score. AppTweak connects every visibility gap directly to your ASO keywords, Apple Ads campaigns, and the competitors winning that intent — in the same platform where you run your ASO and Apple Ads.

**Known AI Visibility competitors and their positioning:**
- **Profound** — leading dedicated AI visibility tool for enterprise web brands. Genuinely strong: 10 AI engines, Agent Analytics (shows how AI systems crawl your site), Workflows for AI-optimised content. Complementary, not competitive — Profound can't track app recommendation dynamics. Frame as "and."
- **Semrush / Ahrefs** — domain-based AI visibility. Structural blind spot: apps with minimal web presence (or where the website is a store redirect) return incomplete or zero data. OkCupid and Balance meditation app (owned by The Mind Company via themindcompany.com) are verified examples from Confluence.
- **Amplitude** — product analytics platform (4,300+ customers including Atlassian, Square, Under Armour) that launched AI Visibility in October 2025, available free to all existing Amplitude customers. Their differentiating angle is behavioral context: they connect AI search visibility with downstream product analytics — you can see who arrived from ChatGPT and track what they did next. Web and brand-focused, not app-discovery focused. The "when they win" case is usually not a purchase decision: the prospect already uses Amplitude for product analytics and gets AI Visibility at no extra cost. Frame as complementary — Amplitude answers "what did AI-referred users do after they arrived?" AppTweak answers "is your app being recommended in the first place?"
- **AirOps** — content operations platform that expanded into AI visibility. Web and content-centric by design. Complementary framing applies.

---

## Case studies

Use these to anchor "3 reasons" and objection responses with proof. Match to the prospect's vertical or use case.

**Primary source — always fetch this first:**
Google Drive doc maintained by the team, updated as new case studies publish:
https://docs.google.com/presentation/d/1Az6AxDQoSq5FRdqmULAfQ_wLvVCbM9Pcycrpenm2BR4/edit
Organised by vertical: Shopping, Travel, Fintech, Music, Games, Agency, Lifestyle. Fetch and match to the prospect's category. This is the live source — prefer it over the fallback list below.

**Fallback — use only if Google Drive is inaccessible:**
- **Sykes Holiday Cottages** — +45% visibility, highest rankings YTD after moving from agency to AppTweak in-house. → Agency comparisons, capability-building arguments.
- **Bolt** — +8.6% incremental installs with organic CPPs. → Incrementality, proving ROI to leadership.
- **SoundCloud** — -39% CPI, +58% ASA conversion rate (CPPs); 3x budget, 4x non-brand downloads, 190% ROAS (Atlas AI + exact match discovery). → Apple Ads / CPP conversations, SplitMetrics comparisons.
- **King** — 62% reduction in recurring ASO tasks. → Consulting/efficiency, gaming vertical.
- **Binance** — 95,000+ incremental yearly installs, #1 in 45 markets with CPPs. → Fintech/crypto, CPP, API/reporting.
- **Vinted** — +210 new keywords in top 10 across 6 European markets in 6 months. → Market expansion, keyword discovery.
- **CoinSwitch** — +400% conversion rate in 5–6 months. → Fintech, CSL/creative optimisation.
⚠️ These may be outdated — verify against the Drive doc when possible.

---

## From battlecard to sales collateral

The output template above is internal/verbal prep — a battlecard, not a finished asset. Once
the gaps and reframes are solid (either context), hand off to the **sales-enablement-assets**
skill to build the actual pitch materials: one-pagers, demo scripts, objection-handling guides,
competitive comparison sheets, ROI cases. Feed it the confirmed "3 reasons," reframes, and
proof points from here as its competitive-context input — don't re-derive them there.

---

## Rules

- For AppTweak product details not covered here, refer to the marketing-brain skill.
- **Live research first.** G2, web, and Slack #competition (AppTweak context) or web/G2/Capterra (outside-AppTweak context) are the source of truth for competitor strengths. The anchors below are stable context for AppTweak only, not a database, and don't apply outside that context. Never fabricate or guess competitor capabilities.
- **Structural deltas over feature gaps.** When building a new competitive argument (not reusing a verified AppTweak anchor), don't stop at "they don't have X yet" — that can disappear with their next release. Use [references/mechanism-method.md](references/mechanism-method.md) to find the difference in how the product is architected, trace it to a real blind spot, and back it with a proof point or example. See the mechanism-method step above. This applies in both contexts.
- **Positioning anchors, global positioning, and case studies below are AppTweak-only.** Don't apply them, adapt them, or reference AppTweak proof points when working outside-AppTweak context — research and build fresh for that company instead.
- **Written vs. oral output — this matters.** Competitive framing (what a competitor claims, how they position themselves, their gaps) is for internal education and verbal conversations only. It must never appear in written prospect-facing output like emails, follow-ups, or shared documents. When drafting anything written, the tone is confident and AppTweak-forward — no competitor names used negatively, no "they say X", no gap lists. If asked to draft an email in a competitive context, focus on AppTweak's value for the prospect's specific situation. The competitive intel informs the angle; it doesn't appear in the copy.
- Competitive tone is confident and grounded, never aggressive.
- Always say "Apple Ads" not "Apple Search Ads."
- ⚠️ Pricing from internal sources is directional — verify before using with a prospect.
- 🔍 Items marked this way need a live check before high-stakes use.
- 📎 Items marked this way have a specific verification step noted inline.
- Never surface source notes verbatim in responses — use the underlying claim with confidence.
- For unknown competitors: research first, apply the template, flag anything unverified. Only escalate to the team if the deal is high-stakes and the research leaves real gaps.