#!/usr/bin/env python3
"""Check or apply the workflow pointer in every repository.

The pointer is ``.github/workflows/pipeline.yml``. It is byte-identical in every
repository and only calls reusable workflows from ``gardusi-gustavo/.github``.
Logic changes never touch it; only an interface change does.

Usage:

    sync_workflows.py --check
    sync_workflows.py --check --json
    sync_workflows.py --apply --yes
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import subprocess
import sys

def _gh_home() -> pathlib.Path:
    env = os.environ.get("GH_HOME")
    if env:
        return pathlib.Path(env)
    candidates = [
        pathlib.Path.home() / ".config" / "gh",
        pathlib.Path("/data/data/com.termux/files/home/.config/gh"),
    ]
    for candidate in candidates:
        if (candidate / "registry.json").exists():
            return candidate
    return candidates[0]


GH_HOME = _gh_home()
REGISTRY = pathlib.Path(os.environ.get("WORKSPACE_GH_REGISTRY", GH_HOME / "registry.json"))
WORKSPACE = pathlib.Path(os.environ.get("WORKSPACE_ROOT", pathlib.Path.home() / "github"))
TEMPLATE = pathlib.Path(__file__).resolve().parents[1] / "templates" / "callers" / "pipeline.yml"
TARGET = pathlib.Path(".github/workflows/pipeline.yml")
BRANCH = "workflow/pipeline"
EXCLUDE = {
    "gardusi-gustavo/.github",          # source of truth
    "gardusi-gustavo/gardusi-gustavo",  # profile and docs
}


def load_registry() -> dict:
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def repos(reg: dict, only: list[str] | None = None) -> list[tuple[str, str, pathlib.Path]]:
    """Return (repo slug, domain, local path) for every registered repository."""
    found = []
    for domain in reg.get("domains", []):
        for repo in domain.get("repos", []):
            path = pathlib.Path(repo["path"])
            name = repo["github"].split("/")[-1]
            if only and name not in only:
                continue
            if path.is_dir() and repo["github"] not in EXCLUDE:
                found.append((repo["github"], domain["config_dir"], path))
    return found


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def state(template: bytes, path: pathlib.Path) -> tuple[str, str]:
    target = path / TARGET
    if not target.exists():
        return "missing", "-"
    current = target.read_bytes()
    if current == template:
        return "ok", digest(current)
    return "drift", digest(current)


def check(reg: dict, as_json: bool, only: list[str]) -> int:
    template = TEMPLATE.read_bytes()
    rows = []
    for slug, _domain, path in repos(reg, only):
        status, current = state(template, path)
        rows.append({"repo": slug, "state": status, "target": current, "wanted": digest(template)})
    if as_json:
        print(json.dumps(rows, indent=2))
    else:
        for row in rows:
            print(f"{row['repo']:55} {row['state']:8} {row['target']}/{row['wanted']}")
        drifted = sum(1 for row in rows if row["state"] != "ok")
        print(f"\n{len(rows)} repositories, {drifted} need the pointer")
    return 0


def gh(args: list[str], config_dir: str) -> subprocess.CompletedProcess:
    env = dict(os.environ, GH_CONFIG_DIR=config_dir)
    return subprocess.run(["gh", *args], text=True, env=env, capture_output=True, timeout=180)


def run(args: list[str], cwd: pathlib.Path) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, timeout=300)


def apply_one(slug: str, config_dir: str, path: pathlib.Path, template: bytes, yes: bool) -> str:
    status, _ = state(template, path)
    if status == "ok":
        return "ok"
    target = path / TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    if not yes:
        print(f"[dry-run] {slug}: would write {TARGET} and open a pull request")
        return "planned"
    run(["git", "checkout", "-B", BRANCH], path)
    target.write_bytes(template)
    run(["git", "add", str(TARGET)], path)
    commit = run(["git", "commit", "-m", "workflows: add the shared pipeline pointer"], path)
    if commit.returncode != 0:
        return f"commit failed: {commit.stderr.strip()[:80]}"
    push = run(["git", "push", "git@github.com:" + slug + ".git", f"HEAD:refs/heads/{BRANCH}"], path)
    if push.returncode != 0:
        return f"push failed: {push.stderr.strip()[:120]}"
    pr = gh(["pr", "create", "--repo", slug, "--base", "main", "--head", BRANCH,
             "--title", "workflows: add the shared pipeline pointer",
             "--body", "Adds the byte-identical pointer to the reusable CI and release "
                       "workflows in gardusi-gustavo/.github.\n\nLogic lives in .github; "
                       "this file only defines the triggers."], config_dir)
    if pr.returncode != 0:
        return f"pr failed: {pr.stderr.strip()[:120]}"
    return pr.stdout.strip().splitlines()[-1]


def apply(reg: dict, yes: bool, only: list[str]) -> int:
    template = TEMPLATE.read_bytes()
    for slug, config_dir, path in repos(reg, only):
        try:
            print(f"{slug:55} {apply_one(slug, config_dir, path, template, yes)}")
        except Exception as exc:
            print(f"{slug:55} error: {exc}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="sync_workflows.py", description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="report drift only")
    group.add_argument("--apply", action="store_true", help="write the pointer and open pull requests")
    parser.add_argument("--json", action="store_true", help="machine-readable output for --check")
    parser.add_argument("--yes", action="store_true", help="confirm --apply")
    parser.add_argument("--repo", action="append", default=[], help="limit to these repository names")
    args = parser.parse_args()

    reg = load_registry()
    if args.check:
        return check(reg, args.json, args.repo)
    return apply(reg, args.yes, args.repo)


if __name__ == "__main__":
    raise SystemExit(main())
