from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

from .database import engine
from . import models

from .routers.client import tasks as client_tasks
from .routers.api import tasks as api_tasks

# Create fastapi app
app = FastAPI()
app.include_router(api_tasks.router)
app.include_router(client_tasks.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Create a connection to the database using the engine
models.Base.metadata.create_all(bind=engine)


