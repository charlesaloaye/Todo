from fastapi import FastAPI

from db.database import Base, engine
from routers import admin, auth, todos

Base.metadata.create_all(engine)

app = FastAPI()


app.include_router(todos.router)
app.include_router(auth.router)
app.include_router(admin.router)
