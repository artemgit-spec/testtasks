from fastapi import APIRouter, Depends, status
from typing import Annotated, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.models import Task

from db.base_engine import get_db
from db.models import StatusTask
from schemas.task_model import TaskModel, PrintTaskModel
from service.service_task import (
    create_new_task,
    info_task_id,
    new_status_task,
    all_task_user,
)


r_tasks = APIRouter(prefix="/tasks", tags=["Управление задачами"])


@r_tasks.post("/create", status_code=status.HTTP_201_CREATED)
async def create_task(
    db: Annotated[AsyncSession, Depends(get_db)], create_model: TaskModel
):
    user = await create_new_task(db, create_model)
    return user


@r_tasks.get("/info/{id}")
async def info_task(db: Annotated[AsyncSession, Depends(get_db)], id: int):
    tasks = await info_task_id(db, id)
    return tasks


@r_tasks.patch("/update/{id}/status")
async def update_task(
    db: Annotated[AsyncSession, Depends(get_db)], new_status: StatusTask, id: int
):
    return await new_status_task(db, id, new_status)


@r_tasks.get("/tasks/")
async def all(db: Annotated[AsyncSession, Depends(get_db)], user_id: int):
    return all_task_user(db, user_id)


@r_tasks.get("/all-tasks", response_model=List[PrintTaskModel])
async def all_tasks(db: Annotated[AsyncSession, Depends(get_db)]):
    res = await db.scalars(select(Task))
    tasks = res.all()
    return tasks
