# KGBos shared GitHub defaults

This public `.github` repository provides shared GitHub community-health defaults for repositories owned by `KGBos` that do not define their own equivalent files.

The initial community-health baseline is intentionally conservative. It is assembled from established public GitHub patterns first; KGBos-specific workflow conventions are considered separately rather than being mixed into the generic defaults.

## Shared defaults

- `CODE_OF_CONDUCT.md` — common collaboration expectations
- `CONTRIBUTING.md` — generic contribution guidance
- `SECURITY.md` — private vulnerability-reporting guidance
- `.github/ISSUE_TEMPLATE/` — generic bug and feature Issue Forms
- `.github/PULL_REQUEST_TEMPLATE.md` — a lightweight pull-request template

GitHub gives repository-local community-health files precedence over these defaults. A project can therefore replace any shared default with guidance that better fits that repository.

## Development workflow baseline

[`docs/development-workflow.md`](docs/development-workflow.md) records a separate, neutral issue/branch/pull-request/CI/review/merge baseline derived primarily from conventional GitHub Flow and pull-request practice.

[`AGENTS.md`](AGENTS.md) is the agent-facing entry point for that baseline. Unlike GitHub community-health defaults, `AGENTS.md` is **not automatically inherited** by other repositories. Downstream repositories or agent runtimes must explicitly reference, copy, or synchronize it if they want to adopt it.

[`docs/documentation-standard.md`](docs/documentation-standard.md) is an
optional shared default for documentation structure, evidence, and review.
Repositories must explicitly adopt it; local technical and safety contracts
remain authoritative.

The development baseline deliberately stops short of KGBos-specific orchestration such as the conveyor-belt model, dispatcher behavior, named builder/reviewer roles, reviewer quorum, merge ownership, or deployment state machines. Those should be evaluated separately after the neutral baseline is exercised in real work.

## What is intentionally not global

The community-health baseline does not impose a shared license, CODEOWNERS file, funding configuration, formal governance model, support channel, project-specific CI, CLA/DCO requirement, labels, assignees, or repository-specific test commands. Those require project or account-specific decisions and should not be invented by a generic default.

Likewise, repository-specific architecture, build commands, release processes, deployment procedures, and ownership remain local even when a repository adopts the shared development workflow baseline.

## Research

The community-health comparison set and rationale are recorded under [`docs/research/`](docs/research/). The development workflow document records its own primary GitHub sources.

## Repository self-governance

The `rulesets/`, `scripts/`, and `.github/workflows/apply-ruleset.yml` files manage this repository's own branch rules as code. They are implementation infrastructure for this repository, not inherited community-health defaults for other repositories.
