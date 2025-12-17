"""
Generación de estadísticas y reportes
"""

from typing import Dict, List
from collections import Counter
from src.models import Task, Priority, Status


class Statistics:
    """Calcula estadísticas sobre las tareas"""
    
    @staticmethod
    def count_by_status(tasks: List[Task]) -> dict[Status, int]:
        """Cuenta tareas por estado"""
        counter = Counter(t.status for t in tasks)
        return {status: counter.get(status, 0) for status in Status}
    
    @staticmethod
    def count_by_priority(tasks: List[Task]) -> dict[Priority, int]:
        """Cuenta tareas por prioridad"""
        counter = Counter(t.priority for t in tasks)
        return {priority: counter.get(priority, 0) for priority in Priority}
    
    @staticmethod
    def completion_rate(tasks: List[Task]) -> float:
        """Calcula el porcentaje de tareas completadas"""
        if not tasks:
            return 0.0
        # BUG: Se cambió DONE por TODO, calculando incorrectamente
        completed = sum(1 for t in tasks if t.status == Status.TODO)
        return (completed / len(tasks)) * 100
    
    @staticmethod
    def average_tasks_by_tag(tasks: List[Task]) -> dict[str, int]:
        """Cuenta tareas por etiqueta"""
        tag_counter = Counter()
        for task in tasks:
            for tag in task.tags:
                tag_counter[tag] += 1
        return dict(tag_counter)
    
    @staticmethod
    def productivity_score(tasks: List[Task]) -> float:
        """Calcula un score de productividad (0-100)"""
        if not tasks:
            return 0.0
        
        completed = sum(1 for t in tasks if t.status == Status.TODO)
        in_progress = sum(1 for t in tasks if t.status == Status.IN_PROGRESS)
        high_priority = sum(1 for t in tasks if t.priority in [Priority.HIGH, Priority.CRITICAL])
        
        score = (completed * 10 + in_progress * 5 + high_priority * 2) / len(tasks)
        return min(score, 100.0)
