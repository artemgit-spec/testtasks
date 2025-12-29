from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class TaskModel(BaseModel):
    user_id: int = 1
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="без содержания")
    created_at: datetime

    class Config:
        from_attributes = True


class PrintTaskModel(BaseModel):
    id: int
    user_id: int = 1
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="без содержания")
    created_at: datetime
    status: Optional[str] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
