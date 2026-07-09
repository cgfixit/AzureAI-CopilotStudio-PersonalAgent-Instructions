# Codex Setup

This directory contains Codex-facing guidance for this docs-only prompt repository.

## Skills

- `$preflight`: run the local CI mirror before Markdown commits.
- `$azureai-optimize`: inspect prompt, CI, README, and security-hardening gaps.
- `$codex-verify`: verify repo-local Codex docs, command wrappers, and CI workflow hardening surfaces.
- `$new-example`: create a new deployable example under `examples/`.
- `$sync-template`: propagate approved `TEMPLATE.md` contract changes to examples.
- `$red-team`: simulate the adversarial validation battery for an example file.

## Commands

```bash
python .codex/scripts/repo_audit.py preflight .
python .codex/scripts/repo_audit.py analyze .
python .codex/scripts/repo_audit.py verify-codex .
```

## Notes

- `.claude/skills/` remains available for Claude users.
- `.codex/skills/` is the Codex-native mirror and should be kept in sync when workflow
  behavior changes.
- `.codex/commands/` contains lightweight repo-local wrappers for the most common
  Codex entrypoints.
- The Python audit entrypoints are the Windows-friendly default; the legacy shell
  scripts remain as optional Unix mirrors.
- `.codex/ponytail-plugin.json` records the Ponytail plugin metadata used for minimal
  diffs; it is not a vendored copy of the plugin.
