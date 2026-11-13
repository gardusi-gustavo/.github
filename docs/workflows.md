# Workflows

Every consumer repository runs exactly two workflows, both imported from
`gardusi-gustavo/package-yml`.

| Kind | Lives in | Replicated per repo |
| --- | --- | --- |
| Event logic | `package-yml`, `event-*.yml` | no |
| Event triggers | each repo, `pr.yml` and `release.yml` | yes, byte-identical |
| Experimental logic | `package-yml`, `experimental-*.yml` | no |
| Repository code | each repo, `scripts/` and `infra/docker/` | yes |

## The two callers

**`pr.yml`** — every pull request:

```yaml
name: pr
on:
  pull_request:
    branches: [main]
permissions:
  contents: read
jobs:
  ci:
    uses: gardusi-gustavo/package-yml/.github/workflows/event-ci.yml@release/v1
```

**`release.yml`** — every tag:

```yaml
name: release
on:
  push:
    tags: ["v*"]
permissions:
  contents: write
jobs:
  release:
    uses: gardusi-gustavo/package-yml/.github/workflows/event-release.yml@release/v1
```

There is no combined `pipeline.yml`. No `schedule`, `issue_comment`,
`repository_dispatch`, or `push: branches` trigger belongs in a consumer
repository.

Logic changes in `event-ci.yml` / `event-release.yml` reach every repository
without a pull request because the callers reference `release/v1`. The callers
change only when the interface changes.

## Repository surface

```text
.github/workflows/pr.yml        pull request CI
.github/workflows/release.yml   tag release
scripts/test.sh                 optional
scripts/release.sh              optional
infra/docker/ci.dockerfile      optional, opt-in via ci.container
infra/config/repo.json          language, release type, commands
```

## Experimental workflows

Everything that is not PR or tag lives in this repository and is **not enabled**:

```text
.github/workflows/experimental-update.yml    pull-based caller sync
.github/workflows/reusable-backup.yml        backup
.github/workflows/reusable-ingest.yml        ingestion
.github/workflows/reusable-pages.yml         Pages deploy
.github/workflows/reusable-agent.yml         comment commands
```

They are `workflow_call` only, so they never fire on their own. A manual dispatch
is the test; a schedule is added only after that passes. Propagation to consumers
is tracked by a single issue in this repository.

## Language setup

`event-ci.yml` infers the language from the repository name (`package-<lang>`) or
`infra/config/repo.json` `.ci.language`, then installs the toolchain: Python,
Node, Go, Rust, Java/Kotlin/Scala, .NET, Ruby, PHP, Elixir, Lua, Swift, Zig, or
Terraform. C++ and shell need no extra setup. A repository can override anything
with `scripts/setup.sh`.

## Resolution order

`event-ci.yml` chooses the first available option:

1. `infra/docker/ci.dockerfile` builds and runs the script inside the image, but
   only when `infra/config/repo.json` sets `.ci.container` to `true`;
2. `scripts/test.sh` runs directly;
3. `infra/config/repo.json` `.ci.command` or `.ci.script` runs;
4. otherwise the job fails with a clear message.

`event-release.yml` uses `scripts/release.sh` when present; otherwise it archives
the tag and publishes a GitHub release from `dist/*`.

## Ref strategy

| Ref | Consumer pull requests on logic change | Use |
| --- | --- | --- |
| `release/v1` branch | none | current default |
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

`--check` compares `pr.yml` and `release.yml` in every repository with
`templates/callers/`. It also reports a leftover `pipeline.yml`. Expected steady
state: every repository reports `ok`.

`--apply` writes the callers, removes `pipeline.yml`, pushes a `workflow/callers`
branch over SSH, and opens a pull request. It is idempotent.

## Rules

- Never edit `pr.yml` or `release.yml` by hand; change the template or run the sync.
- Never copy reusable logic into a repository.
- Scheduled and experimental workflows stay here until validated.
- The builder may not modify `.github/workflows/**`.
