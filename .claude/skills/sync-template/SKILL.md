---
name: sync-template
description: Propagate a TEMPLATE.md change to all examples in each file's own dialect, bump both version histories, and validate. Use after any edit to TEMPLATE.md's shared contract (sections, rules, placeholders), or when asked to bring examples in line with the template.
---

# Sync Template — propagate a TEMPLATE.md change across the library

TEMPLATE.md is the canonical source; the 7 examples are its instantiations. When
the shared contract changes, every example needs the change *in its own dialect* —
this is the multi-hour chore behind release v1.4 ("Added o3 Reasoning Protocol to
TEMPLATE.md and all examples"), systematized.

## Step 1: Capture and classify the delta

```bash
git diff $(git merge-base HEAD origin/main) -- TEMPLATE.md
```

Classify each hunk (a change can be several):

| Class | Meaning | Propagation duty |
|---|---|---|
| **NEW-SECTION** | A section added to the contract (e.g. Reasoning Protocol in v1.4) | Add a domain-adapted equivalent to every example |
| **RULE-CHANGE** | Wording/strength of an existing rule changed | Update the corresponding passage in every example that carries it |
| **PLACEHOLDER-SET** | A `[TOKEN]` added, renamed, or removed | See Step 4 — three extra files must move in lockstep |
| **REMOVAL / WEAKENING** | A rule or section removed, or safety language softened | **STOP.** Confirm with the owner before propagating — removals change the product's safety posture |

## Step 2: The dialect map — how to insert into each file

Dialect variation is frozen (see CLAUDE.md). Propagate *content*, never structure:

| Dialect | Files | Insertion guidance |
|---|---|---|
| TEMPLATE-faithful | `incident-response.md` | Headings mirror TEMPLATE.md — insert in the same relative position with near-identical heading text. |
| Coder/KB family | `ps1AgentCoder.md`, `pythonAgentCoder.md`, `yaragenerator.md` | Rules go in their rules sections (Forbidden Actions, Behavioral Rules, Reasoning Protocol) — never inside "Mandatory Output Templates A/B", which are the agent's *output* formats. `#`-comment header block, "Ground truth / Strong patterns / Advisory" tier names. |
| Narrative-tiered | `cloud-infra.md`, `veeamGPT.md` | Sections are prose-heavy with renamed headings ("Sources to Use With High Authority", "Tutorial Creation Protocol") and `<checkpoint>` syntax instead of `> ✅ **Checkpoint**:`. Insert under the analogous renamed heading; keep their checkpoint syntax. |
| Numbered outlier | `Network&SecurityAgent.md` | Sections are `N. Title` numbered 1-13. Append content *within* the closest existing numbered section — do not renumber 13 headings for one insertion. Tier hierarchy is a table; edit rows, not headings. |

`veeamGPT.md` is reference-only (non-MIT) but **in maintenance scope** — license ≠
maintenance. Propagate to it too; just never "fix" its `#REDACTED`/`PLACHOLDER`
sanitization tokens while you're in there.

## Step 3: Adaptation rules (per example)

1. **Harvest, don't invent.** Domain values for any new placeholder-bearing prose
   come from the example's *own existing text* (its products, versions, tools,
   escalation contacts). A sync must never introduce new domain facts — if an
   example lacks the needed fact, mark that file SKIPPED with a reason rather than
   fabricating.
2. **Never paste template text containing live `[DOMAIN_*]` tokens** into an
   example — instantiate first. (Preflight C1 catches this; don't rely on it.)
3. **Match the file's typography** — en-dash vs hyphen, emoji use, heading case,
   bullet glyphs (`•` vs `-`). The diff should look native to each file.
4. **Additive-first.** Prefer inserting alongside existing content over rewriting
   it; only touch existing sentences when the RULE-CHANGE explicitly demands it.
5. **Record skips.** Any example not updated gets an explicit reason (e.g. "already
   has an equivalent, stricter rule").

## Step 4: PLACEHOLDER-SET changes ripple further

If a `[TOKEN]` was added, renamed, or removed in TEMPLATE.md, the same commit must
also update:

1. `README.md` "Customize Placeholders" block (the authoritative token list),
2. TEMPLATE.md's own "Customization Instructions for Your Organization" section,
3. `.claude/skills/preflight/check.sh` C2 expected-count comment (and the three
   lockstep locations if the *exclusion list* changed — see CLAUDE.md).

## Step 5: Bump BOTH version histories

- TEMPLATE.md `## Version History`: add the next `- **vX.Y** (Mon YYYY): …` entry.
- README.md `## Version History`: add the matching entry, modeled on v1.4's
  ("Added X to TEMPLATE.md and all examples; …").
These two histories have drifted before (TEMPLATE stalled at v1.2 while README
reached v1.5) — a sync is the moment to keep them moving together.

## Step 6: Propagation report

Put this table in the commit body or PR description:

```
| File | Change applied | Status |
|---|---|---|
| incident-response.md | <what> | applied |
| cloud-infra.md | <what, adapted how> | adapted |
| veeamGPT.md | — | SKIPPED: <reason> |
| ... | | |
```

Every one of the 7 examples appears — "applied", "adapted", or "SKIPPED: reason".
No silent omissions.

## Step 7: Validate

Run `/preflight` and get exit 0. C1 catches leaked `[DOMAIN_*]` tokens, C3 catches
a propagation that accidentally deleted an invariant section, C6 catches a missed
README update.
