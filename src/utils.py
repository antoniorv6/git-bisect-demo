"""
Funciones de utilidad general
"""

from datetime import datetime, timedelta
from typing import List
from src.models import Task


class DateUtils:
    """Utilidades para manejo de fechas"""
    
    @staticmethod
    def format_date(date: datetime) -> str:
        """Formatea una fecha de manera legible"""
        return date.strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def is_overdue(task: Task, days: int = 7) -> bool:
        """Verifica si una tarea está vencida"""
        delta = datetime.now() - task.created_at
        return delta.days > days
    
    @staticmethod
    def get_age_in_days(task: Task) -> int:
        """Obtiene la antigüedad de una tarea en días"""
        delta = datetime.now() - task.created_at
        return delta.days


class TextUtils:
    """Utilidades para manejo de texto"""
    
    @staticmethod
    def truncate(text: str, max_length: int = 50) -> str:
        """Trunca un texto a una longitud máxima"""
        if len(text) <= max_length:
            return text
        return text[:max_length - 3] + "..."
    
    @staticmethod
    def sanitize_title(title: str) -> str:
        """Limpia un título de caracteres especiales"""
        return ''.join(c for c in title if c.isalnum() or c.isspace())
    
    @staticmethod
    def generate_slug(text: str) -> str:
        """Genera un slug a partir de un texto"""
        text = text.lower()
        text = ''.join(c if c.isalnum() or c.isspace() else '-' for c in text)
        return '-'.join(text.split())


class ValidationUtils:
    """Utilidades para validación"""
    
    @staticmethod
    def validate_title(title: str) -> bool:
        """Valida que el título sea correcto"""
        return len(title.strip()) > 0 and len(title) <= 200
    
    @staticmethod
    def validate_tags(tags: List[str]) -> bool:
        """Valida que las etiquetas sean correctas"""
        if not tags:
            return True
        return all(len(tag.strip()) > 0 and len(tag) <= 30 for tag in tags)
