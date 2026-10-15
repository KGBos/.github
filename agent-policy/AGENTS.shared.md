# Shared agent baseline

This policy is the portable development baseline for KGBos repositories. Repository-specific instructions and direct task requirements take precedence where they are more specific. Read the most specific applicable `AGENTS.md` before changing files.

## Load instructions after checkout

- If a repository, worktree, or checkout appears after the conversation starts, read its root `AGENTS.md` and all applicable nested `AGENTS.md` files before inspecting or editing project files.
- Do not assume the agent runtime discovers repository instructions retroactively after a clone or checkout.
- When an applicable instruction points to another document, open and read that document. A link alone does not mean its contents were loaded.

## Work from clear scope

- Start non-trivial work from a tracked issue, task, bug report, or other durable description when the repository requires one or it adds useful context.
- Read the repository's contribution guidance and relevant project documentation before implementation.
- Keep the change focused on the requested outcome. Track unrelated findings separately.
- Work on a short-lived branch from the repository's current default branch; keep protected branches deployable.

## Implement and verify

- Make the smallest change that satisfies the requested behavior.
- Before handoff, inspect the diff and run the relevant verification commands documented by the repository.
- Update tests and documentation when they help preserve the behavior or explain an important decision.
- Report the exact checks run and any material limitations. Never claim checks, reviews, deployments, or production verification that did not happen.

## Pull requests and review

- Use a pull request to propose a coherent change. Explain what changed, why, related context, verification evidence, and material limitations.
- A draft pull request may be used for work in progress. Follow repository-specific criteria for when it is ready for review.
- Required automated checks must pass on the current pull-request head. Investigate failures rather than bypassing them unless the repository defines an explicit exception.
- Address substantive review feedback and resolve blocking conversations before merge.
- Merge only when the repository's required checks, approvals, and other gates are satisfied. Authoring a change does not grant approval or merge authority.
- Deployment, release, and production acceptance are separate from merge unless the repository explicitly includes them in its definition of done.

## Repository and agent boundaries

- Follow the most specific applicable repository instructions for architecture, commands, ownership, safety, review readiness, and deployment.
- Do not assume `AGENTS.md` is automatically inherited across repositories or supported identically by every agent runtime. Repositories adopting this baseline should check in a generated copy with their local rules.
- Keep personal preferences in the user's own agent configuration; do not move private preferences into shared repository policy.
