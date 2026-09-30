#!/usr/bin/env python3
"""Reconcile a repository ruleset from a checked-in JSON definition."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

API_VERSION = "2026-03-10"
DEFAULT_RULESET = Path("rulesets/master-protection.json")


def request_json(method: str, url: str, token: str, payload: dict[str, Any] | None = None) -> Any:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("X-GitHub-Api-Version", API_VERSION)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            return json.loads(body) if body else None
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {method} {url} failed: HTTP {exc.code}: {detail}") from exc


def desired_matches_current(desired: Any, current: Any) -> bool:
    """Return True when every desired field is present with the same value."""
    if isinstance(desired, dict):
        return isinstance(current, dict) and all(
            key in current and desired_matches_current(value, current[key])
            for key, value in desired.items()
        )
    if isinstance(desired, list):
        return isinstance(current, list) and len(desired) == len(current) and all(
            desired_matches_current(left, right) for left, right in zip(desired, current)
        )
    return desired == current


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY"), help="owner/repo")
    parser.add_argument("--ruleset", type=Path, default=DEFAULT_RULESET)
    parser.add_argument("--dry-run", action="store_true", help="validate and print desired state without API calls")
    args = parser.parse_args()

    desired = json.loads(args.ruleset.read_text(encoding="utf-8"))
    required = {"name", "target", "enforcement", "conditions", "rules"}
    missing = sorted(required - desired.keys())
    if missing:
        raise SystemExit(f"ruleset is missing required keys: {', '.join(missing)}")

    if args.dry_run:
        print(json.dumps(desired, indent=2, sort_keys=True))
        return 0

    if not args.repo or "/" not in args.repo:
        raise SystemExit("repository is required via --repo owner/repo or GITHUB_REPOSITORY")

    token = os.environ.get("RULESET_ADMIN_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        raise SystemExit(
            "missing RULESET_ADMIN_TOKEN (or GH_TOKEN); applying repository rulesets requires Administration: write permission"
        )

    base = f"https://api.github.com/repos/{args.repo}/rulesets"
    rulesets = request_json("GET", f"{base}?includes_parents=false", token)
    existing = next((item for item in rulesets if item.get("name") == desired["name"]), None)

    if existing is None:
        created = request_json("POST", base, token, desired)
        print(f"created ruleset {created['id']}: {desired['name']}")
        return 0

    ruleset_id = existing["id"]
    current = request_json("GET", f"{base}/{ruleset_id}?includes_parents=false", token)
    if desired_matches_current(desired, current):
        print(f"ruleset {ruleset_id} already matches desired state")
        return 0

    request_json("PUT", f"{base}/{ruleset_id}", token, desired)
    print(f"updated ruleset {ruleset_id}: {desired['name']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
