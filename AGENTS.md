# Codex Repository Instructions

## Verdict

This is a documentation and prompt-engineering repository. There is no app, package
manager, build system, or unit-test suite. The product is the Markdown instruction
content in `TEMPLATE.md` and `examples/*.md`.

## Repository Map

- `TEMPLATE.md` is the canonical generic template. Keep its `[UPPER_SNAKE_CASE]`
  placeholders unfilled.
- `examples/*.md` are deployable, filled-in agent instructions. They must not contain
  leftover `[UPPER_SNAKE_CASE]` placeholders.
- `README.md` is the public index and the source of truth for placeholder lists,
  repository structure, license scope, and version history.
- `.github/workflows/` contains the CI gates and non-blocking prose checks.
- `.codex/skills/` contains Codex-native workflows converted from `.claude/skills/`.
- `.codex/commands/` contains lightweight repo-local command notes for the main
  Codex entrypoints.
- `.claude/skills/` remains for Claude users; do not edit it unless the change is
  intentionally cross-agent.

## Required Workflow

1. Read `README.md`, `TEMPLATE.md`, and this file before editing prompt content.
2. Preserve each file's existing dialect, headings, typography, and safety language.
3. Do not fill placeholders in `TEMPLATE.md`.
4. Do not leave placeholders in `examples/*.md`.
5. For any add, rename, or delete under `examples/`, update the README structure,
   license scope, and version history in the same commit.
6. Before committing Markdown changes, run:

```bash
python .codex/scripts/repo_audit.py preflight .
```

7. After cloning the repo or changing `.codex/` or workflow files, verify the
   repo-local Codex setup with:

```bash
python .codex/scripts/repo_audit.py verify-codex .
```

## Safety Rules

- Never commit real or realistic secrets, tokens, API keys, private keys, or internal
  emails. Use obviously fake values such as `your-api-key-here` or
  `support@example.com`.
- Do not soften "never", "must", "zero tolerance", source hierarchy, escalation, or
  security wording unless the owner explicitly asks.
- Do not delete, rename, or hollow out published examples without explicit approval.
- Do not make non-blocking CI checks blocking unless explicitly requested.
- The tree wins for file existence; `README.md` wins for license scope and placeholder
  inventory.

## Ponytail

Use the Ponytail plugin discipline for repo changes: smallest correct diff, no
speculative abstraction, stdlib/native tools first, deletion over churn. The plugin
metadata pointer is `.codex/ponytail-plugin.json`; install the actual plugin from its
upstream marketplace or repository rather than vendoring it here.
