from interface import WindowBase


class MainWindow(WindowBase):

    def show(self):
        print("Показать главное окно")

    def hide(self):
        print("Скрыть главное окно")
