---
name: azureai-optimize
description: Analyze and optimize this documentation repository for Azure AI / Copilot Studio personal-agent instructions, prompt safety invariants, README drift, CI coverage, and security-hardening gaps.
---

# AzureAI Optimize

Use this for periodic repo improvement passes. This is a docs-only prompt library:
there is no app runtime, package manager, or unit-test suite.

## Steps

1. Run the analyzer:

```bash
python .codex/scripts/repo_audit.py analyze .
```

2. Pick the smallest justified fix from the findings.
3. Preserve the existing dialect of every edited Markdown file.
4. Do not fill placeholders in `TEMPLATE.md`.
5. Do not leave placeholders in `examples/*.md`.
6. Run preflight before committing:

```bash
python .codex/scripts/repo_audit.py preflight .
```

## Guardrails

- Prefer README/tree drift fixes, placeholder hygiene, and CI mirror alignment over
  broad prose rewrites.
- Do not change the meaning of safety, escalation, source hierarchy, or security
  language without explicit owner approval.
- Use Ponytail discipline: one small improvement per PR unless the fixes are tightly
  coupled.

The shell analyzer remains at `.codex/skills/azureai-optimize/analyze.sh` for Unix
users, but the Python audit entrypoint above is the Codex default.
