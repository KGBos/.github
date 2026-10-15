# Pull request review standard and guidelines

This document defines the shared standard for reviewing pull requests across KGBos repositories. It provides human and agent reviewers with a consistent structure for review summaries, verdicts, and optional inline priority tags.

Repository-specific instructions (such as `AGENTS.md` and local deployment or architecture contracts) take precedence over this shared baseline.

---

## 1. Principles of independent review

1. **Maker-Checker separation**: The author of a change must never act as the independent reviewer of their own pull request. When an AI agent authors a pull request, the review must be conducted by a human or a dedicated reviewer agent running in a separate, isolated context with its own identity.
2. **Adversarial & objective inquiry**: Reviewers must actively check for logic regressions, edge cases, error-handling gaps, race conditions, and security risks rather than assuming the code works because CI is green.
3. **Verify what was run, not what was assumed**: Reviewers must state the exact evidence gathered—including specific commands, test suites, or manual reproductions—and explicitly note any constraints or tests that were not run.
4. **Exact-head verification**: Review verdicts apply strictly to the specific commit SHA evaluated. Any subsequent push requires checking the new diff.

---

## 2. Review verdicts and gates

Every pull request review must conclude with an explicit GitHub review verdict:

| Verdict | Meaning | When to use |
|---|---|---|
| **`APPROVE`** | Satisfies quality gates | The change meets requirements, improves code health, has verified test evidence, and has no unresolved blocking findings. |
| **`REQUEST_CHANGES`** | Blocks merge | A material defect, security vulnerability, regression, broken contract, or missing required test was found. |
| **`COMMENT`** | Advisory / informational | Feedback, clarifying questions, or architectural observations where the reviewer is not formally blocking or approving. |

---

## 3. Top-level review template

Review summaries should be structured, concise, and informative. When posting a formal review on GitHub, follow this template:

```markdown
### Code Review: PR #<number> — `<title>`

**Reviewer**: `<name or app/bot-identity>`
**Reviewed commit**: `<full or short SHA>`
**Verdict**: **APPROVE** | **REQUEST CHANGES** | **COMMENT**

---

### 1. Summary & scope assessment
<A plain-English evaluation of what the PR accomplishes, whether the scope is focused, and whether it aligns with related issues and repository architecture.>

### 2. Verification & test evidence
<Concrete evidence of what was tested or run:>
- `bash scripts/test`: **PASS** (<details on test suites run>)
- `git diff --check origin/master...HEAD`: **Clean**
- <Any manual scenario reproduction, benchmark, or tool output>
- *(Explicitly note any skipped checks or unverified environments)*

### 3. Actionable findings overview
<Summary of key findings, categorized by severity (P0–P3). If no blockers were found, state: "No blocking issues identified.">

- **Blocking (P0/P1)**: <Description or link to inline comment>
- **Non-blocking (P2/P3 / Nits)**: <Description or link to inline comment>

### 4. Next steps
<Clear statement of who owns the next action: e.g., author to address feedback, or maintainer ready for merge.>
```

---

## 4. Inline comment priority tags (optional)

When leaving comments on specific diff lines, reviewers are strongly encouraged—though not strictly required—to prefix comments with **colored severity badges**.

These tags make comment priority instantly visible to authors, distinguishing release-blocking defects from optional stylistic nits.

### Severity levels

| Severity | Color | Meaning & action |
|---|---|---|
| **P0 — Critical** | Dark Red | Immediate severe harm, data loss, active security exposure, or total service outage. Must request changes and block merge. |
| **P1 — High** | Red / Orange | Likely material correctness defect, security vulnerability, concurrency bug, or broken invariant. Must request changes and block merge. |
| **P2 — Medium** | Yellow / Orange | Meaningful edge-case weakness, unhandled return code, or latent maintainability concern. Blocks merge only if it directly defeats the PR's core purpose. |
| **P3 — Low / Nit** | Blue | Minor style preference, documentation clarification, formatting, or optional refactoring suggestion. Advisory; does **not** block merge. |

### Rendered Markdown badge syntax

GitHub does not have native color tags for review comments. Use static [Shields.io](https://shields.io) Markdown image badges. These URLs contain no private repository data, commit SHAs, or client information.

#### Style A: Full label badge
```markdown
![P0 Critical](https://img.shields.io/badge/P0-Critical-darkred)
![P1 High](https://img.shields.io/badge/P1-High-red)
![P2 Medium](https://img.shields.io/badge/P2-Medium-orange)
![P3 Low](https://img.shields.io/badge/P3-Low-blue)
```

**Preview:**
- ![P0 Critical](https://img.shields.io/badge/P0-Critical-darkred)
- ![P1 High](https://img.shields.io/badge/P1-High-red)
- ![P2 Medium](https://img.shields.io/badge/P2-Medium-orange)
- ![P3 Low](https://img.shields.io/badge/P3-Low-blue)

#### Style B: Compact inline header badge
```markdown
**<sub><sub>![P1 Badge](https://img.shields.io/badge/P1-orange?style=flat)</sub></sub>  <Finding title>**
**<sub><sub>![P2 Badge](https://img.shields.io/badge/P2-yellow?style=flat)</sub></sub>  <Finding title>**
**<sub><sub>![P3 Badge](https://img.shields.io/badge/P3-blue?style=flat)</sub></sub>  <Finding title>**
```

### Inline comment example

```markdown
**<sub><sub>![P1 Badge](https://img.shields.io/badge/P1-orange?style=flat)</sub></sub>  Shared lock is not held across the full cleanup routine**

`cleanup()` calls `rm -rf -- "${STAGING_ROOT}"` after releasing file descriptor 9.
If a concurrent backup process launches during this window, it can acquire the
lock and begin writing to the staging root while this instance is still deleting it.

**Suggested fix:** Keep the lock held until process exit, and ensure `STAGING_OWNED_BY_US`
is evaluated inside the trap before any destructive file operation.
```

---

## 5. Thread resolution etiquette

1. **Authors fix, reviewers verify**: Authors should reply to inline review comments with the fixing commit SHA and a brief explanation of what changed, but should **not** resolve the thread.
2. **Reviewers resolve**: The independent reviewer inspects the fix against the new head commit, verifies the test evidence, and clicks **Resolve conversation**.
3. **No phantom comments**: Reviewers should only post inline comments where genuine, actionable feedback exists. Do not fabricate inline comments to meet a quota. If there are no line-level findings, state *"No actionable inline findings"* in the top-level review.
