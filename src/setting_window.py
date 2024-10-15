from interface import WindowBase


class SettingWindow(WindowBase):

    def show(self):
        return "Показать окно настройки"

    def hide(self):
        return "Скрыть настройки окна"
