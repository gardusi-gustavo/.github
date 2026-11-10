# Governance

Account-wide inventory, policy, bundle order, GitHub rulesets, and App manifest.

- `repos.json` — master repository inventory
- `policy.json` — merge, PR, label, and agent policy
- `bundle-order.json` — topological backup and restore order
- `rulesets/` — GitHub branch and tag rulesets
- `app-manifest.json` — GitHub App manifest

Reusable workflows live in `.github/workflows/reusable-*.yml` and are pinned by
tag from consuming repositories.
