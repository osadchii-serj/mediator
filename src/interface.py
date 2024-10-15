from abc import ABC, abstractmethod


class WindowBase(ABC):

    @abstractmethod
    def show(self):
        raise NotImplementedError()

    @abstractmethod
    def hide(self):
        raise NotImplementedError()
