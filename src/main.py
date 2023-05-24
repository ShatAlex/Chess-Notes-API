from fastapi import FastAPI, Depends

from auth.base_config import auth_backend, fastapi_users, current_user
from auth.models import User
from auth.schemas import UserRead, UserCreate

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


@app.get('/matches/{match_id}')
def hi(match_id: int = 1, user: User = Depends(current_user)):
    return f'hi, {match_id}, from {user.username}'
