# Changelog / 変更履歴

DMGs for every release are available from [Releases](https://github.com/den0206/reborn-releases/releases).
Tags use the `Ver_X.Y.Z` form; a rebuild of the same `X.Y.Z` is tagged `Ver_X.Y.Z+N`, which the in-app
update check treats as newer than `X.Y.Z`.

各リリースの DMG は [Releases](https://github.com/den0206/reborn-releases/releases) から取得できます。
タグは `Ver_X.Y.Z` 形式で、同一 `X.Y.Z` の再ビルドには `Ver_X.Y.Z+N` が付きます
（`+N` はアプリのアップデート確認で `X.Y.Z` より新しい版として扱われます）。

> Entries below the marker are maintained automatically by
> [`.github/workflows/sync-release-docs.yml`](.github/workflows/sync-release-docs.yml): each published
> release is inserted here with its release notes verbatim. Release notes are authored in Japanese.
>
> 以下のエントリは [`.github/workflows/sync-release-docs.yml`](.github/workflows/sync-release-docs.yml)
> が自動で維持します。公開されたリリースのノートがそのまま挿入されます。
> 手元で反映したいときは `./scripts/refresh-docs.sh`（公開リリースを読み取って
> README・CHANGELOG・Issue テンプレートを更新する。認証不要）。

<!-- BEGIN:releases -->

## Ver_0.0.5 — 2026-08-11

### 変更点

#### 新機能
- F-20 の固定ショートカット ⌃⌥⌘Q を追加
- F-17 の再起動をまたぐ結果通知を追加

### 既知の問題

- なし

## Ver_0.0.4 — 2026-08-10

### 変更点

#### 新機能
- 全アプリ終了(F-20)を追加し popover の Liquid Glass 入れ子を解消

### 既知の問題

- なし

## Ver_0.0.3+1 — 2026-08-08

### 変更点

#### 新機能
- 上書き更新の成否表示と除外候補の隔離を配線する

#### 修正
- codesign -R の requirement に先頭 = を付ける
- 許可要求を未決定時の1回に制限する
- 破損 settings.json を quarantine する
- ウィンドウ不足を noWindowAvailable として集計する

### 既知の問題

- なし

## Ver_0.0.3 — 2026-08-08

### 変更点

#### 新機能
- 上書き更新の成否表示と除外候補の隔離を配線する

#### 修正
- 許可要求を未決定時の1回に制限する
- 破損 settings.json を quarantine する
- ウィンドウ不足を noWindowAvailable として集計する

### 既知の問題

- なし

## Ver_0.0.2+2 — 2026-08-07

### 追加

- **設置場所ガード** — マウント中の DMG・外付けディスク・Gatekeeper の移動保護下から起動した場合に、`アプリケーション` フォルダへの移動を提案するようになりました。
- **アンインストール** — 設定 >「情報」から、ログイン項目の解除 → 本体をゴミ箱 → 保存データ削除、までを一度に実行できるようになりました。
- `.app` と DMG の両方に署名・公証・ステープルを行うようになりました。

### 修正

- オンボーディングで、アクセシビリティの許可プロンプトをシステム設定を開くより先に出すようにしました（プロンプトが出ないまま進めなくなる問題の修正）。
- デバッグビルドがリリース版のグローバルショートカットを奪わないようにしました。

<details>
<summary>English</summary>

**Added** — Install location guard: offers to move Reborn into `Applications` when launched from a mounted
DMG, an external drive, or Gatekeeper's translocation. Uninstall: Settings > "About" now unregisters the
login item, trashes the app, and removes stored data in one step. Both the `.app` and the DMG are now
signed, notarized, and stapled.

**Fixed** — Onboarding shows the Accessibility prompt before opening System Settings, so the permission row
is always created. Debug builds no longer take over the release build's global shortcuts.

</details>

## Ver_0.0.2+1 — 2026-08-03

### 追加

- **アプリ内アップデート** — 新版検出時に、進捗表示付きで DMG を取得し、署名・公証・Team ID を検証してから自身を置き換えて再起動できるようになりました。
- **クリーン復元** — 同じレイアウトを 5 分以内にもう一度選ぶと、確認のうえレイアウト外のアプリを終了してから配置し直せるようになりました（既定 OFF）。
- **成功サウンド** — 保存・復元の成功時に控えめなシステムサウンドを鳴らすようになりました（設定で切替・既定 ON）。
- Liquid Glass サーフェスとデザイントークンを導入し、設定画面の区分・スクロール・Reduce Motion 対応を整理しました。
- レイアウト一覧を要約表示にし、配置プレビューの高さをドラッグで変えられるようになりました。
- 除外アプリの一覧と追加メニューにアプリアイコンを表示するようになりました。
- 再ビルド番号 `+N` を、より新しい版として比較するようになりました。

### 修正

- 設定・レイアウトファイルをパーミッション `0600` で書き込むようにし、保存失敗をログに残すようにしました。
- 旧バージョンで保存したレイアウトが読み込めなくなる場合がある問題を修正しました（後方互換デコードの追加）。
- 常駐タスクの循環参照によるメモリ保持を解消しました。
- アップデート処理の残骸を掃除するようにし、外部プロセスの出力読み取りを修正しました。

<details>
<summary>English</summary>

**Added** — In-app update: downloads the DMG with a progress indicator, verifies signature, notarization,
and Team ID, then replaces the app and relaunches. Clean restore: re-selecting the same layout within 5
minutes offers to quit apps outside the layout before rearranging (off by default). Success sound: a
discreet system sound after a successful save or restore (toggleable, on by default). Liquid Glass surfaces
and design tokens, plus reworked settings grouping, scrolling, and Reduce Motion support. The layout list is
summarized and the layout preview can be resized by dragging. App icons in the exclusion list and its add
menu. Rebuild numbers (`+N`) are compared as newer versions.

**Fixed** — Settings and layout files are written with `0600` permissions and save failures are logged.
Layouts saved by older versions no longer fail to load (backward-compatible decoding). Removed a retain
cycle in long-lived tasks. Update leftovers are cleaned up and external process output reading was fixed.

</details>

## Ver_0.0.2 — 2026-08-02

### 追加

- **配置プレビュー** — 保存済みレイアウトをミニマップで確認できるようになりました。アプリごとに色分けし、モニターバッジで選択をトグルできます。
- **自動復元** — 設定の単一トグルに集約し、モニター構成の変化を検知して一致するレイアウトを適用します。
- 同名のレイアウトを保存したときに、末尾へ番号を付けて一意化するようになりました。

<details>
<summary>English</summary>

**Added** — Layout preview: a minimap of saved layouts, color-coded per app, with the display badge toggling
selection. Auto restore: consolidated into a single setting that detects display configuration changes and
applies the matching layout. Saving a layout with a duplicate name now appends a number to keep names unique.

</details>

## Ver_0.0.1+2 — 2026-08-01

**Full Changelog**: https://github.com/den0206/reborn-releases/commits/Ver_0.0.1+2

## Ver_0.0.1+1 — 2026-08-01

**Full Changelog**: https://github.com/den0206/reborn-releases/commits/Ver_0.0.1+1

## Ver_0.0.1 — 2026-08-01

最初の公開リリース。

- レイアウトの保存・復元・管理（一覧・リネーム・上書き更新・削除・並べ替え）
- モニターを UUID で同定するマルチモニター対応と、構成不一致時の相対座標での再配置
- モニター枚数ガード（台数が保存時と異なる場合は復元しない）
- アクセシビリティ権限のオンボーディング
- グローバルショートカット、ログイン時に起動、復元結果の通知
- 書き出し / 読み込み、除外アプリ、プライバシーモード
- アップデート確認（手動発火のみ）

<details>
<summary>English</summary>

First public release — save, restore, and manage layouts (list, rename, update in place, delete, reorder);
multi-monitor support with UUID-based display identification and relative-coordinate remapping; display
count guard; Accessibility permission onboarding; global shortcuts, open at login, restore summary
notifications; export / import, app exclusions, privacy mode; update check (manual trigger only).

</details>

<!-- END:releases -->
