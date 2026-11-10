# .github

Account-wide control center for `gardusi-gustavo`.

## Contents

| Path | Purpose |
| --- | --- |
| `.github/workflows/reusable-*.yml` | versioned reusable workflows pinned by consumers |
| `governance/` | repository inventory, policy, bundle order, rulesets, App manifest, archive manifest |
| `.github/ISSUE_TEMPLATE/` | default issue and feature forms |
| `.github/PULL_REQUEST_TEMPLATE.md` | default pull request checklist |
| `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` | account-wide community health defaults |

## Versioning

Reusable workflows are pinned by tag:

```yaml
uses: gardusi-gustavo/.github/.github/workflows/reusable-ci-python.yml@v0.1.1
```

Do not reference `@main` from consuming repositories.

## Workflow roles

- `workflow-event` — event-driven CI callers.
- `workflow-scheduled` — cron ingestion and backup jobs.
- `workflow-manual` — manual and interactive agent operations.

## Profile

The portfolio landing page is
[`gardusi-gustavo`](https://github.com/gardusi-gustavo/gardusi-gustavo).
