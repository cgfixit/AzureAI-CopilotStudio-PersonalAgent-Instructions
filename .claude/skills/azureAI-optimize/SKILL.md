---
name: azureAI-optimize
description: Analyze and optimize this repository — enhance templates/examples for Azure AI o3 personal agents, add CI workflows, harden security, add new domain examples, fix structural gaps.
---

Optimize the AzureAI-CopilotStudio-PersonalAgent-Instructions repository. This is a documentation/prompt-engineering library (no build system, no tests). Every deliverable is a Markdown file containing system instructions for enterprise AI personal agents.

## Step 1: Run the analysis driver

```bash
bash .claude/skills/azureAI-optimize/analyze.sh .
```

Read the output carefully. It reports:
1. **Unfilled placeholders** in `examples/` (bugs — these should be filled)
2. **Missing core sections** per example (Purpose, Core Mission, Forbidden Actions, Escalation, Security, Source Hierarchy)
3. **Azure AI o3 reasoning protocol** presence/absence per file
4. **README ↔ examples/ consistency** (files missing from the README structure block)
5. **CI workflow gaps** (markdown lint, link check, placeholder audit)
6. **Security hardening** (action pinning, CODEOWNERS, branch protection)
7. **Domain coverage** (existing vs suggested new domains)

## Step 2: Pick an optimization category and execute

Based on the analysis output and the user's request, choose one or more of these categories. If the user didn't specify, pick the highest-impact items from the analysis.

### A. Enhance examples for Azure AI Enterprise o3

The `examples/Network&SecurityAgent.md` is the reference implementation for o3 optimization — it includes a `## Reasoning Protocol (o3-Optimized)` section with a structured pre-response checklist (QUERY TYPE → LAYER/DOMAIN → ENVIRONMENT ASSUMPTIONS → GROUNDING CHECK → VERSION STRICTNESS → FAILURE MODES → SELF-CRITIQUE → OUTPUT DECISION) and explicit confidence rules.

For each example flagged as `ENHANCE` in the analysis:

1. Read `examples/Network&SecurityAgent.md` sections 2 (Reasoning Protocol) and 3 (Response Modes) as the pattern to follow.
2. Add a domain-appropriate `## Reasoning Protocol (o3-Optimized)` section after Core Mission. Adapt the checklist dimensions to the domain (e.g., for PowerShell: EDITION → MODULE AVAILABILITY → COMPATIBILITY → ERROR HANDLING STRATEGY; for YARA: RULE TYPE → TARGET ARTIFACT → FP RISK → PERFORMANCE IMPACT).
3. Add explicit confidence-surfacing rules: state confidence with source, escalate below 70%.
4. Add a `## Response Modes` table mapping trigger phrases to output modes (Procedure, Quick Fact, Troubleshoot, etc.).
5. Preserve all existing content — these are additive enhancements.

### B. Enhance TEMPLATE.md generically

Add an **optional** `## Reasoning Protocol` section to `TEMPLATE.md` with `[DOMAIN_REASONING_DIMENSIONS]` placeholders. This keeps the template generic while showing adopters where to add reasoning-model optimization. Include a note that this section is designed for reasoning models (o3, o4-mini, etc.) and can be omitted for standard chat models.

### C. Add new domain examples

Use the `/new-example` command (or follow its instructions manually):
1. Read `TEMPLATE.md` for the canonical structure.
2. Create `examples/<domain>.md` — fill every `[PLACEHOLDER]`, keep all core sections.
3. Include an o3 Reasoning Protocol section (pattern from Network&SecurityAgent.md).
4. Update `README.md` Repository Structure and Version History.

Suggested domains from the analysis: healthcare/clinical-protocols, legal/compliance, finance/finops, devops/incident-response.

### D. Add CI workflows

Create new workflow files under `.github/workflows/`:

- **`markdown-lint.yml`** — Run `markdownlint-cli2` on push/PR to `main`. Use `DavidAnson/markdownlint-cli2-action` (pinned to SHA). Catches inconsistent heading styles, trailing whitespace, line length issues.
- **`link-check.yml`** — Run `lychee` link checker on push/PR. Use `lycheeverse/lychee-action` (pinned to SHA). Catches dead documentation URLs.
- **`placeholder-audit.yml`** — Run the placeholder scan from `analyze.sh` as a CI check. Fail the build if any `examples/*.md` file contains unfilled `[UPPER_SNAKE_CASE]` placeholders (excluding known structural syntax).

All workflows should:
- Trigger on `push` and `pull_request` to `main`
- Pin actions to commit SHAs (not version tags) for supply-chain security
- Use `permissions: contents: read` minimum

### E. Security hardening

1. **Pin existing workflow actions to SHAs.** In `devskim.yml` and `gitleaks.yml`, replace `@v1`/`@v2`/`@v3`/`@v4` tags with the full commit SHA for the same release. Look up the SHA from the action's releases page or use `git ls-remote`.
2. **Add `CODEOWNERS`** at `.github/CODEOWNERS` — assign `@cgfixit` (or the appropriate owner) as default reviewer for all files, with specific ownership for `.github/workflows/` and `TEMPLATE.md`.
3. **Add `.gitattributes`** — mark `*.md` as `text eol=lf` for consistent line endings across platforms.
4. **Add Dependabot config** — `.github/dependabot.yml` to watch GitHub Actions for version updates (weekly cadence).

### F. Fix structural gaps

Address issues from analysis sections 1 (unfilled placeholders) and 2 (missing sections):
- Fill any remaining `[PLACEHOLDER]` tokens in examples with domain-appropriate values.
- Add missing Escalation Protocol, Security & Privacy, or Forbidden Actions sections to examples that lack them, following the patterns in `TEMPLATE.md` and `cloud-infra.md`.

## Step 3: Validate

After making changes, run validation:
```bash
bash .claude/skills/azureAI-optimize/analyze.sh .
```

Also run `/preflight` (`bash .claude/skills/preflight/check.sh .`) — the local mirror of every blocking CI gate — and get exit 0.

Confirm:
- No new unfilled placeholders introduced
- All modified files retain the core section invariants
- No content that looks like real secrets, keys, or tokens
- README reflects any new files added

## Step 4: Commit and push

Commit with a descriptive message summarizing which optimization categories were applied. Push to the working branch and create a PR (or push to `main` if instructed).

## Gotchas

- **TEMPLATE.md placeholders must stay unfilled** — it is the generic source. Only examples get filled in.
- **Licensing scope** — MIT covers only `TEMPLATE.md`, `cloud-infra.md`, `ps1AgentCoder.md`, `yaragenerator.md`, and `incident-response.md` (the README license block is the single authority). New examples default to MIT-covered unless they reference proprietary products (like the Veeam example). Update the README license block accordingly.
- **Gitleaks scans full history** — never commit real-looking secrets, even in examples. Use obviously fake values (`your-api-key-here`, `support@example.com`).
- **The placeholder audit has a blind spot** — `veeamGPT.md` uses non-bracket sanitization tokens (`#REDACTED.com` URLs, `PLACHOLDER.storylane.io`, `REDACTED@REDACTED.com`) that the `[UPPER_SNAKE]` regex cannot see. These are *intentional* redactions in a reference-only file: do not "fix" them, and do not imitate the pattern in new examples.
- **Before acting on any factual claim in this Gotchas list, re-verify it against the tree** (grep/ls) — earlier revisions of this list described already-fixed bugs as live, and stale meta-guidance causes bad edits.
