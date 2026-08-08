#!/bin/sh
# 公開リリースを読み取って、版に依存するドキュメントを更新する。
#
#   ./scripts/refresh-docs.sh                        最新の公開リリースに合わせて更新
#   ./scripts/refresh-docs.sh --regenerate Ver_0.0.3 指定タグの節を本文から作り直す
#   REPO=owner/name ./scripts/refresh-docs.sh        取得先リポジトリを変える
#
# ワークフロー(sync-release-docs.yml)もローカルもこれを通す。取得の仕方が 2 か所に
# 分かれていると「CI では直るのに手元では直らない(逆も)」が起きるため。
#
# 取得は gh があれば gh、無ければ curl。どちらも公開リポジトリの REST を読むだけで
# 認証は要らない。/releases はリリース本文まで 1 回で返すので、タグごとの追加取得は不要。
set -eu

REPO="${REPO:-den0206/reborn-releases}"
API="repos/${REPO}/releases?per_page=100"

OUT="$(mktemp)"
trap 'rm -f "$OUT"' EXIT

if ! { command -v gh >/dev/null 2>&1 && gh api "$API" >"$OUT" 2>/dev/null; }; then
    curl -fsSL -H 'Accept: application/vnd.github+json' \
        "https://api.github.com/${API}" >"$OUT"
fi

python3 "$(dirname "$0")/sync-release-docs.py" "$OUT" "$@"
