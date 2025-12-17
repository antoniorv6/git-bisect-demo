# TaskMaster - Sistema de Gestión de Tareas

Un sistema completo y profesional de gestión de tareas para demostrar git bisect.

## 🚀 Características

- ✅ Gestión completa de tareas (CRUD)
- 🔍 Motor de búsqueda y filtrado avanzado
- 📊 Sistema de estadísticas y reportes
- 🔔 Notificaciones inteligentes
- 📤 Exportación a múltiples formatos (CSV, JSON, Markdown)
- 💾 Persistencia en JSON
- 🎯 CLI para uso desde terminal

## 📁 Estructura del Proyecto

```
taskmaster/
├── src/
│   ├── __init__.py
│   ├── models.py          # Modelos de datos (Task, Project)
│   ├── storage.py         # Capa de persistencia
│   ├── task_manager.py    # Lógica de negocio principal
│   ├── search.py          # Motor de búsqueda
│   ├── statistics.py      # Cálculo de estadísticas
│   ├── notifications.py   # Sistema de notificaciones
│   ├── export.py          # Exportación de datos
│   ├── utils.py           # Utilidades generales
│   └── cli.py             # Interfaz de línea de comandos
├── tests/
│   ├── test_models.py
│   ├── test_task_manager.py
│   ├── test_search.py
│   ├── test_statistics.py
│   ├── test_notifications.py
│   └── test_export.py
└── README.md
```

## 🧪 Ejecutar Tests

```bash
# Todos los tests
python -m unittest discover tests

# Test específico
python -m unittest tests.test_statistics

# Con verbose
python -m unittest discover tests -v
```

## 💻 Uso de la CLI

```bash
# Crear tarea
python -m src.cli add "Comprar leche" "Ir al supermercado"

# Listar tareas
python -m src.cli list

# Ver estadísticas
python -m src.cli stats
```

## 📊 Ejemplo de Uso

```python
from src.task_manager import TaskManager
from src.storage import Storage
from src.models import Priority

# Inicializar
storage = Storage()
manager = TaskManager(storage)

# Crear tarea
task = manager.create_task(
    "Implementar feature X",
    "Añadir funcionalidad de...",
    Priority.HIGH
)

# Listar tareas
tasks = manager.list_tasks()

# Estadísticas
from src.statistics import Statistics
rate = Statistics.completion_rate(tasks)
```

## 🎯 Prioridades

- `LOW`: Baja prioridad
- `MEDIUM`: Prioridad media (por defecto)
- `HIGH`: Alta prioridad
- `CRITICAL`: Crítica

## 📈 Estados

- `TODO`: Por hacer
- `IN_PROGRESS`: En progreso
- `DONE`: Completada
- `CANCELLED`: Cancelada

## 🤝 Contribuir

Este proyecto es una demostración educativa de git bisect.

## 📝 Licencia

MIT License - Proyecto educativo
