---
name: sol-optimize
description: Audit and minimally optimize one or all examples/*.md instruction files for GPT-5.6 Sol while preserving domain safety, source hierarchy, version strictness, escalation, and output contracts. Use when migrating o3-focused examples to Sol, replacing o3-specific reasoning scaffolding, or reviewing example prompts against current GPT-5.6 prompting guidance.
---

# Sol Optimize

Optimize deployable examples only. Do not edit `TEMPLATE.md`, CI, or unrelated repo
surfaces unless the user explicitly expands scope.

## Workflow

1. Establish scope.
   - If the user names an `examples/*.md` file, target only that file.
   - Otherwise inventory every example and select the smallest coherent set with a
     concrete Sol-specific problem.
   - Run `python .codex/scripts/repo_audit.py analyze .` before editing.
   - Treat its o3 guidance result as baseline hygiene, not proof of Sol readiness.
2. Refresh current model guidance.
   - Use `$openai-docs` to fetch the live GPT-5.6 model guidance and its
     `Prompting best practices` section.
   - If that skill is unavailable, use only
     `https://developers.openai.com/api/docs/guides/model-guidance?model=gpt-5.6`.
   - Treat live OpenAI documentation as canonical. Do not hardcode pricing, limits,
     availability, or optional feature behavior in example prompts.
3. Audit each target against the Sol rubric below.
4. Make the smallest behavior-preserving edit in the file's existing dialect.
5. Validate every changed example and report measured versus wording-only results.

## Sol Rubric

Preserve domain facts and every safety invariant: authoritative-source hierarchy,
version strictness, forbidden actions, escalation, security/privacy, connected-tool
scope, checkpoints, and required output formats.

Prefer:

- lean, outcome-oriented instructions that state each rule once;
- explicit goals, context, hard constraints, required evidence, success criteria,
  stopping conditions, and output format;
- one clear autonomy and approval policy that permits safe in-scope work and stops
  before external, destructive, costly, or scope-expanding actions;
- targeted clarification only when ambiguity materially changes correctness or safety;
- concise, precise descriptions for tools that are actually available;
- observable verification before claiming completion.

Remove or tighten only when redundant or harmful:

- o3-specific labels or long internal reasoning checklists;
- repeated safety, approval, style, or tool-routing instructions;
- generic brevity rules that omit required evidence or caveats;
- examples that duplicate a rule without encoding a domain requirement or measured fix.

Never request hidden chain-of-thought, tell Sol to "think harder," or expose private
reasoning. Do not add `max`, Pro, ultra, multi-agent, Programmatic Tool Calling,
persisted reasoning, caching, or API parameters to prompt files unless the user asks
and the deployment supports them. Model execution settings belong in deployment
configuration, not these instruction examples.

## Validation

1. Run `python .codex/scripts/repo_audit.py preflight .`.
2. Apply `$red-team` to every materially changed example.
3. When a GPT-5.6 Sol deployment is available, compare representative tasks using
   the existing reasoning effort, then one level lower. Measure correctness, evidence,
   unnecessary escalation, tool behavior, format compliance, tokens, latency, and cost.
4. Without a live deployment, label the result as a wording-only optimization. Do not
   claim measured model improvement.

## Report

Return targeted files, changes made, intentionally unchanged rules, validation evidence,
and deployment-eval gaps. Keep unrelated examples and `TEMPLATE.md` unchanged.
