---
name: preflight
description: Run the local CI mirror (placeholder audit, secret scan, structural invariants, chat-artifact scan, README sync check) before any commit that touches a Markdown file. Use when asked to validate/check the repo, and as the mandatory final step of /new-example and /sync-template.
---

# Preflight — local CI mirror

Every blocking CI gate in this repo, runnable locally in seconds. **Run this before
every commit that touches a `.md` file.** A commit that fails preflight will fail CI;
worse, a secret that reaches history is permanent (Gitleaks scans every commit ever
made, so "fixed in the next commit" does not un-fail CI).

## Step 1: Run the checker

```bash
bash .claude/skills/preflight/check.sh .
```

Exit 0 = safe to commit. Exit 1 = fix the listed FAILs first. WARN/SKIP lines are
informational and mirror the checks CI deliberately runs as non-blocking.

## Step 2: Fix failures — check ID → rule → remediation

| Check | Rule it enforces (CLAUDE.md) | How to fix |
|---|---|---|
| **C1** unfilled placeholder in an example | "No leftover `[UPPER_SNAKE_CASE]` tokens in `examples/`" | Replace the token with a concrete, domain-appropriate value. If it's genuinely structural syntax, see *Forbidden remediations* below before touching the exclusion list. |
| **C2** TEMPLATE.md token count below floor | "TEMPLATE.md placeholders must remain unfilled — it is the generic source" | Restore the filled-in tokens from `git diff TEMPLATE.md`. If you deliberately removed placeholders as part of an approved template change, update the expected count comment in `check.sh` in the same commit and say so in the PR body. |
| **C3** missing core invariant | "Dialect variation is tolerated; invariant omission is not" | Add the missing section in *that file's own dialect* (see the dialect map in CLAUDE.md). Copy the shape from `TEMPLATE.md` or `examples/incident-response.md`, then adapt wording to the file's style. |
| **C4** chat artifact near end of file | "Instruction files must read as system prompts end-to-end" | Delete the conversational sentence(s). They are output from the chat session that produced the file, not part of the deliverable. |
| **C5** secret-shaped string | "Never commit anything that looks like a real secret — Gitleaks scans full history" | Replace with an obviously fake value (`your-api-key-here`, `support@example.com`, `<YOUR_TOKEN>`). Never use realistic formats, even invented ones. |
| **C6** README out of sync | "The sync triangle: examples/ ↔ Repository Structure ↔ license block ↔ Version History, same commit" | Add/correct the README entry (case-exact filenames). If README references a file that doesn't exist, determine which side is wrong before editing — see *Forbidden remediations*. |
| **C7** markdownlint issues | CI runs this non-blocking by documented decision | Optional cleanup. Do not make the CI job blocking to "enforce" it. |

## Forbidden remediations

These make the symptom disappear while making the repo worse. Never do them:

1. **Never extend the C1 exclusion list to silence a hit.** The exclusion list
   exists in exactly three lockstep locations (`placeholder-audit.yml`,
   `analyze.sh`, `check.sh`). It grows only when a *new intentional structural
   syntax* is introduced deliberately — and then in all three files in one commit,
   with the addition called out in the PR body.
2. **Never edit `check.sh` to get a failing tree to pass.** The checker models CI;
   changing the model doesn't change CI. (Exception: a deliberate, stated change
   to the contract itself, applied under the lockstep rule.)
3. **Never delete a README entry just because C6 flagged it.** First check which
   side is wrong: the tree is the source of truth for *what exists*; the README is
   the source of truth for *license scope*. A missing file usually means the README
   gained a typo (fix the README) — but it can also mean a file was renamed without
   the sync triangle (fix may be restoring the name).
4. **Never "fix" `veeamGPT.md`'s `#REDACTED` / `PLACHOLDER` / `REDACTED@REDACTED.com`
   tokens.** They are intentional sanitization of a reference-only file and are
   invisible to C1 by design.

## Step 3: What the script cannot check — verify by hand

- **License classification is correct** — a new example referencing proprietary
  vendor products belongs in the reference-only set, not the MIT list. README
  license block is the single authority.
- **Factual claims are real** — versions, deprecation dates, CVE-style claims in
  examples must be verifiable against the vendor's Tier 1 docs, or the products
  must be clearly fictional. The scanner can't tell a hallucinated version from a
  real one.
- **Safety language is intact** — diff the file and confirm no "Never/Zero
  Tolerance/must" phrasing got softened as a side effect of your edit.
- **Tone matches the file's dialect** — heading style, en-dash vs hyphen, emoji
  callouts should match the file you edited, not your habits.

## Relationship to CI and the other skills

| This check | CI equivalent | Blocking in CI? |
|---|---|---|
| C1 | `placeholder-audit.yml` | Yes |
| C5 | `gitleaks.yml` (full history) | Yes |
| C7 | `markdown-lint.yml` | No (by documented decision) |
| — | `devskim.yml`, `link-check.yml` | Yes / No — no local mirror; low false-positive risk for prose |

`/new-example` and `/sync-template` both end by running this skill. If you are
about to commit and haven't run it, run it.
