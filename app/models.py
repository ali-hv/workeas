from sqlalchemy import Column, String, Integer, DateTime, Enum, func
from enum import Enum as PyEnum
from datetime import datetime

from .database import Base


class Priority(PyEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    date = Column(DateTime, default=datetime.now())
    priority = Column(Enum(Priority))