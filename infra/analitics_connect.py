import pandas as pd
import sqlalchemy
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from interfaces.database_connection import IDatabaseConnection


class PostgreConnection(IDatabaseConnection):
    def __init__(self, database: str, user: str, password: str, host: str, port: str):
        self.__db_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        self.__engine = sqlalchemy.create_engine(self.__db_url)
        self.conn = self.__engine.connect()

    def execute_query(self, query: str):
        try:
            res = self.conn.execute(text(query))
        except Exception as X:
            return X
        return res

    def query_to_pd_dataframe(self, query):
        return pd.read_sql(query, con=self.conn)
    
    def get_session(self):
        Session = sessionmaker(bind=self.__engine)
        return Session()

