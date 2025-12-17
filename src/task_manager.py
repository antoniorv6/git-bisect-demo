"""
Lógica de negocio para gestión de tareas
"""

from typing import List, Optional
from src.models import Task, Priority, Status
from src.storage import Storage


class TaskManager:
    """Gestiona las operaciones sobre tareas"""
    
    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks: List[Task] = storage.load_tasks()
        self._next_id = max([t.id for t in self.tasks], default=0) + 1
    
    def create_task(self, title: str, description: str = "", 
                   priority: Priority = Priority.MEDIUM) -> Task:
        """Crea una nueva tarea"""
        task = Task(title, description, priority)
        task.id = self._next_id
        self._next_id += 1
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Obtiene una tarea por su ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def list_tasks(self, status: Optional[Status] = None) -> List[Task]:
        """Lista todas las tareas, opcionalmente filtradas por estado"""
        if status is None:
            return self.tasks.copy()
        return [t for t in self.tasks if t.status == status]
    
    def update_status(self, task_id: int, status: Status) -> bool:
        """Actualiza el estado de una tarea"""
        task = self.get_task(task_id)
        if task:
            task.status = status
            self.storage.save_tasks(self.tasks)
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """Elimina una tarea"""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.storage.save_tasks(self.tasks)
            return True
        return False
