# Shared CI runner policy

**Status:** Accepted policy direction; rollout and live readiness remain
unverified.

## Decision

The designated self-hosted runner host is the sole host for CI across the
repositories we work on. GitHub-hosted Actions and other hosts are not
fallback capacity. If the runner host is unavailable, CI must remain visibly
queued or fail; it must not silently reroute to a different host.

GitHub-hosted Actions minutes have routinely run out before the monthly reset.
This policy accepts the availability tradeoff of depending on the runner host
rather than treating exhausted hosted minutes as a reason to move work to a
different host.

This document does not change any repository's workflows or settings. Each
repository retains its own event triggers, commands, token permissions, and
required checks, while its runner selection must conform to this policy. Each
repository must explicitly adopt this policy and select a runner group scoped
to that repository on the runner host. This shared document does not
automatically configure GitHub Actions or inherit into another repository.

## Repository adoption record

Each participating repository keeps its adoption record at
`docs/ci-runner-adoption.md`, in the same reviewed change that adopts this
policy. Keep one record in that repository; do not build a public central
inventory in this repository. The local record must contain:

- **Policy revision:** the exact `.github` commit SHA being adopted.
- **Repository and runner scope:** that repository's full slug, the permitted
  runner group, and evidence that the group's repository allowlist includes
  only authorized participants.
- **Accountable owner:** the maintainer responsible for adoption and upkeep.
- **Explicit acceptance:** the accepting maintainer, date, and issue or PR link
  that records acceptance. Do not infer acceptance from a merge or a bot's
  implementation.
- **Workflow scope:** the adopting workflow/job names and the policy boundary
  each uses; note any CI jobs intentionally disabled or not yet migrated.
- **Current-head CI evidence:** run URL, exact tested commit SHA, workflow/job,
  result, and evidence of the runner group/host used. Evidence must be for the
  current PR head before merge and for the resulting default-branch commit
  after adoption.
- **Readiness evidence:** links and pass/fail/not-tested results for each
  control in the readiness checklist below, with observation date and
  independent verifier.
- **Exceptions:** write `none`, or record the approved exception's scope,
  reason, compensating controls, approver, approval link, and expiry/review
  date. An exception cannot authorize another runner host, remove the
  no-fallback rule, or weaken the untrusted-job trust boundary.

Do not include credentials, secret values, or a list of other repositories in
an adoption record. Keep necessary repository-specific evidence in that
repository and redact sensitive details from public records.

## Untrusted pull-request jobs

Treat pull-request code as untrusted until it has been reviewed. Run each
untrusted job in fresh, disposable isolation on the runner host, and destroy
that isolation after the job, including canceled jobs. Reusing an ephemeral
runner registration alone does not prove per-job isolation.

Untrusted jobs must not:

- execute directly on a persistent host operating system;
- access host filesystems, mounts, sockets, credentials, or other host state;
- receive repository or organization secrets or host credentials;
- reach the LAN or tailnet; or
- reuse mutable runner state from another job.

The runner group and repository allowlist must be explicit and limited to the
repositories that have adopted this policy. Do not encode a private repository
inventory in this public document. A workflow must not add GitHub-hosted or
alternate-host fallback behavior.

## Rollout and verification boundary

Before any repository rolls out this policy, an independent reviewer must
verify the configured runner-group and repository scope and the isolation
controls above. The repository's adoption record must link current, observable
evidence for each item and record `pass`, `fail`, or `not tested`:

1. **Fresh per-job isolation:** Record the isolation mechanism, immutable
   image/version identifier, and job/run ID to environment ID mapping. A
   harmless marker created in one job must be absent in a later job; evidence
   must show a new environment for each job.
2. **Cleanup, including cancellation:** Record a successful run and a
   deliberately canceled non-sensitive run. After each, verify that the
   disposable environment is destroyed, any job-scoped runner registration
   is removed, and no job process or writable environment remains available
   for reuse.
3. **Host boundary:** Review the isolation configuration for host filesystem
   mounts, container/VM sockets, host credentials, and other host state. From
   inside the job, verify that representative host paths and sockets are
   inaccessible. Do not expose host paths or credential details in public
   evidence.
4. **Secret exclusion:** Review the untrusted-job workflow and its configured
   environments to verify that repository/organization secrets and host
   credentials are not passed or mounted. Record configuration evidence, not
   secret names or values.
5. **LAN and tailnet denial:** Record the network isolation/egress policy and
   controlled probes from a job showing that LAN and tailnet test destinations
   are unreachable. Redact addresses or names when they reveal private
   infrastructure.
6. **No cross-job mutable state:** Record the marker test and verify that
   runner-local files, processes, and writable layers are not visible to a
   later job. Any separately managed cache or artifact must be explicit and
   must not provide a path to host state.
7. **No fallback when the runner host is unavailable:** In a controlled
   non-production scheduling check, make no eligible runner available.
   Verify the check remains queued or fails and that no GitHub-hosted
   or alternate-host job starts. Record the run/check URL and tested commit.

The independent verifier records their identity, date, evidence links, and
result in the adoption record. The verifier must be distinct from the PR
author. A `not tested` or failed item blocks rollout.
Do not run these checks against production or expose untrusted code to a
persistent host to obtain evidence.

This policy is a target, not evidence that a runner is registered, correctly
scoped, isolated, or ready. Publishing it does not authorize runner
provisioning or registration, host configuration, workflow rollout, merge, or
deployment. Those actions require their own scoped authorization and
verification. Each participating repository must record its adoption and
current-head CI evidence in its own reviewed change. Do not publish private
repository inventories or sensitive runner details here.
