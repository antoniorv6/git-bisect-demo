"""
Sistema de notificaciones y alertas
"""

from typing import List, Callable
from src.models import Task, Priority, Status
from src.utils import DateUtils


class NotificationRule:
    """Representa una regla de notificación"""
    
    def __init__(self, name: str, condition: Callable[[Task], bool], 
                 message_template: str):
        self.name = name
        self.condition = condition
        self.message_template = message_template
    
    def check(self, task: Task) -> bool:
        """Verifica si se cumple la condición"""
        return self.condition(task)
    
    def generate_message(self, task: Task) -> str:
        """Genera el mensaje de notificación"""
        return self.message_template.format(
            title=task.title,
            priority=task.priority.name,
            age=DateUtils.get_age_in_days(task)
        )


class NotificationSystem:
    """Sistema de gestión de notificaciones"""
    
    def __init__(self):
        self.rules: List[NotificationRule] = []
        self._setup_default_rules()
    
    def _setup_default_rules(self):
        """Configura reglas de notificación por defecto"""
        # Tareas críticas
        self.add_rule(
            "critical_task",
            lambda t: t.priority == Priority.CRITICAL and t.status != Status.DONE,
            "⚠️ CRÍTICO: '{title}' requiere atención inmediata!"
        )
        
        # Tareas antiguas
        self.add_rule(
            "old_task",
            lambda t: DateUtils.get_age_in_days(t) > 30 and t.status == Status.TODO,
            "📅 La tarea '{title}' tiene {age} días sin completar"
        )
        
        # Tareas en progreso mucho tiempo
        self.add_rule(
            "stuck_task",
            lambda t: DateUtils.get_age_in_days(t) > 14 and t.status == Status.IN_PROGRESS,
            "🔄 La tarea '{title}' lleva {age} días en progreso"
        )
    
    def add_rule(self, name: str, condition: Callable[[Task], bool], 
                 message: str):
        """Añade una nueva regla de notificación"""
        rule = NotificationRule(name, condition, message)
        self.rules.append(rule)
    
    def check_task(self, task: Task) -> List[str]:
        """Verifica todas las reglas para una tarea"""
        notifications = []
        for rule in self.rules:
            if rule.check(task):
                notifications.append(rule.generate_message(task))
        return notifications
    
    def check_all_tasks(self, tasks: List[Task]) -> dict[int, List[str]]:
        """Verifica todas las reglas para todas las tareas"""
        results = {}
        for task in tasks:
            notifications = self.check_task(task)
            if notifications:
                results[task.id] = notifications
        return results
from typing import Dict
