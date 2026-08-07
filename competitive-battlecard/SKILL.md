---
name: competitive-battlecard
description: "Generate competitive battlecards for B2B SaaS sales teams. Triggers: 'battlecard', 'competitive analysis', 'how do we beat [competitor]', 'competitor profile', 'competitive positioning', 'win/loss analysis', 'deal strategy vs [competitor]', 'competitive brief'. Produces structured, evidence-backed battlecards with positioning, objection handling, trap questions, and landmine strategies that sales reps can use in live deals."
---

# Competitive Battlecard Generator

This workflow produces battlecards that sales reps actually use — not marketing fluff that gets ignored. Every claim requires a proof point, every objection response includes a specific talk track, and every trap question is a genuine discovery question that exposes competitor weaknesses without sounding adversarial.

## Workflow

### Phase 1: Intel Gathering

**Read [references/intel-gathering-guide.md](references/intel-gathering-guide.md) before starting this phase.**

**Inputs required from the user:**
- Your company name and product
- Competitor name and product
- Your target buyer persona (role, company size, industry)
- Any specific deal context (optional — if this is for a live deal)

**Steps:**

1. **Use web search if available.** Search for:
   - `[competitor] pricing` — capture published pricing and packaging
   - `[competitor] vs [your product]` — find existing comparisons, G2 head-to-heads
   - `[competitor] reviews site:g2.com OR site:capterra.com` — extract real user sentiment
   - `[competitor] product updates 2025 2026` — find recent feature launches
   - `[competitor] case studies` — identify their strongest verticals and claims
   - `[competitor] engineering blog` — reveal technical architecture and direction

2. **Use Firecrawl or web fetch if available** to scrape:
   - Competitor's pricing page
   - Competitor's product/features page
   - Competitor's "why us" or comparison pages
   - Recent press releases

3. **If no web tools are available**, work with what the user provides and your training knowledge. Be explicit about what you know vs. what you're inferring. Flag any claim that needs verification with `[VERIFY]`.

4. **Organize intel into four buckets:**
   - Product capabilities (features, integrations, platform)
   - Go-to-market (pricing, packaging, sales motion, target market)
   - Company trajectory (funding, hiring, partnerships, roadmap signals)
   - Customer sentiment (reviews, churn signals, NPS indicators)

**Output:** An intel brief (internal, not shown to user unless requested). Move to Phase 2.

### Phase 2: Competitive Positioning Analysis

**Steps:**

1. **Identify the 3-5 dimensions that matter most** to the target buyer persona. Do not list every possible dimension — pick the ones where deals are actually won and lost. Common high-signal dimensions:
   - Time to value / implementation complexity
   - Total cost of ownership (not just license cost)
   - Specific capability depth in the buyer's use case
   - Integration with the buyer's existing stack
   - Vendor stability and support quality

2. **For each dimension, make a clear call:** Win, Lose, or Parity. Do not hedge. If it's close, pick a direction and note the nuance. Sales reps need clear guidance, not "it depends."

3. **Identify your landmines** — the 2-3 areas where you have a decisive advantage. These become your trap questions.

4. **Identify your vulnerabilities** — the 2-3 areas where the competitor genuinely wins. These become your objection handling priorities. Never pretend weaknesses don't exist.

5. **Define the narrative frame.** Complete this sentence: "We are the [category description] for [persona] who need [key differentiator], unlike [competitor] which [competitor's trade-off]." This is the positioning spine of the battlecard.

**Output:** Positioning analysis with clear win/lose/parity calls. Move to Phase 3.

### Phase 3: Battlecard Assembly

**Read [references/example-battlecard.md](references/example-battlecard.md) before writing your first battlecard to calibrate quality and tone.**

Assemble the battlecard using the structure defined in the Battlecard Structure section below. Write for a sales rep who has 30 seconds to find the answer they need. Every section must be scannable.

**Writing rules:**
- Use bullet points, not paragraphs
- Lead with the strongest point in each section
- Every competitive claim needs a proof point (source, data, or customer quote)
- Talk tracks should be conversational — write how a rep would actually speak
- Trap questions must be genuine discovery questions, not gotcha questions
- Keep the entire battlecard under 1500 words (excluding the quick reference table)

**Output:** Complete draft battlecard. Move to Phase 4.

### Phase 4: Quality Scoring

**Read [references/scoring-rubric.md](references/scoring-rubric.md) and self-score the battlecard.**

1. Score each dimension on the 1-5 scale defined in the rubric
2. Calculate the total score
3. Apply the threshold:
   - **40+ (Ship it):** Present the battlecard to the user
   - **25-39 (Needs revision):** Revise the weakest dimensions before presenting
   - **Below 25 (Start over):** Return to Phase 1 for more intel

4. If any single dimension scores a 1, that dimension must be revised regardless of total score.

5. Include the score breakdown in a collapsed/summary section at the end of the battlecard so the user can see it.

**Output:** Scored and potentially revised battlecard. Move to Phase 5.

### Phase 5: Output & Iteration

1. Present the battlecard in clean markdown format
2. After the battlecard, provide:
   - The quality score summary
   - A list of any `[VERIFY]` flags that need user validation
   - 2-3 specific suggestions for strengthening the battlecard with additional intel
3. Ask the user:
   - "Are there specific deal situations or objections you'd like me to expand on?"
   - "Do you have internal win/loss data or customer quotes I should incorporate?"

## Battlecard Structure

Use exactly this section structure. Do not rename or reorder sections.

### 1. Quick Reference (Top of Card)
A table with exactly these rows:
| Field | Detail |
|---|---|
| Competitor | Name, one-line description |
| Last Updated | Date |
| Our Win Rate vs. Them | Percentage or "Unknown — recommend tracking" |
| Their Sweet Spot | Where they win most often (persona, use case, segment) |
| Our Sweet Spot | Where we win most often against them |
| TL;DR | 2 sentences max. The single most important thing a rep needs to know. |

### 2. Positioning Narrative
3-4 sentences maximum. The story frame for every conversation against this competitor. Must include: who they are, what trade-off they've made, and why that trade-off hurts the buyer.

### 3. Where We Win (3-5 Bullets)
Each bullet: **Advantage** — Evidence. Source.
Only include advantages that are defensible and verifiable. No vaporware claims.

### 4. Where They Win (2-3 Bullets)
Each bullet: **Their advantage** — Honest assessment. How to neutralize.
Never skip this section. Reps lose credibility when they can't acknowledge competitor strengths.

### 5. Trap Questions
3-5 discovery questions that a rep can ask the prospect to expose competitor weaknesses. Each question must:
- Sound like a natural discovery question (not "Have you noticed [competitor] sucks at X?")
- Target a genuine gap or architectural limitation
- Include a parenthetical note explaining what the question reveals

### 6. Landmines
2-3 things a rep can say or demonstrate early in the sales process that will create evaluation criteria the competitor can't meet. Each must include:
- The landmine statement or demo moment
- Why the competitor can't match it
- When to deploy it in the sales cycle

### 7. Objection Handling
The top 4-6 objections a rep will hear. For each:
- **Objection:** Exact words the prospect might say
- **What's really going on:** The underlying concern
- **Response:** Conversational talk track (not a script — a framework)
- **Proof point:** Specific evidence to back up the response

### 8. Competitive Pricing Intelligence
- Their published pricing model (or best available intel)
- Common discounting patterns
- Total cost of ownership comparison (include implementation, training, ongoing)
- How to reframe pricing conversations to value

### 9. Red Flags That Signal This Competitor Is in the Deal
5-7 signals that indicate the prospect is also evaluating this competitor, even if they haven't said so.

### 10. Quick Win Plays
2-3 specific actions a rep can take immediately when they learn this competitor is in the deal.

## Quality Gates

These are pass/fail. A battlecard that fails any gate must be revised before delivery.

1. **Every competitive claim has a proof point or is flagged `[VERIFY]`.** Zero unsupported claims allowed.
2. **The "Where They Win" section is honest.** If it reads like marketing spin, it fails.
3. **Trap questions sound like real discovery questions.** If a prospect would feel interrogated, rewrite.
4. **Objection responses are conversational.** If they sound like a press release, rewrite.
5. **The battlecard is under 1500 words** (excluding the quick reference table). Reps won't read a novel.
6. **Every section is populated.** No "TBD" or "Coming soon" — either write it or flag what's needed.
7. **The positioning narrative passes the "bar test."** Could a rep explain this to a friend at a bar in 30 seconds? If not, simplify.

## Reference Files

- **[example-battlecard.md](references/example-battlecard.md)**: Read this before writing your first battlecard to calibrate quality and tone.
- **[scoring-rubric.md](references/scoring-rubric.md)**: Read this during Phase 4 to self-score the battlecard.
- **[intel-gathering-guide.md](references/intel-gathering-guide.md)**: Read this during Phase 1 when you need guidance on where to find competitive intelligence.

## Common Mistakes

| Mistake | Why It's Bad | Do This Instead |
|---|---|---|
| Listing every feature difference | Reps can't process 30 dimensions in a live call. Buries the signal. | Pick the 3-5 dimensions that actually decide deals. Ruthlessly cut the rest. |
| Pretending you have no weaknesses | Reps discover the truth in deals and lose trust in all your content. | Be honest about 2-3 areas where the competitor wins, then arm reps with neutralization strategies. |
| Writing trap questions that sound like attacks | Prospects see through adversarial questions and it damages trust. | Write genuine discovery questions that happen to expose competitor gaps. |
| Using marketing language in talk tracks | No rep says "our best-in-class solution leverages synergies." It sounds fake. | Write how humans talk. Short sentences. Concrete examples. |
| Skipping pricing intelligence | Reps get ambushed by competitor pricing claims in deals. | Include whatever pricing intel you have, even if incomplete. Flag gaps. |
| Building a static document | Competitive landscapes change quarterly. Stale battlecards are worse than none. | Include a "Last Updated" date and flag intel that's older than 90 days. |
| Making claims without evidence | One wrong claim destroys the battlecard's credibility with the sales team. | Every claim gets a proof point, a source, or a `[VERIFY]` flag. No exceptions. |
