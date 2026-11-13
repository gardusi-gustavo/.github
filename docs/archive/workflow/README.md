# Retired workflow repositories

The `workflow-*` repositories are retired. Workflow logic lives in
`gardusi-gustavo/package-yml`; the two event callers live in each consumer.

| Repository | Useful content | Disposition |
| --- | --- | --- |
| `workflow-event` | ingestion notes, migration issues | archived here; issues exported before deletion |
| `workflow-scheduled` | cron notes and task layout | archived here; ingestion code moves to the database repos |
| `workflow-manual` | `/agent` protocol | archived here; the dispatcher was already dead |

Delete only after the Git bundles and issue exports exist. Archive is reversible;
deletion is not.
