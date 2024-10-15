from interface import WindowBase


class SettingWindow(WindowBase):

    def show(self):
        print("Показать окно настройки")

    def hide(self):
        print("Скрыть настройки окна")
