from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional

from app.database import get_db
from app import models, schemas
from app.settings import router


@router.get("/api/tasks/")
def api_get_tasks(priority: Optional[str] = None, date: Optional[datetime] = None, db: Session = Depends(get_db)):
    # Store argument names in a tuple
    arg_names = ('priority', 'date')
    # Get the arguments passed in the URL
    args = (priority, date)
    # Create a list of filters based on the arguments passed in the URL
    filters = [getattr(models.Task, arg_names[i]) == args[i] for i in range(len(args)) if args[i]]

    # Query the database for tasks that match the filters
    tasks = db.query(models.Task).filter(*filters).all()

    # Return the tasks that match the filters
    return tasks


@router.get("/api/tasks/{task_id}")
def api_get_task(task_id: int, db: Session = Depends(get_db)):
    # Get the task from the database using the task_id
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    # Return the task
    return task


@router.post("/api/tasks/add/", response_model=schemas.Task)
def api_add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    # Create a new task object using the task schema
    if 'model_dump' in dir(task):
        db_task = models.Task(**task.model_dump())
    else:
        db_task = models.Task(**task)
    # Add the task to the database
    db.add(db_task)
    # Commit the changes to the database
    db.commit()
    # Refresh the task object
    db.refresh(db_task)
    # Return the task
    return db_task


@router.get('/api/tasks/delete/{task_id}')
def api_delete_task(task_id: int, db: Session = Depends(get_db)):
    db.query(models.Task).filter(models.Task.id == task_id).delete()
    db.commit()

    return {"status": 200,
            "message": "Task deleted successfully"}
