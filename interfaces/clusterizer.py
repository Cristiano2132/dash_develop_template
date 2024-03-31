from abc import ABC, abstractmethod

class IClusterizer(ABC):

    @abstractmethod
    def execute(self, n_clusters=None):
        pass

    @abstractmethod
    def get_labels(self):
        pass
