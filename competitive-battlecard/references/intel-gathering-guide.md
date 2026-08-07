# Competitive Intelligence Gathering Guide

Where to find competitive intel, what to look for, and how to keep it current.

## Primary Sources (Highest Signal)

### Review Sites (G2, Capterra, TrustRadius)

**What to look for:**
- Filter by recency — reviews older than 12 months reflect a different product
- Read 1-star and 2-star reviews: these reveal real pain points, not just unhappy people
- Read the "switching from" reviews: why did customers leave the competitor?
- Note which features get praised vs. complained about repeatedly
- Check their G2 Grid placement and compare trajectory quarter-over-quarter

**Search queries:**
- `site:g2.com "[competitor name]" reviews`
- `site:capterra.com "[competitor name]" cons`
- G2 head-to-head comparison pages: `g2.com/compare/[you]-vs-[them]`

### Job Postings (Product Direction Signals)

**What to look for:**
- Engineering roles reveal technical stack and architecture bets
- Product roles reveal strategic focus areas (new market, new feature category)
- Sales roles reveal GTM motion (enterprise push, PLG expansion, new vertical)
- "Must have experience with [technology]" reveals their stack and migration plans
- Sudden hiring spikes in a function signal investment or problems

**Where to look:**
- Their careers page (scrape with Firecrawl if available)
- LinkedIn Jobs filtered by company
- Search: `site:linkedin.com/jobs "[competitor name]"`

### Pricing Pages

**What to look for:**
- Published pricing vs. "Contact sales" (signals market segment)
- Feature gating between tiers (what do they reserve for enterprise?)
- Usage-based vs. seat-based vs. flat rate (reveals business model assumptions)
- Free tier limitations (reveals acquisition strategy)
- Capture screenshots — pricing changes without announcement

**Check quarterly.** Pricing changes signal strategic shifts.

### Engineering and Product Blogs

**What to look for:**
- Architecture posts reveal scalability constraints and technical debt
- "How we built X" posts reveal technical approach and limitations
- Migration stories reveal what they're moving away from (and why)
- Open source contributions reveal technical bets

### SEC Filings and Investor Materials (Public Companies)

**What to look for:**
- 10-K risk factors: they're legally required to disclose competitive threats
- Revenue breakdowns by segment
- Customer count and NRR metrics
- "Competition" section of S-1 or 10-K filings
- Earnings call transcripts (searchable on SeekingAlpha)

## Secondary Sources

### Analyst Reports
- Gartner Magic Quadrants and Market Guides
- Forrester Waves
- IDC MarketScape
- Note: these lag 6-12 months behind reality

### Industry Publications
- Trade publications covering the competitor's industry
- Conference talk recordings (check YouTube for their talks)
- Podcast appearances by competitor leadership

### Social Media and Community
- LinkedIn posts by their employees (especially product and engineering leads)
- Twitter/X threads about their product
- Reddit discussions mentioning the competitor
- Hacker News threads (for technical products)
- Their community forums or Slack channels (if public)

### Customer and Prospect Signals
- Win/loss interview feedback mentioning the competitor
- Sales call recordings where the competitor is discussed
- Customer advisory board feedback
- Support ticket themes (your own — "Can you do what [competitor] does with X?")

## High-Signal Competitive Signals to Monitor

| Signal | What It Might Mean | Urgency |
|---|---|---|
| Sudden hiring surge in engineering | Major product investment or rebuild | Medium — watch what ships in 3-6 months |
| New VP/C-suite hire from adjacent space | Entering a new market or pivoting strategy | High — expect messaging changes |
| Partnership announcement | Filling a product gap or expanding distribution | Medium — assess impact on your deals |
| Pricing change (especially reduction) | Market pressure or repositioning | High — impacts active deals immediately |
| Customer case study in your core vertical | Directly competing for your ICP | High — assess and update battlecard |
| Acquisition | Filling a capability gap or buying distribution | High — reassess competitive landscape |
| Layoffs | Financial pressure or strategic refocus | Medium — could signal pricing flexibility |
| SOC2/ISO/HIPAA certification | Targeting regulated industries | Medium if you're in those industries |
| API/integration announcement | Platform play or partner ecosystem expansion | Medium — assess integration overlap |
| Negative press (breach, outage, controversy) | Temporary vulnerability window | High but time-limited — arm reps immediately |

## Structuring Ongoing Monitoring

### Weekly (15 minutes)
- Google Alert for competitor name (set up once)
- Skim their blog/changelog for new announcements
- Check LinkedIn for new job postings

### Monthly (30 minutes)
- Review new G2/Capterra reviews
- Check pricing page for changes
- Scan for new case studies or customer logos

### Quarterly (1-2 hours)
- Full competitive landscape review
- Update all active battlecards
- Review win/loss data for competitive trends
- Check analyst report updates

### Trigger-Based (As Needed)
- New product launch by competitor → immediate battlecard update
- Competitor mentioned in active deal → pull latest intel
- Major company event (funding, acquisition, leadership change) → assess impact

## Intel Confidence Levels

Tag every claim in the battlecard with a confidence level:

| Level | Source Type | Example |
|---|---|---|
| **Confirmed** | Published page, official announcement, direct observation | "Their enterprise plan starts at $X/seat (pricing page, captured Jan 2026)" |
| **Reported** | Review site, customer interview, analyst report | "Multiple G2 reviews cite slow API performance (n=12 reviews, 2025)" |
| **Inferred** | Job posting, hiring pattern, indirect signal | "Likely building mobile app based on 5 mobile engineer postings (Dec 2025)" |
| **Unverified** | Single source, rep anecdote, hearsay | "One prospect mentioned they're switching platforms [VERIFY]" |
