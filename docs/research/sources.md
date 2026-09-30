# Research sources

This baseline was assembled from public repositories and current platform/community standards. The goal is to identify durable patterns, not to copy any one organization's process wholesale.

## Platform documentation

- GitHub Docs — default community health files: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
- GitHub Docs — Issue Forms syntax: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms
- GitHub Docs — issue and pull request templates: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates

Key platform behavior confirmed from the documentation:

- a public account-level `.github` repository can provide defaults to repositories that do not define their own equivalent files;
- repository-local files take precedence over account defaults;
- if a repository defines its own valid issue templates or issue-template configuration in `.github/ISSUE_TEMPLATE`, the default `ISSUE_TEMPLATE` folder is not merged with it;
- issue templates and their `config.yml` belong under `.github/ISSUE_TEMPLATE`;
- pull request templates can be stored in `.github`, the repository root, or `docs`;
- a default license cannot be inherited from the `.github` repository.

## Community standards

- Contributor Covenant 3.0 adoption guide: https://www.contributor-covenant.org/adopt/
- Contributor Covenant 3.0: https://www.contributor-covenant.org/version/3/0/

The shared `CODE_OF_CONDUCT.md` is an adaptation of Contributor Covenant 3.0 rather than a newly invented conduct framework. The adaptation keeps reporting and enforcement instructions appropriate for a personal GitHub account and includes the required attribution and license reference.

## Shared `.github` repositories studied

1. GitHub — https://github.com/github/.github
   - deliberately small community-health core plus profile and repository-lint policy
2. Microsoft — https://github.com/microsoft/.github
   - broad policy hub with security, organization policy, automation, dependency configuration, and profile metadata
3. Kubernetes — https://github.com/kubernetes/.github
   - minimal shared security and ownership/contact material
4. CNCF — https://github.com/cncf/.github
   - minimal organization-wide files and profile metadata
5. HashiCorp — https://github.com/hashicorp/.github
   - small shared code-of-conduct and security baseline
6. Home Assistant — https://github.com/home-assistant/.github
   - community-health documents, support/funding guidance, and profile metadata
7. Homebrew — https://github.com/Homebrew/.github
   - extensive shared automation/config synchronization, security policy, and community-health files
8. Angular — https://github.com/angular/.github
   - security/policy automation, organization synchronization, and dependency policy
9. Flutter — https://github.com/flutter/.github
   - detailed contribution, security, support, pull-request, and profile defaults
10. Fastify — https://github.com/fastify/.github
    - modern YAML Issue Forms, PR template, contribution/security guidance, and formal project governance
11. Sigstore — https://github.com/sigstore/.github
    - issue templates, PR template, community-health docs, profile, and workflow templates
12. Supabase — https://github.com/supabase/.github
    - issue templates, PR template, contribution/security docs, funding, and workflow templates

## Repo-local AI/product setups studied

These do not provide a public account-wide `.github` baseline, but they are useful evidence for what mature repositories keep local rather than centralizing.

13. OpenAI Codex — https://github.com/openai/codex
    - local Issue Forms, CODEOWNERS, workflows, actions, scripts, and dependency automation
14. Anthropic Claude Code — https://github.com/anthropics/claude-code
    - local Issue Forms, workflows, scripts, and security-related repository configuration
15. xAI Python SDK — https://github.com/xai-org/xai-sdk-python
    - local Issue Forms, PR template, CODEOWNERS, and workflows

## Interpretation rule

A pattern was treated as a baseline candidate when it was both broadly reusable and safe to apply across unrelated repositories. Organization-specific legal agreements, funding, formal governance, support destinations, labels, ownership maps, project commands, and specialized automation were not promoted to the shared baseline merely because a large project uses them.
