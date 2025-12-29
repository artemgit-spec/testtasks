from fastapi import HTTPException, status
from datetime import datetime
from sqlalchemy import select

from db.models import Task
from celery_task.celery_tasks import process_task


async def create_new_task(db, model):
    new_task = Task(
        user_id=model.user_id,
        title=model.title,
        description=model.description,
        created_at=model.created_at,
    )
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    process_task.delay(new_task.id)
    return {"detail": "Задача создана"}


async def info_task_id(db, id):
    task = await db.scalar(select(Task).where(Task.id == id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="задача не найдена"
        )
    return task


# добавить при смене статуса время закрытия задачи
async def new_status_task(db, id, status):
    task = await info_task_id(db, id)
    if task.status == status:
        return {"detail": "у задачи уже 'этот статус'"}
    if status.value == "done":
        task.updated_at = datetime.now()
        task.status = status
        await db.commit()
        await db.refresh(task)
        return {"detail": "Задача закрыта"}
    task.status = status
    await db.commit()
    await db.refresh(task)
    return {"detail": f"{status.value}"}


async def all_task_user(db, id):
    tasks = await db.scalars(select(Task).where(Task.user_id == id)).all()
    if tasks is None:
        return {"detail": "У пользователя нет задач"}
    return tasks
