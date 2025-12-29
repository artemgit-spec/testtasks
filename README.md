
Приложение для создания задач
Стек технологий:

- FastAPI — backend-фреймворк
- SQLAlchemy — ORM
- PostgreSQL — база данных
- Alembic — миграции
- Pydantic — валидация данных

Структура проекта:
APIExchangeThings/
├── celery_taks/        # Задачи Celery
├── db/                 # БД и SQLAlchemy модели
├── migration/          # Миграции
├── routers/            # FastAPI маршруты
├── schemas/            # Pydantic-схемы
├── service/            # Бизнес-логика
├── alembic.ini
├── main.py             # Точка входа
├── README.md
└── requirements.txt

Запуск сервера: 
uvicorn main:app --reload

Запуск Redis:
redis-server.exe

Запуск Celery:
celery -A celery_task.celery_app.app_celery worker --pool=solo
