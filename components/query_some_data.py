from sqlalchemy.orm import Query

from schemas.internal import LBGMarketDataDaily


def get_ohlc_data_filtered():
    return Query(
        [
            LBGMarketDataDaily.ID,
            LBGMarketDataDaily.DATE,
            LBGMarketDataDaily.HIGH,
        ]
    ).filter(LBGMarketDataDaily.ID == 2)
