# AzureAI Optimize

Use `.codex/skills/azureai-optimize/SKILL.md` as the source of truth for periodic
repo improvement passes.

When the user asks to optimize prompt quality, Codex setup, or CI hygiene:

- run `python .codex/scripts/repo_audit.py analyze .`
- pick the smallest justified fix from the findings
- preserve each file's dialect and safety wording
- finish with `python .codex/scripts/repo_audit.py preflight .` if Markdown changed
