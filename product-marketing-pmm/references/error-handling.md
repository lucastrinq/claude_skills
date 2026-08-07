# Error Handling

## Module Not Found

**Symptom**: User references a module that doesn't exist in the registry (e.g. "activate SEO module")
**Resolution**: "That module isn't currently in the PMM skill. Available modules are: ICP & Persona, Competitive Intelligence, Win/Loss, Messaging & Positioning, 4Ps, and Product Launch Playbook. Would you like me to note this as a module to build?"

---

## Required Module is Inactive

**Symptom**: User asks a question that clearly requires a disabled module
**Resolution**: Do not silently produce a degraded answer. Say: "This request needs the [Module] module, which is currently inactive. Want me to activate it for this response?"

---

## External Skill Unavailable

**Symptom**: `messaging-positioning` or `product-launch-playbook` skill is not installed or not accessible
**Resolution**: "The [Skill Name] skill doesn't appear to be installed. I can provide a basic version of this output using built-in knowledge, but for the full framework I recommend installing it from your skill library. Shall I proceed with the basic version?"

---

## Ambiguous Module Routing

**Symptom**: Request spans multiple modules and it's unclear which to apply
**Resolution**: Name the modules you're considering and ask: "This touches both [Module A] and [Module B]. Should I apply both, or focus on one? Both are currently active."

---

## Insufficient Context to Apply Framework

**Symptom**: User asks for an ICP, competitive analysis, or win/loss output but provides no company/product context
**Resolution**: Ask the minimum viable questions before proceeding — never produce a generic template filled with placeholders. Ask: "To make this useful rather than generic, I need a few details: [1–3 specific questions]."
