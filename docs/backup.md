# Backup

There is no scheduled backup workflow. The operator runs the backup over SSH,
which keeps the credential surface at one key and no token.

## Run

```bash
bash scripts/backup.sh ~/github ~/backups/$(date -u +%F)
```

The script creates one `git bundle` per local repository, verifies it, and lists
the result. Bundles are ordinary git repositories:

```bash
git clone backup.bundle restored
```

## What to keep

- the bundles for every repository, including the retired `workflow-*` repos at
  least once;
- an offline copy (external drive, encrypted vault, or a second device);
- the date in the directory name so retention is obvious.

## Retention

| Copy | Retention |
| --- | --- |
| local `~/backups` | 14 days |
| offline copy | monthly, keep the last 3 |
| retired repositories | keep permanently until deletion is final |

## Restore drill

Once a month: clone one bundle into a temporary directory, run its test command,
and delete the clone. A backup that has never been restored is a guess.

## Before deleting a repository

```bash
git -C <repo> bundle create ~/backups/<date>/<repo>.bundle --all
git -C <repo> bundle verify ~/backups/<date>/<repo>.bundle
```

Only then archive or delete the repository in the UI. Archived history is
recoverable; deleted history is not.
