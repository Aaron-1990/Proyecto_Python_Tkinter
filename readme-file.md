# Gestor de Tareas con Python y Tkinter

Esta aplicación es un gestor de tareas desarrollado con Python y Tkinter, diseñado para ayudarte a mantener un registro organizado de tus actividades diarias. La aplicación implementa el patrón de diseño Modelo-Vista-Controlador (MVC) para mantener una estructura de código limpia y mantenible.

## Características Principales

La aplicación ofrece las siguientes funcionalidades:

- Añadir nuevas tareas con una interfaz intuitiva
- Marcar tareas como completadas
- Eliminar tareas que ya no son necesarias
- Visualizar estadísticas de tareas totales y completadas
- Persistencia de datos (las tareas se guardan automáticamente)
- Interfaz gráfica responsiva y fácil de usar

## Requisitos del Sistema

Para ejecutar esta aplicación, necesitarás:

- Python 3.10 o superior
- Tkinter (biblioteca de GUI para Python)
- Sistema operativo compatible (Windows, Linux, macOS)

En sistemas Linux basados en Debian/Ubuntu, puedes instalar Tkinter con:
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

## Estructura del Proyecto

El proyecto sigue una arquitectura MVC y está organizado en los siguientes archivos:

- `models.py`: Define la lógica de negocio y el manejo de datos
- `views.py`: Implementa la interfaz gráfica de usuario
- `controllers.py`: Coordina la interacción entre el modelo y la vista
- `main.py`: Punto de entrada de la aplicación
- `tasks.json`: Archivo donde se almacenan las tareas (se crea automáticamente)

## Instalación

1. Clona este repositorio o descarga los archivos:
```bash
git clone [URL_del_repositorio]
cd gestor-tareas
```

2. Asegúrate de tener Python y Tkinter instalados:
```bash
python --version
python -c "import tkinter"
```

## Uso

Para iniciar la aplicación, ejecuta:
```bash
python main.py
```

### Funcionalidades Principales:

1. **Añadir una Tarea:**
   - Escribe la tarea en el campo de texto superior
   - Presiona el botón "Añadir Tarea" o la tecla Enter

2. **Completar una Tarea:**
   - Selecciona la tarea de la lista
   - Presiona el botón "Completar"
   - La tarea se marcará con un ✓

3. **Eliminar una Tarea:**
   - Selecciona la tarea de la lista
   - Presiona el botón "Eliminar"
   - Confirma la eliminación en el diálogo

4. **Ver Estadísticas:**
   - Las estadísticas se muestran automáticamente en la parte inferior
   - Se actualiza en tiempo real con cada cambio

## Arquitectura

La aplicación utiliza el patrón MVC para separar las responsabilidades:

- **Modelo (`models.py`):**
  - Maneja la lógica de negocio
  - Gestiona el almacenamiento de datos
  - Proporciona métodos para manipular tareas

- **Vista (`views.py`):**
  - Crea la interfaz gráfica
  - Maneja la disposición de elementos
  - Proporciona métodos para actualizar la UI

- **Controlador (`controllers.py`):**
  - Coordina acciones entre modelo y vista
  - Maneja eventos de usuario
  - Actualiza el modelo y la vista según sea necesario

## Persistencia de Datos

Las tareas se guardan automáticamente en un archivo JSON (`tasks.json`) después de cada operación. Esto asegura que tus tareas persistan entre sesiones de la aplicación.

## Desarrollo

Si deseas contribuir o modificar la aplicación:

1. La aplicación usa una arquitectura modular
2. Cada componente (modelo, vista, controlador) puede ser modificado independientemente
3. Sigue las convenciones de código de Python (PEP 8)
4. Mantén la separación de responsabilidades según el patrón MVC

## Solución de Problemas

1. **La aplicación no inicia:**
   - Verifica que Python está instalado correctamente
   - Asegúrate de tener Tkinter instalado
   - Comprueba que estás en el directorio correcto

2. **Las tareas no se guardan:**
   - Verifica los permisos de escritura en el directorio
   - Comprueba que el archivo tasks.json no está bloqueado

## Licencia

Sin Licencia.