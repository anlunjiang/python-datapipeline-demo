from sqlalchemy import Column, DateTime, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LBGMarketDataDaily(Base):
    __tablename__ = "LBG_OHLC_1DAY"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    DATE = Column(DateTime)
    OPEN = Column(Float(precision=5))
    HIGH = Column(Float(precision=5))
    LOW = Column(Float(precision=5))
    CLOSE = Column(Float(precision=5))
    VOLUME = Column(Integer)
    TEST_COL = Column(Integer)
