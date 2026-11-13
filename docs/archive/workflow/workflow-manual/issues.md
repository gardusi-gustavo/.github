# workflow-manual issues

Exported 2026-11-13 from the public GitHub API.

## #10 [closed] workflows: add the shared pipeline pointer

- kind: PR
- labels: -
- created: 2026-11-12T19:41:56Z

Adds the byte-identical pointer to the reusable CI and release workflows in gardusi-gustavo/.github.

Logic lives in .github; this file only defines the triggers.

## #9 [closed] Add the default community health files

- kind: PR
- labels: -
- created: 2026-11-12T18:54:42Z

Adds CONTRIBUTING, SECURITY, and CODE_OF_CONDUCT under .github/, sourced from gardusi-gustavo/package-md.

## #8 [closed] Remove duplicated workflows now provided by the shared pipeline

- kind: PR
- labels: -
- created: 2026-11-12T17:48:32Z

The pointer in .github/workflows/pipeline.yml provides PR CI and tag releases from gardusi-gustavo/.github. Removes the replaced workflow files. backup.yml and deploy.yml are kept until their central replacements exist.

## #7 [closed] workflows: add the shared pipeline pointer

- kind: PR
- labels: -
- created: 2026-11-12T03:34:10Z

Adds the byte-identical pointer to the reusable CI and release workflows in gardusi-gustavo/.github.

Logic lives in .github; this file only defines the triggers.

## #6 [open] [agent 2.2] Add a backup verification task

- kind: Issue
- labels: task, source:database-agent, rank:2.2
- created: 2026-11-10T11:02:17Z

## Context

Backups exist but are not checked.

## Limits

- Max commits: 5
- Max file changes: 4

## Expected outcome

A failed backup is visible.

## Acceptance criteria

- Verification is scripted
- Status is recorded

## Source

Retired `database-agent` task `docs/issues/2.2-add-a-backup-verification-task.json`.


## #5 [open] [agent 2.1] Document data lineage

- kind: Issue
- labels: task, source:database-agent, rank:2.1
- created: 2026-11-10T11:02:15Z

## Context

The source of each dataset is unclear.

## Limits

- Max commits: 5
- Max file changes: 4

## Expected outcome

Every dataset has a lineage record.

## Acceptance criteria

- Producer is documented
- Source is documented

## Source

Retired `database-agent` task `docs/issues/2.1-document-data-lineage.json`.


## #4 [open] [agent 1.4] Add a dataset catalog

- kind: Issue
- labels: task, source:database-agent, rank:1.4
- created: 2026-11-10T11:02:13Z

## Context

Consumers need an index.

## Limits

- Max commits: 5
- Max file changes: 4

## Expected outcome

A client can discover the latest file.

## Acceptance criteria

- Catalog is generated in CI
- Checksums are included

## Source

Retired `database-agent` task `docs/issues/1.4-add-a-dataset-catalog.json`.


## #3 [open] [agent 1.3] Add retention and pruning

- kind: Issue
- labels: task, source:database-agent, rank:1.3
- created: 2026-11-10T11:02:10Z

## Context

Daily files accumulate indefinitely.

## Limits

- Max commits: 5
- Max file changes: 4

## Expected outcome

The repository stays within budget.

## Acceptance criteria

- Retention is documented
- Pruning is tested

## Source

Retired `database-agent` task `docs/issues/1.3-add-retention-and-pruning.json`.


## #2 [open] [agent 1.2] Add schema validation to CI

- kind: Issue
- labels: task, source:database-agent, rank:1.2
- created: 2026-11-10T11:02:07Z

## Context

The current CI only checks JSON syntax.

## Limits

- Max commits: 5
- Max file changes: 4

## Expected outcome

Invalid datasets fail CI.

## Acceptance criteria

- Validation runs locally
- Failures name the file

## Source

Retired `database-agent` task `docs/issues/1.2-add-schema-validation-to-ci.json`.


## #1 [open] [agent 1.1] Freeze the agent dataset envelope

- kind: Issue
- labels: task, source:database-agent, rank:1.1
- created: 2026-11-10T11:02:05Z

## Context

The first release needs one stable shape.

## Limits

- Max commits: 5
- Max file changes: 4

## Expected outcome

Consumers can validate every daily file.

## Acceptance criteria

- Envelope schema is committed
- One sample file passes

## Source

Retired `database-agent` task `docs/issues/1.1-freeze-the-agent-dataset-envelope.json`.

