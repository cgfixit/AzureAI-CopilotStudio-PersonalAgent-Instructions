# Universal AI Personal Agent Safety Instructions
(With specific examples)

> Production-tested (at current employer due to default GPT o3 hallucinating when connected to internet) Template and <a href="https://github.com/cgfixit/AzureAI-CopilotStudio-PersonalAgent-Instructions/tree/main/examples"> /examples folder</a> with 8+ personal agent instructions verified and tuned for o3, plus paired `-5.6Sol.md` versions tailored to GPT-5.6 Sol (I use the TEMPLATE.md as a project/space file in perplexity to noticeable improvement) Personal agent TEMPLATE.md instructions w/ examples for enterprise/all companies and people using AI agents that prioritize accuracy, version-control, and anti-hallucination safeguards. I mean why would we pay our increased power bills for a token predictor to lie to us based on conflicting internet/RAG/citations or bad/unclear context in prompt.

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

Designed for real-world deployment in **Azure AI Studio**, **Microsoft Copilot Studio**, **Grok Skills**, **Perplexity Pro or Max Project/Spaces instruction supplement** **agentic coding harnesses/tools** **OpenAI Assistants API**, **Anthropic Claude Projects like Claude Code** **Generic MCP server connectors**, and similar AI/agent frameworks.

---

## Key Features

| Problem | Solution |
|---------|----------|
| 🚨 **Hallucinations** | 3-Tier source hierarchy (official internal or highly reputable sources/docs > Marketing Whitepapers > Personal Tech Notes ;) |
| 📅 **Version drift** | Mandatory version validation in every tutorial via agentic skill/tool call |
| 🔐 **Security risks** | Tool scoping + PII protection + audit logging (optional) + sensitive langugage filters |
| ❓ **Scope creep** | Environment clarification rules force specificity to ask for clarity on context or state conflicting answers in corpus scope |
| ⚖️ **Compliance** | Built-in HIPAA/GDPR/SOC2/GDPR/CCPA/ escalation protocols |

**Battle-tested:** v1.0 ran in production at a global enterprise software company before being generalized for public release.
**Specific use cases in addition to TEMPLATE.md**
- cloud-infra.md (Multi-cloud infrastructure - Azure, AWS, cloud-agnostic)
- incident-response.md (DevOps incident response and SRE runbooks/postmortems)
- langchain-agents.md (Deep Agents harnesses with local open-weight models, scoped tools, HITL, and CyClaw references)
- legal-compliance.md (Modern technology legal/compliance workflows)
- Network&SecurityAgent.md (Network and security engineering, Azure OpenAI o3 optimized)
- ps1AgentCoder.md (PowerShell coding agent, PS 5.1 + 7+)
- pythonAgentCoder.md (Python coding agent, 3.12+)
- veeamGPT.md (Veeam Backup & Replication reference only, not MIT)
- yaragenerator.md (YARA rule generator and cross-platform integration)

Each example also has a `-5.6Sol.md` counterpart for OpenAI GPT-5.6 Sol. These
variants replace o3-specific internal reasoning checklists with lean, outcome-first
execution policies while preserving each domain's safety, source, escalation, and
verification requirements. They follow the current
[GPT-5.6 prompting guidance](https://developers.openai.com/api/docs/guides/model-guidance?model=gpt-5.6).

---

## Quick Start

### 1. Copy the Template
Download [`TEMPLATE.md`](TEMPLATE.md) or copy the raw markdowns from examples/ into your AI agent's system instructions field.

### 2. Customize Placeholders
Search and replace these brackets with your specific values:

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
[CURRENT_YEAR]             → "2025"
[DOMAIN_SPECIFIC_DOCS]     → "Release Notes, API Reference"
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
---
### 4. Deploy to Your Platform

#### Azure AI Studio / Copilot Studio
1. Navigate to your agent configuration
2. Paste the customized template into the **System Message** field
3. Enable **"On Your Data"** if using indexed content (recommended)
4. Test with version-specific queries

#### OpenAI Assistants API
```python
client.beta.assistants.create(
    name="Technical Support Agent",
    instructions=open("TEMPLATE.md").read(),  # Your customized version
    model="gpt-4-turbo-preview",
    tools=[{"type": "retrieval"}]
)
```

#### Anthropic Claude (Projects)
1. Create a new Project
2. Paste the template into **Custom Instructions**
3. Upload your Tier 1 documentation to the Project knowledge base

### 4. Test Edge Cases
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
Veeam Confidential – Internal Use Only (Unless you confirm or test in a lab first)
Validated against Veeam Backup for AWS v4.0 (archived documentation) on 10 Jul 2026

Enable Encryption on an Amazon S3 Backup Repository (VB-AWS v4.0) That Will Be Imported into Veeam Backup & Replication
Purpose: Encrypt all backup data written to an S3-based repository in Veeam Backup for AWS so that, when the repository is later imported into Veeam Backup & Replication (VBR) as an External Repository, backup files remain AES-256 encrypted at rest.

Requirements
• Veeam Component: Veeam Backup for AWS 4.0 appliance already deployed and accessible via its web UI
• Permissions: VB-AWS administrator role (to add/edit repositories) and an AWS IAM role/user that can:
– Read/Write the target S3 bucket/folder
– Encrypt/Decrypt with the chosen AWS KMS key (if using KMS)
• Repository target: Existing or new Amazon S3 bucket/folder
• If KMS encryption is chosen: Symmetric CMK created in the SAME AWS Region as the bucket
• VBR 12 or later with the “External Repository” feature (read-only) enabled to consume the backups

Procedure

Open the VB-AWS management console → Configuration (menu) → Backup Repositories.
Click Add Repository.

Step 1 – Repository Name
• Enter a descriptive Name (e.g., “S3-Prod-Enc”).
⚠️ [Checkpoint] — Wizard advances with no validation errors.

Step 2 – Repository Settings
• Choose Amazon S3 and browse to the required Bucket.
• Select Create new folder or pick an existing folder.
⚠️ [Checkpoint] — Bucket and folder appear in the path field.

Step 3 – Worker & Performance (accept defaults or tune as per design).
⚠️ [Checkpoint] — Worker settings saved.

Step 4 – Encryption

Click Edit Encryption Settings.
Toggle Enable encryption → On.
Choose one method:
• Use password encryption → Enter a strong passphrase + hint.
• Use KMS encryption key → Select the desired symmetric CMK from the drop-down list.
![⚠️Warning] IAM role specified for the repository must have kms:Encrypt, kms:Decrypt, kms:GenerateDataKey*, kms:DescribeKey on that CMK.
Confirm and close the dialog.
⚠️ [Checkpoint] — “Encryption: Enabled” is displayed in the wizard summary.
Step 5 – Finish
• Review the summary → Finish.
• Wait for the “Backup repository successfully created” status.
⚠️ [Checkpoint] — New repository shows “Encrypted” column = Yes.

Update or create Backup Policies
• Edit existing policies (or create new ones) and point them to the newly encrypted repository.
• Save and run the policy to produce encrypted backup chains.

Import into Veeam Backup & Replication (optional)
• In VBR, open Inventory → External Repositories → Add Repository.
• Provide VB-AWS appliance address and credentials.
• Select the encrypted repository; VBR will prompt for the same password or detect the KMS key automatically (if VBR proxy has IAM permissions).
⚠️ [Checkpoint] — Repository appears under External Repositories; backups are listed but remain encrypted at rest.

![Troubleshooting]
• “KMS key not found” — Verify CMK Region and IAM permissions (kms:ListKeys, kms:DescribeKey).
• Policy fails with “AccessDeniedException: KMS” — Ensure the CMK is enabled and not in PendingDeletion state.
• Forgot the password? — Data is unrecoverable without the original password; open a Support ticket but be prepared for destructive re-seeding.

Frequently Asked Questions
Q: Can I turn encryption on later for an existing, non-encrypted repository?
A: Yes. Edit the repository → Encryption → Enable and run new backups. Existing unencrypted files stay unencrypted; only new backup chains use encryption. (Ref: “Editing Backup Repository Settings”)

Q: Does VBR need the password every time?
A: Only once per console session. VBR caches the key in RAM for that session.

Q: Is client-side encryption compatible with S3 Server-Side Encryption?
A: Yes; VB-AWS performs its own AES-256 encryption before sending data to S3, regardless of any server-side encryption you may have enabled at the bucket level.

**Verification**
- PowerShell: `Get-BackupJob -Name "JobName" | Select EncryptionEnabled` → should return `True`
- Event ID 1234 in Application log: "Encryption enabled for job [JobName]"

Sources:
Veeam Help Center – “Step 4. Enable Data Encryption” (Veeam Backup for AWS 4.0)
https://helpcenter.veeam.com/archive/vbaws/40/guide/repositories_add_encryption.html
Veeam Help Center – “Backup Repository Encryption” (Veeam Backup for AWS 4.0)
https://helpcenter.veeam.com/archive/vbaws/40/guide/encryption_repository_level.html
```

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
└── LICENSE                        ← MIT License (scoped — see above)
```

---

## Contributing

Issues and PRs are welcome! Focus areas:
- **Domain examples**: Healthcare, legal, finance, manufacturing
- **Integration guides**: AWS Bedrock, Google Vertex AI, LangChain
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
