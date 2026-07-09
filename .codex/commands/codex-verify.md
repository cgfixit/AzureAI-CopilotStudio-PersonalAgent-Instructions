# Codex Verify

Use `.codex/skills/codex-verify/SKILL.md` as the source of truth for repo-local
Codex verification.

When onboarding a fresh clone or publishing `.codex/` or workflow changes:

- run `python .codex/scripts/repo_audit.py verify-codex .`
- fix missing command wrappers, bash-only Codex docs, or workflow hardening drift
- keep manual-only GitHub settings called out explicitly instead of pretending the repo tree can prove them
