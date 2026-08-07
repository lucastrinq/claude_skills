---
name: win-loss-analyzer
description: "Analyze B2B SaaS win/loss data to extract strategic insights and actionable recommendations. Use when reviewing closed deals, analyzing sales call transcripts, identifying win/loss patterns, running competitive loss deep-dives, preparing QBR insights, or when leadership asks 'why are we losing to [competitor]?' or 'what's driving our win rate?' Handles CRM exports, call transcripts, interview notes, and survey data."
---

# Win/Loss Analyzer

Turn raw deal data and sales call transcripts into strategic recommendations that improve win rates, inform product roadmap, and sharpen competitive positioning. This workflow enforces statistical rigor, separates signal from noise, and produces audience-specific reports — not just charts.

## Workflow

### Phase 1: Data Intake & Classification

**Ask the user what data they have.** What's possible depends entirely on input quality.

| Input Available | Analysis Possible | Not Possible |
|---|---|---|
| CRM export (structured data) | Win rates, trends, segmentation, cycle analysis | Root cause, qualitative themes |
| Call transcripts (Gong, Chorus, etc.) | Theme extraction, verbatim quotes, sentiment | Statistical win rates, trend analysis |
| Win/loss interview notes | Root cause, decision drivers, competitive intel | Statistically significant patterns |
| Survey responses | Quantified sentiment, ranked factors | Deep qualitative understanding |
| CRM + transcripts | Full analysis — quantitative patterns + qualitative depth | Nothing major |
| Rep debrief notes only | Directional themes (low confidence) | Anything statistically rigorous |

**Steps:**
1. Ask what data formats are available
2. Clarify the analysis goal: overall health check, competitive deep-dive, product feedback, or sales effectiveness
3. Identify the time period and any filters (segment, region, deal size)
4. Set expectations: "Based on what you've provided, here's what I can and can't tell you"

**Quality gate:** Do not proceed until you know what data you're working with and have set honest expectations about analytical limits.

### Phase 2: Data Cleaning & Coding

**Read [references/loss-taxonomy.md](references/loss-taxonomy.md) to standardize categorization.**

**For structured data (CRM exports):**
1. Check for completeness — flag missing fields, note sample sizes
2. Standardize outcome categories: Won, Lost (competitive), Lost (no decision), Lost (other)
3. Bucket deal sizes into ranges appropriate for the dataset
4. Normalize competitor names (catch variations and misspellings)

**For qualitative data (transcripts, notes):**
1. Extract verbatim quotes — preserve exact buyer language
2. Code each insight with a primary theme from the loss taxonomy
3. Tag sentiment: strong positive, mild positive, neutral, mild negative, strong negative
4. Identify the stated decision driver vs. contributing factors
5. Flag "said vs. meant" — when a buyer says "too expensive" they often mean "unclear ROI"

**Quality gate:** Every loss must be categorized. Any categorization you're uncertain about gets flagged as "needs validation."

### Phase 3: Quantitative Analysis

**Run [scripts/win_loss_calculator.py](scripts/win_loss_calculator.py) if structured CRM data is available.**

Calculate and present:
1. **Overall win rate** with period-over-period trend
2. **Win rate by segment** (size, industry, region)
3. **Win rate by competitor** — rank competitors by threat level
4. **Win rate by lead source** — identify highest-converting channels
5. **Sales cycle analysis** — average days by outcome, stage-by-stage drop-off
6. **Loss reason distribution** — both by count and by revenue-weighted value
7. **Deal size correlation** — win rate by deal size bucket

**Statistical rigor rules (non-negotiable):**
- Flag any cut where n < 30: "Directional only — sample too small for statistical significance"
- Never state causation from correlation: "Deals from Source X win more often" not "Source X causes wins"
- Include confidence intervals for key metrics when sample sizes allow
- Note confounding variables: "Enterprise win rate is higher, but enterprise deals also have 2x more stakeholder meetings"
- When comparing periods, note if the comparison is apples-to-apples (same mix of segments, deal sizes, etc.)

**Quality gate:** Every metric includes its sample size. No unsupported causal claims.

### Phase 4: Qualitative Theme Extraction

**For transcripts and interview notes:**

1. **Theme identification**: Read all qualitative inputs and identify the top 5-8 recurring themes. Don't force-fit into predetermined categories — let themes emerge, then map them to the loss taxonomy.

2. **Quote extraction**: For each theme, pull 2-3 verbatim quotes that best represent it. Buyer language is more credible than your summary.

3. **Decision driver analysis**: For each deal, identify:
   - The stated reason (what they told us)
   - The likely root cause (what was actually driving the decision)
   - Contributing factors (what made it worse)

4. **Competitive intelligence extraction**: When competitors are mentioned, capture:
   - Specific capabilities cited
   - Pricing comparisons shared
   - Perception vs. reality (do they really have that capability?)

5. **Product feedback synthesis**: Extract feature requests and capability gaps, tagged with:
   - Frequency (how many deals mentioned it)
   - Revenue impact (total deal value of deals that cited it)
   - Urgency (blocker vs. nice-to-have)

**Quality gate:** Themes are backed by multiple data points, not a single anecdote treated as a trend.

### Phase 5: Synthesis & Recommendations

**Connect quantitative patterns to qualitative root causes.**

1. **Pattern matching**: Where quantitative data shows a trend (e.g., declining win rate in enterprise), qualitative data should explain why
2. **Root cause prioritization**: Rank issues by (frequency × revenue impact × addressability)
3. **Recommendation development**: For each root cause, provide:
   - The insight (what's happening)
   - The evidence (quantitative + qualitative)
   - The recommendation (specific, actionable, owned by a team)
   - Expected impact (if we fix this, win rate should improve by X based on Y deals affected)
4. **Limit to top 3-5 recommendations.** More than 5 means nothing gets prioritized.

**Quality gate:** Every recommendation has evidence from both quantitative and qualitative data (when both are available). Pure-quant or pure-qual recommendations are flagged as lower confidence.

### Phase 6: Report Generation

**Route to the right format for the audience.** Read [references/example-analysis.md](references/example-analysis.md) to calibrate output quality.

| Audience | Report Type | Focus | Length |
|---|---|---|---|
| Executive leadership | Executive Summary | Key metrics, revenue impact, top 3 actions | 1-2 pages |
| PMM team | Competitive Deep-Dive | Win/loss by competitor, positioning gaps, battlecard updates | 3-5 pages |
| Product team | Product Insights | Feature requests ranked by frequency × deal value, competitive gaps | 2-3 pages |
| Sales leadership | Sales Enablement Brief | Training gaps, objection handling updates, process improvements | 2-3 pages |

Ask the user which audience(s) they need reports for. Default to Executive Summary if unclear.

## Output Format Standards

**Executive Summary structure:**
1. Headline metrics (win rate, trend, top loss reason, revenue impact)
2. Key insight (1-2 sentences — the most important finding)
3. Loss reason breakdown (table with count, revenue, % of total)
4. Competitive landscape (win rate vs. each major competitor)
5. Top 3 recommendations with expected impact and owner
6. Data quality notes and caveats

**All reports must include:**
- Time period analyzed
- Sample sizes for every metric
- Data sources used
- Confidence level (high/medium/low) for each finding
- Explicit caveats and limitations

## Reference Files

- **[example-analysis.md](references/example-analysis.md)**: Read before writing your first analysis to calibrate quality, structure, and statistical rigor.
- **[interview-guide.md](references/interview-guide.md)**: Read when the user needs help designing win/loss interviews or structuring customer conversations.
- **[loss-taxonomy.md](references/loss-taxonomy.md)**: Read during Phase 2 to standardize loss categorization consistently.

## Scripts

- **[win_loss_calculator.py](scripts/win_loss_calculator.py)**: Run during Phase 3 on structured CRM data. Accepts CSV input, outputs a markdown analysis report with win rates, segmentation, and statistical flags.

## Common Mistakes

| Mistake | Why It's Bad | Do This Instead |
|---|---|---|
| Treating all losses equally | A $500K enterprise loss to your top competitor is not the same as a $10K SMB no-decision. Revenue-weighting changes the story. | Always present both count-based and revenue-weighted views. Lead with revenue-weighted. |
| Drawing conclusions from small samples | "We're losing 100% of deals in healthcare" sounds alarming until you realize n=3. | Flag sample sizes. Never state a trend below n=30. Use "directional" language for small samples. |
| Confusing symptoms with root causes | "We lost on price" is usually a symptom. The root cause is often unclear ROI, wrong champion, or poor discovery. | Push past the stated reason. Ask "why was price the deciding factor?" to find the real issue. |
| Ignoring no-decisions | No-decisions are often your biggest loss bucket and the most addressable. They're not "the prospect's fault." | Track and analyze no-decisions separately. They often reveal sales process issues, not product issues. |
| Presenting data without recommendations | Leaders don't want a dashboard. They want "here's what's happening, here's what to do about it, and here's what it'll cost if we don't." | Every finding needs a "so what" and a "now what." |
| Cherry-picking quotes | One angry quote doesn't make a trend. One glowing quote doesn't mean you're winning. | Require 3+ data points before calling something a pattern. Note frequency alongside every theme. |
| Mixing correlation and causation | "Deals with executive sponsors win more" doesn't mean adding sponsors causes wins. It might mean bigger deals get both. | Use "correlates with" not "causes." Note potential confounders. |
