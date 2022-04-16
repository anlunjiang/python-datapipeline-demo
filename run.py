from components.get_api_data import pandas_append_sql, read_from_csv
from components.query_some_data import get_ohlc_data_filtered
from log_config.loggingconf import logger
from schemas.connection import Database
from schemas.internal import LBGMarketDataDaily
from util.queries import query_to_dataframe
from util.setup_environment import run_mysql_docker_container, setup_db_environment


def main():
    logger.info("Running Docker Environment")
    setup_db_environment()
    run_mysql_docker_container()
    df = read_from_csv()
    pandas_append_sql(df, table=LBGMarketDataDaily.__tablename__)
    with Database().session_scope() as session:
        q = get_ohlc_data_filtered()
        df = query_to_dataframe(q, session=session)
    print(df)


if __name__ == "__main__":
    main()
