# Codex Onboarding

Use `.codex/skills/codex-onboarding/SKILL.md` as the source of truth for
resyncing this repo from `origin/main`, verifying the Codex setup, and preparing
the smallest safe PR branch.

When starting from a fresh clone or after a sync:

- ensure the checkout is on `main`
- run `python .codex/scripts/repo_audit.py verify-codex .`
- inspect workflow hardening and manual GitHub settings explicitly
- run `python .codex/scripts/repo_audit.py preflight .` if Markdown changed
