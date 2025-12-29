import uvicorn
from fastapi import FastAPI

from routers.router_task import r_tasks
from routers.router_user import r_user

app = FastAPI(title="Test Task Progect")


app.include_router(r_user)
app.include_router(r_tasks)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

"""
для запуска всего приложения нужно запускать параллельно:
1)запустить приложение
2)запустить селери
3)запусить редис командой redis-server.exe
    можно проверить, работает ли редис командой redis-cli ping
"""
