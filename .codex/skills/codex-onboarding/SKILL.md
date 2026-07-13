---
name: codex-onboarding
description: Resync this docs-only repository to origin/main, verify repo-local Codex setup, and prepare the smallest safe change set for a PR.
---

# Codex Onboarding

Use this when cloning, resyncing, or preparing a fresh Codex session in this repository.

## Steps

1. Confirm the checkout is on `main` and aligned with `origin/main`.
2. Verify the repo-local Codex setup:

```bash
python .codex/scripts/repo_audit.py verify-codex .
```

3. Inspect `.github/workflows/*.yml` for root `permissions: contents: read`,
   pinned third-party action SHAs, and non-blocking prose checks where intended.
4. If Markdown or prompt instructions changed, run:

```bash
python .codex/scripts/repo_audit.py preflight .
```

5. Use `karpathy-skills:karpathy-guidelines` for reasoning discipline and
   `ponytail:ponytail` for the smallest correct diff when those plugins are
   available in the current session.
6. Keep manual GitHub settings explicit when the tree cannot prove them
   (branch protection, app installation scope, or review rules).

## Guardrails

- Do not pretend local files can prove GitHub-side permissions.
- Do not expand scope beyond onboarding, verification, and the smallest justified fix.
- Prefer repo-native Python entrypoints over bash-only instructions.
