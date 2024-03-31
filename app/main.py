from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

from .database import engine
from .tasks import models

from .tasks.routers.client import tasks as client_tasks
from .tasks.routers.api import tasks as api_tasks

# Create fastapi app
app = FastAPI(
    title="Workeas",
    description="Don't forget any task anymore !",
    version="0.0.1",)

# Include routers
app.include_router(api_tasks.router)
app.include_router(client_tasks.router)

# Include static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Redirect root path to docs path
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


# Create a connection to the database using the engine
models.Base.metadata.create_all(bind=engine)


