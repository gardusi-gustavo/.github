# Pull requests: draft, then ready

PRs are created as **drafts**. Draft means “waiting”: no CI runs. Marking a PR
**ready for review** is the daily warm-up that starts CI. There is no empty
commit and nothing to re-run.

## Daily loop

```text
issue
  │  generate.yml (manual, opencode + GITHUB_TOKEN)
  ▼
draft PR            no CI, merge blocked
  │  operator marks the PR ready for review
  ▼
CI runs             ci / ci
  │  main account reviews carefully
  ▼
approve + merge     one approval required
```

## Generator

`generate.yml` is manual (`workflow_dispatch`) and takes:

| Input | Meaning |
| --- | --- |
| `issue` | issue number to build |
| `branch` | branch name |
| `title` | PR title |

It uses `scripts/generate.sh` in the repository, the repository's own
`GITHUB_TOKEN`, and opens a **draft** PR. It never approves or merges.

Required repository settings, once per repo:

```
Settings → Actions → General
  Workflow permissions: Read and write
  Allow GitHub Actions to create and approve pull requests
```

## CI trigger

`event-pull-request.yml` runs on:

```yaml
on:
  pull_request:
    types: [opened, ready_for_review, synchronize, reopened]
jobs:
  ci:
    if: github.event.pull_request.draft == false
```

So:

- a draft PR produces no CI;
- marking it ready produces `ci / ci`;
- later commits to a ready PR re-run CI;
- reopening or refreshing also runs CI.

No `workflow_dispatch`, no empty commits.

## Approval

The standard ruleset requires one approving review. The PR author is
`github-actions[bot]`, so the main account can approve it. The bot never
approves.

## Manual fallback

If a PR is created without the generator:

```bash
git checkout -b change/name
git push -u origin change/name
python3 scripts/pr_links.py --branch change/name
```

Open the compare link, create the PR as a draft, then mark it ready when you
intend to review it.
