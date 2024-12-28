# controllers.py
class TaskController:
    """
    Clase que actúa como intermediario entre el modelo y la vista.
    Maneja las acciones del usuario y coordina las actualizaciones.
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.setup_event_handlers()
    
    def setup_event_handlers(self):
        """Configura los manejadores de eventos de la vista"""
        self.view.bind_add_task(self.handle_add_task)
        self.view.bind_complete_task(self.handle_complete_task)
        self.view.bind_delete_task(self.handle_delete_task)
    
    def handle_add_task(self, task_text):
        """Maneja la adición de una nueva tarea"""
        if task_text.strip():
            self.model.add_task(task_text)
            self.view.clear_input()
            self.refresh_view()
            self.model.save_to_file()
        else:
            self.view.show_warning("Por favor ingrese una tarea.")
    
    def handle_complete_task(self, index):
        """Maneja el marcado de una tarea como completada"""
        if index is not None:
            self.model.toggle_task_completion(index)
            self.refresh_view()
            self.model.save_to_file()
        else:
            self.view.show_info("Por favor seleccione una tarea.")
    
    def handle_delete_task(self, index):
        """Maneja la eliminación de una tarea"""
        if index is not None:
            if self.view.confirm_deletion():
                self.model.remove_task(index)
                self.refresh_view()
                self.model.save_to_file()
        else:
            self.view.show_info("Por favor seleccione una tarea.")
    
    def refresh_view(self):
        """Actualiza la vista con los datos actuales del modelo"""
        tasks = self.model.tasks
        stats = self.model.get_statistics()
        self.view.update_task_list(tasks)
        self.view.update_statistics(stats)
    
    def load_initial_data(self):
        """Carga los datos iniciales y actualiza la vista"""
        self.model.load_from_file()
        self.refresh_view()