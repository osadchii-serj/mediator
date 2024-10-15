from interface import WindowBase


class HelpWindow(WindowBase):

    def show(self):
        print("Показать окно справки")

    def hide(self):
        print("Скрыть окно справки")
