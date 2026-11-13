# workflow-event issues

Exported 2026-11-13 from the public GitHub API.

## #7 [closed] workflows: add the shared pipeline pointer

- kind: PR
- labels: -
- created: 2026-11-12T19:41:46Z

Adds the byte-identical pointer to the reusable CI and release workflows in gardusi-gustavo/.github.

Logic lives in .github; this file only defines the triggers.

## #6 [closed] Add the default community health files

- kind: PR
- labels: -
- created: 2026-11-12T18:54:32Z

Adds CONTRIBUTING, SECURITY, and CODE_OF_CONDUCT under .github/, sourced from gardusi-gustavo/package-md.

## #5 [closed] Remove duplicated workflows now provided by the shared pipeline

- kind: PR
- labels: -
- created: 2026-11-12T17:48:19Z

The pointer in .github/workflows/pipeline.yml provides PR CI and tag releases from gardusi-gustavo/.github. Removes the replaced workflow files. backup.yml and deploy.yml are kept until their central replacements exist.

## #4 [closed] workflows: add the shared pipeline pointer

- kind: PR
- labels: -
- created: 2026-11-12T03:34:00Z

Adds the byte-identical pointer to the reusable CI and release workflows in gardusi-gustavo/.github.

Logic lives in .github; this file only defines the triggers.

## #3 [closed] Bump docker/build-push-action from 6 to 7

- kind: PR
- labels: dependencies, github_actions
- created: 2026-11-09T23:40:01Z

Bumps [docker/build-push-action](https://github.com/docker/build-push-action) from 6 to 7.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/docker/build-push-action/releases">docker/build-push-action's releases</a>.</em></p>
<blockquote>
<h2>v7.0.0</h2>
<ul>
<li>Node 24 as default runtime (requires <a href="https://github.com/actions/runner/releases/tag/v2.327.1">Actions Runner v2.327.1</a> or later) by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/build-push-action/pull/1470">docker/build-push-action#1470</a></li>
<li>Remove deprecated <code>DOCKER_BUILD_NO_SUMMARY</code> and <code>DOCKER_BUILD_EXPORT_RETENTION_DAYS</code> envs by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/build-push-action/pull/1473">docker/build-push-action#1473</a></li>
<li>Remove legacy export-build tool support for build summary by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/build-push-action/pull/1474">docker/build-push-action#1474</a></li>
<li>Switch to ESM and update config/test wiring by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/build-push-action/pull/1466">docker/build-push-action#1466</a></li>
<li>Bump <code>@​actions/core</code> from 1.11.1 to 3.0.0 in <a href="https://redirect.github.com/docker/build-push-action/pull/1454">docker/build-push-action#1454</a></li>
<li>Bump <code>@​docker/actions-toolkit</code> from 0.62.1 to 0.79.0 in <a href="https://redirect.github.com/docker/build-push-action/pull/1453">docker/build-push-action#1453</a> <a href="https://redirect.github.com/docker/build-push-action/pull/1472">docker/build-push-action#1472</a> <a href="https://redirect.github.com/docker/build-push-action/pull/1479">docker/build-push-action#1479</a></li>
<li>Bump minimatch from 3.1.2 to 3.1.5 in <a href="https://redirect.github.com/docker/build-push-action/pull/1463">docker/build-push-action#1463</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/docker/build-push-action/compare/v6.19.2...v7.0.0">https://github.com/docker/build-push-action/compare/v6.19.2...v7.0.0</a></p>
<h2>v6.19.2</h2>
<ul>
<li>Preserve port in <code>GIT_AUTH_TOKEN</code> host by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/build-push-action/pull/1458">docker/build-push-action#1458</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/docker/build-push-action/compare/v6.19.1...v6.19.2">https://github.com/docker/build-push-action/compare/v6.19.1...v6.19.2</a></p>
<h2>v6.19.1</h2>
<ul>
<li>Derive <code>GIT_AUTH_TOKEN</code> host from GitHub server URL by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/build-push-action/pull/1456">docker/build-push-action#1456</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/docker/build-push-action/compare/v6.19.0...v6.19.1">https://github.com/docker/build-push-action/compare/v6.19.0...v6.19.1</a></p>
<h2>v6.19.0</h2>
<ul>
<li>Scope default git auth token to <code>github.com</code> by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/build-push-action/pull/1451">docker/build-push-action#1451</a></li>
<li>Bump brace-expansion from 1.1.11 to 1.1.12 in <a href="https://redirect.github.com/docker/build-push-action/pull/1396">docker/build-push-action#1396</a></li>
<li>Bump form-data from 2.5.1 to 2.5.5 in <a href="https://redirect.github.com/docker/build-push-action/pull/1391">docker/build-push-action#1391</a></li>
<li>Bump js-yaml from 3.14.1 to 3.14.2 in <a href="https://redirect.github.com/docker/build-push-action/pull/1429">docker/build-push-action#1429</a></li>
<li>Bump lodash from 4.17.21 to 4.17.23 in <a href="https://redirect.github.com/docker/build-push-action/pull/1446">docker/build-push-action#1446</a></li>
<li>Bump tmp from 0.2.3 to 0.2.4 in <a href="https://redirect.github.com/docker/build-push-action/pull/1398">docker/build-push-action#1398</a></li>
<li>Bump undici from 5.28.4 to 5.29.0 in <a href="https://redirect.github.com/docker/build-push-action/pull/1397">docker/build-push-action#1397</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/docker/build-push-action/compare/v6.18.0...v6.19.0">https://github.com/docker/build-push-action/compare/v6.18.0...v6.19.0</a></p>
<h2>v6.18.0</h2>
<ul>
<li>Bump <code>@​docker/actions-toolkit</code> from 0.61.0 to 0.62.1 in <a href="https://redirect.github.com/docker/build-push-action/pull/1381">docker/build-push-action#1381</a></li>
</ul>
<blockquote>
<p>[!NOTE]
<a href="https://docs.docker.com/build/ci/github-actions/build-summary/">Build summary</a> is now supported with <a href="https://docs.docker.com/build-cloud/">Docker Build Cloud</a>.</p>
</blockquote>
<p><strong>Full Changelog</strong>: <a href="https://github.com/docker/build-push-action/compare/v6.17.0...v6.18.0">https://github.com/docker/build-push-action/compare/v6.17.0...v6.18.0</a></p>
<h2>v6.17.0</h2>
<ul>
<li>Bump <code>@​docker/actions-toolkit</code> from 0.59.0 to 0.61.0 by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/build-push-action/pull/1364">docker/build-push-action#1364</a></li>
</ul>
<blockquote>
<p>[!NOTE]
Build record is now exported using the <a href="https://docs.docker.com/reference/cli/docker/buildx/history/export/"><code>buildx history export</code></a> command instead of the legacy export-build tool.</p>
</blockquote>
<p><strong>Full Changelog</strong>: <a href="https://github.com/docker/build-push-action/compare/v6.16.0...v6.17.0">https://github.com/docker/build-push-action/compare/v6.16.0...v6.17.0</a></p>
<h2>v6.16.0</h2>
<ul>
<li>Handle no default attestations env var by <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a href="https://redirect.github.com/docker/build-push-action/pull/1343">docker/build-push-action#1343</a></li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/docker/build-push-action/commit/c3c9e263c25d99ce0380d002d59b67737d91b0dc"><code>c3c9e26</code></a> Merge pull request <a href="https://redirect.github.com/docker/build-push-action/issues/1621">#1621</a> from docker/dependabot/npm_and_yarn/docker/actions-t...</li>
<li><a href="https://github.com/docker/build-push-action/commit/459b6741834dcd35f946352017e7675bd2089d42"><code>459b674</code></a> [dependabot skip] chore: update generated content</li>
<li><a href="https://github.com/docker/build-push-action/commit/4dedcb23c91d79c1629bf53ec2c3bcfffef5b34e"><code>4dedcb2</code></a> chore(deps): Bump <code>@​docker/actions-toolkit</code> from 0.99.0 to 0.100.0</li>
<li><a href="https://github.com/docker/build-push-action/commit/379bf63a979bd70751945601fa04c50674509952"><code>379bf63</code></a> Merge pull request <a href="https://redirect.github.com/docker/build-push-action/issues/1620">#1620</a> from crazy-max/buildx-error-message</li>
<li><a href="https://github.com/docker/build-push-action/commit/9877975c9e0b0b661592ff61049069507f9bc2f6"><code>9877975</code></a> chore: update generated content</li>
<li><a href="https://github.com/docker/build-push-action/commit/7ed0556ffafb8eb312463411ef0a84a1dfe24d94"><code>7ed0556</code></a> use the shared Buildx error summary helper</li>
<li><a href="https://github.com/docker/build-push-action/commit/91670ba5a4df99a24efff8637a78c83fd1b0f6b1"><code>91670ba</code></a> Merge pull request <a href="https://redirect.github.com/docker/build-push-action/issues/1618">#1618</a> from docker/dependabot/npm_and_yarn/docker/actions-t...</li>
<li><a href="https://github.com/docker/build-push-action/commit/80dbc8614a5c0ce4356740f69179cf829ecdc79a"><code>80dbc86</code></a> [dependabot skip] chore: update generated content</li>
<li><a href="https://github.com/docker/build-push-action/commit/50cac3a3b6f55e6015d6483d1dd72a3ecb90d20d"><code>50cac3a</code></a> chore(deps): Bump <code>@​docker/actions-toolkit</code> from 0.98.0 to 0.99.0</li>
<li><a href="https://github.com/docker/build-push-action/commit/03b4d6cac0163b44733e1fa60adfd6da560ee4d1"><code>03b4d6c</code></a> Merge pull request <a href="https://redirect.github.com/docker/build-push-action/issues/1617">#1617</a> from crazy-max/fix-metadata-workflow-commands</li>
<li>Additional commits viewable in <a href="https://github.com/docker/build-push-action/compare/v6...v7">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=docker/build-push-action&package-manager=github_actions&previous-version=6&new-version=7)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)


</details>

### Comments
**dependabot[bot]** (2026-11-10T00:21:17Z):

Looks like docker/build-push-action is no longer a dependency, so this is no longer needed.

## #2 [closed] Bump actions/setup-python from 5 to 7

- kind: PR
- labels: dependencies, github_actions
- created: 2026-11-09T23:39:57Z

Bumps [actions/setup-python](https://github.com/actions/setup-python) from 5 to 7.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/actions/setup-python/releases">actions/setup-python's releases</a>.</em></p>
<blockquote>
<h2>v7.0.0</h2>
<h2>What's Changed</h2>
<h3>Enhancements</h3>
<ul>
<li>Migrate to ESM and upgrade dependencies by <a href="https://github.com/priyagupta108"><code>@​priyagupta108</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1330">actions/setup-python#1330</a></li>
<li>Pin SHA commits and update docs with latest versions by <a href="https://github.com/HarithaVattikuti"><code>@​HarithaVattikuti</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1338">actions/setup-python#1338</a></li>
<li>Remove the pip-install input by <a href="https://github.com/gowridurgad"><code>@​gowridurgad</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1336">actions/setup-python#1336</a></li>
</ul>
<h3>Bug Fix</h3>
<ul>
<li>Fix to Classify stderr warning messages as warnings instead of errors in annotations by <a href="https://github.com/lmvysakh"><code>@​lmvysakh</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1335">actions/setup-python#1335</a></li>
<li>Validate and retry manifest fetch to prevent silent failures by <a href="https://github.com/priyagupta108"><code>@​priyagupta108</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1332">actions/setup-python#1332</a></li>
</ul>
<h3>Dependency Upgrade</h3>
<ul>
<li>Bump certifi from 2020.6.20 to 2024.7.4 in /<strong>tests</strong>/data by <a href="https://github.com/dependabot"><code>@​dependabot</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1328">actions/setup-python#1328</a></li>
<li>Remove EOL Python versions and Bumps numpy text fixture by <a href="https://github.com/priya-kinthali"><code>@​priya-kinthali</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1333">actions/setup-python#1333</a></li>
<li>Upgrade <code>@​actions/cache</code> to 6.2.0 by <a href="https://github.com/philip-gai"><code>@​philip-gai</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1337">actions/setup-python#1337</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/lmvysakh"><code>@​lmvysakh</code></a> made their first contribution in <a href="https://redirect.github.com/actions/setup-python/pull/1335">actions/setup-python#1335</a></li>
<li><a href="https://github.com/philip-gai"><code>@​philip-gai</code></a> made their first contribution in <a href="https://redirect.github.com/actions/setup-python/pull/1337">actions/setup-python#1337</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/actions/setup-python/compare/v6...v7.0.0">https://github.com/actions/setup-python/compare/v6...v7.0.0</a></p>
<h2>v6.3.0</h2>
<h2>What's Changed</h2>
<h3>Enhancement</h3>
<ul>
<li>Add RHEL support and include Linux distro in cache keys by <a href="https://github.com/priyagupta108"><code>@​priyagupta108</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1323">actions/setup-python#1323</a></li>
<li>Fix pip cache error handling on Windows by <a href="https://github.com/priyagupta108"><code>@​priyagupta108</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1040">actions/setup-python#1040</a></li>
</ul>
<h3>Dependency update</h3>
<ul>
<li>Upgrade minimatch from 3.1.2 to 3.1.5 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1281">actions/setup-python#1281</a></li>
<li>Upgrade actions dependencies by <a href="https://github.com/gowridurgad"><code>@​gowridurgad</code></a> with <a href="https://github.com/Copilot"><code>@​Copilot</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1303">actions/setup-python#1303</a></li>
<li>Upgrade <code>@​actions/cache</code> to 5.1.0, log cache write denied by <a href="https://github.com/jasongin"><code>@​jasongin</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1324">actions/setup-python#1324</a></li>
<li>Upgrade dependency versions and test workflow configuration by <a href="https://github.com/HarithaVattikuti"><code>@​HarithaVattikuti</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1322">actions/setup-python#1322</a></li>
</ul>
<h3>Documentation</h3>
<ul>
<li>Update advanced-usage.md by <a href="https://github.com/Dunky-Z"><code>@​Dunky-Z</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/811">actions/setup-python#811</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/gowridurgad"><code>@​gowridurgad</code></a> with <a href="https://github.com/Copilot"><code>@​Copilot</code></a> made their first contribution in <a href="https://redirect.github.com/actions/setup-python/pull/1303">actions/setup-python#1303</a></li>
<li><a href="https://github.com/jasongin"><code>@​jasongin</code></a> made their first contribution in <a href="https://redirect.github.com/actions/setup-python/pull/1324">actions/setup-python#1324</a></li>
<li><a href="https://github.com/Dunky-Z"><code>@​Dunky-Z</code></a> made their first contribution in <a href="https://redirect.github.com/actions/setup-python/pull/811">actions/setup-python#811</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/actions/setup-python/compare/v6.2.0...v6.3.0">https://github.com/actions/setup-python/compare/v6.2.0...v6.3.0</a></p>
<h2>v6.2.0</h2>
<h2>What's Changed</h2>
<h3>Dependency Upgrades</h3>
<ul>
<li>Upgrade dependencies to Node 24 compatible versions by <a href="https://github.com/salmanmkc"><code>@​salmanmkc</code></a> in <a href="https://redirect.github.com/actions/setup-python/pull/1259">actions/setup-python#1259</a></li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/actions/setup-python/commit/6d4fd22b20465ccc0f7354476588e8df7c9ca0e0"><code>6d4fd22</code></a> Cache upgrade to 6.3.0 (<a href="https://redirect.github.com/actions/setup-python/issues/1370">#1370</a>)</li>
<li><a href="https://github.com/actions/setup-python/commit/ec52d0af729a7c50ced4261d17a07916f43f5b8e"><code>ec52d0a</code></a> Bump <code>@​typescript-eslint/eslint-plugin</code> from 8.62.0 to 8.71.1 (<a href="https://redirect.github.com/actions/setup-python/issues/1369">#1369</a>)</li>
<li><a href="https://github.com/actions/setup-python/commit/ff73b2463e2f3baa703f830da214b8dfeeaeccf8"><code>ff73b24</code></a> Bump prettier from 3.8.4 to 3.9.9 and package.json from 7.0.0 to 7.1.0 (<a href="https://redirect.github.com/actions/setup-python/issues/1363">#1363</a>)</li>
<li><a href="https://github.com/actions/setup-python/commit/0e40890053525508c059c61932a6b8614f9e95db"><code>0e40890</code></a> Bump brace-expansion from 5.0.9 to 5.0.12 (<a href="https://redirect.github.com/actions/setup-python/issues/1365">#1365</a>)</li>
<li><a href="https://github.com/actions/setup-python/commit/3892123fbe74688ccc83ec7c465dc688359e5199"><code>3892123</code></a> Bump ts-jest from 29.4.11 to 29.4.14 (<a href="https://redirect.github.com/actions/setup-python/issues/1361">#1361</a>)</li>
<li><a href="https://github.com/actions/setup-python/commit/660965736c4aecc62797ea07d351a3c259f14660"><code>6609657</code></a> Bump undici from 6.28.0 to 6.29.0 (<a href="https://redirect.github.com/actions/setup-python/issues/1364">#1364</a>)</li>
<li><a href="https://github.com/actions/setup-python/commit/e1be392b26fb1917a7b2c455817e4b4dad6544ce"><code>e1be392</code></a> Bump <code>@​types/semver</code> from 7.7.1 to 7.8.0 (<a href="https://redirect.github.com/actions/setup-python/issues/1359">#1359</a>)</li>
<li><a href="https://github.com/actions/setup-python/commit/06da6279cdbca41027908073e81a4544dc79c06b"><code>06da627</code></a> Bump <code>@​vercel/ncc</code> from 0.44.0 to 0.45.0 (<a href="https://redirect.github.com/actions/setup-python/issues/1357">#1357</a>)</li>
<li><a href="https://github.com/actions/setup-python/commit/af9bcc7548695e66d75709de6f29e337624b8de8"><code>af9bcc7</code></a> Bump eslint-plugin-jest from 29.15.2 to 29.16.6 (<a href="https://redirect.github.com/actions/setup-python/issues/1342">#1342</a>)</li>
<li><a href="https://github.com/actions/setup-python/commit/7aeabeba5501120d873c50398519dbfd0657031c"><code>7aeabeb</code></a> Bump <code>@​typescript-eslint/parser</code> from 8.62.0 to 8.70.0 (<a href="https://redirect.github.com/actions/setup-python/issues/1343">#1343</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/actions/setup-python/compare/v5...v7">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/setup-python&package-manager=github_actions&previous-version=5&new-version=7)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)


</details>

### Comments
**dependabot[bot]** (2026-11-10T00:21:12Z):

Looks like actions/setup-python is no longer a dependency, so this is no longer needed.

## #1 [closed] Bump actions/create-github-app-token from 1 to 3

- kind: PR
- labels: dependencies, github_actions
- created: 2026-11-09T23:39:54Z

Bumps [actions/create-github-app-token](https://github.com/actions/create-github-app-token) from 1 to 3.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/actions/create-github-app-token/releases">actions/create-github-app-token's releases</a>.</em></p>
<blockquote>
<h2>v3.0.0</h2>
<h1><a href="https://github.com/actions/create-github-app-token/compare/v2.2.2...v3.0.0">3.0.0</a> (2026-03-14)</h1>
<ul>
<li>feat!: node 24 support (<a href="https://redirect.github.com/actions/create-github-app-token/issues/275">#275</a>) (<a href="https://github.com/actions/create-github-app-token/commit/2e564a0bb8e7cc2b907b2401a2afe177882d4325">2e564a0</a>)</li>
<li>fix!: require <code>NODE_USE_ENV_PROXY</code> for proxy support (<a href="https://redirect.github.com/actions/create-github-app-token/issues/342">#342</a>) (<a href="https://github.com/actions/create-github-app-token/commit/4451bcbc139f8124b0bf04f968ea2586b17df458">4451bcb</a>)</li>
</ul>
<h3>Bug Fixes</h3>
<ul>
<li>remove custom proxy handling (<a href="https://redirect.github.com/actions/create-github-app-token/issues/143">#143</a>) (<a href="https://github.com/actions/create-github-app-token/commit/dce0ab05f36f30b22fd14289fd36655c618e4e8e">dce0ab0</a>)</li>
</ul>
<h3>BREAKING CHANGES</h3>
<ul>
<li>Custom proxy handling has been removed. If you use HTTP_PROXY or HTTPS_PROXY, you must now also set NODE_USE_ENV_PROXY=1 on the action step.</li>
<li>Requires <a href="https://github.com/actions/runner/releases/tag/v2.327.1">Actions Runner v2.327.1</a> or later if you are using a self-hosted runner.</li>
</ul>
<h2>v3.0.0-beta.6</h2>
<h1><a href="https://github.com/actions/create-github-app-token/compare/v3.0.0-beta.5...v3.0.0-beta.6">3.0.0-beta.6</a> (2026-03-13)</h1>
<h3>Bug Fixes</h3>
<ul>
<li><strong>deps:</strong> bump <code>@​actions/core</code> from 1.11.1 to 3.0.0 (<a href="https://redirect.github.com/actions/create-github-app-token/issues/337">#337</a>) (<a href="https://github.com/actions/create-github-app-token/commit/b04413352d4644ac2131b9a90c074f5e93ca18a1">b044133</a>)</li>
<li><strong>deps:</strong> bump minimatch from 9.0.5 to 9.0.9 (<a href="https://redirect.github.com/actions/create-github-app-token/issues/335">#335</a>) (<a href="https://github.com/actions/create-github-app-token/commit/5cbc65624c9ddc4589492bda7c8b146223e8c3e4">5cbc656</a>)</li>
<li><strong>deps:</strong> bump the production-dependencies group with 4 updates (<a href="https://redirect.github.com/actions/create-github-app-token/issues/336">#336</a>) (<a href="https://github.com/actions/create-github-app-token/commit/6bda5bc1410576b9a0879ce6076d53345485bba9">6bda5bc</a>)</li>
<li><strong>deps:</strong> bump undici from 7.16.0 to 7.18.2 (<a href="https://redirect.github.com/actions/create-github-app-token/issues/323">#323</a>) (<a href="https://github.com/actions/create-github-app-token/commit/b4f638f48ee0dcdbb0bc646c48e4cb2a2de847fe">b4f638f</a>)</li>
</ul>
<h2>v3.0.0-beta.5</h2>
<h1><a href="https://github.com/actions/create-github-app-token/compare/v3.0.0-beta.4...v3.0.0-beta.5">3.0.0-beta.5</a> (2026-03-13)</h1>
<ul>
<li>fix!: require <code>NODE_USE_ENV_PROXY</code> for proxy support (<a href="https://redirect.github.com/actions/create-github-app-token/issues/342">#342</a>) (<a href="https://github.com/actions/create-github-app-token/commit/d53a1cdfde844c958786293adcaf739ecb8b5eb9">d53a1cd</a>)</li>
</ul>
<h3>BREAKING CHANGES</h3>
<ul>
<li>Custom proxy handling has been removed. If you use HTTP_PROXY or HTTPS_PROXY, you must now also set NODE_USE_ENV_PROXY=1 on the action step.</li>
</ul>
<h2>v3.0.0-beta.4</h2>
<h1><a href="https://github.com/actions/create-github-app-token/compare/v3.0.0-beta.3...v3.0.0-beta.4">3.0.0-beta.4</a> (2026-03-13)</h1>
<h3>Bug Fixes</h3>
<ul>
<li><strong>deps:</strong> bump <code>@​octokit/auth-app</code> from 7.2.1 to 8.0.1 (<a href="https://redirect.github.com/actions/create-github-app-token/issues/257">#257</a>) (<a href="https://github.com/actions/create-github-app-token/commit/bef1eaf1c0ac2b148ee2a0a74c65fbe6db0631f1">bef1eaf</a>)</li>
<li><strong>deps:</strong> bump <code>@​octokit/request</code> from 9.2.3 to 10.0.2 (<a href="https://redirect.github.com/actions/create-github-app-token/issues/256">#256</a>) (<a href="https://github.com/actions/create-github-app-token/commit/5d7307be63501c0070c634b0ae8fec74e8208130">5d7307b</a>)</li>
<li><strong>deps:</strong> bump glob from 10.4.5 to 10.5.0 (<a href="https://redirect.github.com/actions/create-github-app-token/issues/305">#305</a>) (<a href="https://github.com/actions/create-github-app-token/commit/5480f4325a18c025ee16d7e081413854624e9edc">5480f43</a>)</li>
<li><strong>deps:</strong> bump p-retry from 6.2.1 to 7.1.0 (<a href="https://redirect.github.com/actions/create-github-app-token/issues/294">#294</a>) (<a href="https://github.com/actions/create-github-app-token/commit/dce3be8b284f45e65caed11a610e2bef738d15b4">dce3be8</a>)</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/actions/create-github-app-token/blob/main/CHANGELOG.md">actions/create-github-app-token's changelog</a>.</em></p>
<blockquote>
<h1>Changelog</h1>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/actions/create-github-app-token/commit/64ab729a6294000f5aa4a4bc0b73d1f32bc45510"><code>64ab729</code></a> chore(main): release 3.3.0 (<a href="https://redirect.github.com/actions/create-github-app-token/issues/402">#402</a>)</li>
<li><a href="https://github.com/actions/create-github-app-token/commit/f3a828e4b91180d3a46ac1f4b43fa8384b0dea07"><code>f3a828e</code></a> ci: create signed dist commits in release workflow (<a href="https://redirect.github.com/actions/create-github-app-token/issues/404">#404</a>)</li>
<li><a href="https://github.com/actions/create-github-app-token/commit/655017ffa7c6b0c6e4210729fa6bce35cacd8ca0"><code>655017f</code></a> docs: clarify when owner grants access to all repositories (<a href="https://redirect.github.com/actions/create-github-app-token/issues/378">#378</a>)</li>
<li><a href="https://github.com/actions/create-github-app-token/commit/12461a3a794e67c032f1eff5bb95ece9427eb4fb"><code>12461a3</code></a> fix(deps): bump nested undici from 6.24.0 to 6.29.0 (<a href="https://redirect.github.com/actions/create-github-app-token/issues/403">#403</a>)</li>
<li><a href="https://github.com/actions/create-github-app-token/commit/a47236f79f79fcbc3532af49fe3a5ded89529b6e"><code>a47236f</code></a> feat: update permission inputs (<a href="https://redirect.github.com/actions/create-github-app-token/issues/399">#399</a>)</li>
<li><a href="https://github.com/actions/create-github-app-token/commit/a69c19ddfdf8e1ab093900e0064524ce9309c807"><code>a69c19d</code></a> fix(deps): bump the production-dependencies group across 1 directory with 3 u...</li>
<li><a href="https://github.com/actions/create-github-app-token/commit/d5cb7ae41d64331820d88810a4878e0942ec992a"><code>d5cb7ae</code></a> build(deps): bump actions/checkout from 6 to 7 (<a href="https://redirect.github.com/actions/create-github-app-token/issues/384">#384</a>)</li>
<li><a href="https://github.com/actions/create-github-app-token/commit/575da866bd0a42d7f234a8645831d55573252b09"><code>575da86</code></a> build(deps): bump stefanzweifel/git-auto-commit-action from 7.1.0 to 7.2.0 in...</li>
<li><a href="https://github.com/actions/create-github-app-token/commit/e85f677b44da0d1f08115ce52cdfd8fd2c69874a"><code>e85f677</code></a> test: omit stack traces from snapshots (<a href="https://redirect.github.com/actions/create-github-app-token/issues/401">#401</a>)</li>
<li><a href="https://github.com/actions/create-github-app-token/commit/9419396df4d5672241cfb593dadc19758e54a204"><code>9419396</code></a> build(deps-dev): bump c8 from 11.0.0 to 12.0.0 (<a href="https://redirect.github.com/actions/create-github-app-token/issues/400">#400</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/actions/create-github-app-token/compare/v1...v3">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/create-github-app-token&package-manager=github_actions&previous-version=1&new-version=3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)


</details>

### Comments
**dependabot[bot]** (2026-11-10T00:21:14Z):

Looks like actions/create-github-app-token is no longer a dependency, so this is no longer needed.
