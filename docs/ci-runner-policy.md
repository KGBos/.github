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
controls above. Verification must establish that each job starts in fresh
isolation, that the isolation is destroyed afterward, and that host access,
secrets, LAN/tailnet reachability, and cross-job mutable state are unavailable
to untrusted code. The review must also confirm that the runner host's
unavailability leaves CI visibly queued or failed with no alternate-host
fallback.

This policy is a target, not evidence that a runner is registered, correctly
scoped, isolated, or ready. Publishing it does not authorize runner
provisioning or registration, host configuration, workflow rollout, merge, or
deployment. Those actions require their own scoped authorization and
verification. Each participating repository must record its adoption and
current-head CI evidence in its own reviewed change. Do not publish private
repository inventories or sensitive runner details here.
