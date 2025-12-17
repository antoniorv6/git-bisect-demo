"""
Modelos de datos para la aplicación TaskMaster
"""

from datetime import datetime
from enum import Enum
from typing import Optional, List


class Priority(Enum):
    """Prioridad de las tareas"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Status(Enum):
    """Estado de las tareas"""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    CANCELLED = "cancelled"


class Task:
    """Representa una tarea en el sistema"""
    
    def __init__(self, title: str, description: str = "", 
                 priority: Priority = Priority.MEDIUM):
        self.id: Optional[int] = None
        self.title = title
        self.description = description
        self.priority = priority
        self.status = Status.TODO
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.tags: List[str] = []
    
    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', status={self.status.value})"
    
    def to_dict(self):
        """Convierte la tarea a diccionario"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority.value,
            'status': self.status.value,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'tags': self.tags
        }


class Project:
    """Representa un proyecto que contiene tareas"""
    
    def __init__(self, name: str, description: str = ""):
        self.id: Optional[int] = None
        self.name = name
        self.description = description
        self.tasks: List[Task] = []
        self.created_at = datetime.now()
    
    def add_task(self, task: Task):
        """Añade una tarea al proyecto"""
        self.tasks.append(task)
    
    def __repr__(self):
        return f"Project(id={self.id}, name='{self.name}', tasks={len(self.tasks)})"
