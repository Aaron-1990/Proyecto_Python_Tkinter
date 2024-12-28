# models.py
from datetime import datetime
import json

class Task:
    """
    Clase que representa una tarea individual.
    Maneja los datos y el estado de una única tarea.
    """
    def __init__(self, text, completed=False):
        self.text = text
        self.completed = completed
        self.date_created = datetime.now()
    
    def to_dict(self):
        """Convierte la tarea a un diccionario para almacenamiento JSON"""
        return {
            'text': self.text,
            'completed': self.completed,
            'date_created': self.date_created.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea una tarea desde un diccionario (usado al cargar desde JSON)"""
        task = cls(data['text'])
        task.completed = data['completed']
        task.date_created = datetime.strptime(data['date_created'], "%Y-%m-%d %H:%M:%S")
        return task

class TaskList:
    """
    Clase que gestiona la colección de tareas.
    Maneja las operaciones sobre el conjunto de tareas y su persistencia.
    """
    def __init__(self):
        self.tasks = []
    
    def add_task(self, text):
        """Añade una nueva tarea a la lista"""
        task = Task(text)
        self.tasks.append(task)
        return task
    
    def remove_task(self, index):
        """Elimina una tarea de la lista por su índice"""
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
    
    def toggle_task_completion(self, index):
        """Cambia el estado de completado de una tarea"""
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed
            return self.tasks[index]
    
    def get_statistics(self):
        """Calcula estadísticas sobre las tareas"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        return {'total': total, 'completed': completed}
    
    def save_to_file(self, filename='tasks.json'):
        """Guarda las tareas en un archivo JSON"""
        try:
            data = [task.to_dict() for task in self.tasks]
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error al guardar las tareas: {e}")
    
    def load_from_file(self, filename='tasks.json'):
        """Carga las tareas desde un archivo JSON"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except FileNotFoundError:
            self.tasks = []
        except Exception as e:
            print(f"Error al cargar las tareas: {e}")
            self.tasks = []