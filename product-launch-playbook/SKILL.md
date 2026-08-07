---
name: product-launch-playbook
description: "Generates complete, tier-appropriate product launch plans with strategic briefs, workback schedules, asset matrices, RACI ownership, and go/no-go checklists. Use when asked to create a launch plan, GTM strategy, feature launch, product release plan, launch brief, go-to-market plan, launch readiness review, or launch retrospective. Covers the full lifecycle from tiering through post-launch review."
---

# Product Launch Playbook

This skill generates execution-ready product launch plans calibrated to launch tier. It produces strategic briefs with specific timelines, asset matrices, RACI ownership, and measurable quality gates — not generic checklists. Every output is tailored to the scope, audience, and risk profile of the specific launch.

## Workflow

Execute these phases sequentially. Each phase has a quality gate that must pass before proceeding.

### Phase 1: Launch Classification

Gather these inputs from the user (ask if not provided):
1. **What is launching** — new product, major feature, minor feature, enhancement, or bug fix
2. **Target audience impact** — new segment, existing segment expansion, or existing users only
3. **Revenue impact** — new revenue stream, expansion revenue, retention play, or none
4. **Competitive dynamics** — first to market, parity, catch-up, or not applicable
5. **Launch date** — fixed date, flexible window, or TBD

Apply the Launch Tiering Framework below to assign Tier 1, 2, or 3. State the tier and cite the specific criteria that triggered it. If criteria span tiers, round UP.

### Phase 2: Launch Brief

Generate the full launch brief using the Launch Brief Template below. Calibrate depth by tier:
- **Tier 1**: Every section fully developed. 1500-2000 words total.
- **Tier 2**: All sections included, moderate depth. 800-1200 words total.
- **Tier 3**: Abbreviated brief — Strategic Context, Key Messaging, Asset List, Timeline only. 300-500 words.

Before writing your first launch brief, read [example-launch-brief.md](references/example-launch-brief.md) to calibrate tone, depth, and specificity.

### Phase 3: Cross-Functional Workback

Generate a workback schedule counting backwards from launch date. Use these default timelines if the user has not specified:
- **Tier 1**: 12 weeks pre-launch
- **Tier 2**: 8 weeks pre-launch
- **Tier 3**: 3 weeks pre-launch

Structure the workback as a table with columns: Week, Workstream, Deliverable, Owner (role), Status. Include these workstreams per tier:

| Workstream | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Product Readiness | Yes | Yes | Yes |
| Messaging & Positioning | Yes | Yes | Lightweight |
| Content & Assets | Yes | Yes | Minimal |
| Sales Enablement | Yes | Yes | Email only |
| Customer Marketing | Yes | Yes | In-app only |
| PR & Analyst Relations | Yes | No | No |
| Partner/Channel | Yes | If applicable | No |
| Demand Generation | Yes | Yes | No |
| Customer Success Prep | Yes | Yes | Email only |
| Executive Communications | Yes | Lightweight | No |

### Phase 4: Asset Planning

Generate the asset matrix showing every deliverable, its owner, due date, and status. Read [comms-templates.md](references/comms-templates.md) before drafting any communications assets.

**Tier 1 Asset List:**
- Launch brief (PMM)
- Positioning document (PMM)
- Press release (PMM + Comms)
- Blog post — thought leadership angle (PMM + Content)
- Blog post — product announcement (PMM + Content)
- Customer email — segmented by persona (PMM + Lifecycle)
- Sales one-pager (PMM + Sales Enablement)
- Sales deck update or standalone deck (PMM + Sales Enablement)
- Demo script and talk track (PMM + SE)
- Internal FAQ (PMM)
- Help center and docs update (PMM + Technical Writing)
- In-app messaging and tooltips (PMM + Product)
- Social media copy — LinkedIn, X (PMM + Social)
- Webinar or live demo event (PMM + Demand Gen)
- Analyst briefing materials (PMM + AR)
- Customer case study or early access testimonial (PMM + Customer Marketing)
- Landing page or website update (PMM + Web)
- Video — product walkthrough (PMM + Creative)

**Tier 2 Asset List:** All of the above minus press release, analyst briefing, video, and webinar.

**Tier 3 Asset List:** Release notes, help center update, in-app messaging, internal Slack announcement, customer email (single segment).

### Phase 5: Launch Readiness Review

Generate a go/no-go checklist. Every item must be marked Pass, Fail, or Waived (with justification). A single Fail on a critical item blocks launch.

**Critical Items (any Fail = no-go):**
- [ ] Product is code-complete and deployed to staging
- [ ] Core messaging reviewed and approved by PMM lead
- [ ] Sales team has been briefed and has enablement materials
- [ ] Help center documentation is published or staged
- [ ] No unresolved P0/P1 bugs in launch scope

**Important Items (Fail = launch with documented risk acceptance):**
- [ ] Customer-facing email reviewed and scheduled
- [ ] Blog post drafted and in review
- [ ] Social media copy approved and scheduled
- [ ] In-app messaging configured and tested
- [ ] CS team briefed on known issues and workarounds
- [ ] Demand gen campaigns configured

**Nice-to-Have Items (Fail = note for retro):**
- [ ] Video walkthrough complete
- [ ] Partner communications sent
- [ ] Analyst briefing scheduled
- [ ] Executive blog or LinkedIn post drafted

Present the readiness review as a table: Item, Category, Status, Owner, Notes.

### Phase 6: Post-Launch Review

Read [launch-retrospective-guide.md](references/launch-retrospective-guide.md) before generating the retrospective plan. Generate:
1. Metrics review schedule (T+7, T+30, T+90)
2. Stakeholder feedback collection plan
3. Execution scoring rubric
4. Action items template

---

## Launch Tiering Framework

Assign the tier by matching against these criteria. If ANY criterion in a tier is met, that tier applies. If criteria span tiers, assign the higher tier.

| Criterion | Tier 1 (Major) | Tier 2 (Moderate) | Tier 3 (Minor) |
|---|---|---|---|
| **Product scope** | New product line, new platform, or complete redesign | Major feature, significant feature bundle, or new integration | Enhancement, minor feature, UX improvement, bug fix |
| **Audience** | Enters a new market segment or persona | Expands value for existing segment | Existing users only, no acquisition play |
| **Revenue** | New revenue stream or new pricing model | Expansion revenue or upsell enabler | Retention or satisfaction play, no direct revenue |
| **Competitive** | First-to-market or major differentiation | Competitive parity or leapfrog on specific capability | Table stakes or catch-up |
| **Exec visibility** | Board/investor narrative, CEO involvement | VP-level sponsorship | Director-level or below |
| **Default timeline** | 12+ weeks pre-launch | 6-10 weeks pre-launch | 2-4 weeks pre-launch |
| **External comms** | Press, analysts, event keynote | Blog, email, social | Release notes, in-app, changelog |

**Examples:**
- **Tier 1**: AI-powered analytics suite targeting a new buyer persona (data teams). New pricing tier. Press embargo.
- **Tier 2**: Real-time collaboration in an existing product. Competitive differentiation. Upsell to higher plans.
- **Tier 3**: Keyboard shortcuts, CSV export improvements, onboarding flow fixes.

---

## Launch Brief Template

Use this exact structure. Adjust depth per tier as noted in Phase 2.

**1. Launch Overview** (50-100 words)
What is launching, when, and why it matters. One paragraph.

**2. Strategic Context** (100-200 words)
Why now. Market or competitive dynamics. Fit within product roadmap and company strategy.

**3. Target Audience** (100-150 words)
Primary persona: job title, pain point, current workaround. Secondary persona if applicable. Segment size estimate.

**4. Key Messaging** (150-250 words)
- **Positioning statement**: For [audience] who [pain point], [product/feature] is a [category] that [key benefit]. Unlike [alternative], it [differentiator].
- **Three value pillars**: Headline, one-sentence proof point, supporting metric or proof each.
- **Objection handling**: Top 3 anticipated objections with responses.

**5. Success Metrics** (50-100 words)
Table: Metric, Target at T+30, Target at T+90, Owner. Cover adoption, engagement, revenue, sentiment.

**6. Risks and Mitigations** (50-100 words)
Table: Risk, Likelihood (H/M/L), Impact (H/M/L), Mitigation, Owner.

**7. Workback Schedule** — generated in Phase 3, referenced here.

**8. RACI Matrix** — rows per deliverable, columns for PMM, Product, Engineering, Sales, CS, Marketing, Exec. One R, one A per row.

**9. Asset Checklist** — generated in Phase 4, referenced here.

---

## Quality Gates

| Transition | Gate Criteria |
|---|---|
| Phase 1 to Phase 2 | Tier assigned and confirmed by user. All five classification inputs answered. |
| Phase 2 to Phase 3 | Launch brief complete. User has reviewed key messaging. Launch date confirmed or estimated. |
| Phase 3 to Phase 4 | Workback schedule complete with owners on every workstream. User confirms timeline is feasible. |
| Phase 4 to Phase 5 | Every asset has an owner and a due date. No orphaned deliverables. |
| Phase 5 to Phase 6 | Go/no-go decision made. All critical items pass. Important-item failures have documented risk acceptance. |

If the user wants to skip a phase, state what they are skipping and the risk. Proceed only on confirmation.

---

## Reference Files

- **[example-launch-brief.md](references/example-launch-brief.md)**: Read before writing your first launch brief. Complete Tier 2 brief with realistic metrics, personas, RACI, and 8-week workback.
- **[comms-templates.md](references/comms-templates.md)**: Read during Phase 4 when drafting communications. Templates for exec summaries, customer emails, blog posts, social copy, sales enablement.
- **[launch-retrospective-guide.md](references/launch-retrospective-guide.md)**: Read during Phase 6. Metrics review schedule, feedback collection, scoring rubric, retrospective document template.

---

## Common Mistakes

| Mistake | Why It Happens | What To Do Instead |
|---|---|---|
| Treating every launch as Tier 1 | PMMs default to max effort to avoid missing anything | Apply the tiering framework. Tier 3 with Tier 1 effort wastes cross-functional goodwill and causes launch fatigue. |
| Writing messaging before defining audience | Jumping to "what sounds good" before grounding in who cares | Complete Target Audience first. Messaging flows from persona pain points, not product capabilities. |
| Building the workback forward from today | Starting from "what can we do first" instead of "what must be done by when" | Always work backwards from launch date. The last deliverable due determines the real start date. |
| Skipping the go/no-go review | Assuming everything is on track because no one raised a flag | Run the Phase 5 checklist even for Tier 3. Ten minutes, catches gaps every time. |
| One email for all customers | Treating the customer base as homogeneous | Segment at minimum by power users vs. casual users. Pain points and excitement triggers differ. |
| No success metrics pre-launch | "We will figure out success after" | Define metrics in the brief. If you cannot define success, the launch lacks strategic clarity. |
| Forgetting internal audiences | All energy on external comms; Sales learns from the blog | Brief Sales and CS before external launch. They are the first line of customer communication. |
