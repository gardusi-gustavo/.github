# Architecture

The current shape of the workspace, as of the mise-en-place phase.

## Repositories

| Domain | Repos | Role |
| --- | --- | --- |
| `contract-*` | 6 | interface contracts (JSON Schema, Protobuf, GraphQL, OpenAPI, SQL, WIT) |
| `package-*` | 21 | language and tooling references, including `package-yml` and `package-md` |
| `database-*` | 5 | datasets |
| `dashboard-*` | 5 | static UIs |
| `game-*` | 3 | interactive products |
| `workflow-*` | 3 | pipeline-specific repos |
| meta | 2 | `package-yml`, profile |
| private | 1 | operator-only, no automation |

Total: 46 active repositories.

## Two workflow classes

| Class | Lives in | Credential | Enabled |
| --- | --- | --- | --- |
| Event | each repo, pointer to `package-yml@release/v1` | `GITHUB_TOKEN` | yes (CI + release) |
| Scheduled | each repo, thin caller to a reusable workflow | `GITHUB_TOKEN` | **no, by design** |

No scheduled workflow is enabled. The templates exist; the schedules do not.

## Credentials

- **SSH** for the operator: clone, push, tags, workflow files.
- **`GITHUB_TOKEN`** for every workflow, scoped to the repository that runs it.
- **No PAT, no GitHub App, no cross-repo token.**

Consequences:

- a bot-created PR does not trigger `pull_request` CI;
- cross-repo work is a human action, coordinated by an issue;
- template updates are **pull-based**: each repo checks `package-yml` and opens a PR in itself.

## Update flow (designed, not enabled)

```text
package-yml/release/v1
        │  raw fetch, public, no auth
        ▼
repo experimental update (workflow_dispatch, not enabled)
        │  compare pr/release callers, branch, commit, push
        ▼
pull request in the same repo (GITHUB_TOKEN)
        ▼
caller PR in the same repo (human merges)
```

The caller is `templates/experimental/update.yml`. It has **no `schedule:`** and is
not distributed; it only runs when a human dispatches it.

## Central repositories

| Repo | Responsibility |
| --- | --- |
| `package-yml` | reusable workflows, caller templates, sync and scaffold tools |
| `package-md` | documentation templates, community health files |
| `contract-json` | governance inventory, policy, workspace manifest |
| `package-sh` | shell tooling and agent guardrail blocks |

## Current state

| Item | Count |
| --- | ---: |
| Repos with the `pr.yml` + `release.yml` pointer | 40 |
| Repos with local community files | 39 |
| Repos with `dependabot.yml` | 41 |
| Repos with `backup.yml` | 38 |
| Repos with `deploy.yml` | 4 |

## Known gaps

- `package-cpp` has three failing algorithm tests.
- `contract-sql` and `database-wiki` lack the pointer and community files.
- Dependabot version-update configs are still present; they should be removed once
  the janitor exists.
- `workflow-manual` should be archived after its issues move to `workflow-event`.
- `release/v1` should be protected in the UI.
