# Development workflow baseline

This document defines the neutral KGBos development workflow baseline.

It intentionally starts with conventional GitHub Flow and pull-request practice before adding any KGBos-specific orchestration, agent roles, conveyor-belt stages, deployment states, or merge-ownership rules.

The goal is to establish a boring default, use it in real repositories, and add extra process only when a concrete problem justifies it.

## Baseline flow

```text
tracked work
    ↓
short-lived branch
    ↓
implement + verify
    ↓
pull request
    ↓
automated checks
    ↓
review + feedback
    ↓
merge
    ↓
follow-up / cleanup
```

### 1. Start from clear work

For non-trivial changes, begin from an issue, task, bug report, or other durable description of the problem and expected result.

Very small maintenance changes may begin directly when a separate issue would add no useful context. Repositories may require issue-first work locally.

Before changing code, read the repository's contribution guidance and agent instructions. Repository-local instructions are authoritative for repository-specific commands, architecture, ownership, and safety constraints.

### 2. Work on a short-lived branch

Create a branch from the current default branch and keep the work isolated from the protected branch.

Prefer one coherent change per branch. Avoid mixing unrelated cleanup or feature work into the same pull request.

If the work becomes too large to review safely, split it into independently understandable changes where practical. Stacked pull requests are acceptable when the repository and tooling support them.

### 3. Implement and verify before review

Make the smallest change that satisfies the intended behavior.

Before requesting review:

- inspect the resulting diff;
- run the relevant local tests, linters, formatters, or validation commands documented by the repository;
- update tests and documentation when behavior changes;
- remove accidental, generated, debug, or unrelated changes.

An agent should review its own diff before handing work off. Self-review is a quality-control step, not a substitute for an independent review when one is required.

### 4. Open a pull request

Use a pull request to propose the change to the default branch.

A useful pull request explains:

- what changed;
- why it changed;
- the related issue or context when one exists;
- how the change was verified;
- any material limitations, risks, or follow-up work.

Opening a draft pull request early is reasonable when early visibility or collaboration is useful. A repository may choose to wait until implementation is ready instead.

Keep out-of-scope findings separate rather than continuously expanding the current pull request. Open or link follow-up issues when appropriate.

### 5. Let automated checks validate the current head

Continuous integration, builds, tests, linters, security checks, and other repository-required status checks should run against the pull request's current head.

Do not treat checks from an older commit as evidence for a newer revision. When a required check fails, investigate the failure rather than bypassing it unless the repository has an explicit exception process.

Repositories should use branch protection or rulesets when they need these requirements enforced rather than relying only on convention.

### 6. Review and incorporate feedback

Review should focus on correctness, security, maintainability, scope, test evidence, and consistency with repository guidance.

When review identifies a problem, update the same branch and pull request unless the feedback is intentionally out of scope. Re-request review after substantial changes when appropriate.

Resolve meaningful review conversations before merge. Repository rules determine whether an approval is required and who is eligible to provide it.

For agent-authored work, an independent human or agent review can provide useful separation between implementation and checking, but this baseline does not prescribe a specific reviewer identity, quorum, or merge owner. Those are repository or later KGBos policy decisions.

### 7. Merge only when the repository's gates are satisfied

Merge when:

- the change is in scope and ready;
- merge conflicts are resolved;
- required automated checks have completed successfully;
- required reviews or approvals are satisfied;
- no unresolved blocking feedback remains.

Use the repository's configured merge method. This baseline does not require merge commits, squash merges, rebases, a merge queue, or a particular person or agent to press the merge button.

Delete the working branch after merge when it is no longer needed.

### 8. Keep post-merge work explicit

Link or close the originating issue when the merged change satisfies it.

Deployment, release, production verification, rollback, and operational monitoring are separate concerns unless the repository explicitly includes them in its pull-request lifecycle.

If a merged change reveals new work, create a follow-up issue rather than silently extending the definition of done after the fact.

## What this baseline deliberately does not decide

The following are intentionally left to repository-local policy or a later shared KGBos layer:

- which agent claims or implements work;
- automatic dispatch or assignment;
- maker/checker role names;
- reviewer quorum;
- who has merge authority;
- exact pull-request size limits;
- required issue taxonomy or labels;
- deployment state machines;
- release cadence;
- environment-specific verification;
- repository-specific test commands;
- CODEOWNERS or component ownership;
- whether every change must have a pre-existing issue.

These may be valuable, but they should be introduced because they solve observed problems rather than being assumed as part of the neutral baseline.

## Agent instruction boundary

The canonical shared agent entry point is [`../AGENTS.md`](../AGENTS.md).

`AGENTS.md` is not a GitHub default community-health file and is not automatically inherited by repositories owned by `KGBos`. A repository or agent runtime must explicitly reference, copy, or synchronize the shared instructions if it wants to use them. Repository-local and more-specific instructions take precedence for the files they govern.

## Basis

This baseline is primarily derived from GitHub's documented GitHub Flow and pull-request model:

- GitHub Flow: https://docs.github.com/en/get-started/using-github/github-flow
- About pull requests: https://docs.github.com/en/pull-requests/get-started/about-pull-requests
- Status checks: https://docs.github.com/en/pull-requests/reference/status-checks
- Protected branches: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- Resolving reviews: https://docs.github.com/en/pull-requests/concepts/resolving-reviews

The baseline adapts that human collaboration model to agent-authored changes without introducing additional KGBos-specific orchestration yet.
