'''Interface from the orm repository'''
from abc import ABC, abstractmethod

class IORMRepository(ABC):
    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def select_all(self):
        pass
