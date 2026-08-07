# Launch Brief — CloudSync Real-Time Collaboration

**Launch Tier:** 2 (Major Feature)
**Target Launch Date:** March 18, 2026
**Brief Owner:** PMM
**Status:** Draft — pending stakeholder review
**Last Updated:** January 20, 2026

---

## Strategic Context

### What We're Launching

Real-Time Collaboration: multiple users can simultaneously edit, comment, and share CloudSync workspaces with live cursors, inline comments, and granular permissions. This transforms CloudSync from a "save and share" tool into a "work together live" platform.

### Why Now

- **Customer demand:** #1 requested feature for 3 consecutive quarters (427 votes on our public roadmap)
- **Competitive pressure:** CompetitorA launched collaborative editing in Q3 2025. We're seeing it cited in 22% of competitive losses (per Q4 win/loss analysis).
- **Strategic fit:** Company OKR Q1: "Increase team adoption from 1.8 to 3.2 avg users per account." Collaboration is the unlock.

### Competitive Context

- **CompetitorA** launched collaboration 6 months ago. Positioning: "built for teams." Weakness: no permissions model — everything is fully open.
- **CompetitorB** has basic sharing but not real-time. They're likely 6-12 months from parity (based on job postings and recent engineering blog).
- **Our advantage:** We're launching with granular permissions (viewer/editor/admin per section), which neither competitor has. This is the differentiator for regulated industries and enterprise security teams.

## Target Audience

### Primary: Team Leads and Managers (Mid-Market)
- **Pain:** "I set up CloudSync for my workflow, but my team uses spreadsheets because they can't work in it together"
- **Need:** Collaborate without giving up control of their workspace structure
- **Decision criteria:** Permissions, ease of onboarding teammates, no disruption to existing workflows

### Secondary: IT / Security (Enterprise)
- **Pain:** "Shadow IT tools proliferate because approved tools don't support collaboration"
- **Need:** Approved collaboration that meets security requirements
- **Decision criteria:** SSO, granular permissions, audit logs, admin controls

### Anti-Personas (NOT for this launch)
- Individual users with no team — this feature doesn't change their experience
- Developers wanting Git-like collaboration — that's a different architecture

## Positioning & Messaging

### One-Line Positioning
CloudSync Real-Time Collaboration: work together in real time with the permissions and control your team actually needs.

### Key Messages

1. **"Collaborate without chaos"** — Real-time editing with granular permissions means your team can work together without anyone accidentally breaking your setup.
   - *Proof point:* Section-level permissions (viewer/editor/admin) — unique in category
   - *Proof point:* Beta customer reduced workspace duplication by 73%

2. **"Your team is already here — now they can work here"** — Invite teammates into your existing workspace. No migration, no new tool to learn. They see your structure and start contributing immediately.
   - *Proof point:* Average time from invite to first edit: 4 minutes (beta data)
   - *Proof point:* 89% of beta invitees active within first week

3. **"Enterprise-grade collaboration, not consumer-grade sharing"** — Built for teams that need audit trails, SSO, and admin controls — not another tool IT has to fight.
   - *Proof point:* Full audit log for every change, SOC2 compliant from day one
   - *Proof point:* Admin can set default permissions at the workspace, folder, or section level

### Differentiation
Unlike CompetitorA's "everything is open" model, CloudSync gives teams granular control. Unlike CompetitorB's basic sharing, CloudSync is truly real-time with live cursors and inline comments.

## Success Metrics

### Leading Indicators (T+7 to T+30)
| Metric | Target | Measurement |
|---|---|---|
| Workspace invites sent | 5,000 in first 30 days | Product analytics |
| Multi-user workspaces | 15% of active workspaces | Product analytics |
| Feature page visits | 10,000 unique | Website analytics |
| Blog post engagement | 3,000 reads, 200 shares | CMS analytics |

### Lagging Indicators (T+30 to T+90)
| Metric | Target | Measurement |
|---|---|---|
| Avg users per account | 1.8 → 2.5 (path to 3.2 OKR) | Product analytics |
| Competitive win rate (vs. CompetitorA) | Improve from 42% to 52% | CRM |
| Net new team plan upgrades | 200 accounts | Billing |
| NPS for collaboration features | >50 | In-app survey |

### Measurement Plan
- T+7: Initial adoption check (invites, activations, feature usage)
- T+30: Full metrics review, first customer feedback synthesis
- T+60: Win rate impact assessment (enough deal cycle time for signal)
- T+90: Full retrospective with revenue attribution

## Risks & Dependencies

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Performance issues at scale (>20 concurrent editors) | Medium | High — bad first impression | Load testing through Feb; launch with soft limit of 25 concurrent, increase post-launch |
| Existing users confused by new UI elements | Low | Medium | In-app guided tour for existing users; "What's new" modal on first visit |
| CompetitorA announces permissions update before our launch | Medium | Medium — dilutes our differentiator | Accelerate launch by 1 week if signal detected; emphasize depth of our permissions model |
| Support team overwhelmed with permissions questions | Medium | Low | Pre-launch FAQ and decision tree for support; dedicated Slack channel first 2 weeks |

**External dependencies:**
- SSO integration testing with top 3 IdPs must complete by March 4
- Help center articles must be live by March 11 (T-7)
- Marketing landing page design finalized by February 28

---

## Cross-Functional Workback (8-Week Timeline)

| Week | Date | Product | PMM | Marketing | Sales | CS | Support |
|---|---|---|---|---|---|---|---|
| W1 | Jan 20 | Beta feedback synthesis | Launch brief draft | — | — | — | — |
| W2 | Jan 27 | Final feature scope locked | Messaging approved | Landing page brief | — | — | — |
| W3 | Feb 3 | Performance testing begins | Competitive positioning update | Landing page design | — | Identify at-risk accounts | — |
| W4 | Feb 10 | Beta → RC | Demo script + battlecard update | Landing page development | Sales training content draft | Customer comms draft | FAQ draft |
| W5 | Feb 17 | RC testing | Blog post draft | Email sequences built | Sales training scheduled | CSM talking points | Support training content |
| W6 | Feb 24 | Go/no-go criteria review | All content in final review | Social media scheduled | Sales training delivered | CS team briefed | Support FAQ live (internal) |
| W7 | Mar 3 | Final regression | Assets approved | Landing page live (hidden) | Demo environment ready | Customer comms approved | Support monitoring plan |
| W8 | Mar 10 | Release prep | Go/no-go recommendation | All assets staged | Pre-launch deal outreach | Pre-launch notifications | War room plan |
| **Launch** | **Mar 18** | **Ship it** | **Coordinate launch day** | **All channels go live** | **Outbound blitz** | **Customer notifications** | **Monitor + respond** |

## RACI Matrix

| Deliverable | PMM | Product | Marketing | Sales | CS | Support |
|---|---|---|---|---|---|---|
| Launch brief | **A/R** | C | I | I | I | I |
| Messaging & positioning | **A/R** | C | C | C | I | I |
| Blog post | **A** | C | **R** | I | I | I |
| Customer email | **A/R** | C | C | I | C | I |
| Sales training | **A/R** | C | I | C | I | I |
| Demo script | **A/R** | C | I | C | I | I |
| Landing page | C | I | **A/R** | I | I | I |
| Help documentation | C | **A** | I | I | I | **R** |
| In-app messaging | C | **A/R** | C | I | I | I |
| Go/no-go decision | C | **A** | I | I | I | I |

*R = Responsible (does the work), A = Accountable (final decision), C = Consulted, I = Informed*
