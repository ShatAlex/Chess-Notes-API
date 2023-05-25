from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class ResultType(Enum):
    loss = 'loss'
    win = 'win'
    draw = 'draw'


class GameModeCreate(BaseModel):
    id: int
    mode: str
    rules: str
    time_limit: datetime

    class Config:
        orm_mode = True


class MatchCreate(BaseModel):
    id: int
    result: ResultType
    opponents_rating: int
    played_on: datetime
    moves: str
    gamemode: int

    class Config:
        orm_mode = True
        use_enum_values = True
