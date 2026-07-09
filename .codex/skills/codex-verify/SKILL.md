---
name: codex-verify
description: Verify the repo-local Codex setup after clone or before publish: Windows-ready entrypoints, command wrappers, CI workflow hardening surfaces, and supporting policy files.
---

# Codex Verify

Use this after cloning the repo, after changing `.codex/`, or before publishing CI or
repo-onboarding updates.

## Steps

1. Run the verifier:

```bash
python .codex/scripts/repo_audit.py verify-codex .
```

2. If it flags Codex doc drift, fix `AGENTS.md`, `.codex/README.md`, or the affected
   command wrapper.
3. If it flags workflow drift, fix the YAML or supporting file, not the verifier.
4. If you changed Markdown instructions, finish with:

```bash
python .codex/scripts/repo_audit.py preflight .
```

## Guardrails

- Treat Windows readiness as a first-class requirement; do not rely on WSL-only
  `bash` entrypoints for Codex workflows.
- Keep repo-local command notes lightweight. They should point to the skill or audit
  source of truth, not duplicate long procedures.
- Leave manual GitHub settings checks explicit when the repo tree cannot prove them
  (for example branch protection or app-install scope).
