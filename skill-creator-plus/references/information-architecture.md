# Skill Information Architecture — Best Practices

## The Three-Level Loading System

Skills use progressive disclosure to keep SKILL.md lean while making rich documentation available on demand.

| Level | What | Size target | Always loaded? |
|---|---|---|---|
| 1 | Frontmatter (name + description) | ~100 words | ✅ Yes |
| 2 | SKILL.md body | < 500 lines | ✅ When skill triggers |
| 3 | Bundled resources (references/, scripts/, assets/) | Unlimited | ❌ On demand only |

**Rule of thumb**: if a section in SKILL.md is longer than ~20 lines and isn't needed for every use of the skill, it belongs in `references/`.

---

## What Goes Where

### Keep in SKILL.md
- Workflow steps (the "what to do" sequence)
- Decision logic ("if X then Y")
- Pointers to reference files with clear "when to read" guidance
- Short checklists and quick-reference tables

### Move to references/
- Detailed documentation, specs, or API patterns
- Error handling guides and troubleshooting trees
- Large example sets or templates
- Domain-specific deep dives (e.g., per-platform instructions)
- Anything the skill only needs for specific sub-tasks

### Move to scripts/
- Repetitive or deterministic operations (file transforms, packaging, eval runs)
- Anything that benefits from being executed rather than read

### Move to assets/
- Template files, fonts, icons used in outputs

---

## How to Reference Files from SKILL.md

Always tell Claude *what* is in the file and *when* to read it. Never just list a file path.

**Format:**
```
Before [doing X], consult `references/name-of-file.md` for:
- Topic A
- Topic B
- Topic C
```

**Examples:**

```markdown
Before writing queries, consult `references/api-patterns.md` for:
- Rate limiting guidance
- Pagination patterns
- Error codes and handling
```

```markdown
If the user encounters connection issues, see `references/troubleshooting.md`
for MCP connection errors, authentication failures, and timeout handling.
```

```markdown
For per-platform deployment differences, consult the relevant file in
`./references/` — aws.md, gcp.md, or azure.md — based on the user's target.
```

**To refer to a directory:**
> "Search or consult the **`./references/`** directory for..."

---

## Domain Organization Pattern

When a skill supports multiple variants (platforms, frameworks, languages), organize by variant so Claude only loads what's relevant:

```
skill-name/
├── SKILL.md              ← workflow + selection logic
└── references/
    ├── variant-a.md
    ├── variant-b.md
    └── variant-c.md
```

SKILL.md handles the decision ("which variant applies here?"), then directs to the right file. Claude reads only the relevant one.

---

## Large Reference Files

For reference files over ~300 lines, always include a table of contents at the top so Claude can navigate efficiently:

```markdown
## Table of Contents
1. [Authentication patterns](#auth)
2. [Rate limiting](#rate-limiting)
3. [Error codes](#errors)
4. [Pagination](#pagination)
```

---

## Error Handling in Reference Files

Error handling documentation belongs in `references/`, not SKILL.md. Structure it as:

```markdown
## Common Issues

### [Error Name]
**Symptom**: What the user or Claude sees
**Cause**: Why it happens
**Fix**:
1. Step one
2. Step two
3. Step three

### MCP Connection Failed
**Symptom**: "Connection refused" error
**Cause**: MCP server not running or API key invalid
**Fix**:
1. Verify MCP server is running: Settings > Extensions
2. Confirm API key is valid
3. Try reconnecting: Settings > Extensions > [Your Service] > Reconnect

### Authentication Error
**Symptom**: 401 or "Unauthorized" response
**Fix**:
1. Check credentials are set correctly
2. Verify token hasn't expired
3. Re-authenticate via the connector settings
```

Then in SKILL.md, add a single pointer:
```markdown
If you hit errors during execution, consult `references/troubleshooting.md`
for common issues including connection failures, auth errors, and timeouts.
```

---

## Description Quality Checklist

A strong skill description follows this format:

**[What it does] + [When to use it] + [Key capabilities]**

And optionally:
- **Negative triggers**: "Do NOT use for X" — makes the skill more precise and avoids false triggers
- **Keyword density**: Include technical synonyms and domain terms users might say
- **Nuance**: The more specific, the better the triggering accuracy

### Example — weak description:
> "Helps with API integrations."

### Example — strong description:
> "Build and debug REST and GraphQL API integrations, including authentication flows, rate limiting, pagination, and error handling. Use when the user asks about calling external APIs, writing API clients, handling webhooks, OAuth flows, or debugging HTTP errors. Also trigger for 'how do I connect to X service', 'my API calls are failing', or 'write me a fetch/axios/requests wrapper'. Do NOT use for database queries, internal function calls, or UI components that don't involve external HTTP requests."

### Negative trigger examples:
- "Do NOT use for general Python questions unrelated to the skill's domain"
- "Do NOT use when the user just wants a quick code snippet — this skill is for full workflow guidance"
- "Do NOT use for frontend styling — this skill covers backend logic only"
