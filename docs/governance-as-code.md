# Governance as code

Repository governance should be reviewable and version controlled. The checked-in ruleset JSON is the desired state; GitHub repository settings are deployed state.

## Master protection

`rulesets/master-protection.json` protects `master` by:

- requiring changes to reach `master` through a pull request;
- blocking branch deletion; and
- blocking force pushes.

The initial policy intentionally does not require approvals, status checks, or code-coverage thresholds. Those can be added later through normal pull requests when the corresponding workflow is mature.

## Applying the ruleset

`.github/workflows/apply-ruleset.yml` runs after relevant policy files land on `master` and calls `scripts/reconcile-ruleset.py`.

The helper is idempotent: it creates the named repository ruleset if it does not exist, updates it when the desired state changes, and exits without changing anything when the live ruleset already matches.

## Credential requirement

Create a repository Actions secret named `RULESET_ADMIN_TOKEN` containing either:

- a fine-grained personal access token with **Administration: write** permission for this repository; or
- a GitHub App installation token with equivalent repository administration permission.

The normal workflow `GITHUB_TOKEN` is not assumed to have the administration permission required to manage repository rulesets. If `RULESET_ADMIN_TOKEN` is missing, deployment fails clearly instead of silently skipping governance changes.

Do not commit credentials to this repository.

## Local validation

The desired JSON can be validated without credentials or API calls:

```bash
python3 scripts/reconcile-ruleset.py --dry-run
```

After the admin credential is configured, the workflow reconciles the live GitHub ruleset after changes merge to `master`.
