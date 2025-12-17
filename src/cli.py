"""
Interfaz de línea de comandos
"""

import sys
from src.task_manager import TaskManager
from src.storage import Storage
from src.models import Priority, Status
from src.statistics import Statistics


class CLI:
    """Interfaz de línea de comandos para TaskMaster"""
    
    def __init__(self):
        storage = Storage()
        self.manager = TaskManager(storage)
    
    def run(self, args: list):
        """Ejecuta el comando especificado"""
        if len(args) < 1:
            self.show_help()
            return
        
        command = args[0]
        
        if command == "add":
            self.add_task(args[1:])
        elif command == "list":
            self.list_tasks()
        elif command == "stats":
            self.show_stats()
        elif command == "help":
            self.show_help()
        else:
            print(f"Comando desconocido: {command}")
            self.show_help()
    
    def add_task(self, args: list):
        """Añade una nueva tarea"""
        if len(args) < 1:
            print("Error: Se requiere un título")
            return
        
        title = args[0]
        description = args[1] if len(args) > 1 else ""
        task = self.manager.create_task(title, description)
        print(f"✓ Tarea creada con ID: {task.id}")
    
    def list_tasks(self):
        """Lista todas las tareas"""
        tasks = self.manager.list_tasks()
        if not tasks:
            print("No hay tareas")
            return
        
        print(f"\n{'ID':<5} {'Título':<30} {'Prioridad':<12} {'Estado':<15}")
        print("-" * 70)
        for task in tasks:
            print(f"{task.id:<5} {task.title:<30} {task.priority.name:<12} {task.status.value:<15}")
    
    def show_stats(self):
        """Muestra estadísticas"""
        tasks = self.manager.list_tasks()
        if not tasks:
            print("No hay tareas")
            return
        
        completion = Statistics.completion_rate(tasks)
        productivity = Statistics.productivity_score(tasks)
        
        print("\n=== Estadísticas ===")
        print(f"Total de tareas: {len(tasks)}")
        print(f"Tasa de completitud: {completion:.1f}%")
        print(f"Puntuación de productividad: {productivity:.1f}")
    
    def show_help(self):
        """Muestra la ayuda"""
        print("""
TaskMaster - Sistema de Gestión de Tareas

Comandos:
  add <título> [descripción]  - Crea una nueva tarea
  list                        - Lista todas las tareas
  stats                       - Muestra estadísticas
  help                        - Muestra esta ayuda
        """)


if __name__ == "__main__":
    cli = CLI()
    cli.run(sys.argv[1:])
