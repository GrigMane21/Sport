from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Sport(Base):
    __tablename__ = "sports"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    is_olympic = Column(Boolean, default=False)
