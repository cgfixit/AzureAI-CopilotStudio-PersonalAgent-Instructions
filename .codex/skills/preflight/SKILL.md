---
name: preflight
description: Run the local CI mirror before commits that touch Markdown or prompt instructions.
---

# Preflight

Run this before every commit that changes Markdown prompt content:

```bash
bash .codex/skills/preflight/check.sh .
```

Exit 0 means the local blocking checks passed. Fix failures in content, not in the
checker, unless the owner explicitly approved a contract change.

## Checks

- No leftover `[UPPER_SNAKE_CASE]` placeholders in `examples/`
- `TEMPLATE.md` still retains its placeholder inventory
- Core safety invariants remain present in every example
- No chat-session trailers at the end of instruction files
- No obvious secret-shaped strings
- README and `examples/` stay synchronized
- Markdown lint is informational, matching CI policy
