# Governance research sources

This document tracks the public repositories being studied before KGBos conventions are finalized.

## Centralized `.github` examples

### GitHub — `github/.github`
Public shared repository with a deliberately small set of organization-wide community health files such as `CONTRIBUTING.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md`.

Source: https://github.com/github/.github

### Microsoft — `microsoft/.github`
A much broader shared repository containing organization policy configuration, security guidance, automation, and shared repository standards.

Source: https://github.com/microsoft/.github

### Kubernetes — `kubernetes/.github`
A minimal shared repository described as providing default files across the Kubernetes organization. It emphasizes security/contact and ownership metadata rather than a large workflow framework.

Source: https://github.com/kubernetes/.github

### CNCF — `cncf/.github`
A public organization-wide repository used for shared project files and public organization metadata.

Source: https://github.com/cncf/.github

## AI-heavy repo-local examples

### OpenAI — `openai/codex`
No public `openai/.github` repository was found during the initial survey. Codex keeps substantial GitHub machinery locally, including issue templates, `CODEOWNERS`, workflows, scripts, actions, and dependency automation.

Source: https://github.com/openai/codex

### Anthropic — `anthropics/claude-code`
No public `anthropics/.github` repository was found during the initial survey. Claude Code keeps issue templates, scripts, workflows, and repository-specific GitHub configuration locally.

Source: https://github.com/anthropics/claude-code

### xAI — `xai-org/xai-sdk-python`
No public `xai-org/.github` repository was found during the initial survey. The Python SDK keeps `CODEOWNERS`, issue templates, a pull-request template, and workflows locally.

Source: https://github.com/xai-org/xai-sdk-python

## Early synthesis questions

The initial sample already exposes several real design choices:

1. Should the shared `.github` repository stay intentionally minimal, or become the broad engineering-policy hub?
2. Which conventions belong centrally versus in repository-local `AGENTS.md` or `.github/` files?
3. Which shared rules should be documentation only, and which should be enforced through GitHub automation?
4. How should human decisions block and later unblock agent work?
5. How aggressively should parent/child issues be used to decompose independently reviewable work?

These questions should be resolved from the wider comparison set rather than by copying any single organization.
