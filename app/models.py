from sqlalchemy import Column, Integer, String
from .database import Base

class SportItem(Base):
    __tablename__ = "sports"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    players_count = Column(Integer)
    description = Column(String)

