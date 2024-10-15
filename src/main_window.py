from interface import WindowBase


class MainWindow(WindowBase):

    def show(self):
        return "Показать главное окно"

    def hide(self):
        return "Скрыть главное окно"
