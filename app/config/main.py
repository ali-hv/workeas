from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

from .database import engine

from tasks.routers import client as tasks_client
from tasks.routers import api as tasks_api
from tasks import models

# Create fastapi app
app = FastAPI(
    title="Workeas",
    description="Don't forget any task anymore !",
    version="0.0.1",)

# Include routers
app.include_router(tasks_api.router)
app.include_router(tasks_client.router)

# Include static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Redirect root path to docs path
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


# Create a connection to the database using the engine
models.Base.metadata.create_all(bind=engine)


