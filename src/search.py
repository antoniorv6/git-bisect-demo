"""
Funcionalidad de búsqueda y filtrado de tareas
"""

from typing import List, Callable
from src.models import Task, Priority, Status


class SearchEngine:
    """Motor de búsqueda para tareas"""
    
    @staticmethod
    def search_by_title(tasks: List[Task], query: str) -> List[Task]:
        """Busca tareas por título"""
        query_lower = query.lower()
        return [t for t in tasks if query_lower in t.title.lower()]
    
    @staticmethod
    def search_by_tag(tasks: List[Task], tag: str) -> List[Task]:
        """Busca tareas por etiqueta"""
        return [t for t in tasks if tag in t.tags]
    
    @staticmethod
    def filter_by_priority(tasks: List[Task], priority: Priority) -> List[Task]:
        """Filtra tareas por prioridad"""
        return [t for t in tasks if t.priority == priority]
    
    @staticmethod
    def filter_by_status(tasks: List[Task], status: Status) -> List[Task]:
        """Filtra tareas por estado"""
        return [t for t in tasks if t.status == status]
    
    @staticmethod
    def sort_by_priority(tasks: List[Task], descending: bool = True) -> List[Task]:
        """Ordena tareas por prioridad"""
        return sorted(tasks, key=lambda t: t.priority.value, reverse=descending)
    
    @staticmethod
    def sort_by_date(tasks: List[Task], descending: bool = True) -> List[Task]:
        """Ordena tareas por fecha de creación"""
        return sorted(tasks, key=lambda t: t.created_at, reverse=descending)
