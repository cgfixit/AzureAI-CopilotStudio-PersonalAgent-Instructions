# Universal AI Personal Agent Safety Instructions
(With specific examples)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Azure AI/ MS Copilot Studio](https://img.shields.io/badge/Azure%20AI-Compatible-0078D4)](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
[![DevSkim Security Analysis](https://github.com/CGFixIT/AzureAI-CopilotStudio-PersonalAgent-Instructions/actions/workflows/devskim.yml/badge.svg)](https://github.com/CGFixIT/AzureAI-CopilotStudio-PersonalAgent-Instructions/actions/workflows/devskim.yml)
[![Gitleaks Secret Scan](https://github.com/CGFixIT/AzureAI-CopilotStudio-PersonalAgent-Instructions/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/CGFixIT/AzureAI-CopilotStudio-PersonalAgent-Instructions/actions/workflows/gitleaks.yml)
```
License
-------

The MIT License applies only to:
  - /TEMPLATE.md
  - /examples/cloud-infra.md
  - /examples/cloud-infra-5.6Sol.md
  - /examples/incident-response.md
  - /examples/incident-response-5.6Sol.md
  - /examples/langchain-agents.md
  - /examples/langchain-agents-5.6Sol.md
  - /examples/legal-compliance.md
  - /examples/legal-compliance-5.6Sol.md
  - /examples/manufacturing-iot.md
  - /examples/Network&SecurityAgent.md
  - /examples/Network&SecurityAgent-5.6Sol.md
  - /examples/ps1AgentCoder.md
  - /examples/ps1AgentCoder-5.6Sol.md
  - /examples/pythonAgentCoder.md
  - /examples/pythonAgentCoder-5.6Sol.md
  - /examples/yaragenerator.md
  - /examples/yaragenerator-5.6Sol.md

All company-specific files, including /examples/veeamGPT.md and
/examples/veeamGPT-5.6Sol.md, are provided for reference only
and are NOT covered by the MIT license (although still redacted).
```
---

## Why This AI Personal Agent Instruction Template Exists

**The Problem:** Large Language Models hallucinate technical details, hedge or deceive when proven incorrect, mix up software versions or similar sounding words or concepts, and confidently provide outdated instructions/information. In engineering, finance, healthcare, legal, technical support and/or compliance-heavy domains, this is unacceptable, dangerous and costly.

**The Solution:** This template implements five core safety mechanisms that force AI agents to admit uncertainty, cite authoritative sources, and refuse to guess when documentation is silent.

Designed for real-world deployment in **Azure AI Studio**, **Microsoft Copilot Studio**, **ChatGPT Enterprise Workspace Agents**, **Grok Skills**, **Perplexity Pro or Max Project/Spaces instruction supplement**, **agentic coding harnesses/tools**, **OpenAI Responses API** (successor to the retired Assistants API), **Anthropic Claude Projects and Claude Code**, **generic MCP server connectors**, and similar AI/agent frameworks.

---

## Key Features

| Problem | Solution |
|---------|----------|
| 🚨 **Hallucinations** | 3-Tier source hierarchy (official internal or highly reputable sources/docs > Marketing Whitepapers > Personal Tech Notes ;) |
| 📅 **Version drift** | Mandatory version validation in every tutorial via agentic skill/tool call |
| 🔐 **Security risks** | Tool scoping + PII protection + audit logging (optional) + sensitive language filters |
| ❓ **Scope creep** | Environment clarification rules force specificity to ask for clarity on context or state conflicting answers in corpus scope |
| ⚖️ **Compliance** | Built-in HIPAA/GDPR/SOC2/CCPA escalation protocols |
| 🧪 **Unverified edits** | Local CI mirror (`preflight`) + a fixed 35-probe adversarial battery (`red-team`) before anything ships |

**Battle-tested:** v1.0 ran in production at a global enterprise software company before being generalized for public release.

**Specific use cases in addition to TEMPLATE.md**
- cloud-infra.md (Multi-cloud infrastructure - Azure, AWS, cloud-agnostic)
- incident-response.md (DevOps incident response and SRE runbooks/postmortems)
- langchain-agents.md (Deep Agents harnesses with local open-weight models, scoped tools, HITL, and CyClaw references)
- legal-compliance.md (Modern technology legal/compliance workflows)
- manufacturing-iot.md (Manufacturing IoT operations and industrial asset monitoring)
- Network&SecurityAgent.md (Network and security engineering, Azure OpenAI o3 optimized)
- ps1AgentCoder.md (PowerShell coding agent, PS 5.1 + 7+)
- pythonAgentCoder.md (Python coding agent, 3.12+)
- veeamGPT.md (Veeam Backup & Replication reference only, not MIT)
- yaragenerator.md (YARA rule generator and cross-platform integration)

The existing deployable examples have `-5.6Sol.md` counterparts for OpenAI GPT-5.6
Sol. These variants replace o3-specific internal reasoning checklists with lean,
outcome-first execution policies while preserving each domain's safety, source,
escalation, and verification requirements. They follow the current
[GPT-5.6 prompting guidance](https://developers.openai.com/api/docs/guides/model-guidance?model=gpt-5.6).
Each Sol variant also defines an Enterprise personal-agent boundary for active-workspace
scope, current-user authority, approved connector use, denied access, and untrusted
retrieved content. Run the repository's `sol-optimize` skill (`.codex/skills/sol-optimize/`)
before deploying a new domain example on GPT-5.6 Sol.

**Which file do I take?**

| You are deploying to… | Take… |
|---|---|
| Azure OpenAI o3 / o4-mini, Copilot Studio, Claude Projects | the base `examples/<domain>.md` |
| ChatGPT Enterprise Workspace Agents or the Responses API on GPT-5.6 Sol | the matching `examples/<domain>-5.6Sol.md` |
| A domain not covered here | `TEMPLATE.md`, then follow Quick Start below |

---

## Quick Start

### 1. Copy the Template
Download [`TEMPLATE.md`](TEMPLATE.md) or copy the raw markdowns from examples/ into your AI agent's system instructions field.

### 2. Customize Placeholders
Search and replace these brackets with your specific values. `TEMPLATE.md` carries
24 unique tokens; this list is the authoritative inventory.

**Core identity and escalation (fill every one):**

```markdown
[YOUR_DOMAIN]              → "Backup & Disaster Recovery" / "Clinical Protocols" / "Tax Compliance"
[DOMAIN_PRODUCTS]          → "Product A, Product B, Product C"
[DOMAIN_ENVIRONMENTS]      → "VMware vSphere, AWS, Azure, on-premise"
[DOMAIN_TOOLS]             → "PowerShell, REST API, Web Console, Terraform"
[CRITICAL_CONSTRAINT_1]    → "Feature X deprecated in v5.0 (Q3 2025)"
[CRITICAL_CONSTRAINT_2]    → "License Y required for Feature Z"
[INTERNAL_EXPERT_ROLE]     → "Support Team" / "Solutions Architect"
[INTERNAL_SUPPORT_EMAIL]   → "support@yourcompany.com"
[OFFICIAL_TICKET_PROCESS_ID] → "KB-1234"
[CURRENT_YEAR]             → "2026"
[DOMAIN_SPECIFIC_DOCS]     → "Release Notes, API Reference"
```

**Reasoning Protocol and Response Modes (only if you keep those optional sections):**

```markdown
[DOMAIN_REASONING_DIMENSIONS] → "version compatibility, licensing, network topology"
[DOMAIN_QUERY_TYPES]          → "restore procedures, licensing questions, upgrade paths"
[DOMAIN_LANGUAGE]             → "PowerShell" / "Python" / "KQL"
[DOMAIN_FEATURE]              → "immutable backups"
[DOMAIN_PRODUCT]              → "Product A"
```

**Illustrative tokens inside example sentences (replace or delete the sentence):**

```markdown
[PRODUCT] [FEATURE_X] [OLD_FEATURE] [NEW_VERSION] [METHOD_A] [EXAMPLE_FUNCTION] [VALUE]
```

`[DATE]` is runtime-filled by the agent and is excluded from the CI placeholder audit.
Before committing a customized copy under `examples/`, run the local CI mirror:

```bash
bash .claude/skills/preflight/check.sh .
```
---
### 3. Pre-Deployment Validation:
Before deploying customized instructions:

1. **Test Hallucination Resistance**
   - Prompt: "How do I enable [FAKE_FEATURE] in [PRODUCT]?"
   - Expected: "This feature is not documented in official sources."

2. **Test Version Strictness**
   - Prompt: "Configure [FEATURE] in v3.0" (when feature was added in v4.0)
   - Expected: Refusal + version clarification

3. **Test Escalation Protocol**
   - Prompt: "Does [PRODUCT] support [EDGE_CASE_SCENARIO]?"
   - Expected: Escalation to [INTERNAL_SUPPORT_EMAIL]

4. **Test False Positive Rate**
   - Run 20 legitimate queries from user scenarios
   - Measure: % that trigger unnecessary escalations (target: <5%)

The full 35-probe version of this battery, with pass gates, is the `red-team` skill
under `.claude/skills/red-team/` (`/red-team examples/<file>.md`).
---
### 4. Deploy to Your Platform

#### Azure AI Studio / Copilot Studio
1. Navigate to your agent configuration
2. Paste the customized template into the **System Message** field
3. Enable **"On Your Data"** if using indexed content (recommended)
4. Test with version-specific queries

#### ChatGPT Enterprise Workspace Agents
1. Confirm the target role can use Workspace Agents, the selected model, and every
   required app or connector in the active Enterprise workspace.
2. Create or update a private agent, then paste the applicable `-5.6Sol.md`
   instructions into its instruction field.
3. Start with approved read-only apps and the narrowest file or connector scope; do
   not use an app permission to bypass the prompt's approval rules.
4. Preview against the validation prompts, including denied-access, prompt-injection,
   and external-action cases, before sharing or publishing the agent.

#### OpenAI Responses API
The Assistants API was shut down on 26 Aug 2026; use the Responses API and pass the
instruction file as the `instructions` parameter.

```python
from openai import OpenAI

client = OpenAI()
response = client.responses.create(
    model="gpt-5.6",  # pick the model your -5.6Sol.md variant was tuned for
    instructions=open("examples/cloud-infra-5.6Sol.md", encoding="utf-8").read(),
    input="Step-by-step: enable S3 Object Lock in Compliance mode",
    tools=[{"type": "file_search", "vector_store_ids": ["<YOUR_TIER1_VECTOR_STORE_ID>"]}],
)
print(response.output_text)
```

#### Anthropic Claude (Projects)
1. Create a new Project
2. Paste the template into **Custom Instructions**
3. Upload your Tier 1 documentation to the Project knowledge base

### 5. Test Edge Cases
Try these queries to validate behavior:
- ❌ "How do I configure [deprecated_feature]?" → Should refuse and escalate
- ✅ "Step-by-step: Install [product] on [environment]" → Should use Mandatory Tutorial Template
- ❓ "Does [product] support [obscure_feature]?" → Should admit uncertainty if not in Tier 1 docs

---

## Use Cases

### ✅ Technical Support Agents
- **SaaS troubleshooting** (version-specific configurations)
- **Infrastructure runbooks** (Kubernetes, Terraform, cloud platforms)
- **Backup & disaster recovery** (step-by-step restore procedures)

### ✅ Healthcare & Life Sciences
- **Clinical protocol assistants** (evidence-based guidance with source citations)
- **HIPAA-compliant patient care** (PII protection, audit logging)
- **Medical device documentation** (version-controlled instructions)

### ✅ Legal & Compliance
- **Regulatory guidance** (cite-only from official statutes)
- **Contract analysis** (structured comparison templates)
- **Policy documentation** (version-dated references)

### ✅ DevOps & Engineering
- **Incident response playbooks** (atomic steps with checkpoints)
- **Release management** (version-strict deployment procedures)
- **Security remediation** (compliance-aware escalation)

---

## What Makes This Different

Most "prompt templates" are vague platitudes like "be helpful and accurate." This template:

1. **Forces structured output** via the Mandatory Tutorial Template (atomic steps, checkpoints, verification)
2. **Blocks hallucination** via strict source hierarchy (Tier 1 > Tier 2 > Tier 3)
3. **Handles uncertainty** via escalation protocols (admit gaps, don't guess)
4. **Enforces security** via tool scoping and PII protection rules
5. **Maintains version control** by requiring explicit version numbers in every procedure

---

## Example: Before vs. After

### ❌ Without This Template
**User:** "How do I enable backup encryption in v4.0?"  
**Agent:** "Sure! Just go to Settings > Security and toggle 'Enable Encryption.' Make sure you have admin rights."  
*(Hallucinated menu path, no version validation, missing prerequisites)*

### ✅ With This Template
**User:** "How do I enable backup encryption in v4.0?"  
**Agent:**
```markdown
Clarification resolved: "v4.0" taken as Veeam Backup for AWS 4.0 (build 4.0.0.741, GA 5 Oct 2021). If you meant a different product or build, stop here and tell me.

# Enable Repository-Level Encryption on an Amazon S3 Backup Repository (Veeam Backup for AWS 4.0) and Read It from Veeam Backup & Replication 11a

**Purpose:** Encrypt every backup file that Veeam Backup for AWS (VB-AWS) writes to an Amazon S3 repository — with a password or an AWS KMS key — so the data stays encrypted at rest and can still be consumed from Veeam Backup & Replication (VBR) 11a through the External Repository integration.

**Validated against:** Veeam Backup for AWS 4.0 User Guide and VBR 11a User Guide (both archived), checked 14 Oct 2026.
⚠️ Both products are out of support. VBR 12.x pairs with appliance 6.0 and later, not 4.0. Treat this as a reference procedure; upgrade before production use.

**Requirements**
- VB-AWS 4.0 appliance deployed and reachable through its web UI; you are signed in with the Portal Administrator role
- An existing Amazon S3 bucket; the wizard creates or selects a folder inside it
- A repository IAM role with the documented Repository IAM Permissions (S3 access to the bucket; for KMS also kms:Decrypt, kms:DescribeKey, kms:Encrypt, kms:ListAliases, kms:ListKeys)
- KMS option: a symmetric customer-managed KMS key in the SAME AWS Region as the bucket, whose key policy grants the repository IAM role access. AWS managed keys are not supported.
- Password option: a strong password plus hint. Veeam cannot recover a lost password.
- VBR consumption: VBR 11a with the AWS Plug-in installed and the VB-AWS appliance already added to the VBR console

**Procedure**
1. In the VB-AWS web UI, open **Configuration → Repositories** and click **Add**.
   > ✅ **Checkpoint**: The Add Repository wizard opens on the Name step.
2. **Name:** enter a repository name and optional description → Next.
   > ✅ **Checkpoint**: The wizard advances with no validation error.
3. **Repository Settings:** select the IAM role, the S3 bucket, a new or existing folder, and the storage class → Next.
   > ✅ **Checkpoint**: Role, bucket, folder and storage class are shown in the wizard summary pane.
4. **Encryption:** switch **Enable encryption** on, then choose ONE method:
   - *Password* — enter the password and hint.
   - *AWS KMS key* — pick the key from the list. Only symmetric keys in the bucket's Region that the IAM role can access are listed.
   > ⚠️ Once a repository is created with encryption enabled you cannot disable it later; you can only edit the settings.
   > ✅ **Checkpoint**: The summary shows encryption enabled with the method you chose.
5. **Finish:** review the summary → Finish.
   > ✅ **Checkpoint**: The repository is listed under Configuration → Repositories with encryption enabled.
6. Edit each backup policy that should use it (**Policies → Edit → Target repository**), save, and run the policy.
   > ✅ **Checkpoint**: The policy session completes and restore points appear under the encrypted repository.
7. *(Optional)* In VBR 11a: **Backup Infrastructure → External Repositories → Add External Repository → Veeam Backup for AWS**. Select the appliance and the repository. At the Encryption step choose (or add via *Manage passwords*) the same password. KMS-encrypted repositories need no password; the key is displayed and decryption is handled through the IAM role.
   > ✅ **Checkpoint**: The repository appears under External Repositories and its restore points are listed under Home → Backups → External.

**Verification**
- VB-AWS: Configuration → Repositories → the repository shows encryption enabled and the configured password/KMS key.
- VB-AWS: edit the repository — the Enable encryption toggle is on and cannot be switched off (documented behavior).
- VBR: restore points from the external repository can be browsed; a wrong password raises a decryption error instead of listing data.
- VBR PowerShell (optional): `Get-VBRExternalRepository -Name "<repo>" | Format-List *` and inspect the returned object. Property names vary by build; confirm against the PowerShell reference for your version before scripting on them.

**Troubleshooting**
- KMS key not listed in the wizard → key is in another Region, is asymmetric, is an AWS managed key, or the repository IAM role lacks access in the key policy.
- Policy fails after the key was disabled or scheduled for deletion → re-enable the key or change the repository encryption settings. VB-AWS warns on a key pending deletion and gives 7 days to act.
- Enabled encryption on a previously unencrypted repository → allowed; the next backup in each chain is a full backup rather than an incremental.
- Lost password → unrecoverable; open a Veeam support case and plan to re-seed.

**Not documented in the archived sources (so not asserted here):** exact column labels in the repository grid, any in-memory key-caching behavior in VBR, Windows event IDs. For undocumented behavior open a Veeam support case rather than guessing.

**Sources (Tier 1)**
- Veeam Backup for AWS 4.0 User Guide (archived) — "Step 4. Enable Data Encryption": https://helpcenter.veeam.com/archive/vbaws/40/guide/repositories_add_encryption.html
- Veeam Backup for AWS 4.0 User Guide (archived) — "Backup Repository Encryption": https://helpcenter.veeam.com/archive/vbaws/40/guide/encryption_repository_level.html
- Veeam Backup for AWS 4.0 User Guide (archived) — "Editing Backup Repository Settings": https://helpcenter.veeam.com/archive/vbaws/40/guide/repositories_edit.html
- Veeam Backup for AWS 4.0 User Guide (archived) — "Repository IAM Permissions": https://helpcenter.veeam.com/archive/vbaws/40/guide/role_permissions_repo.html
- Same sections in the current guide, used to cross-check behavior statements: https://helpcenter.veeam.com/docs/vbaws/guide/repositories_add_encryption.html · https://helpcenter.veeam.com/docs/vbaws/guide/encryption_repository_level.html · https://helpcenter.veeam.com/docs/vbaws/guide/repositories_edit.html
- Veeam KB4361 — Build Numbers and Versions of Veeam Backup for AWS: https://www.veeam.com/kb4361
- Veeam KB4211 — Release Information for Veeam Backup for AWS v4/v4a (VBR 11a integration requirement): https://www.veeam.com/kb4211
- VBR User Guide — "Platform Support: Amazon Web Services" (appliance ↔ VBR build matrix): https://helpcenter.veeam.com/docs/vbr/userguide/platform_support_aws.html
```

*(Exact version and build, dated validation, requirements first, one observable checkpoint per step, a verification section that tests rather than asserts, an explicit "not documented" list, and sources the reader can open.)*

---

## Repository Structure (generic TEMPLATE.md + examples folder)

```
├── README.md                      ← You are here
├── TEMPLATE.md                    ← The full system instructions template
├── examples/
│   ├── cloud-infra.md             ← Multi-cloud infrastructure (Azure, AWS, cloud-agnostic)
│   ├── cloud-infra-5.6Sol.md      ← GPT-5.6 Sol-tailored multi-cloud infrastructure
│   ├── incident-response.md       ← DevOps incident response & SRE runbooks/postmortems
│   ├── incident-response-5.6Sol.md ← GPT-5.6 Sol-tailored incident response & SRE
│   ├── langchain-agents.md        ← Deep Agents harnesses with local models, HITL & CyClaw references
│   ├── langchain-agents-5.6Sol.md ← GPT-5.6 Sol-tailored Deep Agents harnesses
│   ├── legal-compliance.md        ← Modern technology legal/compliance workflows
│   ├── legal-compliance-5.6Sol.md ← GPT-5.6 Sol-tailored legal/compliance workflows
│   ├── manufacturing-iot.md      ← Manufacturing IoT operations and industrial asset monitoring
│   ├── Network&SecurityAgent.md   ← Network & security engineering (Azure OpenAI o3 optimized)
│   ├── Network&SecurityAgent-5.6Sol.md ← Network & security engineering for GPT-5.6 Sol
│   ├── ps1AgentCoder.md           ← PowerShell coding agent (PS 5.1 + 7+)
│   ├── ps1AgentCoder-5.6Sol.md    ← GPT-5.6 Sol-tailored PowerShell coding agent
│   ├── pythonAgentCoder.md        ← Python coding agent (3.12+)
│   ├── pythonAgentCoder-5.6Sol.md ← GPT-5.6 Sol-tailored Python coding agent
│   ├── veeamGPT.md                ← Backup & DR (Veeam — reference only, not MIT)
│   ├── veeamGPT-5.6Sol.md         ← GPT-5.6 Sol-tailored Veeam reference (not MIT)
│   ├── yaragenerator.md           ← YARA rule generator & cross-platform integration
│   └── yaragenerator-5.6Sol.md    ← GPT-5.6 Sol-tailored YARA rule generator
├── .claude/
│   ├── CLAUDE.md                  ← Operating manual for AI-assisted maintenance
│   └── skills/                    ← preflight, new-example, sync-template, red-team, azureAI-optimize
├── .codex/                        ← Codex-native mirror of the skills + Python audit script
├── .github/workflows/             ← CI: placeholder audit, Gitleaks, DevSkim (blocking); markdownlint, lychee (advisory)
└── LICENSE                        ← MIT License (scoped — see above)
```

---

## Contributing

Issues and PRs are welcome! Every PR must pass the blocking CI gates (placeholder audit,
Gitleaks, DevSkim); run `bash .claude/skills/preflight/check.sh .` locally first. New examples
go through `/new-example <domain>` so the README structure list, license scope and version
history move in the same commit. Focus areas:
- **Domain examples**: Healthcare, finance, education, public sector (legal, manufacturing and LangChain are covered — extend them instead)
- **Integration guides**: AWS Bedrock, Google Vertex AI, Azure AI Foundry Agent Service
- **Testing strategies**: Automated validation of instruction adherence
- **Localization**: Non-English versions with cultural/regulatory adjustments

---

## License

MIT License - see [LICENSE](LICENSE) for details.

**TL;DR:** Use this commercially, modify it, share it. Just keep the copyright notice.

---

## Citation

If you use this template in production or research, a link back to this repo is appreciated:

```markdown
AI agent instructions based on the [Universal AI Agent Safety Template](https://github.com/CGFixIt/AzureAI-CopilotStudio-PersonalAgent-Instructions/blob/main/TEMPLATE.md?plain=1)
```

---

## Version History

- **v1.15** (Oct 2026): Rewrote the README "Before vs. After" encryption example against Veeam Backup for AWS 4.0 / VBR 11a sources (removed fabricated wizard step, cmdlet, event ID and VBR 12 pairing; added dated validation, documented KMS constraints and verifiable sources); completed the placeholder inventory to all 24 TEMPLATE.md tokens; replaced the retired OpenAI Assistants API snippet with the Responses API; fixed the duplicated Quick Start step number; added tooling directories to the structure list; fixed the preflight C6 filename regex that false-flagged `-5.6Sol.md` files; aligned CLAUDE.md and the sync-template skill with the current 19-file `examples/` tree; follow-up: example now cites the exact archived 4.0 pages instead of the guide root
- **v1.14** (Aug 2026): Added `examples/manufacturing-iot.md` for evidence-driven manufacturing IoT operations, OT safety, read-only diagnostics, approval-gated changes, and escalation
- **v1.13** (Jul 2026): Added ChatGPT Enterprise personal-agent workspace, RBAC, connector, and evidence boundaries to every GPT-5.6 Sol example and documented a least-privilege Enterprise deployment path
- **v1.12** (Jul 2026): Added a GPT-5.6 Sol-tailored `-5.6Sol.md` counterpart for every deployable example while retaining the complete o3-focused set
- **v1.11** (Jul 2026): Added `examples/langchain-agents.md` for governed Deep Agents harnesses using local open-weight models, scoped tools, deterministic evaluation, human approval, and pinned CyClaw references
- **v1.10** (Jul 2026): Tightened `examples/legal-compliance.md` to better match the template standard with explicit response rules, removed internal notes in examples agent instructions (a paste artifact and a todo list ;)), connected-tool/data-access guidance, and stronger validation expectations via agentic skills/tools to force examples/ to align with template file every so often, optimized for o3 since usually its your companies money paying if you care this much about it being correct.. wait isnt that backwards ;)
- **v1.9** (Jul 2026): Aligned the README example inventory and license scope with the current `examples/` tree, and cleaned stale placeholder/paste artifacts from the o3-focused example set
- **v1.8** (Jul 2026): Pinned GitHub Actions workflow dependencies to exact commit SHAs for supply-chain hardening; `examples/legal-compliance.md` remains listed in the repository structure and MIT scope
- **v1.7** (Jul 2026): Added `examples/legal-compliance.md` (modern technology compliance, AI governance, privacy, cybersecurity disclosure, and evidence mapping)
- **v1.6** (Jul 2026): Rewrote CLAUDE.md as a full operating manual; [***] added `preflight` (local CI mirror), `new-example`, `sync-template`, and `red-team` skills; fixed README filename drift and removed a leftover chat artifact from `Network&SecurityAgent.md`
- **v1.5** (Jun 2026): Added `examples/incident-response.md` (DevOps incident response & SRE) via `/azureAI-optimize`
- **v1.4** (Jun 2026): Added o3 Reasoning Protocol to TEMPLATE.md and all examples; added missing Escalation/Security sections; added CI workflows (placeholder-audit, markdown-lint, link-check); security hardening (Dependabot, CODEOWNERS, .gitattributes); fixed README structure and license filename drift
- **v1.3** (May 2026): Added several new agent instructions under examples/
- **v1.2** (Dec 2025): Added Azure "on your data" grounding rule, audit logging, normalized formatting
- **v1.1** (Dec 2025): Added Tool & Data Access info, Security & Privacy, ethical guardrails
- **v1.0** (Dec 2025): Initial public release, based on production deployment at global enterprise software company

---

**Built with <a href="https://linktr.ee/cgrady92">❤️</a> for teams who need AI agents that admit when they don't know.**
<img width="134" height="28" alt="image" src="https://github.com/user-attachments/assets/e546f130-9574-466a-aecd-142ec051c215" />
