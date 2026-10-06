# Shared documentation standard

This is the default for documentation changes in KGBos repositories that
explicitly adopt it. Repository-specific instructions and domain contracts
take precedence. This guide supplies a common writing and review method; it
does not replace local architecture, operations, security, or verification
rules.

## Write for a reader's task

Before drafting or revising a page, identify its reader and the job they need
to do. Use [Diátaxis](https://diataxis.fr/) to keep the page focused:

- **Tutorial:** guide a learner through a first successful experience.
- **How-to:** help a reader who already has context complete a specific task.
- **Reference:** state exact facts, interfaces, configuration, or contracts.
- **Explanation:** help a reader understand why a system or decision works as
  it does.

Use the type that helps readers. Do not create empty folders or split pages
just to match a diagram. Keep project-specific exceptions where readers will
find them.

## Make claims traceable

Treat generated prose as a draft, not as evidence. Check every important claim
against the source that owns it:

- Link to repository files, configuration, code, or tests for repository
  behavior. Prefer a stable file or section link over a line number that will
  drift.
- Use official, version-matched upstream documentation for external product
  behavior. Record the relevant version when behavior is version-sensitive.
- For live state, record the host or system, observation time, command or
  method, and result in the repository's dated evidence location. A checked-in
  desired-state file does not prove the running system matches it.
- Label proposals, historical observations, and unverified procedures so they
  cannot be mistaken for accepted policy or current live state.

Keep each fact in one authoritative place and link to it elsewhere. When an
important fact changes, update its owner and the affected dependent docs in the
same change. Preserve historical evidence as evidence; do not rewrite an old
result to make it appear current.

## Review AI-assisted drafts

Treat AI-written text as an unverified draft. Before accepting it:

- Remove repeated explanations; each section should add information.
- Trace factual claims to the code, configuration, tests, or authoritative
  documentation that supports them. Do not keep plausible-sounding guesses.
- Verify command syntax, API fields, paths, UI labels, and version details
  against their source. Do not fill gaps by inventing specifics.
- Check whether the information belongs in an existing page or authoritative
  document before creating a new page or duplicating a contract.
- Label proposals, assumptions, and unverified examples so readers can tell
  them apart from confirmed behavior.

## Write usable procedures

For a procedure, include the prerequisites, target and scope, ordered steps,
expected result, failure or stop conditions, and recovery or rollback path when
one exists. Make destructive or externally visible actions unmistakable and
follow the repository's approval rules. Show commands in enough context that a
reader knows where and as whom to run them. Do not imply a command was tested
when it was only generated or reviewed.

Validate examples against the owning implementation when practical. Run
procedures only in a safe, isolated environment; do not touch production just
to make documentation appear verified. If a procedure has not been rehearsed,
say so and identify the remaining acceptance step.

## Use clear, consistent language

Use the [Google developer style guide](https://developers.google.com/style) as
a reference for clarity, grammar, formatting, and terminology. Prefer direct,
active sentences, familiar terms, descriptive headings, and examples that can
be understood without guessing. Follow a repository's established vocabulary
and explain unavoidable jargon. Project-specific style wins when it makes the
documentation clearer for that project's readers.

## Format Markdown source

Wrap prose near 80 columns to keep source files and diffs readable. This is a
source-formatting convention, not a limit on rendered page width: keep normal
paragraphs intact and do not add hard breaks just to control how text appears
in a viewer. Keep links, headings, tables, and code readable; do not split a
link or code token just to meet the column target.

## Review according to risk

Review the documentation in the same change as the behavior or policy it
describes. At minimum, check the intended reader and purpose, authority and
evidence for consequential claims, links, copied commands and examples, and
consistency with related contracts.

Spend the most review effort on recovery, security, data handling, deployment,
access, and other instructions where a wrong step can cause harm or lockout.
Repository policy decides who must review and what verification is required;
this shared standard does not add a global approval role or merge gate.

Use available checks for mechanical errors such as broken local links,
formatting, and examples with automated validation. Passing a linter or link
checker proves only the checks it ran; it does not prove a claim is true or a
runbook works against a live system.

## Documentation change checklist

- [ ] The page has a clear reader, purpose, and owning location.
- [ ] AI-assisted text was checked for repetition, unsupported claims, invented
      specifics, and misplaced or duplicated content.
- [ ] Important claims have an identifiable source; live observations are
      dated and separated from intended state.
- [ ] Instructions include scope, expected results, and relevant stop or
      recovery conditions.
- [ ] Related docs link to the authority instead of copying facts that can
      drift.
- [ ] Relevant repository checks were run, or the unrun checks and reason are
      stated accurately.
