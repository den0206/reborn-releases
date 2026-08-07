#!/usr/bin/env python3
"""公開済みリリースに合わせて README / CHANGELOG を書き換える。

`.github/workflows/sync-release-docs.yml` から呼ばれる。標準ライブラリのみ・通信なし
(リリース情報は gh CLI が取得して JSON で渡す)。

    scripts/sync-release-docs.py <releases.json> [--regenerate TAG[,TAG...]]

<releases.json> は `gh release list --json tagName,publishedAt,isDraft,isPrerelease,body` の出力。

書き換える箇所:
  - README.md / README.ja.md の <!-- BEGIN:latest-release --> ブロック(最新版と公開日)
  - CHANGELOG.md の <!-- BEGIN:releases --> ブロック(タグごとの節を新しい順に並べる)

CHANGELOG は**未知のタグだけ**を描画して足す。既にある節は触らないので、公開後に手で
整えた文面が次回の実行で消えることはない。リリース本文を編集し直して反映したいときだけ
--regenerate でタグを名指しする(ワークフローの手動実行から渡せる)。
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "den0206/reborn-releases"

LATEST_BEGIN = "<!-- BEGIN:latest-release -->"
LATEST_END = "<!-- END:latest-release -->"
RELEASES_BEGIN = "<!-- BEGIN:releases -->"
RELEASES_END = "<!-- END:releases -->"


def fail(message: str) -> None:
    print(f"::error::{message}", file=sys.stderr)
    raise SystemExit(1)


def replace_block(text: str, begin: str, end: str, body: str, name: str) -> str:
    """begin/end マーカーの内側を body で置き換える。マーカーが無ければエラー。"""
    start = text.find(begin)
    stop = text.find(end)
    if start == -1 or stop == -1 or stop < start:
        fail(f"{name} に {begin} / {end} のマーカーが揃っていません")
    return text[: start + len(begin)] + body + text[stop:]


def published_date(release: dict) -> str:
    """ISO8601 の publishedAt を YYYY-MM-DD にする。欠けていれば空文字。"""
    raw = release.get("publishedAt") or ""
    try:
        return (
            datetime.fromisoformat(raw.replace("Z", "+00:00"))
            .astimezone(timezone.utc)
            .strftime("%Y-%m-%d")
        )
    except ValueError:
        return ""


def version_of(tag: str) -> str:
    """タグ Ver_X.Y.Z(+N) から X.Y.Z(+N) を取り出す。Ver_ が無ければタグそのまま。"""
    return tag[4:] if tag.startswith("Ver_") else tag


def demote_headings(body: str) -> str:
    """本文中の見出しを、いちばん浅いものが ### になるようまとめて下げる。

    CHANGELOG のタグ見出し(##)より浅い見出しがリリース本文に入っていると、
    文書構造が壊れて目次も崩れるため。相対的な深さは保つ。
    """
    levels = [len(m) for m in re.findall(r"(?m)^(#{1,6})(?= )", body)]
    if not levels:
        return body
    delta = 3 - min(levels)
    if delta <= 0:
        return body
    return re.sub(
        r"(?m)^(#{1,6})(?= )",
        lambda m: "#" * min(len(m.group(1)) + delta, 6),
        body,
    )


def render_section(release: dict) -> str:
    tag = release["tagName"]
    date = published_date(release)
    heading = f"## {tag} — {date}" if date else f"## {tag}"
    body = demote_headings((release.get("body") or "").strip())
    if not body:
        body = f"[Release ページ](https://github.com/{REPO}/releases/tag/{tag})"
    return f"{heading}\n\n{body}\n"


# タグ見出し: "## <tag>" と、その後ろに続く任意の文字列(既定は " — YYYY-MM-DD")。
# 日付の書式を手で整えても節を見失わないよう、タグ名より後ろは緩く受ける。
# 節の切り出しに使ってよいかは、下の known_tags / Ver_ 判定で絞る。
_SECTION_HEADING = re.compile(r"(?m)^## (\S+)(?:\s.*)?$")


def split_sections(block: str, known_tags: "set[str] | None" = None) -> "dict[str, str]":
    """CHANGELOG の releases ブロックをタグ見出し単位に割る(タグ → 節本文)。

    境界にするのは「## <タグ> …」の行のうち、タグが known_tags に含まれるか
    Ver_ で始まるものだけ。節内へ手で足した ## 見出し(「## 補足」等)は
    本文として残し、偽タグ化して別の場所へ飛ばさない。
    """
    known = known_tags or set()
    starts: list[tuple[int, str]] = []
    for match in _SECTION_HEADING.finditer(block):
        tag = match.group(1)
        if tag in known or tag.startswith("Ver_"):
            starts.append((match.start(), tag))

    sections: dict[str, str] = {}
    for i, (start, tag) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(block)
        sections[tag] = block[start:end].rstrip() + "\n"
    return sections


def update_readmes(latest: dict) -> "list[str]":
    version = version_of(latest["tagName"])
    date = published_date(latest)
    blocks = {
        "README.md": (
            '\n<p align="center">\n'
            f"  Latest release: <strong>{version}</strong>"
            + (f" (released {date})" if date else "")
            + "\n</p>\n"
        ),
        "README.ja.md": (
            '\n<p align="center">\n'
            f"  最新版: <strong>{version}</strong>"
            + (f"（{date} 公開）" if date else "")
            + "\n</p>\n"
        ),
    }
    changed = []
    for name, block in blocks.items():
        path = ROOT / name
        if not path.exists():
            fail(f"{name} が見つかりません")
        before = path.read_text(encoding="utf-8")
        after = replace_block(before, LATEST_BEGIN, LATEST_END, block, name)
        if after != before:
            path.write_text(after, encoding="utf-8")
            changed.append(name)
    return changed


def update_changelog(releases: "list[dict]", regenerate: "set[str]") -> "list[str]":
    path = ROOT / "CHANGELOG.md"
    before = path.read_text(encoding="utf-8")
    start = before.find(RELEASES_BEGIN)
    stop = before.find(RELEASES_END)
    if start == -1 or stop == -1 or stop < start:
        fail("CHANGELOG.md に releases マーカーが揃っていません")

    known_tags = {r["tagName"] for r in releases}
    sections = split_sections(
        before[start + len(RELEASES_BEGIN) : stop], known_tags
    )
    for release in releases:
        tag = release["tagName"]
        if tag in regenerate or tag not in sections:
            sections[tag] = render_section(release)

    # 並び順は公開日の降順。API に無いタグ(削除されたリリース等)は末尾に残す。
    order = [r["tagName"] for r in releases]
    order += [tag for tag in sections if tag not in order]
    block = "\n\n" + "\n\n".join(sections[tag].rstrip() for tag in order) + "\n\n"

    after = before[: start + len(RELEASES_BEGIN)] + block + before[stop:]
    if after == before:
        return []
    path.write_text(after, encoding="utf-8")
    return ["CHANGELOG.md"]


def main() -> None:
    args = sys.argv[1:]
    regenerate: set[str] = set()
    if "--regenerate" in args:
        i = args.index("--regenerate")
        if i + 1 >= len(args):
            fail(
                "usage: sync-release-docs.py <releases.json> "
                "[--regenerate TAG[,TAG...]]"
            )
        regenerate = {t.strip() for t in args[i + 1].split(",") if t.strip()}
        del args[i : i + 2]
    if len(args) != 1:
        fail(
            "usage: sync-release-docs.py <releases.json> "
            "[--regenerate TAG[,TAG...]]"
        )

    releases = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    releases = [r for r in releases if not r.get("isDraft") and not r.get("isPrerelease")]
    if not releases:
        print("::notice::公開済みリリースがありません。何もしません。")
        return

    # gh は新しい順で返すが、依存せず publishedAt の降順に並べ直す。
    releases.sort(key=lambda r: r.get("publishedAt") or "", reverse=True)

    changed = update_readmes(releases[0]) + update_changelog(releases, regenerate)
    if changed:
        print(f"::notice::更新: {', '.join(changed)}")
    else:
        print("::notice::ドキュメントは既に最新です。")


if __name__ == "__main__":
    main()
