---
name: new-example
description: Scaffold a complete, deploy-ready domain example in examples/ from TEMPLATE.md — domain research, o3 Reasoning Protocol, ≥2 dated critical constraints, license classification, README sync, preflight validation. Use when asked to add or create a new domain-specific agent instruction file.
argument-hint: <domain-name> (e.g. "kubernetes-ops", "tax-compliance")
---

# New Example — full scaffold protocol

Produce a new fully-instantiated agent instruction file for the requested domain.
The output must be indistinguishable in quality from `examples/incident-response.md`
(the canonical shape): a standalone system prompt someone can paste into
Azure AI Studio / Copilot Studio / OpenAI Assistants / Claude Projects unedited.

## Step 0: Name and scope

- Filename: kebab-case, `examples/<domain>.md` (e.g. `finops-governance.md`).
  Existing filenames are frozen — never rename an existing example to make room.
- Collision check: confirm the file doesn't exist and the domain doesn't
  substantially overlap one of the current examples (cloud-infra, incident-response,
  network/security, PowerShell coding, Python coding, Veeam backup/DR, YARA). If it
  overlaps, propose extending the existing file instead and stop for user
  confirmation.

## Step 1: Research the domain BEFORE writing

Collect, with dates and real URLs where they exist:

1. **Products & versions** — the 3-6 products/tools the agent will cover, each with
   its current major version. *Honesty rule:* if the domain uses real products,
   every version, deprecation, and behavior claim you write must be verifiable
   against that vendor's official docs. If you cannot verify, use clearly fictional
   products (like TEMPLATE.md's "Product X") — never plausible-but-invented claims
   about real ones.
2. **≥2 critical constraints** — hard, dated rules of the form the template's
   `[CRITICAL_CONSTRAINT_*]` placeholders expect ("X was deprecated in vN (date) —
   never state it works in vN+1", "Feature Y requires license Z"). These anchor the
   file's version-strictness and later feed `/red-team` test generation.
3. **Tiered sources** — Tier 1: the domain's official docs/release notes/API
   references (real URLs); Tier 2: official blogs/best-practice guides; Tier 3:
   internal-notes categories.
4. **Escalation contact** — fake but plausible (`<domain>-support@example.com`,
   ticket process ID like `KB-<DOMAIN>-WORKFLOW`). Never a real internal address.
5. **Reasoning dimensions** — the 4-8 domain-specific checklist dimensions for the
   o3 Reasoning Protocol (what must the agent pin down before answering: edition?
   platform? version? blast radius? licensing?).
6. **Response-mode triggers** — the 4-6 phrasings users in this domain actually use,
   mapped to output modes (Procedure / Quick Fact / Troubleshoot / Design / Clarify).

## Step 2: Scaffold from TEMPLATE.md

- Read `TEMPLATE.md`; keep its section skeleton and order:
  Purpose & Core Mission → Response Rules (+ Tool & Data Access) → Reasoning
  Protocol (o3-Optimized) → Response Modes → Mandatory Tutorial Template →
  Forbidden Actions (Zero Tolerance) → Authoritative Source Hierarchy (Strict,
  Tier 1/2/3) → Formatting & Validation → Security & Privacy → Escalation
  Protocol → Response Quality Checklist.
- **Drop the template's meta sections** — they instruct the *adopter*, not the
  agent: Customization Instructions, Key Safety Principles, Example
  Implementation, Version History. An example is a finished system prompt; meta
  commentary in it is a bug.
- Start the file with the standard header comment block (copy the shape from
  `examples/incident-response.md`):

  ```markdown
  <!---
  //  Community Resource – CGFixIT Personal AI Agent Instructions
  //  <Domain> Agent
  //  Scope: <one line>
  //  Maintained by: CGFixIT (https://cgfixit.com | https://github.com/CGFixIT)
  //  Use with: Azure OpenAI o3, Copilot Studio, OpenAI Assistants, Anthropic Claude Projects
  -->
  ```

- Rename the Reasoning Protocol heading to `## Reasoning Protocol (o3-Optimized)`
  (the examples' convention; the "(Optional …)" phrasing stays only in TEMPLATE.md).

## Step 3: Fill every placeholder

- Replace **every** `[UPPER_SNAKE_CASE]` token with the Step 1 values. Zero may
  remain — CI (`placeholder-audit.yml`) blocks the merge otherwise.
- Keep intentional structural syntax verbatim: `[Image: Step_Name]`, `[ ]`
  checklist boxes, `![Warning]`, `![Troubleshooting]`, `[DATE]`, and the exact
  checkpoint line `> ✅ **Checkpoint**: [what must now be true]`.
- Straight ASCII quotes; match TEMPLATE.md's typography. Do not import smart quotes
  or decorative formatting from research sources.

## Step 4: Classify the license

- **Default: MIT** — add the filename to the README license scope block.
- **Vendor-proprietary domain** (the file is mostly about one company's commercial
  product, like veeamGPT.md): reference-only — do NOT add it to the MIT block; it
  falls under the "all other files" clause automatically.
- **Ambiguous:** stop and ask the user before committing.
- Never add MIT license headers inside any file — scope lives only in README.

## Step 5: README sync triangle (same commit as the new file)

1. Repository Structure block: add `│   ├── <name>.md ← <one-line description>` in
   alphabetical position, case-exact.
2. License scope block: add the path if (and only if) Step 4 said MIT.
3. Version History: append `- **vX.Y** (Mon YYYY): Added examples/<name>.md (<domain>)`
   — increment the minor version from the latest entry.

## Step 6: Self-review against the quality bar

Walk the "Example (new or edited)" checklist in CLAUDE.md §Quality bar. Every item
is a yes/no; fix any "no" before proceeding.

## Step 7: Validate

Run `/preflight` (`bash .claude/skills/preflight/check.sh .`) and get exit 0.
Fix failures by fixing the new file — **never** by editing the checker or its
exclusion list.

## Step 8: Report

Summarize: filename, domain, license classification, the 2+ critical constraints
chosen, and the README entries touched. Suggest running `/red-team examples/<name>.md`
to score the new file's hallucination resistance before real deployment.

## Prohibitions

- **Never modify TEMPLATE.md** in a new-example change — it is the generic source
  and its placeholders stay unfilled.
- **No real-looking secrets** anywhere, even illustrative (Gitleaks scans full
  history; a leak is permanent). Use `your-api-key-here` style values.
- **No chat artifacts** — the file must read as a system prompt from the first line
  to the last. No "Let me know…", no "Here's the updated…", no TODO chatter.
- **No unverifiable claims about real products** (see the Step 1 honesty rule).
