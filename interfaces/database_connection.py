from abc import ABC, abstractmethod
import pandas as pd

class IDatabaseConnection(ABC):
    @abstractmethod
    def execute_query(self, query: str):
        pass

    @abstractmethod
    def query_to_pd_dataframe(self, query: str) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_session(self):
        pass
