# main.py
import tkinter as tk
from models import TaskList
from views import TaskView
from controllers import TaskController

def main():
    """Función principal que inicializa y ejecuta la aplicación"""
    # Crear la ventana principal
    root = tk.Tk()
    
    # Crear instancias de MVC
    model = TaskList()
    view = TaskView(root)
    controller = TaskController(model, view)
    
    # Cargar datos iniciales
    controller.load_initial_data()
    
    # Iniciar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()