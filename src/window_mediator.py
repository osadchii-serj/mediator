from dataclasses import dataclass

from setting_window import SettingWindow
from main_window import MainWindow
from help_window import HelpWindow

from interface import WindowBase


@dataclass
class WindowMediator:

    windows = {
        "setting": SettingWindow(),
        "main": MainWindow(),
        "help": HelpWindow(),
    }

    def show(self, win: WindowBase):
        for window in self.windows.values():
            if window is not win:
                window.hide()
        win.show()
