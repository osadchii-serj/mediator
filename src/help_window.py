from interface import WindowBase


class HelpWindow(WindowBase):

    def show(self):
        return "Показать окно справки"

    def hide(self):
        return "Скрыть окно справки"
