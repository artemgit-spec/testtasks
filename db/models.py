from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import Enum as SQEnum
from enum import Enum
from sqlalchemy.orm import relationship
from db.base_engine import Base


class StatusTask(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    created_at = Column(DateTime(timezone=True))
    tasks = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")
    title = Column(String)
    description = Column(String, nullable=True)
    status = Column(SQEnum(StatusTask), name="status_task_enum")
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True), nullable=True)
