
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from assets.database import Base
from datetime import datetime as dt

class Data(Base):

    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=False)
    subscribers = Column(Integer, unique=False)
    reviews = Column(Integer, unique=False)
    timestamp = Column(DateTime, default=dt.now())

    def __init__(self, date=None, subscribers=None, reviews=None, timestamp=None):
        self.date = date
        self.subscribers = subscribers
        self.reviews = reviews
        self.timestamp = timestamp
