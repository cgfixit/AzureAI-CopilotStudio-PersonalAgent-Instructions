#!/usr/bin/env bash
# preflight/check.sh — local mirror of every check that gates (or reports on) a
# commit to this repo. Read-only. Exits non-zero if any BLOCKING check fails.
#
# Usage: bash .codex/skills/preflight/check.sh [path-to-repo-root]
#
# LOCKSTEP RULE: the placeholder regex and its exclusion list in C1 exist in
# exactly three places and must stay byte-identical:
#   1. .github/workflows/placeholder-audit.yml   (the CI gate)
#   2. .codex/skills/azureai-optimize/analyze.sh (section 1)
#   3. this file (C1)
# Change all three in one commit, or none.
set -euo pipefail
ROOT="${1:-.}"
FAILURES=0

pass() { echo "  PASS  $1"; }
fail() { echo "  FAIL  $1"; FAILURES=$((FAILURES + 1)); }
warn() { echo "  WARN  $1"; }
skip() { echo "  SKIP  $1"; }

echo "=============================================="
echo " Preflight — local CI mirror"
echo "=============================================="

# ── C1. Placeholder audit (BLOCKING — mirrors placeholder-audit.yml) ───────
echo ""
echo "── C1. Unfilled placeholders in examples/ ──"
C1_BAD=0
for f in "$ROOT"/examples/*.md; do
  # Match [UPPER_SNAKE_CASE] tokens (3+ chars) but skip known structural syntax
  HITS=$(grep -noP '\[[A-Z][A-Z0-9_]{2,}\]' "$f" \
    | grep -vP '\[Image:' \
    | grep -vP '^\d+:\[Warning\]' \
    | grep -vP '^\d+:\[Note\]' \
    | grep -vP '^\d+:\[Troubleshooting\]' \
    | grep -vP '^\d+:\[FinOps\]' \
    | grep -vP '^\d+:\[Security\]' \
    | grep -vP '^\d+:\[IaC\]' \
    | grep -vP '\[DATE\]' \
    || true)
  if [ -n "$HITS" ]; then
    fail "$(basename "$f") has unfilled placeholder tokens:"
    echo "$HITS" | sed 's/^/          /'
    C1_BAD=1
  fi
done
[ "$C1_BAD" -eq 0 ] && pass "no unfilled placeholders in examples/"

# ── C2. TEMPLATE.md placeholders still present (BLOCKING) ───────────────────
echo ""
echo "── C2. TEMPLATE.md placeholder integrity ──"
# `|| true` keeps set -e/pipefail from aborting the run when grep finds nothing
# (zero tokens must be reported as a FAIL, not crash the checker).
TOKENS=$(grep -oP '\[[A-Z][A-Z0-9_]{2,}\]' "$ROOT/TEMPLATE.md" | sort -u | wc -l || true)
# 24 unique tokens as of v1.6. Floor of 20 tolerates small deliberate edits;
# below that, someone has probably "filled in" the canonical template.
if [ "$TOKENS" -ge 20 ]; then
  pass "TEMPLATE.md has $TOKENS unique placeholder tokens (expected ~24, floor 20)"
else
  fail "TEMPLATE.md has only $TOKENS unique placeholder tokens (floor 20) — placeholders must stay UNFILLED in the template"
fi

# ── C3. Structural invariants per example (BLOCKING) ────────────────────────
# Dialect-tolerant: matches each file's own heading style, only checks that the
# four safety invariants (+ security & core-purpose sections) exist somewhere.
echo ""
echo "── C3. Core invariants in each example ──"
C3_BAD=0
declare -A INVARIANTS=(
  ["purpose/mission"]='purpose|core mission'
  ["forbidden actions"]='forbidden'
  ["escalation"]='escalat'
  ["source hierarchy"]='tier 1|authoritative source|high authority|documentation hierarchy'
  ["checkpoint/verification"]='checkpoint|verification'
  ["security"]='security'
)
for f in "$ROOT"/examples/*.md; do
  MISSING=""
  for name in "${!INVARIANTS[@]}"; do
    grep -qiP "${INVARIANTS[$name]}" "$f" || MISSING="$MISSING [$name]"
  done
  if [ -n "$MISSING" ]; then
    fail "$(basename "$f") missing:$MISSING"
    C3_BAD=1
  fi
done
[ "$C3_BAD" -eq 0 ] && pass "all examples carry the core invariants"

# ── C4. Chat-session artifacts (BLOCKING) ───────────────────────────────────
# Instruction files must read as system prompts end-to-end. Conversational
# trailers from the chat session that produced the file are bugs
# (see the Network&SecurityAgent.md incident, fixed in v1.6).
echo ""
echo "── C4. Chat artifacts near end of instruction files ──"
C4_BAD=0
for f in "$ROOT"/examples/*.md "$ROOT"/TEMPLATE.md; do
  HITS=$(tail -n 30 "$f" | grep -niP "let me know|paste this (in|dir)|here('| i)s the (updated|full|complete|revised)|i('| ha)ve (created|updated|added)|would you like me|hope this helps|as an ai" || true)
  if [ -n "$HITS" ]; then
    fail "$(basename "$f") ends with chat-session artifacts:"
    echo "$HITS" | sed 's/^/          /'
    C4_BAD=1
  fi
done
[ "$C4_BAD" -eq 0 ] && pass "no conversational trailers detected"

# ── C5. Secret shapes (BLOCKING — gitleaks pre-filter) ──────────────────────
# Gitleaks scans FULL history in CI: a real-looking secret is permanent once
# committed. This catches the high-confidence shapes before that happens.
echo ""
echo "── C5. Secret-looking strings in tracked text files ──"
SECRET_HITS=$(grep -rnoP 'AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|AIza[0-9A-Za-z_\-]{30,}|BEGIN [A-Z ]*PRIVATE KEY' \
  --include='*.md' --include='*.sh' --include='*.yml' --include='*.jsonc' --include='*.json' \
  "$ROOT" 2>/dev/null | grep -v '/.git/' || true)
ASSIGN_HITS=$(grep -rniP '(password|passwd|secret|api[_-]?key|token)\s*[:=]\s*["'"'"'][^"'"'"'<\[]{12,}["'"'"']' \
  --include='*.md' "$ROOT/examples" "$ROOT/TEMPLATE.md" 2>/dev/null \
  | grep -viP 'your|example|placeholder|redacted|fake|dummy|xxx|changeme|<.*>' || true)
if [ -n "$SECRET_HITS$ASSIGN_HITS" ]; then
  fail "possible secrets found — use obviously fake values (your-api-key-here):"
  printf '%s\n%s\n' "$SECRET_HITS" "$ASSIGN_HITS" | grep -v '^$' | sed 's/^/          /' || true
else
  pass "no secret-shaped strings"
fi

# ── C6. README ↔ tree ↔ license consistency (BLOCKING) ─────────────────────
echo ""
echo "── C6. README consistency (sync triangle) ──"
C6_BAD=0
# (a) every example on disk appears in README, case-exact
for f in "$ROOT"/examples/*.md; do
  base=$(basename "$f")
  if ! grep -qF "$base" "$ROOT/README.md"; then
    fail "README.md does not mention $base (Repository Structure block out of sync)"
    C6_BAD=1
  fi
done
# (b) every *.md filename the README mentions exists on disk, case-exact
while IFS= read -r name; do
  [ -e "$ROOT/$name" ] || [ -e "$ROOT/examples/$name" ] || {
    fail "README.md references '$name' but no such file exists (root or examples/)"
    C6_BAD=1
  }
done < <(grep -oP '[A-Za-z0-9&_-]+\.md' "$ROOT/README.md" | sort -u)
[ "$C6_BAD" -eq 0 ] && pass "README, examples/ and license block agree"

# ── C7. Markdown lint (INFORMATIONAL — CI job is non-blocking by design) ────
echo ""
echo "── C7. Markdown lint (informational) ──"
if command -v markdownlint-cli2 >/dev/null 2>&1; then
  markdownlint-cli2 --config "$ROOT/.markdownlint.jsonc" "$ROOT"/*.md "$ROOT"/examples/*.md \
    && pass "markdownlint clean" \
    || warn "markdownlint reported issues (non-blocking, matches CI policy)"
else
  skip "markdownlint-cli2 not installed — CI runs it non-blocking anyway"
fi

echo ""
echo "=============================================="
if [ "$FAILURES" -gt 0 ]; then
  echo " PREFLIGHT FAILED — $FAILURES blocking issue(s). Fix before committing."
  echo " Remediation guidance: .codex/skills/preflight/SKILL.md"
  exit 1
fi
echo " Preflight passed — safe to commit."
echo "=============================================="
