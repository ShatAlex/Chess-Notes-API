import time

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session

from matches.models import Match, GameMode
from matches.schemas import MatchCreate, GameModeCreate

router_match = APIRouter(
    prefix='/matches',
    tags=['Matches']
)

router_gamemode = APIRouter(
    prefix='/gamemodes',
    tags=['GameModes']
)


@router_match.get('/')
async def get_specific_matches(result: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Match).where(Match.result == result)
    result = await session.execute(query)
    data = []
    for item in result.all():
        data.append(item[0].__dict__)
    return {
        'status': 'success',
        'data': data,
        'details': None
    }


@router_match.post('/')
async def add_matches(new_match: MatchCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Match).values(**new_match.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router_gamemode.get('/')
async def get_gamemodes(session: AsyncSession = Depends(get_async_session)):
    query = select(GameMode)
    result = await session.execute(query)
    data = []
    for item in result.all():
        data.append(item[0].__dict__)
    return {
        'status': 'success',
        'data': data,
        'details': None
    }


@router_gamemode.post('/')
async def add_gamemode(new_mode: GameModeCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(GameMode).values(**new_mode.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router_gamemode.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Долгоооо"
