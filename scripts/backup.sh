#!/usr/bin/env bash
# Operator backup: one git bundle per local repository. No schedule, no token.
set -euo pipefail

root="${1:-$HOME/github}"
out="${2:-$HOME/backups/$(date -u +%F)}"
mkdir -p "$out"

count=0
while IFS= read -r gitdir; do
  repo="$(dirname "$gitdir")"
  rel="${repo#"$root"/}"
  name="${rel//\//-}"
  bundle="$out/${name}.bundle"
  git -C "$repo" bundle create "$bundle" --all >/dev/null
  git -C "$repo" bundle verify "$bundle" >/dev/null
  count=$((count + 1))
  printf 'ok %s\n' "$bundle"
done < <(find "$root" -mindepth 3 -maxdepth 3 -type d -name .git | sort)

printf '%d bundles in %s\n' "$count" "$out"
