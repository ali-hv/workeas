from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from .models import Priority

class TaskBase(BaseModel):
    title: str
    description: str
    date: Optional[datetime] = datetime.now()
    priority: Priority


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
