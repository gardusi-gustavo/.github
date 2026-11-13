# Caller templates

Every repository consumes workflows from this repository through a thin caller.

| Template | Trigger | Purpose |
| --- | --- | --- |
| `pipeline.yml` | `pull_request`, `push: tags` | PR CI and tag release |
| `update.yml` | `workflow_dispatch` | compare the pointer with this repository and open a PR locally |

Rules:

- copy the file as-is; do not add repository-specific logic;
- `update.yml` has no schedule during mise en place;
- when enabling a schedule, add only the trigger, nothing else;
- repository-specific behaviour belongs in `scripts/` or `infra/docker/`.

The pointer is expected to be identical in every repository. Drift is a bug.
