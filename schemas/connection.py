from contextlib import contextmanager
from typing import List

import pandas as pd
import sqlalchemy as sa
from sqlalchemy.engine.interfaces import Connectable
from sqlalchemy.orm import sessionmaker

from log_config.loggingconf import logger
from utils.general import retrieve_env_var


class Database:
    def __init__(self, engine: Connectable = None):
        if engine is None:
            self.db_user = retrieve_env_var("DB_USER")
            self.db_pwd = retrieve_env_var("DB_PWD")
            self.db_host = retrieve_env_var("DB_HOST")
            self.db_port = retrieve_env_var("DB_PORT")
            self.db_name = retrieve_env_var("DB_NAME")

            self.conn_str = str(
                "mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}".format(
                    user=self.db_user,
                    pwd=self.db_pwd,
                    host=self.db_host,
                    port=self.db_port,
                    dbname=self.db_name,
                ),
            )
            self.engine = sa.create_engine(self.conn_str, pool_recycle=1)
        else:
            self.engine = engine

        self._Session = sessionmaker(bind=self.engine)
        logger.info(f"Database engine created: {self.engine}")

    @contextmanager
    def session_scope(self):
        """
        Provide a transactional scope around a series of operations
        """
        session = self._Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def execute(self, sql_cmds: List):
        """
        Executes a list of sql commands using the self managed session
        """
        assert type(sql_cmds) == list, "SQL commands must be in list format"
        with self.session_scope() as session:
            for cmd in sql_cmds:
                logger.debug(f"Executing SQL cmd: {cmd}")
                session.execute(cmd)

    def query(self, sql_cmd: str):
        """
        Executes and returns the results of a sql SELECT using the self-managed session
        Returns a pandas dataframe
        """
        with self.session_scope() as session:
            logger.debug(f"Querying: {sql_cmd}")
            query = session.execute(sql_cmd)
            rows = query.fetchall()

        return pd.DataFrame(rows, columns=query.keys())
