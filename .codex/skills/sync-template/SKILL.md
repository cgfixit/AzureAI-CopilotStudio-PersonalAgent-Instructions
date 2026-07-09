---
name: sync-template
description: Propagate approved TEMPLATE.md contract changes to all examples in each file's own dialect, update version histories, and validate.
---

# Sync Template

Use this only after an approved change to the shared `TEMPLATE.md` contract.

## Steps

1. Inspect the template diff:

```bash
git diff $(git merge-base HEAD origin/main) -- TEMPLATE.md
```

2. Classify each hunk as new section, rule change, placeholder-set change, or
   removal/weakening.
3. Stop for owner approval on removals, weakenings, or safety-language meaning
   changes.
4. Propagate content to every `examples/*.md` in that file's existing dialect.
5. If placeholders changed, update README placeholder docs and the preflight contract
   in the same commit.
6. Update both relevant version histories.
7. Run:

```bash
python .codex/scripts/repo_audit.py preflight .
```

## Guardrails

- Harvest domain facts from existing example text; do not invent product versions or
  constraints.
- Do not normalize dialects across files.
- Report any skipped file and why.
