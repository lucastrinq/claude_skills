# Loss Categorization Taxonomy

Standardized framework for categorizing deal losses. Every lost deal gets exactly one primary category and one sub-category. Use the decision tree at the bottom for ambiguous cases.

## Primary Categories

### 1. Product Gap

The buyer needed a capability we don't have (or don't have at the required level).

| Sub-Category | Definition | Example | Addressable By |
|---|---|---|---|
| Missing Feature | A specific feature the buyer requires that doesn't exist in our product | "We need native Salesforce bi-directional sync" | Product |
| Integration Gap | Required integration with a tool in their stack doesn't exist or is insufficient | "We need it to work with ServiceNow — your Zapier integration isn't enough" | Product / Partnerships |
| Scalability Limit | Product can't handle their volume, user count, or data requirements | "We tested with 50K records and the UI became unusable" | Engineering |
| Platform / Architecture | Fundamental technical limitation (on-prem requirement, data residency, single-tenant) | "We need on-prem deployment for compliance" | Engineering / Product |
| UX / Usability | Product works but the experience isn't good enough for their users to adopt | "Our team tried it but went back to spreadsheets because it was too complex" | Product / Design |

### 2. Price / Value

The buyer didn't see enough value relative to the investment, or the deal didn't fit their budget.

| Sub-Category | Definition | Example | Addressable By |
|---|---|---|---|
| Too Expensive (Absolute) | Price exceeds their budget regardless of value | "We only have $20K and your minimum is $50K" | Sales / Pricing |
| Unclear ROI | They see the value conceptually but couldn't build a business case | "I couldn't justify it to my CFO" | PMM / Sales Enablement |
| Unfavorable Comparison | Competitor offered similar value at lower price | "ToolX does 80% of what you do for half the price" | PMM / Pricing |
| Unexpected Costs | Implementation, training, migration, or add-on costs surprised them | "The platform is reasonable but $40K for implementation killed it" | Sales / Services |
| Budget Timing | Budget available, but not in this cycle | "We need to wait for next fiscal year" | Sales (pipeline management) |

### 3. Competitive Loss

A specific competitor won the deal.

| Sub-Category | Definition | Example | Addressable By |
|---|---|---|---|
| Feature Win | Competitor had a specific capability that was the deciding factor | "They had the Snowflake connector we need out of the box" | Product |
| Price Win | Competitor offered a better price for comparable value | "They came in 30% lower and the product was close enough" | Pricing / PMM |
| Relationship Win | Competitor had a pre-existing relationship or strategic partnership | "They're already our partner on another project" | Sales / Partnerships |
| Perception Win | Competitor had stronger brand, more references in their industry, or analyst positioning | "They're in the Gartner MQ Leader quadrant and you're not" | Marketing / PMM |
| Platform Win | Buyer chose a platform/suite over a best-of-breed point solution (or vice versa) | "We consolidated onto one vendor for everything" | Strategy / Product |

### 4. Timing / Priority

The buyer wasn't ready to make a decision — not because of us, but because of their situation.

| Sub-Category | Definition | Example | Addressable By |
|---|---|---|---|
| Not a Priority | The problem exists but isn't urgent enough to solve now | "We'll revisit this in Q3 when it becomes critical" | Marketing (demand creation) |
| Budget Freeze | Organization-wide spending halt unrelated to the deal | "Our CEO froze all new vendor spend" | Sales (pipeline timing) |
| Reorg / Leadership Change | Decision-maker changed, project sponsor left, team restructured | "Our VP left and the new one has different priorities" | Sales (relationship management) |
| Competing Project | Internal project or initiative took priority over this purchase | "We're doing a platform migration and can't take on another project" | Sales (timing) |

### 5. Sales Execution

We had a viable product at a viable price but didn't execute the sales process well enough.

| Sub-Category | Definition | Example | Addressable By |
|---|---|---|---|
| Poor Discovery | Didn't identify the real problem, decision criteria, or buying process | (Internal assessment, not buyer-stated) | Sales Enablement |
| Wrong Champion | Invested in someone who couldn't drive the decision | "We were talking to a manager but the VP made the call" | Sales Enablement |
| Slow Response | Lost momentum due to slow follow-up, delayed proposals, or unresponsive communication | "They went dark after we took 2 weeks to get them a proposal" | Sales Ops |
| Weak Demo | Product demonstration didn't connect to the buyer's specific needs | "The demo was generic — they showed us features we'd never use" | Sales Enablement / SE Team |
| Multi-threaded Failure | Only had one contact; lost when that contact couldn't champion alone | "We never met the CFO who killed the deal" | Sales Enablement |

### 6. No Decision

The buyer evaluated solutions but chose to stick with the status quo.

| Sub-Category | Definition | Example | Addressable By |
|---|---|---|---|
| Status Quo Won | Buyer decided their current process (even if manual) is good enough | "We realized we can keep doing this in Excel for now" | Marketing / PMM |
| Change Fatigue | Too much organizational change happening; couldn't absorb another | "Our team is exhausted from the CRM migration" | Sales (timing) |
| Consensus Failure | Buying committee couldn't agree on a solution | "Engineering wanted us, Sales wanted them, so we did nothing" | Sales (multi-threading) |
| Risk Aversion | Buyer was interested but couldn't accept the risk of change | "What if it doesn't work? We can't afford to switch back." | Sales Enablement / CS |

## Decision Tree for Ambiguous Categorization

When a loss could fit multiple categories, use this hierarchy:

1. **Was a specific competitor selected?** → Yes → Category 3 (Competitive Loss), then identify the sub-category (feature, price, relationship, perception, or platform)
2. **Was a specific product gap cited as the primary reason?** → Yes → Category 1 (Product Gap)
3. **Was price/budget the stated blocker?** → Yes → But ask: was price the real reason, or was it unclear ROI? If they would have paid more for a clearly valuable solution → Category 2, Sub: Unclear ROI. If budget was genuinely the constraint → Category 2, appropriate sub.
4. **Did they decide to do nothing?** → Yes → Category 6 (No Decision), then identify sub.
5. **Were there organizational factors outside the deal?** → Yes → Category 4 (Timing)
6. **None of the above clearly?** → Likely Category 5 (Sales Execution) — most "mysterious" losses are actually execution issues.

## Severity Weighting

When analyzing loss patterns, weight by revenue impact:

| Weight | Criteria |
|---|---|
| 3x | Deal size > 2x average deal size (high-value loss) |
| 2x | Deal size between average and 2x average |
| 1x | Deal size below average |
| 0.5x | Deal was early-stage (never reached proposal) — less signal |

This prevents treating a $10K SMB loss the same as a $500K enterprise loss.
