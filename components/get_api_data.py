import yfinance as yf


def get_data():
    aapl_df = yf.download(
        "LLOY.L",
        start="2021-01-01",
        end="2022-01-01",
    )
    return aapl_df.reset_index()
