from abc import ABC, abstractmethod

import pandas as pd
from business.dto import AplicationMapDTO
from infra.aws_cli_connect import AwsCliConnect

from interfaces.database_connection import IDatabaseConnection

class IEngine(ABC):
    def __init__(self):
        self.data_to_be_used: list
        self.target_crs_str: str
        self.s3_bucket_name: str
        self.aws_cli_connection: AwsCliConnect
        self.athena_connection: IDatabaseConnection
        self.analytics_connection: IDatabaseConnection
        self.crs_dict_str: dict
        self.data: pd.DataFrame = None
        self.dto: AplicationMapDTO

    @abstractmethod
    def clusterize(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def initialize_connections(self):
        pass
