---
description: Validate instruction files for leftover placeholders, structural integrity, and accidental secrets
argument-hint: [path] (default: TEMPLATE.md and examples/)
---

Validate the instruction file(s) at: **$ARGUMENTS** (default: `TEMPLATE.md` and everything under `examples/`).

Check and report:
1. **Unfilled placeholders** — in `examples/*.md`, flag any remaining `[UPPER_SNAKE_CASE]` bracket tokens (these are bugs). Ignore intentional syntax: `[Image: ...]`, `[ ]` checklist boxes, `![Warning]`, `![Troubleshooting]`. In `TEMPLATE.md`, placeholders are expected — only confirm they are still present.
2. **Structural integrity** — confirm each example retains the core sections from `TEMPLATE.md`: the 3-Tier Authoritative Source Hierarchy, the Mandatory Tutorial Template shape (Purpose / Validated against / Requirements / Procedure with Checkpoints / Verification), Forbidden Actions, and the Escalation Protocol.
3. **Possible secrets** — scan for anything resembling real API keys, tokens, passwords, private keys, or credentials (Gitleaks runs in CI; catch it before commit). Illustrative placeholders are fine; real-looking secrets are not.
4. **README/LICENSE consistency** — verify every file in `examples/` is listed in the README Repository Structure block, and that the LICENSE scope block matches actual filenames.

Report findings as a concise checklist; do not modify files unless asked.
