from abc import ABCMeta, abstractmethod

class IMethodology(metaclass=ABCMeta):
    "The switch interface, that all commands will implement"

    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"

