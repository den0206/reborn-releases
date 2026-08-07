# プライバシーポリシー / Privacy Policy

日本語 · [English](#english)

**最終更新: 2026-08-08**

---

## 要約

**Reborn はあなたのデータを収集しません。送信もしません。**
すべてのデータはあなたの Mac のローカルディスクにのみ保存されます。

Reborn は完全無料ですが、**その対価としてデータを収益化することはありません**。
広告配信・データの販売・行動分析・プロファイリングのいずれも行いません。

## 収集・保存する情報

Reborn がローカルに保存するのは、レイアウト機能に必要な次の情報だけです。

| 項目 | 内容 |
|------|------|
| ウィンドウの位置・サイズ | 復元先を決めるために必要です |
| ウィンドウのタイトル | 復元時に「どのウィンドウか」を照合するために使います。設定「ウィンドウタイトルを保存しない」で無効にできます |
| 最小化状態 | 保存時に最小化されていたウィンドウを、復元時も最小化するために使います |
| アプリの Bundle ID | ウィンドウの持ち主のアプリを特定するために使います |
| ディスプレイの UUID・解像度・配置 | どのモニターに戻すかを決めるために使います |
| アプリ設定 | 各種トグル、ショートカット割当、除外アプリの一覧 |

保存先は次のとおりです（パーミッション `0600`）。

```
~/Library/Application Support/Reborn
```

## 収集しない情報

- **ウィンドウの内容** — 画面のキャプチャや、ウィンドウ内のテキストの読み取りは一切行いません
- **キー入力** — キーロギングやキーボードイベントの監視は行いません
- **個人情報** — 氏名・メールアドレス・アカウント情報は不要で、収集もしません
- **利用状況・アナリティクス** — 起動回数、機能の利用状況、クラッシュレポートを含め、いかなる分析データも送信しません
- **識別子** — 広告 ID、デバイス ID、インストール ID の類は生成も送信もしません

## ネットワーク通信

Reborn は原則としてネットワーク通信を行いません。例外は、**あなたが自分でボタンを押したときだけ**発生する次の 2 つです。

1. **「アップデートを確認」** — GitHub の公開リリース情報を 1 回だけ取得します
2. **「アップデート」** — 新しいバージョンの DMG をダウンロードします

いずれも通信先は `github.com` および `*.githubusercontent.com` に限定されています。
起動時の自動チェックやバックグラウンド通信は行いません。
これらのリクエストに、あなたを識別できる情報は含まれません（GitHub 側には、公開ファイルへのアクセス時の
通常のリクエスト情報 — IP アドレスや User-Agent など — が記録されます。これは GitHub のプライバシーポリシーの適用範囲です）。

## アクセシビリティ権限について

Reborn は macOS の **アクセシビリティ権限**を必要とします。
他のアプリのウィンドウを移動・リサイズするために、macOS が必須としている権限です。

この権限を通じて Reborn が読み書きするのは、**ウィンドウの位置・サイズ・タイトル・最小化状態のみ**です。
アクセシビリティ権限は技術的にはより広い範囲にアクセスできますが、Reborn はこの用途以外には使用しません。

## 第三者への提供

Reborn はデータを送信しないため、第三者への提供・販売・共有は発生しません。
サードパーティの SDK やライブラリも一切組み込んでいません。

## 他のアプリへの影響

Reborn が他のアプリを終了させるのは、**クリーン復元**機能のときだけです。
設定を有効にしたうえで、確認ダイアログを承認した場合に限られます。
送るのは通常の終了（Quit）のみで、強制終了は行いません。そのため未保存の変更があるアプリは終了されません。

## データの削除

設定 >「情報」→「Reborn をアンインストール…」を実行すると、保存データはすべて削除されます。
手動で削除する場合は `~/Library/Application Support/Reborn` を削除してください。

## お問い合わせ

質問がある場合は [Issues](https://github.com/den0206/reborn-releases/issues) からお知らせください。

---

<a name="english"></a>

# Privacy Policy (English)

**Last updated: 2026-08-08**

## Summary

**Reborn does not collect your data, and does not transmit it anywhere.**
Everything is stored locally on your Mac.

Reborn is completely free, and **your data is not what pays for it**.
There is no ad serving, no sale of data, no behavioral analysis, and no profiling.

## What is stored

Reborn stores only what the layout feature needs, and only on your machine.

| Item | Purpose |
|------|---------|
| Window position and size | Determines where a window is restored to |
| Window title | Used to match "which window is which" at restore time. Can be disabled with the "Do not save window titles" setting |
| Minimized state | Restores windows that were minimized when saved |
| App bundle ID | Identifies which app a window belongs to |
| Display UUID, resolution, and arrangement | Determines which monitor a window returns to |
| App settings | Toggles, shortcut assignments, and the exclusion list |

Stored at (with `0600` permissions):

```
~/Library/Application Support/Reborn
```

## What is never collected

- **Window contents** — no screen capture, no reading of text inside windows
- **Keyboard input** — no key logging, no keyboard event monitoring
- **Personal information** — no name, email, or account is required or collected
- **Usage data or analytics** — no launch counts, no feature usage, no crash reports
- **Identifiers** — no advertising ID, device ID, or install ID is generated or sent

## Network access

Reborn makes no network requests by default. The only exceptions occur **when you press a button yourself**:

1. **"Check for Updates"** — fetches public GitHub release information once
2. **"Update"** — downloads the DMG for the new version

Both are restricted to `github.com` and `*.githubusercontent.com`.
There is no launch-time check and no background traffic.
These requests contain nothing that identifies you (GitHub records the usual request metadata for public
file access — IP address, User-Agent and similar — which falls under GitHub's own privacy policy).

## About Accessibility permission

Reborn requires macOS **Accessibility permission**, which macOS mandates for any app that moves or
resizes another app's windows.

Through that permission, Reborn reads and writes **only window position, size, title, and minimized state**.
Accessibility permission technically grants broader access; Reborn does not use it for anything else.

## Third parties

Since no data leaves your Mac, nothing is shared with, sold to, or disclosed to third parties.
No third-party SDKs or libraries are bundled.

## Effect on other apps

The only feature that quits other apps is **clean restore**, and only when you have enabled the setting
and approved the confirmation. It sends a normal Quit — never a force quit — so apps with unsaved changes
are not terminated.

## Deleting your data

Settings > "About" → "Uninstall Reborn…" removes all stored data.
To remove it manually, delete `~/Library/Application Support/Reborn`.

## Contact

Questions are welcome at [Issues](https://github.com/den0206/reborn-releases/issues).
