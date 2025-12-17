import json
import os
from typing import List, Optional
from src.models import Task, Project, Priority, Status
from datetime import datetime


class Storage:
    """Maneja la persistencia de datos en archivos JSON"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.tasks_file = os.path.join(data_dir, "tasks.json")
        self.projects_file = os.path.join(data_dir, "projects.json")
        self._ensure_data_dir()
        self._cache = {}  # Cache simple para mejorar rendimiento
    
    def _ensure_data_dir(self):
        """Crea el directorio de datos si no existe"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def save_tasks(self, tasks: List[Task]):
        """Guarda las tareas en un archivo JSON"""
        data = [task.to_dict() for task in tasks]
        with open(self.tasks_file, 'w') as f:
            json.dump(data, f, indent=2)
        self._cache.clear()  # Invalidar cache
    
    def load_tasks(self) -> List[Task]:
        """Carga las tareas desde el archivo JSON con cache"""
        cache_key = 'tasks'
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        if not os.path.exists(self.tasks_file):
            return []
        
        with open(self.tasks_file, 'r') as f:
            data = json.load(f)
        
        tasks = []
        for item in data:
            task = Task(item['title'], item['description'])
            task.id = item['id']
            task.priority = Priority(item['priority'])
            task.status = Status(item['status'])
            task.tags = item['tags']
            tasks.append(task)
        
        self._cache[cache_key] = tasks
        return tasks
