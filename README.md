# translation-sample

## 動作環境

- Python3.11

## 環境構築例

```console
python -m venv .venv
.venv/Scripts/activate.ps1
pip install -r requrements.txt
```

## 設定例

### config.yaml

```yaml
services:
  - "deepl" # 環境変数 DEEPL_TOKEN が必要
```

## 実行例

```bash
# python main.py -i input.csv -o output と同じ
python main.py

# 入力ファイルや出力ディレクトリを変えたいとき
python main.py -i hoge.csv -o dist
```