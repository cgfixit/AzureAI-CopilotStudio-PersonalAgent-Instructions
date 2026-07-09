# Codex Setup

This directory contains Codex-facing guidance for this docs-only prompt repository.

## Skills

- `$preflight`: run the local CI mirror before Markdown commits.
- `$azureai-optimize`: inspect prompt, CI, README, and security-hardening gaps.
- `$new-example`: create a new deployable example under `examples/`.
- `$sync-template`: propagate approved `TEMPLATE.md` contract changes to examples.
- `$red-team`: simulate the adversarial validation battery for an example file.

## Commands

```bash
bash .codex/skills/preflight/check.sh .
bash .codex/skills/azureai-optimize/analyze.sh .
```

## Notes

- `.claude/skills/` remains available for Claude users.
- `.codex/skills/` is the Codex-native mirror and should be kept in sync when workflow
  behavior changes.
- `.codex/ponytail-plugin.json` records the Ponytail plugin metadata used for minimal
  diffs; it is not a vendored copy of the plugin.
