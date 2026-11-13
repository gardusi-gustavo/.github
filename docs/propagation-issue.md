# Propagate validated workflow templates

One issue tracks the rollout of anything beyond `pr.yml` and `release.yml`.

- [ ] `update` tested with a manual dispatch on `package-sh`
- [ ] `janitor` tested with a manual dispatch on `package-wat`
- [ ] `backup` tested with a manual dispatch on `package-go`
- [ ] `ingest` tested with a manual dispatch on `database-news`
- [ ] only then add `schedule:` to one class at a time
- [ ] verify `ci / ci` still passes on caller pull requests

No consumer repository gets a scheduled trigger until its class passes the
manual-dispatch test.
