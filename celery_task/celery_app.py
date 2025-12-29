from celery import Celery

"""
celery -A celery_task.celery_app.app_celery worker --pool=solo для запуска 
"""
app_celery = Celery(
    "my_task",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["celery_task.celery_tasks"],
)
