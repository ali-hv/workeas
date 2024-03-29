from pydantic import BaseModel, validator
from datetime import datetime

from .models import Priority

class TaskBase(BaseModel):
    title: str
    description: str
    date: datetime
    priority: Priority

    @validator('date', pre=True)
    def remove_seconds_microseconds(cls, v):
        if isinstance(v, datetime):
            return v.replace(second=0, microsecond=0)
        return v


class TaskCreate(TaskBase):
    pass


class TaskEdit(TaskBase):
    pass


class Task(TaskBase):
    id: int
