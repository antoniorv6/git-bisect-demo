# TaskMaster - Sistema de Gestión de Tareas

Un sistema completo de gestión de tareas para demostrar git bisect.

## Estructura del Proyecto

```
taskmaster/
├── src/
│   ├── models.py          # Modelos de datos
│   ├── storage.py         # Persistencia
│   └── task_manager.py    # Lógica de negocio
├── tests/
│   ├── test_models.py
│   └── test_task_manager.py
└── README.md
```

## Ejecutar Tests

```bash
python -m pytest tests/
# o
python -m unittest discover tests
```
