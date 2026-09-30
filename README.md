# KGBos Engineering Workflow

This repository is the shared governance and engineering workflow layer for KGBos repositories.

Its purpose is to keep common conventions in one place while allowing each repository to define only the rules that are specific to that project.

## Scope

This repository will define shared conventions for:

- issue types and issue forms
- parent/child issue decomposition
- dependency and blocking rules
- human decision gates
- pull request lifecycle and review
- agent workflow conventions
- deployment handoff and verification
- reusable GitHub workflows where appropriate

Repository-local files such as `AGENTS.md` remain responsible for project-specific architecture, commands, safety constraints, and exceptions.

## Rule precedence

1. Shared rules in `KGBos/.github`
2. Repository-specific rules
3. Issue-specific instructions

More-specific instructions override more-general instructions when they explicitly conflict.

## Research approach

The initial convention will be synthesized from mature public engineering repositories rather than invented from scratch. Source repositories will be normalized into a common comparison matrix so agreements become default candidates and genuine disagreements become explicit decision issues.

The comparison set will include organizations with strong public GitHub governance as well as AI-agent-heavy repositories such as OpenAI, Anthropic, and xAI.

## Status

Initial research and synthesis in progress.
