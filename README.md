# stamp-rally-project
スタンプラリー企画のリポジトリ

## 初期設定
### 仮想環境を作る

```
python3 -m venv venv
(末尾のvenvは任意の仮想環境名)
```

### 仮想環境を有効化

```
source ./venv/bin/activate
or
.\venv\Scripts\activate
```

### モジュールの一括インストール

```
pip install -r requirements.txt
```

### .envファイルの作成

- stamp-rally-project直下に`.env`ファイルを作成し、委員会内で配布されている内容を貼り付け後、保存する

### 動作確認をする

```
python3 manage.py migrate
```

```
python3 manage.py runserver
```