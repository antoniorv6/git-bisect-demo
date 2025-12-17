# Arquitectura de TaskMaster

## Capas del Sistema

### 1. Modelos (`models.py`)
- Define las entidades principales: Task, Project
- Enums para Priority y Status
- Métodos de serialización

### 2. Persistencia (`storage.py`)
- Gestiona el almacenamiento en JSON
- Sistema de cache para mejorar rendimiento
- Abstracción de la capa de datos

### 3. Lógica de Negocio (`task_manager.py`)
- Operaciones CRUD sobre tareas
- Gestión de IDs
- Coordinación con storage

### 4. Módulos Auxiliares
- **search.py**: Búsqueda y filtrado
- **statistics.py**: Cálculos y reportes
- **notifications.py**: Alertas y reglas
- **export.py**: Exportación de datos
- **utils.py**: Utilidades generales

### 5. Interfaz (`cli.py`)
- CLI para interacción con el usuario
- Comandos básicos de gestión

## Flujo de Datos

```
CLI → TaskManager → Storage → JSON Files
                ↓
        Search/Statistics/Notifications
```
