import datetime
import os
import typer
from rich.console import Console
from rich.table import Table
from sqlmodel import Session, select
from sqlalchemy import inspect
from app.config import settings
from app.db import engine
from app.models import User, SQLModel
from sqlalchemy.ext.declarative import declarative_base

main = typer.Typer(name="devapp CLI")

@main.command()
def shell():
    """Opens interactive shell"""
    _vars = {
        "settings": settings,
        "engine": engine,
        "select": select,
        "session": Session(engine),
        # "ApplicationMap": ApplicationMap,
        # "ApplicationMapDataSourceKey": ApplicationMapDataSourceKey,
        # "ApplicationMapDataSource": ApplicationMapDataSource,
        # "ApplicationMapProduct": ApplicationMapProduct,
    }
    typer.echo(f"Auto imports: {list(_vars.keys())}")
    try:
        from IPython import start_ipython
        start_ipython(
            argv=["--ipython-dir=/tmp", "--no-banner"], user_ns=_vars
        )
    except ImportError:
        import code
        code.InteractiveConsole(_vars).interact()

@main.command()
def say_hello():
    print("Hello World.")


# @main.command()
# def data_sources_list():
#     '''Lists all data sources'''
#     table_title="devapp data sources"

#     with Session(engine) as session:
#         data_sources = session.exec(select(ApplicationMapDataSource)).all()
#     printer_rows = PrintRows(data_sources)
#     printer_rows.print_table(table_title=table_title)

# @main.command()
# def clean_all_tables():
#     '''Clean all tables'''
#     def clean_table(session, model):
#         session.query(model).delete()
#         session.commit()

#     with Session(engine) as session:
#         clean_table(session, ApplicationMapDataSourceKey)
#         clean_table(session, ApplicationMapProduct)
#         clean_table(session, ApplicationMapDataSource)
#         clean_table(session, ApplicationMap)
#         session.commit()
#     typer.echo("All tables cleaned")

# @main.command()
# def clean_table(table_name: str):
#     '''Clean a table, to see the table names use the command get_tables_names'''
#     def clean_table(session, model):
#         session.query(model).delete()
#         session.commit()

#     with Session(engine) as session:
#         if table_name == "application_map":
#             clean_table(session, ApplicationMap)
#         elif table_name == "application_map_data_source":
#             clean_table(session, ApplicationMapDataSource)
#         elif table_name == "application_map_data_source_key":
#             clean_table(session, ApplicationMapDataSourceKey)
#         elif table_name == "application_map_product":
#             clean_table(session, ApplicationMapProduct)
#         else:
#             typer.echo("Table name not found")
#             return
#         session.commit()
#     typer.echo(f"Table {table_name} cleaned")


@main.command()
def get_tables_names():
    '''Get all tables names'''
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    typer.echo(tables)


@main.command()
def reset_dev_data_base():
    '''Delete all tables'''
    cmd = 'alembic downgrade base'
    os.system(cmd)
    Base = declarative_base()
    Base.metadata.drop_all(engine)
    cmd = 'alembic upgrade head'
    os.system(cmd)
    typer.echo("Data base reseted")


@main.command()
def init_dev_data_base():
    '''Init data base'''
    cmd = 'alembic upgrade head'
    os.system(cmd)
    typer.echo("Data base initialized")



@main.command()
def init_test_data_base():
    '''Init data base for tests'''
    cmd = 'alembic upgrade head'
    os.system(cmd)
    typer.echo("Data base initialized")
#     values_dict = {
#         'method': 'k_means', 
#         'date': datetime.datetime.utcnow(), 
#         'variables': 'test', 
#         'updated_at': datetime.datetime.utcnow(),
#         'created_at': datetime.datetime.utcnow()
#     }
#     new_row = ApplicationMap(**values_dict)
#     with Session(engine) as session:
#             session.add(new_row)
#             session.commit()
#             session.refresh(new_row)


# @main.command()
# def select_all(table_name: str):
#     '''Select all rows from a table, to see the table names use the command get_tables_names'''
#     with Session(engine) as session:
#         if table_name == "application_map":
#             rows = session.exec(select(ApplicationMap)).all()
#         elif table_name == "application_map_data_sources":
#             rows = session.exec(select(ApplicationMapDataSource)).all()
#         elif table_name == "application_map_data_sources_key":
#             rows = session.exec(select(ApplicationMapDataSourceKey)).all()
#         elif table_name == "application_map_product":
#             rows = session.exec(select(ApplicationMapProduct)).all()
#         else:
#             typer.echo("Table name not found")
#             return
#     printer_rows = PrintRows(rows)
#     printer_rows.print_table(table_title=table_name)

@main.command()
def reset_db(
    force: bool = typer.Option(
        False, "--force", "-f", help="Run with no confirmation"
    )
):
    """Resets the database tables"""
    force = force or typer.confirm("Are you sure?")
    if force:
        SQLModel.metadata.drop_all(engine)


class PrintRows:
    def __init__(self, rows: list):
        self.rows = rows

    def print_table(self, table_title: str = None):
        if not self.rows:
            print("No records found")
            return
        table = Table(title=table_title)
        fields = list(self.rows[0].__dict__.keys())[1:]
        for header in fields:
            table.add_column(header, style="magenta")
        for row in self.rows:
            converted_values = [
                getattr(row, field).strftime("%Y-%m-%d %H:%M:%S.%f")
                if field in ("date", "created_at", "updated_at")
                else str(getattr(row, field))
                for field in fields
            ]
            table.add_row(*converted_values)
        Console().print(table)

    