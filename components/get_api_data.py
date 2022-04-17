import pandas as pd

from log_config.loggingconf import logger
from schemas.connection import Database
from util.general import retrieve_env_var


def read_from_csv():
    lbg_df = pd.read_csv(r"data/lbg_stock_price.csv")
    lbg_df["ADJ_CLOSE"] = lbg_df["Adj Close"]
    lbg_df.drop("Adj Close", axis=1, inplace=True)
    return lbg_df.reset_index(drop=True)


def pandas_append_sql(df: pd.DataFrame, table: str):
    db = Database()
    logger.info(f"Appending {df.shape[0]} rows to table: {table}")
    df.to_sql(
        name=table,
        con=db.engine,
        schema=retrieve_env_var("DB_SCHEMA"),
        if_exists="append",
        index=False,
    )
    logger.info("Complete")
