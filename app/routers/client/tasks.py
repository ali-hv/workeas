from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional

from app.routers.api.tasks import api_get_tasks, api_delete_task, api_add_task
from app.settings import templates, router, timezone
from app.utils import convert_datetime
from app.database import get_db


@router.get("/tasks/", response_class=HTMLResponse)
def get_tasks(request: Request, priority: Optional[int] = None, date: Optional[datetime] = None, db: Session = Depends(get_db)):
    tasks = api_get_tasks(priority=priority, date=date, db=db)
    
    if timezone == 'Asia/Tehran':
        tasks = convert_datetime.to_jalali(tasks)
        datetime_dir = "rtl"
    else:
        tasks = convert_datetime.to_gregorian(tasks)
        datetime_dir = "ltr"
    
    return templates.TemplateResponse("tasks/tasks_list.html", {"request": request, "tasks": tasks, "datetime_dir": datetime_dir})


@router.get("/tasks/add", response_class=HTMLResponse)
def add_task(request: Request):
    return templates.TemplateResponse("tasks/add_task.html", {"request": request})


@router.post("/tasks/add", response_class=RedirectResponse)
async def add_task(request: Request, db: Session = Depends(get_db)):
    # add task
    form = await request.form()
    task_data = {
        "title": form['title'],
        "description": form['description'],
        "priority": form['priority'],
        "date": datetime.strptime(form['date'], "%Y-%m-%dT%H:%M")
    }

    api_add_task(task_data, db=db)

    return RedirectResponse(request.url_for('get_tasks'), status_code=303)


@router.get("/tasks/delete/{task_id}", response_class=RedirectResponse)
def delete_task(request: Request, task_id: int, db: Session = Depends(get_db)):
    # delete task
    api_delete_task(task_id=task_id, db=db)

    return RedirectResponse(request.url_for('get_tasks'))