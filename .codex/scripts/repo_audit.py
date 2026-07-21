from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

PLACEHOLDER_RE = re.compile(r"\[[A-Z][A-Z0-9_]{2,}\]")
ALLOWED_PLACEHOLDERS = {
    "[Warning]",
    "[Note]",
    "[Troubleshooting]",
    "[FinOps]",
    "[Security]",
    "[IaC]",
    "[DATE]",
}
CHAT_ARTIFACT_RE = re.compile(
    r"let me know|paste this (in|dir)|here('| i)s the (updated|full|complete|revised)|"
    r"i('| ha)ve (created|updated|added)|would you like me|hope this helps|as an ai",
    re.IGNORECASE,
)
SECRET_RE = re.compile(
    r"AKIA[0-9A-Z]{16}|"
    r"ghp_[A-Za-z0-9]{20,}|"
    r"github_pat_[A-Za-z0-9_]{20,}|"
    r"sk-[A-Za-z0-9]{20,}|"
    r"xox[baprs]-[A-Za-z0-9-]{10,}|"
    r"AIza[0-9A-Za-z_-]{30,}|"
    r"BEGIN [A-Z ]*PRIVATE KEY"
)
ASSIGN_RE = re.compile(
    r"""(?i)(password|passwd|secret|api[_-]?key|token)\s*[:=]\s*["'][^"'<\[]{12,}["']"""
)
IGNORE_ASSIGN_VALUE_RE = re.compile(
    r"your|example|placeholder|redacted|fake|dummy|xxx|changeme|<.*>",
    re.IGNORECASE,
)
README_NAME_RE = re.compile(r"(?<![A-Za-z0-9&_.-])[A-Za-z0-9&][A-Za-z0-9&_.-]*\.md")
INVARIANTS = {
    "purpose/mission": re.compile(r"purpose|core mission", re.IGNORECASE),
    "forbidden actions": re.compile(r"forbidden", re.IGNORECASE),
    "escalation": re.compile(r"escalat", re.IGNORECASE),
    "source hierarchy": re.compile(
        r"tier 1|authoritative source|high authority|documentation hierarchy",
        re.IGNORECASE,
    ),
    "checkpoint/verification": re.compile(r"checkpoint|verification", re.IGNORECASE),
    "security": re.compile(r"security", re.IGNORECASE),
}
ANALYZE_REQUIRED = (
    ("purpose/mission", re.compile(r"Purpose|Core Mission|Identity\s*&\s*Mission", re.IGNORECASE)),
    ("forbidden actions", re.compile(r"Forbidden Actions|Forbidden Behaviors|Zero Tolerance", re.IGNORECASE)),
    ("escalation", re.compile(r"Escalation|escalat", re.IGNORECASE)),
    ("security", re.compile(r"Security", re.IGNORECASE)),
    (
        "source hierarchy",
        re.compile(r"Source Hierarchy|Authoritative Source|Tier 1|Documentation Hierarchy|High Authority", re.IGNORECASE),
    ),
)
EXPECTED_SKILLS = {
    "azureai-optimize",
    "codex-verify",
    "new-example",
    "preflight",
    "red-team",
    "sol-optimize",
    "sync-template",
}
EXPECTED_COMMANDS = {
    "README.md",
    "azureai-optimize.md",
    "codex-verify.md",
    "preflight.md",
}
EXPECTED_WORKFLOWS = {
    "devskim.yml",
    "gitleaks.yml",
    "link-check.yml",
    "markdown-lint.yml",
    "placeholder-audit.yml",
}
ANY_USES_RE = re.compile(r"^\s*uses:\s+(\S+?)\s*$", re.MULTILINE)
PERMISSIONS_BLOCK_RE = re.compile(r"(?ms)^permissions:\s*\n((?:^[ \t]+[^\n]*\n?)*)")


class Reporter:
    def __init__(self) -> None:
        self.failures = 0

    def pass_(self, message: str) -> None:
        print(f"  PASS  {message}")

    def fail(self, message: str) -> None:
        print(f"  FAIL  {message}")
        self.failures += 1

    def warn(self, message: str) -> None:
        print(f"  WARN  {message}")

    def skip(self, message: str) -> None:
        print(f"  SKIP  {message}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def example_files(root: Path) -> list[Path]:
    return sorted((root / "examples").glob("*.md"))


def tracked_text_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() in {".md", ".sh", ".yml", ".jsonc", ".json", ".py"}:
            files.append(path)
    return sorted(files)


def find_placeholders(path: Path) -> list[str]:
    hits: list[str] = []
    for line_no, line in enumerate(read_text(path).splitlines(), start=1):
        for token in PLACEHOLDER_RE.findall(line):
            if token in ALLOWED_PLACEHOLDERS:
                continue
            hits.append(f"{line_no}:{token}")
    return hits


def readme_consistency_issues(root: Path) -> list[str]:
    issues: list[str] = []
    readme_text = read_text(root / "README.md")
    valid_names = {path.name for path in root.glob("*.md")} | {path.name for path in example_files(root)}
    for path in example_files(root):
        if path.name not in readme_text:
            issues.append(f"README.md does not mention {path.name} (Repository Structure block out of sync)")
    for name in sorted(set(README_NAME_RE.findall(readme_text))):
        if name not in valid_names:
            issues.append(f"README.md references '{name}' but no exact-case file exists (root or examples/)")
    return issues


def run_preflight(root: Path) -> int:
    report = Reporter()

    print("==============================================")
    print(" Preflight - local CI mirror")
    print("==============================================")

    print("\n-- C1. Unfilled placeholders in examples/ --")
    c1_bad = False
    for path in example_files(root):
        hits = find_placeholders(path)
        if hits:
            report.fail(f"{path.name} has unfilled placeholder tokens:")
            for hit in hits:
                print(f"          {hit}")
            c1_bad = True
    if not c1_bad:
        report.pass_("no unfilled placeholders in examples/")

    print("\n-- C2. TEMPLATE.md placeholder integrity --")
    template_tokens = set(PLACEHOLDER_RE.findall(read_text(root / "TEMPLATE.md")))
    token_count = len(template_tokens)
    if token_count >= 20:
        report.pass_(f"TEMPLATE.md has {token_count} unique placeholder tokens (expected ~24, floor 20)")
    else:
        report.fail(
            f"TEMPLATE.md has only {token_count} unique placeholder tokens (floor 20) - placeholders must stay UNFILLED in the template"
        )

    print("\n-- C3. Core invariants in each example --")
    c3_bad = False
    for path in example_files(root):
        text = read_text(path)
        missing = [name for name, pattern in INVARIANTS.items() if not pattern.search(text)]
        if missing:
            report.fail(f"{path.name} missing: {' '.join(f'[{name}]' for name in missing)}")
            c3_bad = True
    if not c3_bad:
        report.pass_("all examples carry the core invariants")

    print("\n-- C4. Chat artifacts near end of instruction files --")
    c4_bad = False
    for path in [*example_files(root), root / "TEMPLATE.md"]:
        lines = read_text(path).splitlines()
        start_line = max(1, len(lines) - 29)
        tail_hits = [
            f"{line_no}:{line}"
            for line_no, line in enumerate(lines[-30:], start=start_line)
            if CHAT_ARTIFACT_RE.search(line)
        ]
        if tail_hits:
            report.fail(f"{path.name} ends with chat-session artifacts:")
            for hit in tail_hits:
                print(f"          {hit}")
            c4_bad = True
    if not c4_bad:
        report.pass_("no conversational trailers detected")

    print("\n-- C5. Secret-looking strings in tracked text files --")
    secret_hits: list[str] = []
    for path in tracked_text_files(root):
        for line_no, line in enumerate(read_text(path).splitlines(), start=1):
            if SECRET_RE.search(line):
                secret_hits.append(f"{path.relative_to(root)}:{line_no}:{line.strip()}")
    assign_hits: list[str] = []
    for path in [*example_files(root), root / "TEMPLATE.md"]:
        for line_no, line in enumerate(read_text(path).splitlines(), start=1):
            if ASSIGN_RE.search(line) and not IGNORE_ASSIGN_VALUE_RE.search(line):
                assign_hits.append(f"{path.relative_to(root)}:{line_no}:{line.strip()}")
    if secret_hits or assign_hits:
        report.fail("possible secrets found - use obviously fake values (your-api-key-here):")
        for hit in [*secret_hits, *assign_hits]:
            print(f"          {hit}")
    else:
        report.pass_("no secret-shaped strings")

    print("\n-- C6. README consistency (sync triangle) --")
    c6_issues = readme_consistency_issues(root)
    if c6_issues:
        for issue in c6_issues:
            report.fail(issue)
    else:
        report.pass_("README, examples/ and license block agree")

    print("\n-- C7. Markdown lint (informational) --")
    markdownlint = shutil.which("markdownlint-cli2")
    if markdownlint:
        result = subprocess.run(
            [
                markdownlint,
                "--config",
                str(root / ".markdownlint.jsonc"),
                str(root / "*.md"),
                str(root / "examples/*.md"),
            ],
            capture_output=True,
            text=True,
            shell=False,
        )
        if result.returncode == 0:
            report.pass_("markdownlint clean")
        else:
            report.warn("markdownlint reported issues (non-blocking, matches CI policy)")
            if result.stdout.strip():
                print(result.stdout.rstrip())
            if result.stderr.strip():
                print(result.stderr.rstrip())
    else:
        report.skip("markdownlint-cli2 not installed - CI runs it non-blocking anyway")

    print("\n==============================================")
    if report.failures:
        print(f" PREFLIGHT FAILED - {report.failures} blocking issue(s). Fix before committing.")
        print(" Remediation guidance: .codex/skills/preflight/SKILL.md")
        return 1
    print(" Preflight passed - safe to commit.")
    print("==============================================")
    return 0


def run_analyze(root: Path) -> int:
    print("==============================================")
    print(" AzureAI Optimize - Repository Analysis")
    print("==============================================")

    print("\n-- 1. Unfilled placeholders in examples/ --")
    found_placeholders = False
    for path in example_files(root):
        hits = find_placeholders(path)
        if hits:
            print(f"  WARN  {path.name}:")
            for hit in hits:
                print(f"         {hit}")
            found_placeholders = True
    if not found_placeholders:
        print("  OK    No leftover placeholders found.")

    print("\n-- 2. Core invariant presence in each example --")
    for path in example_files(root):
        text = read_text(path)
        missing = [name for name, pattern in ANALYZE_REQUIRED if not pattern.search(text)]
        if missing:
            print(f"  WARN  {path.name} missing invariants: {'  '.join(missing)}")
        else:
            print(f"  OK    {path.name}")

    print("\n-- 3. Azure AI o3 / reasoning-model optimization --")
    for path in [*example_files(root), root / "TEMPLATE.md"]:
        text = read_text(path)
        if re.search(r"reasoning protocol|o3|chain.of.thought|think step", text, re.IGNORECASE):
            print(f"  OK    {path.name} - has reasoning/o3 guidance")
        else:
            print(f"  ENHANCE  {path.name} - no o3 reasoning protocol found")

    print("\n-- 4. README <-> examples/ consistency --")
    readme_issues = readme_consistency_issues(root)
    if readme_issues:
        for issue in readme_issues:
            print(f"  WARN  {issue}")
    else:
        print("  OK    README and examples are synchronized")

    print("\n-- 5. CI workflows --")
    workflows = sorted((root / ".github" / "workflows").glob("*.yml"))
    for workflow in workflows:
        name = ""
        for line in read_text(workflow).splitlines():
            if line.startswith("name:"):
                name = line.split(":", 1)[1].strip()
                break
        print(f"  EXISTS  {workflow.name}  ->  {name}")
    print("\n  Candidate additions:")
    missing_any = False
    for workflow_name, label in (
        ("markdown-lint.yml", "markdown-lint.yml (markdownlint-cli2 for prose quality)"),
        ("link-check.yml", "link-check.yml (lychee or markdown-link-check for dead URLs)"),
        ("placeholder-audit.yml", "placeholder-audit.yml (automated [PLACEHOLDER] scan on PRs)"),
    ):
        if not (root / ".github" / "workflows" / workflow_name).exists():
            print(f"    - {label}")
            missing_any = True
    if not missing_any:
        print("    (all recommended workflows already exist)")

    print("\n-- 6. Security hardening --")
    unpinned = False
    for workflow in workflows:
        for match in ANY_USES_RE.finditer(read_text(workflow)):
            ref = match.group(1)
            if "@" not in ref:
                continue
            uses_target, uses_ref = ref.rsplit("@", 1)
            if uses_target.startswith("./"):
                continue
            if not re.fullmatch(r"[a-f0-9]{40}", uses_ref, re.IGNORECASE):
                print(f"  HARDEN  {workflow.name} - actions pinned to tags, not SHAs")
                unpinned = True
                break
    if not unpinned:
        print("  OK    All actions pinned to commit SHAs")
    if (root / ".github" / "CODEOWNERS").exists() or (root / "CODEOWNERS").exists():
        print("  OK    CODEOWNERS file exists")
    else:
        print("  ADD   No CODEOWNERS file - consider adding for review gating")
    print("  CHECK Verify branch protection is enabled on 'main' (manual)")

    print("\n-- 7. Domain example coverage --")
    print("  Existing domains:")
    for path in example_files(root):
        print(f"    - {path.stem}")
    print("\n  Suggested new domains (per README contributing guidance):")
    suggestions = (
        ("healthcare / clinical-protocols", ("clinical-protocols", "healthcare")),
        ("legal / compliance", ("legal-compliance", "legal")),
        ("finance / finops", ("finops", "finance")),
        ("manufacturing / iot", ("manufacturing", "iot")),
    )
    for label, needles in suggestions:
        covered = any(any(needle in path.stem for needle in needles) for path in example_files(root))
        suffix = " (covered)" if covered else ""
        print(f"    - {label}{suffix}")

    print("\n==============================================")
    print(" Analysis complete. Run $azureai-optimize to")
    print(" act on these findings.")
    print("==============================================")
    return 0


def permissions_have_contents_read(text: str) -> bool:
    match = PERMISSIONS_BLOCK_RE.search(text)
    return bool(match and re.search(r"^\s*contents:\s*read\s*$", match.group(1), re.IGNORECASE | re.MULTILINE))


def run_verify_codex(root: Path) -> int:
    report = Reporter()

    print("==============================================")
    print(" Codex Verify - repo-local setup audit")
    print("==============================================")

    print("\n-- 1. Codex directories and audit entrypoints --")
    if (root / ".codex").is_dir():
        report.pass_(".codex/ exists")
    else:
        report.fail(".codex/ is missing")
    if (root / ".codex" / "scripts" / "repo_audit.py").is_file():
        report.pass_(".codex/scripts/repo_audit.py exists")
    else:
        report.fail(".codex/scripts/repo_audit.py is missing")
    skill_dirs = {path.name for path in (root / ".codex" / "skills").glob("*") if path.is_dir()}
    missing_skills = sorted(EXPECTED_SKILLS - skill_dirs)
    if missing_skills:
        report.fail(f"missing skill directories: {', '.join(missing_skills)}")
    else:
        report.pass_("expected skill directories are present")

    print("\n-- 2. Windows-friendly Codex docs --")
    agents_text = read_text(root / ".codex" / "AGENTS.md")
    codex_readme_text = read_text(root / ".codex" / "README.md")
    if "python .codex/scripts/repo_audit.py preflight ." in agents_text:
        report.pass_(".codex/AGENTS.md points to the Python preflight entrypoint")
    else:
        report.fail(".codex/AGENTS.md still lacks the Python preflight command")
    if "python .codex/scripts/repo_audit.py analyze ." in codex_readme_text:
        report.pass_(".codex/README.md points to the Python analyzer")
    else:
        report.fail(".codex/README.md still lacks the Python analyzer command")
    if "python .codex/scripts/repo_audit.py verify-codex ." in codex_readme_text:
        report.pass_(".codex/README.md exposes the Codex verification command")
    else:
        report.fail(".codex/README.md still lacks the Codex verification command")

    bash_hits: list[str] = []
    for skill_file in sorted((root / ".codex" / "skills").rglob("SKILL.md")):
        text = read_text(skill_file)
        if "bash .codex/" in text:
            bash_hits.append(str(skill_file.relative_to(root)))
    if bash_hits:
        report.fail(f"bash-only Codex skill instructions remain: {', '.join(bash_hits)}")
    else:
        report.pass_("Codex skill docs no longer require bash-only entrypoints")

    print("\n-- 3. Repo-local command wrappers --")
    commands_dir = root / ".codex" / "commands"
    if commands_dir.is_dir():
        report.pass_(".codex/commands/ exists")
    else:
        report.fail(".codex/commands/ is missing")
    command_files = {path.name for path in commands_dir.glob("*.md")} if commands_dir.is_dir() else set()
    missing_commands = sorted(EXPECTED_COMMANDS - command_files)
    if missing_commands:
        report.fail(f"missing command wrappers: {', '.join(missing_commands)}")
    else:
        report.pass_("expected command wrappers are present")

    print("\n-- 4. GitHub workflow hardening surfaces --")
    workflows_dir = root / ".github" / "workflows"
    workflow_files = {path.name for path in workflows_dir.glob("*.yml")}
    missing_workflows = sorted(EXPECTED_WORKFLOWS - workflow_files)
    if missing_workflows:
        report.fail(f"missing workflow files: {', '.join(missing_workflows)}")
    else:
        report.pass_("expected workflow files are present")
    for workflow in sorted(workflows_dir.glob("*.yml")):
        text = read_text(workflow)
        if permissions_have_contents_read(text):
            report.pass_(f"{workflow.name} has root permissions with contents: read")
        else:
            report.fail(f"{workflow.name} is missing a root permissions block with contents: read")
        unpinned_refs = []
        for match in ANY_USES_RE.finditer(text):
            ref = match.group(1)
            if "@" not in ref:
                continue
            uses_target, uses_ref = ref.rsplit("@", 1)
            if uses_target.startswith("./"):
                continue
            if not re.fullmatch(r"[a-f0-9]{40}", uses_ref, re.IGNORECASE):
                unpinned_refs.append(ref)
        if unpinned_refs:
            report.fail(f"{workflow.name} has unpinned action refs: {', '.join(unpinned_refs)}")
        else:
            report.pass_(f"{workflow.name} pins external actions to commit SHAs")

    print("\n-- 5. Supporting policy files --")
    if (root / ".github" / "CODEOWNERS").is_file():
        report.pass_(".github/CODEOWNERS exists")
    else:
        report.fail(".github/CODEOWNERS is missing")
    if (root / ".github" / "dependabot.yml").is_file():
        report.pass_(".github/dependabot.yml exists")
    else:
        report.fail(".github/dependabot.yml is missing")

    print("\n==============================================")
    if report.failures:
        print(f" CODEX VERIFY FAILED - {report.failures} issue(s) found.")
        return 1
    print(" Codex verify passed - repo-local guidance and CI surfaces look healthy.")
    print("==============================================")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Cross-platform repo audit helpers for this Codex-enabled docs repository.")
    parser.add_argument("mode", choices=("preflight", "analyze", "verify-codex"))
    parser.add_argument("root", nargs="?", default=".")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if args.mode == "preflight":
        return run_preflight(root)
    if args.mode == "analyze":
        return run_analyze(root)
    return run_verify_codex(root)


if __name__ == "__main__":
    sys.exit(main())
