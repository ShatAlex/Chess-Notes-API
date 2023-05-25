from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class GameMode(Base):
    __tablename__ = "gamemode"

    id: int = Column(Integer, primary_key=True)
    mode: str = Column(String, nullable=False)
    rules: str = Column(String, nullable=False)
    time_limit: datetime = Column(TIMESTAMP, nullable=True)
    matches = relationship('Match')


class Match(Base):
    __tablename__ = "match"

    id: int = Column(Integer, primary_key=True)
    result: str = Column(String, nullable=False)
    opponents_rating: int = Column(Integer, nullable=True)
    played_on: datetime = Column(TIMESTAMP, default=datetime.utcnow)
    moves: str = Column(String, nullable=True)
    gamemode = Column(Integer, ForeignKey('gamemode.id'))
