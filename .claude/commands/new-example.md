---
description: Scaffold a new domain-specific agent instruction file in examples/ from TEMPLATE.md
argument-hint: <domain-name> (e.g. "kubernetes-ops", "tax-compliance")
---

Create a new fully-instantiated agent instruction example for the domain: **$ARGUMENTS**

Steps:
1. Read `TEMPLATE.md` to get the canonical structure.
2. Create `examples/<domain>.md` using that exact skeleton — keep all section headings (Purpose & Core Mission, Response Rules, Tool & Data Access, Mandatory Tutorial Template, Forbidden Actions, Authoritative Source Hierarchy, Formatting & Validation, Security & Privacy, Escalation Protocol, Response Quality Checklist).
3. Replace **every** `[UPPER_SNAKE_CASE]` placeholder with concrete, domain-appropriate values. Do not leave any unfilled bracket tokens. (Leave intentional structural syntax intact: `[Image: ...]`, `[ ]` checkboxes, `![Warning]`, `![Troubleshooting]`.)
4. Write at least two domain-specific `[CRITICAL_CONSTRAINT_*]` rules and a realistic escalation contact/ticket process.
5. Update `README.md`: add the new file to the Repository Structure list and, if MIT-covered, to the LICENSE scope block. Add a Version History entry.
6. Do NOT add anything resembling a real secret, key, or token — Gitleaks scans every commit.
