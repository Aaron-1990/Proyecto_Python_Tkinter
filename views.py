# views.py
import tkinter as tk
from tkinter import ttk, messagebox

class TaskView:
    """
    Clase que maneja la interfaz gráfica de usuario.
    Crea y gestiona todos los elementos visuales de la aplicación.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("600x400")
        self.setup_ui()
        
    def setup_ui(self):
        """Configura todos los elementos de la interfaz"""
        # Configuración del tema y estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Variables
        self.task_var = tk.StringVar()
        
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Configuración de grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        
        self.create_input_frame()
        self.create_task_list()
        self.create_stats_frame()
    
    def create_input_frame(self):
        """Crea el frame para la entrada de tareas"""
        input_frame = ttk.Frame(self.main_frame)
        input_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)
        
        self.task_entry = ttk.Entry(
            input_frame,
            textvariable=self.task_var,
            width=40
        )
        self.task_entry.grid(row=0, column=0, padx=5)
        
        self.add_button = ttk.Button(
            input_frame,
            text="Añadir Tarea"
        )
        self.add_button.grid(row=0, column=1, padx=5)
    
    def create_task_list(self):
        """Crea la lista de tareas con scrollbar"""
        list_frame = ttk.Frame(self.main_frame)
        list_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=5)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.task_listbox = tk.Listbox(
            list_frame,
            height=10,
            selectmode=tk.SINGLE,
            yscrollcommand=scrollbar.set
        )
        self.task_listbox.grid(row=0, column=0, sticky="nsew")
        scrollbar.config(command=self.task_listbox.yview)
        
        action_frame = ttk.Frame(list_frame)
        action_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)
        
        self.complete_button = ttk.Button(
            action_frame,
            text="Completar"
        )
        self.complete_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_button = ttk.Button(
            action_frame,
            text="Eliminar"
        )
        self.delete_button.pack(side=tk.LEFT, padx=5)
    
    def create_stats_frame(self):
        """Crea el frame para estadísticas"""
        self.stats_frame = ttk.LabelFrame(
            self.main_frame,
            text="Estadísticas",
            padding="5"
        )
        self.stats_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)
        
        self.stats_label = ttk.Label(self.stats_frame)
        self.stats_label.pack()
    
    # Métodos de binding
    def bind_add_task(self, callback):
        """Vincula el callback para añadir tarea"""
        self.add_button.config(command=lambda: callback(self.task_var.get()))
        self.task_entry.bind('<Return>', lambda e: callback(self.task_var.get()))
    
    def bind_complete_task(self, callback):
        """Vincula el callback para completar tarea"""
        self.complete_button.config(
            command=lambda: callback(self.get_selected_index())
        )
    
    def bind_delete_task(self, callback):
        """Vincula el callback para eliminar tarea"""
        self.delete_button.config(
            command=lambda: callback(self.get_selected_index())
        )
    
    # Métodos de utilidad
    def get_selected_index(self):
        """Obtiene el índice de la tarea seleccionada"""
        selection = self.task_listbox.curselection()
        return selection[0] if selection else None
    
    def clear_input(self):
        """Limpia el campo de entrada"""
        self.task_var.set("")
    
    def update_task_list(self, tasks):
        """Actualiza la lista de tareas"""
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            status = "✓" if task.completed else " "
            self.task_listbox.insert(tk.END, f"[{status}] {task.text}")
    
    def update_statistics(self, stats):
        """Actualiza las estadísticas"""
        self.stats_label.config(
            text=f"Tareas: {stats['total']} | Completadas: {stats['completed']}"
        )
    
    # Métodos de diálogo
    def show_warning(self, message):
        """Muestra un mensaje de advertencia"""
        messagebox.showwarning("Advertencia", message)
    
    def show_info(self, message):
        """Muestra un mensaje informativo"""
        messagebox.showinfo("Info", message)
    
    def confirm_deletion(self):
        """Solicita confirmación para eliminar"""
        return messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta tarea?")