from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional

from app.routers.api.tasks import get_tasks
from app.settings import templates, router
from app.database import get_db


@router.get("/tasks_list/", response_class=HTMLResponse)
def tasks_list(request: Request, priority: Optional[int] = None, date: Optional[datetime] = None, db: Session = Depends(get_db)):
    tasks = get_tasks(priority=priority, date=date, db=db)
    return templates.TemplateResponse("tasks/tasks_list.html", {"request": request, "tasks": tasks})