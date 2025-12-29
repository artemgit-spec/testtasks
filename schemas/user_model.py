from pydantic import BaseModel, EmailStr
from datetime import datetime


class ModelUser(BaseModel):
    email: EmailStr
    created_at: datetime

    class Config:
        orm_model = True
