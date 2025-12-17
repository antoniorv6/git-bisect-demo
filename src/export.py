"""
Exportación de datos a diferentes formatos
"""

import csv
import json
from typing import List
from src.models import Task


class Exporter:
    """Exporta tareas a diferentes formatos"""
    
    @staticmethod
    def to_csv(tasks: List[Task], filename: str):
        """Exporta tareas a CSV"""
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Title', 'Description', 'Priority', 'Status', 'Tags'])
            for task in tasks:
                writer.writerow([
                    task.id,
                    task.title,
                    task.description,
                    task.priority.name,
                    task.status.value,
                    ','.join(task.tags)
                ])
    
    @staticmethod
    def to_json(tasks: List[Task], filename: str):
        """Exporta tareas a JSON"""
        data = [task.to_dict() for task in tasks]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @staticmethod
    def to_markdown(tasks: List[Task], filename: str):
        """Exporta tareas a Markdown"""
        with open(filename, 'w') as f:
            f.write("# Task List\n\n")
            for task in tasks:
                status_icon = "✅" if task.status.value == "done" else "⬜"
                f.write(f"- {status_icon} **{task.title}** ({task.priority.name})\n")
                if task.description:
                    f.write(f"  - {task.description}\n")
                if task.tags:
                    f.write(f"  - Tags: {', '.join(task.tags)}\n")
                f.write("\n")
