#!/usr/bin/env python3
"""Check or apply the two caller workflows in every repository.

Every consumer repository carries exactly:

    .github/workflows/pr.yml       pull_request
    .github/workflows/release.yml  push tags

Both are byte-identical to ``templates/callers``. Logic lives in this repository.

Usage:

    sync_workflows.py --check
    sync_workflows.py --check --json
    sync_workflows.py --apply --yes
    sync_workflows.py --apply --yes --repo package-go
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import subprocess
import sys

GH_HOME = pathlib.Path(os.environ.get("GH_HOME", pathlib.Path.home() / ".config" / "gh"))
REGISTRY = pathlib.Path(os.environ.get("WORKSPACE_GH_REGISTRY", GH_HOME / "registry.json"))
TEMPLATES = pathlib.Path(__file__).resolve().parents[1] / "templates" / "callers"
TARGETS = {
    "pr.yml": pathlib.Path(".github/workflows/pr.yml"),
    "release.yml": pathlib.Path(".github/workflows/release.yml"),
}
LEGACY = pathlib.Path(".github/workflows/pipeline.yml")
BRANCH = "workflow/callers"
EXCLUDE = {
    "gardusi-gustavo/package-yml",
    "gardusi-gustavo/gardusi-gustavo",
    "gardusi-gustavo/contract-wit",
}


def load_registry() -> dict:
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def repos(reg: dict, only: list[str] | None = None):
    for domain in reg.get("domains", []):
        for repo in domain.get("repos", []):
            name = repo["github"].split("/")[-1]
            if only and name not in only:
                continue
            if repo["github"] in EXCLUDE:
                continue
            path = pathlib.Path(repo["path"])
            if path.is_dir():
                yield repo["github"], domain["config_dir"], path


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def state(path: pathlib.Path) -> tuple[str, list[str]]:
    drifted = []
    for name, target in TARGETS.items():
        wanted = (TEMPLATES / name).read_bytes()
        file = path / target
        if not file.exists() or file.read_bytes() != wanted:
            drifted.append(name)
    if (path / LEGACY).exists():
        drifted.append("pipeline.yml")
    return ("ok" if not drifted else "drift"), drifted


def run(args: list[str], cwd: pathlib.Path) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, timeout=300)


def gh(args: list[str], config_dir: str) -> subprocess.CompletedProcess:
    env = dict(os.environ, GH_CONFIG_DIR=config_dir)
    return subprocess.run(["gh", *args], text=True, env=env, capture_output=True, timeout=180)


def check(reg: dict, only: list[str], as_json: bool) -> int:
    rows = []
    for slug, _cfg, path in repos(reg, only):
        status, drifted = state(path)
        rows.append({"repo": slug, "state": status, "files": drifted})
    if as_json:
        print(json.dumps(rows, indent=2))
    else:
        for row in rows:
            print(f"{row['repo']:55} {row['state']:6} {','.join(row['files'])}")
        print(f"\n{len(rows)} repositories, {sum(r['state'] != 'ok' for r in rows)} need callers")
    return 0


def apply_one(slug: str, cfg: str, path: pathlib.Path, yes: bool) -> str:
    status, drifted = state(path)
    if status == "ok":
        return "ok"
    if not yes:
        print(f"[dry-run] {slug}: would write {', '.join(drifted)}")
        return "planned"
    run(["git", "fetch", "-q", "origin"], path)
    run(["git", "checkout", "-q", "main"], path)
    run(["git", "pull", "-q", "--ff-only"], path)
    run(["git", "checkout", "-B", BRANCH], path)
    if (path / LEGACY).exists():
        run(["git", "rm", "-q", str(LEGACY)], path)
    for name, target in TARGETS.items():
        file = path / target
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes((TEMPLATES / name).read_bytes())
        run(["git", "add", str(target)], path)
    commit = run(["git", "commit", "-m", "workflows: split PR and tag callers"], path)
    if commit.returncode != 0:
        return "commit failed"
    push = run(["git", "push", "git@github.com:" + slug + ".git", f"HEAD:refs/heads/{BRANCH}"], path)
    if push.returncode != 0:
        return f"push failed: {push.stderr.strip()[:60]}"
    pr = gh(["pr", "create", "--repo", slug, "--base", "main", "--head", BRANCH,
             "--title", "workflows: split PR and tag callers",
             "--body", "Replaces the combined pipeline with two callers from "
                       "gardusi-gustavo/package-yml: pr.yml (pull_request) and "
                       "release.yml (push tags)."], cfg)
    if pr.returncode != 0:
        return f"pr failed: {pr.stderr.strip()[:60]}"
    return pr.stdout.strip().splitlines()[-1]


def apply(reg: dict, only: list[str], yes: bool) -> int:
    for slug, cfg, path in repos(reg, only):
        try:
            print(f"{slug:55} {apply_one(slug, cfg, path, yes)}")
        except Exception as exc:
            print(f"{slug:55} error: {exc}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="sync_workflows.py", description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--apply", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--yes", action="store_true")
    parser.add_argument("--repo", action="append", default=[])
    args = parser.parse_args()
    reg = load_registry()
    if args.check:
        return check(reg, args.repo, args.json)
    return apply(reg, args.repo, args.yes)


if __name__ == "__main__":
    raise SystemExit(main())
