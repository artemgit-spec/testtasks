from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase


engine = create_async_engine(
    "postgresql+asyncpg://taskuser:12345@localhost:5432/taskdb", echo=True
)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db():
    async with SessionLocal() as s:
        yield s


class Base(DeclarativeBase):
    pass
