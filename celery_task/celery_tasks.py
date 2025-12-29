from celery_task.celery_app import app_celery
import time
from db.models import StatusTask, Task
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select

# Создай синхронный engine и session для Celery
SYNC_DATABASE_URL = "postgresql://taskuser:12345@localhost:5432/taskdb"  # URL
sync_engine = create_engine(SYNC_DATABASE_URL)

from sqlalchemy.orm import sessionmaker

SyncSessionLocal = sessionmaker(bind=sync_engine)


@app_celery.task
def process_task(id):
    time.sleep(5)
    db = SyncSessionLocal()  # Синхронная сессия
    try:
        my_task = db.scalar(select(Task).where(Task.id == id))
        my_task.status = StatusTask.DONE
        db.commit()
        db.refresh(my_task)
        return {"status": my_task.status.value}
    finally:
        db.close()


"""from celery_task.celery_app import app_celery
import time
from db.models import StatusTask, Task
from db.base_engine import SessionLocal
from sqlalchemy import select


@app_celery.task
def process_task(id,):
    time.sleep(5)
    db = SessionLocal()
    my_task = db.scalar(select(Task).where(Task.id == id))
    my_task.status = StatusTask.DONE
    db.commit()
    db.refresh(my_task)
    db.close()
    return {"status": my_task.status.value}
"""
