# Agent protocol

## Caller

Each repository has `.github/workflows/agent.yml`:

```yaml
on:
  issue_comment:
    types: [created]
jobs:
  agent:
    uses: gardusi-gustavo/.github/.github/workflows/reusable-agent.yml@v0.1.1
```

## Handler

`workflow-devops/.github/workflows/agent.yml` checks:

1. The event is a new issue comment.
2. The body starts with `/agent`.
3. The commenter is not a bot.
4. The commenter has `write`, `maintain`, or `admin` permission.
5. The command is dispatched as `agent-command` with a short payload.

The agent runner has no merge authority. It can open branches and PRs; a human
reviews and merges.
