from sqlalchemy import Column, String, Integer, DateTime, Enum
from enum import Enum as PyEnum

from config.database import Base


class Priority(PyEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3

    def __str__(self):
        return str(self.name)
    

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), index=True)
    description = Column(String(1000), index=True)
    date = Column(DateTime)
    priority = Column(Enum(Priority))