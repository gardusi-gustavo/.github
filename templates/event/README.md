# Event templates

Source files for the two consumer workflows. The folder names describe the
trigger; consumers receive flat files because GitHub does not execute
subdirectories under `.github/workflows`.

| Template | Consumer path | Trigger |
| --- | --- | --- |
| `pull-request.yml` | `.github/workflows/event-pull-request.yml` | `pull_request` |
| `release.yml` | `.github/workflows/event-release.yml` | `release: published` |

Rules:

- copy as-is; no repository-specific logic;
- keep the caller job named `ci` in the pull-request workflow so the required
  check stays `ci / ci`;
- no `schedule`, `issue_comment`, `repository_dispatch`, or `push: branches`;
- repository-specific behaviour belongs in `scripts/` or `infra/docker/`.

Experimental callers live in `templates/experimental/` and are not distributed
until tested.
