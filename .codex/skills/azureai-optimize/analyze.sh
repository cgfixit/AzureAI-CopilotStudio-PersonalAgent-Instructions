#!/usr/bin/env bash
# Analyze the repo and report optimization opportunities.
# Usage: bash .codex/skills/azureai-optimize/analyze.sh [path-to-repo-root]
set -euo pipefail
ROOT="${1:-.}"

echo "=============================================="
echo " AzureAI Optimize — Repository Analysis"
echo "=============================================="
echo ""

# ── 1. Placeholder scan (examples only) ──────────────────────────
echo "── 1. Unfilled placeholders in examples/ ──"
found_placeholders=0
for f in "$ROOT"/examples/*.md; do
  # Match [UPPER_SNAKE_CASE] but skip known structural syntax
  hits=$(grep -noP '\[[A-Z][A-Z0-9_]{2,}\]' "$f" \
    | grep -vP '\[Image:' \
    | grep -vP '^\d+:\[Warning\]' \
    | grep -vP '^\d+:\[Note\]' \
    | grep -vP '^\d+:\[Troubleshooting\]' \
    | grep -vP '^\d+:\[FinOps\]' \
    | grep -vP '^\d+:\[Security\]' \
    | grep -vP '^\d+:\[IaC\]' \
    | grep -vP '\[DATE\]' \
    || true)
  if [ -n "$hits" ]; then
    echo "  WARN  $(basename "$f"):"
    echo "$hits" | sed 's/^/         /'
    found_placeholders=1
  fi
done
[ "$found_placeholders" -eq 0 ] && echo "  OK    No leftover placeholders found."
echo ""

# ── 2. Structural completeness ────────────────────────────────────
echo "── 2. Core section presence in each example ──"
required_sections=(
  "Purpose"
  "Core Mission"
  "Forbidden Actions"
  "Escalation"
  "Security"
  "Source Hierarchy|Authoritative Source|Tier 1|Documentation Hierarchy"
)
for f in "$ROOT"/examples/*.md; do
  missing=""
  for section in "${required_sections[@]}"; do
    if ! grep -qiP "$section" "$f"; then
      missing="$missing  $section"
    fi
  done
  if [ -n "$missing" ]; then
    echo "  WARN  $(basename "$f") missing sections:$missing"
  else
    echo "  OK    $(basename "$f")"
  fi
done
echo ""

# ── 3. Azure AI o3 reasoning protocol ────────────────────────────
echo "── 3. Azure AI o3 / reasoning-model optimization ──"
for f in "$ROOT"/examples/*.md "$ROOT"/TEMPLATE.md; do
  has_reasoning=0
  grep -qiP 'reasoning protocol|o3|chain.of.thought|think step' "$f" && has_reasoning=1
  if [ "$has_reasoning" -eq 1 ]; then
    echo "  OK    $(basename "$f") — has reasoning/o3 guidance"
  else
    echo "  ENHANCE  $(basename "$f") — no o3 reasoning protocol found"
  fi
done
echo ""

# ── 4. README consistency ─────────────────────────────────────────
echo "── 4. README ↔ examples/ consistency ──"
for f in "$ROOT"/examples/*.md; do
  base=$(basename "$f")
  if ! grep -q "$base" "$ROOT/README.md"; then
    echo "  WARN  $base not listed in README.md"
  fi
done
# Check for names in README that don't match actual files
echo "  (Manual check: verify README license scope block filenames match actual files)"
echo ""

# ── 5. CI workflow inventory ──────────────────────────────────────
echo "── 5. CI workflows ──"
for wf in "$ROOT"/.github/workflows/*.yml; do
  name=$(grep -m1 '^name:' "$wf" | sed 's/^name: *//')
  echo "  EXISTS  $(basename "$wf")  →  $name"
done
echo ""
echo "  Candidate additions:"
candidates=0
[ ! -f "$ROOT/.github/workflows/markdown-lint.yml" ] && echo "    - markdown-lint.yml (markdownlint-cli2 for prose quality)" && candidates=1
[ ! -f "$ROOT/.github/workflows/link-check.yml" ] && echo "    - link-check.yml (lychee or markdown-link-check for dead URLs)" && candidates=1
[ ! -f "$ROOT/.github/workflows/placeholder-audit.yml" ] && echo "    - placeholder-audit.yml (automated [PLACEHOLDER] scan on PRs)" && candidates=1
[ "$candidates" -eq 0 ] && echo "    (all recommended workflows already exist)"
echo ""

# ── 6. Security hardening check ───────────────────────────────────
echo "── 6. Security hardening ──"
# Check for pinned action versions (SHA vs tag)
unpinned=0
for wf in "$ROOT"/.github/workflows/*.yml; do
  if grep -P 'uses:\s+\S+@v\d' "$wf" | grep -vP '@[a-f0-9]{40}' > /dev/null 2>&1; then
    echo "  HARDEN  $(basename "$wf") — actions pinned to tags, not SHAs"
    unpinned=1
  fi
done
[ "$unpinned" -eq 0 ] && echo "  OK    All actions pinned to commit SHAs"

# Check for CODEOWNERS
if [ -f "$ROOT/.github/CODEOWNERS" ] || [ -f "$ROOT/CODEOWNERS" ]; then
  echo "  OK    CODEOWNERS file exists"
else
  echo "  ADD   No CODEOWNERS file — consider adding for review gating"
fi

# Check for branch protection recommendation
echo "  CHECK Verify branch protection is enabled on 'main' (manual)"
echo ""

# ── 7. Domain coverage ───────────────────────────────────────────
echo "── 7. Domain example coverage ──"
echo "  Existing domains:"
for f in "$ROOT"/examples/*.md; do
  echo "    - $(basename "$f" .md)"
done
echo ""
echo "  Suggested new domains (per README contributing guidance):"
for domain in "healthcare / clinical-protocols" "legal / compliance" "finance / finops" "manufacturing / iot"; do
  slug=$(echo "$domain" | sed 's/ \/ /-/' | tr ' ' '-')
  if ls "$ROOT"/examples/*"${domain##* / }"* >/dev/null 2>&1 || ls "$ROOT"/examples/*"$slug"* >/dev/null 2>&1; then
    echo "    - $domain (covered)"
  else
    echo "    - $domain"
  fi
done
echo ""

echo "=============================================="
echo " Analysis complete. Run \$azureai-optimize to"
echo " act on these findings."
echo "=============================================="
