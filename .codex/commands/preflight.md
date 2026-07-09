# Preflight

Use `.codex/skills/preflight/SKILL.md` as the source of truth for the blocking
pre-commit checks in this repo.

When Markdown or prompt instructions change:

- run `python .codex/scripts/repo_audit.py preflight .`
- treat any `FAIL` as blocking
- keep `TEMPLATE.md` placeholders unfilled
- fix README/example drift in the content, not by weakening the checker
