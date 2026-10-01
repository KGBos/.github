# Shared cross-repository agent dispatcher evaluation

Status: design evaluation only. This document does not migrate the existing `KGBos/homelab-infra` dispatcher or enable dispatch in additional repositories.

## Decision summary

A shared KGBos dispatcher is technically viable, but the reusable unit should be a **versioned validation/controller component**, not a centralized repository-wide runtime.

Recommended shape:

```text
repository-native event
        ↓
thin repo-local caller workflow
        ↓
shared dispatcher controller
(reusable workflow or versioned action)
        ↓
validated normalized dispatch request
        ↓
repo-local execution job / adapter layer
        ↓
repo-specific agent runtime
```

Keep repository-native state authoritative. A repository opts in explicitly and retains control of event triggers, routing, labels, adapters, runner placement, credentials, and execution policy.

Do not migrate the existing `homelab-infra` implementation yet. First prove the shared contract with a second repository or a test fixture so the extraction is driven by real cross-repository reuse rather than abstraction in advance.

## What is repo-agnostic

The current `homelab-infra` implementation contains a coherent generic core that can be extracted without knowing anything about its homelab services or named agent runtimes:

- parse supported GitHub events into a dispatch candidate;
- recognize an explicit command or dispatch label without executing free-form issue text;
- normalize repository, item type, item number, actor, target, source, and source identifier;
- construct a deterministic idempotency key;
- validate that exactly one target was requested;
- validate the target against a caller-supplied route map;
- validate actor authorization against a bounded policy supplied by the caller;
- compute lifecycle label transitions;
- produce a versioned normalized payload for downstream execution;
- format audit/status output;
- provide test fixtures for accepted, rejected, malformed, and duplicate requests.

These behaviors form a protocol/controller library. They do not need to know whether the eventual target is Hermes, Codex, Antigravity, a review bot, or something else.

## What must stay repository-specific

The following should remain local to each participating repository:

- which GitHub events are enabled as dispatch triggers;
- the target names exposed by that repository;
- target-to-adapter mappings;
- runner labels and runner placement;
- adapter implementations and runtime commands;
- target-specific environment variables;
- credentials, tokens, installation IDs, and private infrastructure details;
- authorized bot/App identities beyond any generic permission rule;
- lifecycle label names when a repository chooses different terminology;
- whether dispatch is permitted for issues, pull requests, review requests, or only a subset;
- operational retry policy and execution timeout;
- repository-specific maker/checker, reviewer, and merge rules.

The shared component must consume these as inputs rather than owning a global KGBos agent registry.

## Recommended reusable interface

Prefer a reusable workflow first, with a small library/action underneath it only if reuse warrants the extra packaging.

A caller should remain visibly responsible for its trigger:

```yaml
name: Agent dispatch

on:
  issues:
    types: [labeled]
  issue_comment:
    types: [created]

jobs:
  validate:
    uses: KGBos/.github/.github/workflows/agent-dispatch-controller.yml@<pinned-ref>
    with:
      route-config-path: .github/agent-dispatch.json
      event-kind: ${{ github.event_name }}
    secrets: inherit
```

The exact syntax is illustrative, not an implementation commitment. The important contract is that the caller owns `on:` and explicitly invokes a versioned shared controller.

The shared controller should return only normalized outputs needed by a subsequent local execution job, for example:

```json
{
  "schema_version": 1,
  "repo": "KGBos/example",
  "item_type": "issue",
  "item_number": 42,
  "actor": "KGBos",
  "target": "codex",
  "dispatch_source": "command",
  "idempotency_key": "..."
}
```

It should never return executable issue/comment text.

## Why event triggers remain local

GitHub reusable workflows are called by another workflow; they do not replace the repository's own event subscription. That is desirable here.

A tiny caller workflow makes opt-in explicit and lets each repository constrain its attack surface. One repository may permit `issues:labeled` and `/dispatch` comments, while another may intentionally support only one path.

The caller also provides a visible local audit point for permissions. The shared repository should not silently begin listening to events across all KGBos repositories.

## Authorization model

Use two layers:

1. **Generic rule:** accept human actors only when the caller can establish the required repository permission level.
2. **Repository policy:** accept explicitly configured GitHub App/bot identities only when present in that repository's local allowlist.

Do not maintain an organization-wide list of personal agent identities in `KGBos/.github` unless a future requirement proves that such centralized ownership is necessary.

The controller should fail closed when authorization cannot be established.

## Idempotency and concurrency

Treat concurrency and idempotency as separate controls.

- **Concurrency** serializes competing work for the same repository item.
- **Idempotency** prevents the same dispatch request from executing twice.

The normalized request should include a deterministic idempotency key derived from stable event identity plus repository/item/target context.

A shared library can define the key format, but the durable record of consumed keys must be owned by a storage mechanism that actually survives across jobs/runs. A runner-local `/tmp` file is useful for unit tests but is not a cross-run idempotency store.

Before extracting the current implementation, choose and test a durable mechanism. Reasonable GitHub-native options include a repository-visible state marker/comment, an artifact/cache with carefully defined semantics, or another explicit repository-owned state record. The choice should be evaluated for race behavior and retry ergonomics before being standardized.

## Security boundary for the public `.github` repository

Everything in this repository must be safe to expose publicly.

The shared implementation may contain:

- protocol schemas;
- event parsing and validation logic;
- lifecycle-state helpers;
- generic authorization logic;
- reusable workflows/actions;
- synthetic test fixtures;
- public documentation.

It must not contain:

- tokens or secrets;
- internal hostnames or private IPs;
- runner inventory that reveals private infrastructure unnecessarily;
- private API endpoints;
- agent credentials;
- target-specific shell commands that embed secrets;
- private infrastructure assumptions copied from `homelab-infra`.

Secrets should be resolved only in the caller repository and passed with the smallest possible permissions to the local execution layer.

## Relationship to the agent operating workflow

Dispatch answers one question: **how does an authorized repository event wake a configured execution target exactly once?**

The later agent operating workflow answers different questions: **who builds, who reviews, who may approve, who merges, and what constitutes done?**

Keep these separate.

The dispatcher may emit metadata such as `target=archer`, but it must not manufacture reviewer independence, approvals, merge authority, quorum, or ownership. Repository-local workflow/policy remains authoritative for those decisions.

## Migration strategy

Do not move `homelab-infra` code directly into this repository yet.

Use the following sequence:

1. Define a small versioned normalized-payload schema and configuration schema here.
2. Add controller contract tests using synthetic GitHub event fixtures.
3. Select one second repository or dedicated fixture repository and implement a thin local caller against the shared contract.
4. Compare both callers and identify genuinely duplicated code.
5. Extract only the duplicated generic controller functions into the shared implementation.
6. Run both repositories against a pinned shared version.
7. Only after parity and failure-mode testing, consider replacing the existing `homelab-infra` controller internals with the shared component.

This creates evidence for the abstraction before migration.

## Versioning and compatibility

Callers should pin the shared component to an immutable commit SHA or an intentionally managed major-version tag. Avoid floating `master` for security-sensitive dispatch logic.

The normalized payload and route-config formats should carry explicit schema versions. Additive fields may remain backward-compatible within a major version; removing or changing field semantics should require a new major version.

## Proposed local configuration boundary

A participating repository should keep a small configuration file, for example `.github/agent-dispatch.json`, containing only repository policy and routing data:

```json
{
  "schema_version": 1,
  "targets": {
    "codex": {
      "enabled": true,
      "adapter": "codex",
      "runner_tags": ["self-hosted", "agent-worker"]
    }
  },
  "authorized_bots": ["example-app[bot]"]
}
```

A shared schema may validate the shape, but the data remains local.

## Open questions before implementation

- Which durable GitHub-native idempotency store has acceptable race and retry behavior?
- Should the shared surface be only a reusable workflow, or a reusable workflow wrapping a composite/JavaScript/Python action?
- Which lifecycle/status operations belong in the shared controller versus the caller?
- Should actor authorization accept `maintain` in addition to `admin`/`write`, or should that remain caller-configurable?
- What is the smallest second-repository pilot that exercises the protocol without coupling dispatcher work to LiteFlix or the conveyor-belt process?

## Exit criteria for this evaluation

The design is ready for an implementation issue when:

- a durable idempotency mechanism is chosen;
- a second pilot repository or fixture is identified;
- the normalized payload/config schemas are agreed;
- the caller/shared responsibility boundary above is accepted;
- no migration of `homelab-infra` is required to begin the pilot.

Until then, `homelab-infra` remains the working reference implementation and this repository remains the design/coordination layer.