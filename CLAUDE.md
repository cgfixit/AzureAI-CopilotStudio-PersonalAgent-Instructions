# CLAUDE.md — Operating Manual

This file is the operating manual for working in this repository. Read it as binding
guidance: the rules below exist because each one prevents a specific, observed way of
breaking this repo.

## 1. What this repository is (and is not)

A **documentation / prompt-engineering library**. There is no application code, no
build system, no test suite, no package manager. Every deliverable is a Markdown file
containing **system instructions** for enterprise AI personal agents (Azure AI Studio /
Copilot Studio, OpenAI Assistants, Anthropic Claude Projects).

The product is the **prose and safety structure** of these files. "Passing CI" means
the scanners find nothing — there is nothing to compile or unit-test. The editing goal
is always to *preserve the safety mechanisms the files encode*, never to refactor,
deduplicate, or restyle them. Sole maintainer and reviewer: **@cgfixit** (Chris Grady).

## 2. Map of the repository

| Path | Role |
|---|---|
| `TEMPLATE.md` | **Canonical, domain-agnostic source.** Placeholders stay unfilled. Shared safety edits start here, then propagate (use `/sync-template`). |
| `examples/*.md` | Fully-instantiated derivatives — standalone, copy-paste-ready system prompts. Zero unfilled placeholders. |
| `README.md` | Public landing page — and the **single authority** for two things: the placeholder list ("Customize Placeholders") and the MIT license scope block. |
| `LICENSE` | MIT, but **scoped** — see §6 row 5. |
| `.github/workflows/` | The only automation — see §8. |
| `.claude/skills/` | The executable arm of this manual — see §10. |

### The examples and their dialects

The 7 examples fall into 4 structural **dialects**. Dialect variation is deliberate
and frozen; know which one you are editing:

| Dialect | Files | Signature |
|---|---|---|
| TEMPLATE-faithful | `incident-response.md` | Headings mirror TEMPLATE.md nearly 1:1. The canonical shape for new examples. |
| Coder/KB family | `ps1AgentCoder.md`, `pythonAgentCoder.md`, `yaragenerator.md` | "Mandatory Output Templates A/B", tiers named "Ground truth / Strong patterns / Advisory", `#`-comment header. |
| Narrative-tiered | `cloud-infra.md`, `veeamGPT.md` | "Sources to Use With High Authority", "Tutorial Creation Protocol", `<checkpoint>` syntax instead of `> ✅ **Checkpoint**:`. |
| Numbered outlier | `Network&SecurityAgent.md` | Sections numbered 1–13, tier hierarchy as a table, partly non-standard markdown. |

### The sync triangle

Any add/rename/delete in `examples/` touches **three README blocks in the same
commit**: the Repository Structure list, the license scope block (if MIT), and the
Version History. A file change without its README triangle is an incomplete change.

## 3. The placeholder contract (most important editing rule)

`TEMPLATE.md` uses `[UPPER_SNAKE_CASE]` bracket tokens as substitution points. The
README "Customize Placeholders" block is the authoritative token list.

- In `TEMPLATE.md`: placeholders **must remain unfilled** (24 unique tokens as of
  v1.6). Filling one breaks the product.
- In `examples/*.md`: **zero** unfilled tokens. CI blocks the merge otherwise.

The blocking CI check (`placeholder-audit.yml`) matches `\[[A-Z][A-Z0-9_]{2,}\]` and
excludes exactly this structural syntax: `[Image:`, `[Warning]`, `[Note]`,
`[Troubleshooting]`, `[FinOps]`, `[Security]`, `[IaC]`, `[DATE]`. Also intentional and
never "bugs": `[ ]` checklist boxes, `![Warning]`/`![Troubleshooting]` callouts, and
runtime-fill values like `~[X]%`.

**Lockstep rule:** that regex + exclusion list exists in exactly three files —
`.github/workflows/placeholder-audit.yml`, `.claude/skills/azureAI-optimize/analyze.sh`,
and `.claude/skills/preflight/check.sh`. Change all three in one commit, or none.

Run it locally anytime: `bash .claude/skills/preflight/check.sh .`

## 4. The four invariants every instruction file must keep

1. **3-Tier Source Hierarchy** — Tier 1 (official, versioned docs; never override) >
   Tier 2 (best-practice; cross-check Tier 1) > Tier 3 (personal/internal; advisory,
   verified against Tier 1 and marked so).
2. **Mandatory Tutorial Template** — the deterministic output shape:
   `Purpose` → `Validated against` (exact version + date) → `Requirements` → numbered
   atomic `Procedure` steps with `> ✅ **Checkpoint**: [what must now be true]` →
   `Verification`.
3. **Anti-hallucination / version strictness** — refuse when docs are silent
   ("This specific behavior/version combination is not documented in current
   authoritative sources…"); never claim a deprecated feature works in a newer
   version; never infer environment details.
4. **Escalation Protocol** — undocumented/edge cases route to a named contact or
   ticket process, never to a guess.

**Dialects are frozen:** each dialect expresses these invariants in its own headings
and syntax (§2). Tolerate the variation; never tolerate a missing invariant. Do not
restructure an existing example "to match TEMPLATE.md" — that is churn, not a fix.

## 5. Conventions

Observed in the repo — follow them:

- **Header comment block** at the top of each example (`<!--- // Community Resource –
  CGFixIT … -->` or `#`-comments in the coder family): scope, maintainer, target
  platforms, version line.
- **Filenames are frozen**, including the awkward ones (`Network&SecurityAgent.md`
  with its `&`, `veeamGPT.md` casing). New files: kebab-case.
- **Commits**: short imperative subject ("Add X; fix Y"), body only when it earns it,
  `ci:` prefix reserved for CI/dependency bumps. Work lands via a `claude/*` or
  feature branch → draft PR → @cgfixit merges.
- **Typography is per-file**: some files use en-dashes, `•` bullets, emoji callouts;
  others don't. Match the file you're in. Never run a smart-quote/dash/whitespace
  normalizer — cosmetic sweeps bury the safety-relevant diff.
- **LF line endings** (enforced by `.gitattributes`); markdownlint rules MD013/24/33/
  40/41/46 are disabled on purpose for prompt-block formatting.
- **GitHub Actions are tag-pinned and Dependabot-managed** (weekly, `ci:` commits).

Added by this manual — also follow them:

- **Preflight is the exit gate.** Before any commit that touches a `.md` file:
  `bash .claude/skills/preflight/check.sh .` must exit 0.
- **The tree wins.** Before acting on any factual claim in a meta-doc (this file, a
  SKILL.md gotcha, the README), verify it with grep/ls. This repo has shipped stale
  meta-guidance before; when you find a stale claim, fix it in the same PR.
- **One source of truth for guidance.** Skills live in `.claude/skills/<name>/SKILL.md`;
  don't create parallel command files or duplicate instructions across files.
- **Evidence-cited fixes.** When fixing drift, name the authority in the commit body
  (e.g. "tree has cloud-infra.md; README said multi-cloud-infra.md").

## 6. Mistakes a weaker model makes here — and the rule that prevents each

| # | The mistake | The rule |
|---|---|---|
| 1 | Filling placeholders in `TEMPLATE.md` ("completing" it) | TEMPLATE.md placeholders are the product. Never fill them. Only `examples/` get filled. |
| 2 | Leaving `[UPPER_SNAKE]` tokens in an example | Run preflight before committing; C1 is byte-identical to the CI gate that will reject you. |
| 3 | "Fixing" `[Image: …]`, `[ ]`, `![Warning]`, `[DATE]`, `~[X]%` as leftover placeholders | They are structural syntax on the CI exclusion list (§3). Leave them. |
| 4 | "Improving" safety prose — softening "Never/Zero Tolerance", deduplicating repeated warnings, tightening "verbose" rules | Repetition and absolutism are deliberate prompt engineering. Do not rewrite language you weren't asked to change. |
| 5 | Adding MIT headers to files, or assuming repo-wide MIT | License scope lives **only** in the README block: MIT = `TEMPLATE.md`, `cloud-infra.md`, `ps1AgentCoder.md`, `yaragenerator.md`, `incident-response.md`. Everything else (notably `veeamGPT.md`, `pythonAgentCoder.md`, `Network&SecurityAgent.md`) is reference-only. Never add license headers inside files. |
| 6 | Committing a realistic-looking secret in an illustrative snippet | Gitleaks scans **every commit in history** — a leak is permanent and fails CI forever; fixing requires a history rewrite. Only structurally fake values: `your-api-key-here`, `support@example.com`, `<YOUR_TOKEN>`. |
| 7 | Pasting chat-session output into a deliverable, trailer and all | Instruction files must read as system prompts end-to-end. No "Done. Paste this…", "Let me know if…", "Here's the updated…". (This actually happened — `Network&SecurityAgent.md` shipped with a chat trailer until v1.6.) Preflight C4 scans for it. |
| 8 | "Fixing" `veeamGPT.md`'s `#REDACTED` URLs, `PLACHOLDER` typos, `REDACTED@REDACTED.com` | Intentional sanitization of a reference-only file. Do not restore real URLs/emails, and do not imitate the pattern in new files. |
| 9 | Making `markdown-lint.yml` or `link-check.yml` blocking to "enforce quality" | Both are non-blocking **by documented decision** (pre-existing cosmetic baseline; external link rot). Flip only on an explicit user request. |
| 10 | Editing the placeholder regex or exclusion list in one place | Lockstep rule (§3): all three copies in one commit, or none. |
| 11 | Adding/renaming an example without the README updates | The sync triangle (§2): structure list + license block + Version History, same commit. |
| 12 | Restructuring an old example to match TEMPLATE.md's headings | Dialects are frozen (§4). Propagate content in the file's own dialect; never re-skeleton. |
| 13 | Acting on a meta-doc claim without checking | The tree wins (§5). Verify with grep/ls; fix stale claims when found. |
| 14 | Hand-pinning action SHAs, or "upgrading" workflows ad hoc | Dependabot owns action versions (tag-pinned, weekly). SHA-pinning is a known open hardening goal — do it only as a deliberate, owner-approved, repo-wide change. |

## 7. Quality bar per deliverable — checkable criteria

Every item is a command or a yes/no. "Looks good" is not a criterion.

**A. `TEMPLATE.md` edit**
- [ ] `grep -oP '\[[A-Z][A-Z0-9_]{2,}\]' TEMPLATE.md | sort -u | wc -l` ≥ 24 (or the
      delta is a deliberate, stated placeholder-set change)
- [ ] `grep -c '^## ' TEMPLATE.md` = 15, unless a section was deliberately added and
      the PR body says so
- [ ] No domain-specific product names introduced (it must stay generic)
- [ ] **Both** Version Histories bumped: TEMPLATE.md's own and README's
- [ ] Propagation to examples done via `/sync-template`, or explicitly deferred in the
      PR body
- [ ] If a placeholder was added/renamed: README "Customize Placeholders" block +
      TEMPLATE "Customization Instructions" + `check.sh` count comment updated

**B. Example file (new or edited)**
- [ ] Preflight C1 = 0 hits (no unfilled tokens)
- [ ] All core sections present: Purpose/Core Mission, Forbidden Actions, Escalation,
      Security, Source Hierarchy — plus `## Reasoning Protocol (o3-Optimized)` and
      `## Response Modes`
- [ ] Header comment block present (scope, maintainer, platforms)
- [ ] ≥ 2 dated, domain-specific critical constraints
- [ ] A concrete (fake-but-plausible) escalation contact and ticket process ID
- [ ] `tail -n 30` free of conversational phrases (preflight C4)
- [ ] Sync triangle done; license classified (default MIT; vendor-proprietary →
      reference-only; ambiguous → ask)
- [ ] Every claim about a real product is verifiable in that vendor's Tier 1 docs, or
      the products are clearly fictional

**C. `README.md` edit**
- [ ] Every file in `examples/` appears in the Repository Structure list, case-exact
- [ ] Every filename the README mentions exists on disk (preflight C6)
- [ ] License block filenames match disk exactly
- [ ] Version History entry appended in `- **vX.Y** (Mon YYYY): …` format

**D. CI workflow change**
- [ ] `permissions: contents: read` as baseline (elevate per-job only as needed)
- [ ] Workflow `name:` keeps the `CG ` prefix
- [ ] Blocking vs non-blocking is stated in a YAML comment, with the reason
- [ ] If the placeholder regex/exclusions moved: lockstep rule satisfied (§3)

**E. Skill / `.claude` change**
- [ ] Frontmatter `name` matches the directory name; `description` states when to use
- [ ] Every file path referenced in the skill exists (`ls` each)
- [ ] No guidance duplicated between two files
- [ ] Scripts: `set -euo pipefail`, plain bash, read-only unless the skill says
      otherwise, and a seeded-failure negative test was run

## 8. CI reference

| Workflow | Checks | Blocking? |
|---|---|---|
| `placeholder-audit.yml` | Unfilled tokens in `examples/` | **Yes** |
| `gitleaks.yml` | Secrets — **entire git history** (`fetch-depth: 0`) | **Yes** |
| `devskim.yml` | Static security patterns → SARIF | **Yes** |
| `markdown-lint.yml` | Style (`.markdownlint.jsonc`) | No — by documented decision |
| `link-check.yml` | Dead URLs (lychee) | No — by documented decision |

All five run on push/PR to `main`; the security scanners also run weekly. Local
mirror of everything blocking: `bash .claude/skills/preflight/check.sh .`

## 9. When uncertain — exact escalation rules

**Proceed without asking** (reversible, convention-covered):
- Mechanical drift fixes where the tree is authoritative — including filename-*case*
  corrections inside the README license block
- New examples that follow `/new-example` end to end
- Typo/formatting fixes in **non-safety** prose, matching the file's own style
- Adding a *non-blocking* CI check or updating this manual to match verified reality

**Ask @cgfixit first** (one concise question, with options):
- Any change to the **meaning** of safety language in TEMPLATE.md or the invariant
  sections of examples (Forbidden Actions, source tiers, escalation text)
- Adding or removing an **entry** in the README license block for an existing file
- Deleting or renaming any published example
- Flipping any CI check between blocking and non-blocking
- Content edits to `veeamGPT.md` beyond mechanical fixes (reference-only, sanitized)
- Anything requiring a git history rewrite

**Never** (hard stops, no exceptions):
- Force-push `main` or rewrite published history on it
- Commit a string matching a real credential format, even as an invented example
- Delete or hollow out a safety section to "simplify" a file

**Tie-breakers when documents disagree:**
- License scope or placeholder list → README wins
- Canonical structure → TEMPLATE.md wins
- Any factual claim vs. the actual tree → the tree wins
- Chronology → the newest dated Version History entry wins
- Note the disagreement (and your resolution) in the PR body

**Unattended mode** (no user available): take the reversible path; never cross into
the ask-first list; record the open question in the PR body instead of deciding it.

## 10. Toolbox — the skills and when they fire

| Skill | Fires when | Guarantee |
|---|---|---|
| `/preflight` | Before **every** commit touching a `.md` file | Local mirror of all blocking CI gates; exit 0 = CI-safe |
| `/new-example <domain>` | Adding a domain example | Research → scaffold → license → sync triangle → preflight |
| `/sync-template` | After any TEMPLATE.md contract change | Per-dialect propagation to all 7 examples + both version histories + report |
| `/red-team <examples/file.md>` | Before deploying / after major edits to an example | Fixed 35-probe adversarial battery with hard pass gates |
| `/azureAI-optimize` | Periodic whole-repo improvement pass | analyze.sh findings → categorized fixes → preflight |

`preflight` is the exit gate of every other skill. If you remember one rule from this
manual: **run preflight, and never fix its findings by editing the checker.**
