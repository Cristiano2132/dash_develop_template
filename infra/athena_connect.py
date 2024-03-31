from pyathena import connect
import pandas as pd

from interfaces.database_connection import IDatabaseConnection


class PyAthenaConnetion(IDatabaseConnection):
    def __init__(self, s3_staging_dir: str, region_name: str, access_key_id: str, secret_key_id: str):
        self.conn = connect(aws_access_key_id=access_key_id,
                            aws_secret_access_key=secret_key_id,
                            s3_staging_dir=s3_staging_dir,
                            region_name=region_name)

    def databases(self):
        dbs = self.execute_query("show databases;")
        return dbs

    def tables(self, database):
        tables = self.execute_query("show tables in {0};".format(database))
        return tables

    def execute_query(self, query: str):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                res = cursor.fetchall()
        except Exception as X:
            return []
        finally:
            self.conn.close()
        return res

    def query_to_pd_dataframe(self, query):
        return pd.read_sql_query(query, self.conn)
    
    def get_session(self):
        return None
