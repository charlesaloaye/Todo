from fastapi import FastAPI

from db.database import Base, engine
from routers import auth, todos

Base.metadata.create_all(engine)

app = FastAPI()


app.include_router(todos.router)
app.include_router(auth.router)
