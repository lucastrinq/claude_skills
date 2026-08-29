---
name: token-thrift
description: "Spend tokens economically without degrading output quality, and anticipate cost before starting. Use whenever a task looks token-heavy or long-running — large files or datasets, many tool calls, multi-step agentic work, big web/Slack/Drive scans, repeated reads, or any session likely to fill the context window. Also use when the user asks to \"be efficient\", \"save tokens\", \"go easy on context\", says \"this is a big one\", worries about cost or speed, or when the selected model may not fit the task. When in doubt on a sizeable task, apply it. The goal is fewer wasted tokens, never less substance. Do NOT trigger for: single-shot or text-transformation sessions (formatting, copy edits); dead-end lookups (searching for a file that may not exist); or sessions where only 1–2 tool calls are expected by design."
---

# Token Thrift

Cut the tokens that carry no information — re-sent context, raw tool dumps, formatting scaffolding, preamble, reasoning spent on trivia, redundant turns. Keep, and on hard tasks *increase*, the tokens that carry reasoning and coverage. When a specific saving could plausibly cost quality and the call isn't obvious, ask the user (see "When torn, ask").

Thrift is also a quality move, not just a cost one: as context fills, recall degrades and earlier instructions get forgotten. A lean context usually produces *better* output, which is why most moves below need no permission.

## Part 0 — Before the work starts

**Estimate the risk.** Glance at five signals: prior context carried, input size, tools/files involved, goal ambiguity, likely iteration. If several are high, set up for it — start fresh or compact first, load files narrowly, agree a stop condition.

**Plan before spending on complex work.** Explore briefly, propose a short plan, confirm direction before implementing. Wrong-path rework is the biggest hidden token sink. Skip the plan if the change fits in one sentence.

**Front-load clarifying questions when the deliverable is big.** With prompt caching, chat length is cheap; what's expensive is *regenerating* output (≈5× input price, uncacheable) because the first attempt missed the mark. Working thresholds by expected deliverable size:
- **Under ~800 tokens** (quick answer, short edit): just answer.
- **~800–2,000** (solid answer, short doc, single-purpose script): ask one short round of clarifying questions first.
- **~2,000+** (report, deck, multi-section doc, anything high-stakes): invest in a properly structured brief before starting — via a prompt-building skill if one is available, otherwise a thorough question round.
When unsure of the band, round up; a wrong skip costs more than a wrong ask.

**On revisions, don't regenerate by default.** Most change requests are surgical ("fix this line"). Make the targeted edit; only redo the full output when the change is structural or the user asks for a redo. Ambiguous? Ask.

**Check the model fits the task — and flag it.** Model choice is a real cost/quality lever that can't be changed cleanly mid-conversation, so judge it at the start of any non-trivial task. The rule is not "smarter = more tokens": the most capable model is often *more* token-efficient on genuinely hard, long-horizon, or high-stakes reasoning and worth its price there; a lighter model is right for everyday work, where a top model adds cost and can overthink. If the current model looks mismatched, say so before sinking tokens in: "This looks like [complex/simple] work on [model]; a [more capable/lighter] model would fit better — restart with that, or carry on?" Don't nag borderline cases or re-raise after a decision. When delegating to subagents (where the environment allows per-agent model selection), route mechanical subtasks — search, extraction, summarization — to a cheaper model and keep the capable model for the main reasoning thread.

## Part 1 — Managing context during a task

Every token in context is re-processed on every turn, so these habits have the highest impact.

**Fetch on demand, don't pre-load.** Hold references (paths, queries, URLs) and pull data only when needed. Locate with grep/glob/search before reading; read only relevant ranges, never a whole directory "to be safe". Exception: if the data is small, correctness-critical, or clearly all needed, just load it.

**Don't re-read what's in context** unless there's reason to believe it changed.

**Keep raw bulk out of context.** When a tool would dump a huge payload (10k-row sheets, verbose JSON, long logs), filter/aggregate/slice *before* it lands — in code or a targeted query — and surface only what matters. This is the single biggest lever (Anthropic measured a ~99% drop, 150k→2k tokens, on one such task). Don't filter so hard you drop something the task needs; when unsure, keep more.

**Parallelize independent tool calls** in one turn — each avoided turn avoids re-sending the growing context. Order-dependent steps stay sequential.

**Delegate verbose exploration to a subagent — only when it pays.** A subagent can burn tens of thousands of tokens investigating and return a 1–2k summary, keeping raw dumps out of the main context. But subagents carry real startup overhead; for small tasks, inline is cheaper.

**Clear or compact at natural breakpoints.** Switching to unrelated work? Start fresh. Long task nearing the window? Summarize decisions, open problems, and key file states, discard redundant tool output — and compact *early*, while the session is healthy. Capture anything that might matter later before trimming.

**Choose method by step count.** On few-step tasks, pick the fastest, highest-fidelity method even if it costs more — the absolute difference is small. On many-step tasks, default to the cheaper method: savings compound across every step. This trades cost against *speed*, never against needed quality — never pick the cheap method when precision matters.

**Restart long sessions at natural boundaries** (topic done, older context no longer load-bearing), not on a message counter. When carrying work forward, hand off a short summary: objective, decisions, next action.

## Part 2 — Output discipline

Output tokens cost ~5× input and can never be cached — trimming the response is the highest-leverage saving per token.

**Lead with the answer.** No "Here's what I'll do…", no restating the prompt, no end-of-task recap. On long agentic runs a one-line status note is fine — cut ceremony, not useful visibility.

**Let complexity set length; don't pad.** A tight format (few bullets, short table, schema) caps the generation envelope better than "being brief" — but never crush real analysis into a format that drops substance.

**Minimize formatting overhead.** Heavy bullet scaffolding and nested headers are literal tokens; prefer flowing prose and fold short lists into sentences. Keep real lists for genuinely discrete items.

**Right-size reasoning.** Reasoning bills at output rates, so deliberating on trivia is expensive waste — but under-thinking a hard task is the worse error. If a problem is complex, spend the tokens.

**Commit instead of thrashing.** Pick an approach and follow it; don't re-explore decisions unless new information demands it.

## Part 3 — Setup-level habits

Always-loaded context (CLAUDE.md, instruction files) is re-sent every turn: for each line ask "would removing this cause a mistake?" Move sometimes-relevant workflows into skills (loaded on demand). Disable heavyweight tool integrations that aren't in use. Keep recurring reference documents in Projects rather than re-pasting them.

## Part 4 — Working in Cowork

Cowork's predictable token sinks: broad folder exploration, repeated screenshots, ambiguous instructions, large drafts. Counter them: **inventory before processing** (short file map + proposed approach, then read only what the task needs — unless the task genuinely requires full coverage, in which case confirm and do the full read); **work from the smallest useful surface** (ignore archives, old drafts, binaries); **checkpoint extractively** after a scan pass (source → key fact → why it matters, drop the raw reads); **avoid verbose computer-control** (screenshots are token-heavy; prefer reading a file or a connector directly).

## Part 5 — Environment-specific reinforcements

**In Claude Code sessions:** check whether `rtk` is installed (`command -v rtk`). If it is, prefix supported CLI commands with it (`rtk git status`, `rtk grep …`) — it wraps git/grep/rg/npm/npx/wc/find/ls/read/diff/err/test and returns compact output. If it isn't installed, suggest it once as a token-saving install, then drop it.

**If a "caveman" skill is available** and the user asks for "caveman", "less tokens", or "be brief" mode, switch to that skill's ultra-compressed register instead of just trimming normally.

## When torn, ask

Most moves above are safe — apply them silently. Pause only when a *specific* saving could plausibly cost quality: truncating/sampling data that might need full coverage; skimming sources for a deliverable that may need the full read; capping reasoning on a task that might be harder than it looks; delegating nuanced content to a subagent (game-of-telephone risk); a model that looks mismatched to the task. Keep the ask to one quick decision — cheaper path, thorough path, what's at stake — and don't re-ask once the user has signaled a preference. Default absent a steer: thrift on low-stakes work, coverage on client- or leadership-facing deliverables.

**Gut check before any token-heavy move:** am I about to put something in context (or generate something) that won't change the answer? Cut it. Am I about to cut something the answer needs? Keep it — and if I can't tell, ask.

## Maintenance

Token-efficiency practice shifts with model releases (pricing, thinking defaults, caching mechanics). **Last reviewed: 2026-08-06.** When models or pricing change materially, re-check the output/input price ratio behind the Part 0 thresholds and the model-fit guidance, and update this file.

| Date | What changed |
|---|---|
| 2026-06-05 | Initial skill (authored by Simon; deep-research backed). |
| 2026-08-04 | Genericized wording; linked caveman mode; added front-loading thresholds and revision guardrail. |
| 2026-08-06 | Company-shareable rewrite: removed personal references and personal maintenance plumbing (scheduled task, self-DM, missing reference files); made RTK and caveman conditional on environment; added subagent model routing; cut length ~45% with no habit or guardrail removed. |
