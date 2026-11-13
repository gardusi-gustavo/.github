# Main protection rulesets

One standard ruleset for every active repository.

## Rules

| Rule | Value |
| --- | --- |
| Target | default branch (`~DEFAULT_BRANCH`) |
| Deletion | blocked |
| Non-fast-forward | blocked |
| Linear history | required |
| Pull request | required |
| Required check | `ci / ci` |
| Bypass actors | none |

Files:

| File | Use |
| --- | --- |
| `main.json` | repositories with the `event-pull-request` workflow |
| `main-no-checks.json` | repositories without CI (profile, `contract-wit`) |

## Apply

Rulesets are an **authenticated administration API**. SSH cannot create, update,
or disable them.

### Option A — one-shot credential

Use a temporary fine-grained token with `Administration: write` on all selected
repositories (or a classic token with `repo` scope):

```bash
GH_TOKEN=<admin-token> python3 scripts/apply_rulesets.py --check
GH_TOKEN=<admin-token> python3 scripts/apply_rulesets.py --apply --yes
```

The script:

- reads the repository list from `contract-json/governance/workspace.json`;
- skips retired repositories and the private repo;
- picks `main.json` when `.github/workflows/event-pull-request.yml` exists,
  otherwise `main-no-checks.json`;
- creates or updates the `main-protection` ruleset.

Revoke the token immediately afterwards.

### Option B — UI, one repository at a time

```
Settings → Rules → Rulesets → New branch ruleset
```

Name `main-protection`, target the default branch, enable deletion, non-fast-forward,
linear history, pull request, and required status check `ci / ci`, no bypass actors.

## Order

1. Merge pending branches first. A ruleset blocks direct pushes, including the
   operator's SSH key.
2. Apply rules everywhere.
3. From that point, every change goes through a pull request.

## Exceptions

- `contract-wit` and the profile repository have no CI; use the no-checks variant
  until a test entrypoint exists.
- `private` is operator-only and is skipped.
- `workflow-*` are retired and skipped.
