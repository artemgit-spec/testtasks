from sqlalchemy import select
from db.models import User


async def create_new_user(db, model):
    user = User(email=model.email, created_at=model.created_at)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return {"email": user.email, "created_at": user.created_at}


async def info_id(db, id):
    user = await db.scalar(select(User).where(User.id == id))
    return user
