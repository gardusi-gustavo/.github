# Pull requests without a bot

Direct pushes to `main` are forbidden by the `main-protection` ruleset. Every
change needs a branch, a pull request, and one human approval.

## Method

1. Push a branch over SSH:

   ```bash
   git checkout -b change/name
   git push -u origin change/name
   ```

2. Print the compare link:

   ```bash
   python3 scripts/pr_links.py --branch change/name
   ```

3. Open the link in the browser and create the PR.

4. The main account approves and merges. The bot never approves.

## Why not the bot

A `GITHUB_TOKEN` workflow can create a PR only when the repository enables:

```
Settings → Actions → General
  Workflow permissions: Read and write
  Allow GitHub Actions to create and approve pull requests
```

That is per repository. It is deferred for now; the compare-link method needs no
setting and no credential.

## Ruleset

The standard rule requires one approval:

```json
"required_approving_review_count": 1
```

Apply it to all repositories with `scripts/apply_rulesets.py`, which needs a
one-time administration credential, or manually in the UI. SSH cannot change a
ruleset.


## Bot-created PRs, manual CI

A repository may also run `generate.yml` manually. It uses `GITHUB_TOKEN` to push
a branch and open a PR as `github-actions[bot]`.

- The PR exists and is blocked until approval and checks.
- CI does **not** run automatically, because GitHub suppresses events caused by
  `GITHUB_TOKEN`.
- There is no run to re-run. Trigger CI with an empty commit from the operator:

  ```bash
  git fetch origin bot/change
  git checkout bot/change
  git commit --allow-empty -m "ci: trigger"
  git push origin bot/change
  ```

- Then the main account approves and merges.

Repository settings required for the bot to create the PR:

```
Settings → Actions → General
  Workflow permissions: Read and write
  Allow GitHub Actions to create and approve pull requests
```

The approval rule still requires a human; the bot never approves.
