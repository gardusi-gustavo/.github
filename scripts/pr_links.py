#!/usr/bin/env python3
"""List local branches that are ahead of main and print their compare URLs.

Tokenless: uses git only. Push the branch over SSH, then open the URL in the
browser to create the pull request.
"""
from __future__ import annotations

import argparse
import pathlib
import subprocess

def default_root() -> pathlib.Path:
    termux = pathlib.Path("/data/data/com.termux/files/home/github")
    return termux if termux.is_dir() else pathlib.Path.home() / "github"


ROOT = default_root()


def git(cwd: pathlib.Path, args: list[str]) -> str:
    return subprocess.run(["git", *args], cwd=cwd, text=True,
                          capture_output=True).stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(prog="pr_links.py", description=__doc__)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--branch", help="only this branch name")
    args = parser.parse_args()

    root = pathlib.Path(args.root)
    found = 0
    for gitdir in sorted(root.glob("*/*/.git")):
        repo = gitdir.parent
        slug = git(repo, ["remote", "get-url", "origin"]).rstrip("/")
        slug = slug.removesuffix(".git")
        slug = slug.split(":")[-1] if slug.startswith("git@") else slug.split("github.com/")[-1]
        git(repo, ["fetch", "-q", "origin"])
        heads = git(repo, ["for-each-ref", "--format=%(refname:short)", "refs/heads"]).splitlines()
        merged = set(git(repo, ["branch", "--format=%(refname:short)", "--merged", "origin/main"]).splitlines())
        for branch in heads:
            if branch in merged:
                continue
            if branch == "main":
                continue
            if args.branch and branch != args.branch:
                continue
            ahead = git(repo, ["rev-list", "--count", f"origin/main..{branch}"])
            if ahead and ahead != "0":
                found += 1
                print(f"{slug:55} {branch:24} {ahead:>3} commits")
                print(f"  https://github.com/{slug}/compare/main...{branch}?expand=1")
    if not found:
        print("no branch ahead of main")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
