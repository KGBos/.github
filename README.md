# KGBos shared GitHub defaults

This public `.github` repository provides shared GitHub community-health defaults for repositories owned by `KGBos` that do not define their own equivalent files.

The initial baseline is intentionally conservative. It is assembled from established public GitHub patterns first; KGBos-specific workflow conventions will be considered separately after this baseline is reviewed.

## Shared defaults

- `CODE_OF_CONDUCT.md` — common collaboration expectations
- `CONTRIBUTING.md` — generic contribution guidance
- `SECURITY.md` — private vulnerability-reporting guidance
- `.github/ISSUE_TEMPLATE/` — generic bug and feature Issue Forms
- `.github/PULL_REQUEST_TEMPLATE.md` — a lightweight pull-request template

GitHub gives repository-local community-health files precedence over these defaults. A project can therefore replace any shared default with guidance that better fits that repository.

## What is intentionally not global

The baseline does not impose a shared license, CODEOWNERS file, funding configuration, formal governance model, support channel, project-specific CI, CLA/DCO requirement, labels, assignees, or repository-specific test commands. Those require project or account-specific decisions and should not be invented by a generic default.

Likewise, custom KGBos conventions around agents, decision gates, issue decomposition, deployment modes, and similar workflow rules are intentionally deferred to a later layer.

## Research

The comparison set and rationale for this baseline are recorded under [`docs/research/`](docs/research/).

## Repository self-governance

The `rulesets/`, `scripts/`, and `.github/workflows/apply-ruleset.yml` files manage this repository's own branch rules as code. They are implementation infrastructure for this repository, not inherited community-health defaults for other repositories.
