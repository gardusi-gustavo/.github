#!/usr/bin/env python3
"""Apply the standard main-protection ruleset to every repository.

Requires an administration credential in GH_TOKEN (fine-grained: Administration
write on all selected repositories, or a classic token with repo scope). SSH
cannot do this; the rulesets API is authenticated only.

Usage:

    GH_TOKEN=... python3 scripts/apply_rulesets.py --check
    GH_TOKEN=... python3 scripts/apply_rulesets.py --apply --yes
    GH_TOKEN=... python3 scripts/apply_rulesets.py --apply --yes --repo package-go
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
CHECKS = ROOT / "docs" / "rulesets" / "main.json"
NO_CHECKS = ROOT / "docs" / "rulesets" / "main-no-checks.json"
WORKSPACE = "https://raw.githubusercontent.com/gardusi-gustavo/contract-json/main/governance/workspace.json"
NAME = "main-protection"
SKIP = {"gardusi-gustavo/workflow-event", "gardusi-gustavo/workflow-manual",
        "gardusi-gustavo/workflow-scheduled", "gardusi-gustavo/.github"}


def repos(only: list[str]) -> list[str]:
    if only:
        return [r if "/" in r else f"gardusi-gustavo/{r}" for r in only]
    req = urllib.request.Request(WORKSPACE, headers={"User-Agent": "opencode"})
    data = json.load(urllib.request.urlopen(req))
    found = []
    for domain in data.get("domains", []):
        for name in domain.get("repos", []):
            slug = f"gardusi-gustavo/{name}"
            if slug not in SKIP:
                found.append(slug)
    return found


def gh(args: list[str], stdin: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["gh", *args], input=stdin, text=True,
                          capture_output=True, timeout=120)


def has_caller(slug: str) -> bool:
    p = gh(["api", f"repos/{slug}/contents/.github/workflows/event-pull-request.yml",
            "--jq", ".name"])
    return p.returncode == 0


def existing(slug: str) -> int | None:
    p = gh(["api", f"repos/{slug}/rulesets", "--jq",
            f'.[] | select(.name=="{NAME}") | .id'])
    if p.returncode != 0 or not p.stdout.strip():
        return None
    return int(p.stdout.strip().splitlines()[0])


def apply_one(slug: str, yes: bool) -> str:
    if os.environ.get("GH_TOKEN") is None:
        return "GH_TOKEN is missing"
    source = CHECKS if has_caller(slug) else NO_CHECKS
    body = source.read_text(encoding="utf-8")
    rid = existing(slug)
    action = "update" if rid else "create"
    if not yes:
        return f"would {action} from {source.name}"
    method = "PUT" if rid else "POST"
    path = f"repos/{slug}/rulesets/{rid}" if rid else f"repos/{slug}/rulesets"
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
        handle.write(body)
        name = handle.name
    try:
        p = gh(["api", "--method", method, path, "--input", name])
    finally:
        os.unlink(name)
    if p.returncode != 0:
        return f"failed: {p.stderr.strip()[:80]}"
    return f"{action}d"


def main() -> int:
    parser = argparse.ArgumentParser(prog="apply_rulesets.py", description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--apply", action="store_true")
    parser.add_argument("--yes", action="store_true")
    parser.add_argument("--repo", action="append", default=[])
    args = parser.parse_args()

    targets = repos(args.repo)
    for slug in targets:
        try:
            print(f"{slug:50} {apply_one(slug, args.apply and args.yes)}")
        except Exception as exc:
            print(f"{slug:50} error: {exc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
