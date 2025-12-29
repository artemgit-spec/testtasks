from fastapi import APIRouter, Depends, status
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession as Session

from db.base_engine import get_db
from schemas.user_model import ModelUser
from service.service_user import create_new_user, info_id


r_user = APIRouter(prefix="/users", tags=["Управление пользователями"])


@r_user.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: ModelUser):
    user = await create_new_user(db, create_user)
    return user


@r_user.get("/info/{id}")
async def info_user(db: Annotated[Session, Depends(get_db)], id: int):
    return await info_id(db, id)


"""
Пользователи
1.	POST /users/
Создать нового пользователя.
В запросе передаётся email.
В ответе вернуть созданного пользователя.
2.	GET /users/{user_id}/
Получить информацию о пользователе.
________________________________________

"""
