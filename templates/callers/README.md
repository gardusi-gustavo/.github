# Caller templates

A repository carries exactly two workflows, both imported from
`gardusi-gustavo/package-yml`:

| Template | Trigger | Purpose |
| --- | --- | --- |
| `pr.yml` | `pull_request: branches: [main]` | CI |
| `release.yml` | `push: tags: ["v*"]` | build and publish a release |

Rules:

- copy both files as-is; do not add repository-specific logic;
- there is no combined `pr.yml` + `release.yml`;
- no `schedule`, `issue_comment`, `repository_dispatch`, or `push: branches`
  trigger belongs in a consumer repository;
- repository-specific behaviour belongs in `scripts/` or `infra/docker/`.

Experimental callers (update, janitor, backup, ingest) live in
`templates/experimental/` and are **not** distributed until tested.
