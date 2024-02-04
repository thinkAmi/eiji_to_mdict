# eiji_to_mdict

英辞郎のテキストデータファイルをMDict形式に変換するライブラリです。

## ライブラリのベースとなったソースコード

以下のGistsで公開しているソースコードがベースになっています。  
https://gist.github.com/k141303/b554bef3911ce5ee9f40c42459420b61

ソースコードを公開してくださり、ありがとうございます。

なお、元々のソースコードは以下のコミットで確認できます。  
https://github.com/thinkAmi/eiji_to_mdict/commit/4dea35cfce80c586977bb2eea37165f7070a56a5

　  
## 使い方
### 事前準備
#### 英辞郎のテキストデータ

ローカル環境に英辞郎のテキストデータをダウンロードします。

2024年2月時点では、BOOTHでテキストデータが販売されています。  
https://edp.booth.pm/items/777563

　  
#### Python環境

Pythonの仮想環境を用意します。

```
$ python --version
Python 3.12.1

$ python -m venv env

$ source env/bin/activate
```

仮想環境に `eiji_to_mdict` をインストールします。

なお、PyPIでの公開予定はありませんので、Githubのリポジトリからインストールします。

```
(env) $ python -m pip install "git+https://github.com/thinkAmi/eiji_to_mdict.git"
```

ダウンロードした英辞郎のテキストデータをコピーしておきます。

なお、英辞郎のテキストデータはzipファイルで固められているという前提でいます。

```
(env) $ cp path/to/<英辞郎のテキストデータのファイル名>.zip .
```

### 変換する

`eiji_to_mdict` コマンドで変換します。

```
(env) $ eiji_to_mdict <英辞郎のテキストデータファイル>
```

変換が終わると、以下の2ファイルが作成されます。

- eijiro.mdx
  - 単語辞書
- eijidiom.mdx
  - 熟語辞書

## 開発方法について

このリポジトリをgit cloneし、 `pip install -e .` で開発します。


# 動作確認環境

- Python 3.12.1
- 英辞郎 Ver.144.9（2024年1月10日版）のテキストデータ
- WSL2

# 関連ブログ

- [Pythonを使って、BOOTHで販売している英辞郎のテキストデータをMDict化し、BOOX Leaf2 の辞書に登録してみた - メモ的な思考的な](https://thinkami.hatenablog.com/entry/2024/02/04/185339)