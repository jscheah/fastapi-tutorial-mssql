import turbodbc
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import pandas as pd

SQLALCHEMY_DATABASE_URL = (
    "mssql+turbodbc://sa:Password_123@localhost/testdb"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={
    #     "use_async_io": True,
    #     "read_buffer_size": turbodbc.Megabytes(42),
    #     "prefer_unicode": True,
    #     "autocommit": True,
    # },
)


def execute_query(query: str):
    with engine.connect() as conn:
        df = pd.read_sql_query(query, conn)
        return df


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
