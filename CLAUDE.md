# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **documentation / prompt-engineering library**, not a software project. There is no application code, no build system, no test suite, and no package manager. Every deliverable is a Markdown file containing **system instructions** for enterprise AI personal agents (Azure AI Studio / Copilot Studio, OpenAI Assistants, Anthropic Claude Projects, etc.).

The product is the *prose and structure* of these instruction files. When editing, the goal is to preserve the safety mechanisms they encode, not to refactor code.

## Repository structure & how the pieces relate

- `TEMPLATE.md` — the **canonical, domain-agnostic source**. Everything else derives from it. It defines the reusable contract: Response Rules, the Mandatory Tutorial Template, Forbidden Actions, the 3-tier Authoritative Source Hierarchy, Security & Privacy, and the Escalation Protocol. Edits to a shared safety mechanism should usually start here and then propagate to the examples.
- `examples/` — fully-instantiated versions of `TEMPLATE.md` for specific domains. Each is a standalone, copy-paste-ready system prompt with all placeholders filled in:
  - `cloud-infra.md` (multi-cloud infrastructure), `veeamGPT.md` (backup/DR), `ps1AgentCoder.md` (PowerShell coding agent), `pythonAgentCoder.md` (Python coding agent), `yaragenerator.md` (YARA rule generation), `Network&SecurityAgent.md` (network/security).
- `README.md` — the public landing page: rationale, quick-start, placeholder list, deployment snippets, version history.
- `LICENSE` — MIT, but **scoped**. See licensing note below.
- `.github/workflows/` — the only automation (see CI).

## The placeholder convention (most important editing rule)

`TEMPLATE.md` uses `[UPPER_SNAKE_CASE]` bracket tokens as substitution points (e.g. `[YOUR_DOMAIN]`, `[DOMAIN_PRODUCTS]`, `[CRITICAL_CONSTRAINT_1]`, `[INTERNAL_SUPPORT_EMAIL]`, `[CURRENT_YEAR]`). The README "Customize Placeholders" section is the authoritative list.

- In `TEMPLATE.md`, placeholders **must remain unfilled** — it is the generic source.
- In `examples/*.md`, there should be **no leftover `[PLACEHOLDER]` tokens** — an unfilled bracket in an example is a bug. (Note: literal `[Image: ...]`, `[ ]` checklist boxes, and `![Warning]`/`![Troubleshooting]` callout markers are intentional structural syntax, not placeholders.)

## Core conceptual structure shared by every file

When adding or editing an instruction file, keep these invariants intact — they are the reason the repo exists:

1. **3-Tier Source Hierarchy** — Tier 1 (official docs, never override) > Tier 2 (best-practice, cross-check Tier 1) > Tier 3 (personal/internal notes, must be verified against Tier 1 and marked advisory).
2. **Mandatory Tutorial Template** — the deterministic output shape for procedural answers: `Purpose` → `Validated against` (exact version + date) → `Requirements` → numbered atomic `Procedure` steps with `✅ Checkpoint`s → `Verification`.
3. **Anti-hallucination / version-strictness** — refuse when docs are silent; never claim a deprecated feature works in a newer version; never infer environment details.
4. **Escalation Protocol** — route undocumented/edge cases to an internal contact or ticket process rather than guessing.

A new `examples/*.md` should be recognizable as the same skeleton as `TEMPLATE.md` with domain-specific constraints filled in.

## Licensing nuance (verify before adding/removing license headers)

The MIT license applies **only** to `TEMPLATE.md` and a specific subset of examples (per `README.md`: `cloud-infra.md`, the PowerShell example, `yaragenerator.md`). Other files — notably the **Veeam-specific** example — are reference-only and **not** MIT-covered. Do not add MIT headers to non-covered files, and keep the README license block accurate when adding examples. The README's license list and actual example filenames have drifted historically (e.g. `ps1CodingAgent.md` vs the actual `ps1AgentCoder.md`); reconcile names when touching either.

## CI / validation

Two GitHub Actions run on push and pull_request to `main` (and weekly on cron):
- `.github/workflows/devskim.yml` — Microsoft DevSkim security analysis, uploads SARIF to code scanning.
- `.github/workflows/gitleaks.yml` — Gitleaks secret scan over full history (`fetch-depth: 0`).

There is nothing to build or unit-test. "Passing CI" means these scanners find no issues. Since examples contain illustrative commands, API snippets, and config, **never commit anything that looks like a real secret, key, or token** — Gitleaks scans every commit, so a leak in history fails CI even if later removed.

## Conventions for contributions

Per `README.md`, contributions focus on: new domain examples, integration guides, testing strategies, and localization. Keep `README.md`'s Repository Structure list and Version History in sync when adding files. Match the existing tone: precise, version-dated, citation-driven.
