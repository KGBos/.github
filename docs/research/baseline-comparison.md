# Baseline comparison

Legend: `yes` means the studied source visibly uses that category at the shared `.github` level; `local` means the example was intentionally studied at repository scope rather than as an account-wide default.

| Source | Scope | Code of conduct | Contributing | Security | Issue templates/forms | PR template | Profile/support | Automation / policy hub |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub | shared | yes | yes | yes | no | no | profile | light |
| Microsoft | shared | yes | no | yes | no | no | profile | extensive |
| Kubernetes | shared | no | no | yes | no | no | security contacts | minimal |
| CNCF | shared | yes | no | no | no | no | profile | minimal |
| HashiCorp | shared | yes | no | yes | no | no | no | minimal |
| Home Assistant | shared | yes | yes | yes | no | no | support + profile | light |
| Homebrew | shared | yes | no | yes | no generic forms | no generic PR template | support | extensive |
| Angular | shared | yes | no | yes | no | no | no | extensive |
| Flutter | shared | yes | yes | yes | no | yes | support + profile | light |
| Fastify | shared | yes | yes | yes | YAML forms | yes | no | light |
| Sigstore | shared | yes | yes | yes | templates | yes | profile | workflow templates |
| Supabase | shared | yes | yes | yes | templates | yes | no | workflow templates |
| OpenAI Codex | local | repo-local | repo-local | repo-local | YAML forms | repo-local choice | local | extensive local automation |
| Anthropic Claude Code | local | repo-local | repo-local | repo-local | YAML forms | repo-local choice | local | extensive local automation |
| xAI Python SDK | local | repo-local | repo-local | repo-local | YAML forms | yes | local | local workflows |

## Patterns that survive normalization

### 1. Keep shared defaults generic and override-friendly

The strongest shared repositories either stay intentionally small or reserve their larger policy systems for organization-specific needs. GitHub's own inheritance model reinforces this: repository-local community-health files override defaults rather than being merged field-by-field.

**Baseline result:** global files should contain only guidance that is sensible for nearly every repository.

### 2. Community-health documents are the most stable shared layer

A code of conduct and security policy appear repeatedly across both minimal and extensive shared repositories. Contribution guidance is also common, but the best shared versions defer concrete build/test commands to the target repository.

**Baseline result:** include `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, and `SECURITY.md`.

### 3. Modern issue intake favors structured forms, but shared forms must remain broad

Fastify, OpenAI, Anthropic, and xAI use YAML Issue Forms. Product-specific forms become detailed quickly, which is useful locally but inappropriate as an account-wide default.

**Baseline result:** provide only generic Bug and Feature forms. Do not assign labels, owners, priorities, components, runtimes, or product-specific fields globally.

### 4. A lightweight PR template is broadly useful

Flutter, Fastify, Sigstore, Supabase, and xAI all use PR templates, but their detailed checklists are project-specific. The common core is a description, related context, verification, tests, and documentation.

**Baseline result:** use a short PR template with Summary, Related issues, Verification, and a small generic checklist.

### 5. Do not centralize ownership or project commands

CODEOWNERS, exact test commands, release processes, runtime matrices, CI jobs, and component ownership are repository facts. The AI/product examples especially keep these local.

**Baseline result:** no shared CODEOWNERS, build instructions, test commands, release process, or project CI.

### 6. Optional community files require a real destination or policy

SUPPORT, FUNDING, formal GOVERNANCE, CLA/DCO, and stale-bot policies appear in mature projects when those projects actually have the corresponding support channel, funding relationship, governing body, legal requirement, or maintenance policy.

**Baseline result:** omit them until KGBos has a concrete account-wide policy to express.

### 7. Licenses remain repository-specific

GitHub does not inherit a license from the account `.github` repository. Projects also commonly choose licenses based on the specific repository.

**Baseline result:** do not treat a license in this repository as a default license for other repositories.

### 8. Automation belongs in a separate opt-in layer

Microsoft, Homebrew, and Angular demonstrate that a `.github` repository can become a policy/automation hub, while GitHub, HashiCorp, Kubernetes, and CNCF demonstrate that this is not required for a healthy baseline.

**Baseline result:** preserve this repository's existing ruleset deployment because it governs this repository itself, but do not add cross-repository automation to the baseline pass.

## Resulting baseline tree

```text
.github/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug.yml
│   │   ├── feature.yml
│   │   └── config.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── apply-ruleset.yml        # self-governance, not inherited baseline
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── README.md
├── profile/
│   └── README.md
├── docs/
│   ├── governance-as-code.md
│   └── research/
│       ├── sources.md
│       └── baseline-comparison.md
├── rulesets/
│   └── master-protection.json
└── scripts/
    └── reconcile-ruleset.py
```

The baseline intentionally stops here. KGBos-specific workflow conventions should be evaluated and layered on only after this foundation is accepted.
