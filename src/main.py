from fastapi import FastAPI, Depends

from auth.base_config import auth_backend, fastapi_users, current_user
from auth.models import User
from auth.schemas import UserRead, UserCreate

from matches.router import router_match, router_gamemode
from tasks.router import router as router_task

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

app = FastAPI(
    title='ChessNotes API'
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_match)
app.include_router(router_gamemode)

app.include_router(router_task)


@app.get('/matches/{match_id}')
def hi(match_id: int = 1, user: User = Depends(current_user)):
    return f'hi, {match_id}, from {user.username}'


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
