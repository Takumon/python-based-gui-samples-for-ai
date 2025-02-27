import customtkinter
import py_hot_reload
from enum import Enum
import ai.util as util
from view.FileInput import View as FileInputView
from view.TextInput import View as TextInputView

class Tab(Enum):
    要件定義_テキストから = "要件定義（テキスト入力）"
    要件定義_ファイルから = "要件定義（ファイル入力）"
    検索 = "検索"

class App(customtkinter.CTk):
    """GUIアプリ

    本クラスではタブ切り替えの定義のみを行い、各タブの内容は別クラスに委譲する
    """
    def __init__(self, requirements_definition_from_text,requirements_definition_from_file, search):
        super().__init__()

        self.title("AIを使った開発")
        self.geometry("600x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tab = customtkinter.CTkTabview(master=self)
        self.tab.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nwes")
        Tab_要件定義_テキストから = self.tab.add(Tab.要件定義_テキストから.value)
        Tab_要件定義_ファイルから = self.tab.add(Tab.要件定義_ファイルから.value)
        Tab_検索 = self.tab.add(Tab.検索.value)
        self.tab.set(Tab.要件定義_テキストから.value)

        TextInputView(
            master=Tab_要件定義_テキストから,
            ask_ai_fn=requirements_definition_from_text)

        FileInputView(
            master=Tab_要件定義_ファイルから,
            ask_ai_fn=requirements_definition_from_file)

        FileInputView(
            master=Tab_検索,
            ask_ai_fn=search)


def main():
    app = App(
        util.requirements_definition_from_text,
        util.requirements_definition_from_file,
        util.search)
    app.mainloop()

# コマンド「py-hot-reload app.py」用
py_hot_reload.run_with_reloader(main)
