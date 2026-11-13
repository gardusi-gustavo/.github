# Mise en place

Prepare every repository so workflows can be enabled later without rework. Nothing
scheduled runs yet.

## Per repository

| File | Status | Notes |
| --- | --- | --- |
| `.github/workflows/pipeline.yml` | done in 40 repos | PR CI + tag release |
| `.github/CONTRIBUTING.md` | done in 39 | from `package-md` |
| `.github/SECURITY.md` | done in 39 | from `package-md` |
| `.github/CODE_OF_CONDUCT.md` | done in 39 | from `package-md` |
| `.github/workflows/update.yml` | **not yet** | dispatch-only, no schedule |
| `scripts/test.sh` or `infra/config/repo.json` | per repo | CI entrypoint |
| `infra/docker/ci.dockerfile` | optional | opt-in via `ci.container` |

## Update caller

When a repository is ready for self-update, add `update.yml` from
`templates/callers/update.yml`. It is `workflow_dispatch` only.

Do **not** add `schedule:` until the janitor, backup, and ingest checks are ready.
Enabling a schedule is a separate, deliberate step.

## Order

1. Pointer and community files (mostly done).
2. Test entrypoint (`scripts/test.sh` or `.ci.script`).
3. `update.yml` caller, dispatch-only.
4. Verify one manual dispatch creates a PR in the same repo and CI runs.
5. Add schedules one class at a time: janitor, then backup, then ingest.

## Rules

- Never add a scheduled trigger before the reusable workflow has been tested with
  a manual dispatch.
- One PR per repository.
- The bot prepares a branch and a PR; a human reviews and merges.
- No PAT, no cross-repo token.

## Enabling later

A scheduled caller is the same file with one extra trigger:

```yaml
on:
  workflow_dispatch:
  schedule:
    - cron: "41 3 * * 1"
```

Nothing else changes.
