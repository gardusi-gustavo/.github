# Workflows

GitHub Actions are split in two, because GitHub only fires an event inside the
repository where it happens.

| Kind | Lives in | Replicated per repo |
| --- | --- | --- |
| Event logic | this repository, `event-*.yml` | no |
| Event trigger | each repository, `.github/workflows/pipeline.yml` | yes, byte-identical |
| Scheduled logic and trigger | this repository, `scheduled-*.yml` | no |
| Custom algorithm | each repository, `scripts/` and `infra/docker/` | yes |

## The pointer

Every repository contains exactly one workflow file:

```yaml
name: pipeline
on:
  pull_request:
    branches: [main]
  push:
    tags: ["v*"]
jobs:
  pr:
    if: github.event_name == 'pull_request'
    uses: gardusi-gustavo/.github/.github/workflows/event-ci.yml@release/v1
  release:
    if: github.event_name == 'push'
    permissions:
      contents: write
    uses: gardusi-gustavo/.github/.github/workflows/event-release.yml@release/v1
```

It is a constant. Logic changes in `event-ci.yml` or `event-release.yml` reach
every repository without a pull request, because the pointer references the
`release/v1` branch.

The pointer changes only when the interface changes: a new trigger, a new input,
a new secret. That is expected during the first weeks and close to never once
stable.

## Repository surface

```text
.github/workflows/pipeline.yml     pointer, identical everywhere
scripts/test.sh                    optional
scripts/release.sh                 optional
scripts/ingest.sh                  optional
infra/docker/ci.dockerfile         optional
infra/config/repo.json             language, release type, commands
```

Removed: per-repository copies of CI, backup, deploy, agent, and Dependabot
configuration.

## Resolution order

`event-ci.yml` chooses the first available option:

1. `infra/docker/ci.dockerfile` builds and runs the script inside the image;
2. `scripts/test.sh` runs directly;
3. `infra/config/repo.json` `.ci.command` runs;
4. otherwise the job fails with a clear message.

`event-release.yml` uses `scripts/release.sh` when present; otherwise it archives
the tag and publishes a GitHub release from `dist/*`.

The most frequently edited files are therefore the script and the Dockerfile,
not the workflow.

## Scheduled workflows

Scheduled work has no per-repository replica. It runs here:

```text
.github/workflows/scheduled-backup.yml
.github/workflows/scheduled-ingest-hourly.yml
.github/workflows/scheduled-ingest-daily.yml
```

A scheduled workflow that writes to another repository needs a cross-repository
credential; the built-in `GITHUB_TOKEN` is scoped to this repository only.

## Ref strategy

| Ref | Consumer pull requests on logic change | Use |
| --- | --- | --- |
| `release/v1` branch | none | event logic, current default |
| `v1.x.y` tag | one wave per release | strict freeze |
| commit SHA | one wave per bump | maximum assurance |

Tags matching `v*` are immutable in this account, so a moving major tag is not
available. A protected `release/v1` branch is the equivalent channel.

## Drift check

```bash
python3 scripts/sync_workflows.py --check
python3 scripts/sync_workflows.py --check --json
python3 scripts/sync_workflows.py --apply --yes
```

`--check` compares the pointer hash in every repository with
`templates/callers/pipeline.yml`. Expected steady state: every repository reports
`ok`. A drift report means someone edited the pointer by hand or a repository
missed the bootstrap wave.

`--apply` writes the pointer, pushes a `workflow/pipeline` branch over SSH, and
opens a pull request. It is idempotent: repositories already matching are skipped.

## Rules

- Never edit `pipeline.yml` by hand; change the template or run the sync.
- Never copy reusable logic into a repository.
- Workflow bumps belong to the `source:workflow` lane and do not count against
  the builder's one-pull-request limit.
- The builder may not modify `.github/workflows/**`.
