---
name: new-example
description: Create a complete deployable domain example under examples/ from TEMPLATE.md, with README sync, license classification, and preflight validation.
argument-hint: <domain-name>
---

# New Example

Use this when adding a new domain-specific agent instruction file.

## Steps

1. Check for overlap with existing `examples/*.md`; extend an existing example only
   if the owner asks.
2. Read `TEMPLATE.md`, `README.md`, and `AGENTS.md`.
3. Create `examples/<domain>.md` in kebab-case.
4. Fill every `[UPPER_SNAKE_CASE]` placeholder with concrete domain values.
5. Keep real-product claims verifiable against official docs; otherwise use clearly
   fictional products.
6. Add the README sync triangle in the same commit:
   - Repository Structure entry
   - License scope classification
   - Version History entry
7. Run:

```bash
python .codex/scripts/repo_audit.py preflight .
```

## Guardrails

- Do not edit `TEMPLATE.md` for a new example.
- Do not add real-looking secrets.
- Default license classification is MIT unless the example is vendor-proprietary or
  ambiguous; ask when ambiguous.
