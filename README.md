# .github

Native GitHub platform control center for `gardusi-gustavo`.

## Contents

| Path | Purpose |
| --- | --- |
| `.github/workflows/reusable-*.yml` | versioned reusable workflows pinned by consumers |
| `.github/ISSUE_TEMPLATE/` | default issue and feature forms |
| `.github/PULL_REQUEST_TEMPLATE.md` | default pull request checklist |
| `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` | account-wide community health defaults |

## Governance

Governance manifests live in [`contract-json/governance/`](https://github.com/gardusi-gustavo/contract-json/tree/main/governance).
Executable governance checks live in `package-sh/infra/scripts/governance/`.

## Versioning

Reusable workflows are pinned by tag:

```yaml
uses: gardusi-gustavo/.github/.github/workflows/reusable-ci-python.yml@v0.1.1
```

Do not reference `@main` from consuming repositories.

## Profile

The portfolio landing page is
[`gardusi-gustavo`](https://github.com/gardusi-gustavo/gardusi-gustavo).
