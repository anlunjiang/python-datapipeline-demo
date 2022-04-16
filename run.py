from components.get_api_data import pandas_append_sql, read_from_csv
from log_config.loggingconf import logger
from schemas.internal import LBGMarketDataDaily
from util.setup_environment import run_mysql_docker_container, setup_db_environment


def main():
    logger.info("Running Docker Environment")
    setup_db_environment()
    run_mysql_docker_container()
    df = read_from_csv()
    pandas_append_sql(df, table=LBGMarketDataDaily.__tablename__)


if __name__ == "__main__":
    main()
