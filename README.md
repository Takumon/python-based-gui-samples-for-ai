# python-based-gui-samples-for-ai

AI向けのGUIサンプルです。

- [customtkinter](./customtkinter/)
  - [Customtkinter](https://customtkinter.tomschimansky.com/)制のGUIアプリ
- [reactpy](./reactpy/)
  - [ReactPy](https://reactpy.dev/docs/index.html)制のGUIアプリ

## 起動方法

### ライブラリのインストール

- 以下コマンドを実行して、必要なライブラリをインストールします。
  ```bash
  # リポジトリをクローン
  git clone https://github.com/Takumon/python-based-gui-samples-for-ai.git
  # ディレクトリに移動
  cd python-based-gui-samples-for-ai

  # 仮想環境を作成
  python -m venv venv
  # 仮想環境を有効化(windowsnの場合)
  venv/bin/activate
  # 仮想環境を有効化(linux/macの場合)
  source venv/bin/activate

  # 必要なライブラリをインストール
  pip install -r requirements.txt
  ```

### Customtkinter制GUIの起動

- 以下コマンドを実行します。
  ```bash
  python customtkinter/app.py
  ```
- GUIが起動します。

### ReactPy制GUIの起動

- 以下コマンドを実行します。
  ```bash
  python reactpy/app.py
  ```
- ブラウザにて`http://127.0.0.1:8000/`にアクセスします。
