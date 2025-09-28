import tkinter as tk
from tkinter import messagebox  # Para mostrar alertas e información al usuario


class ListaTareasApp:
    """
    Aplicación GUI de Lista de Tareas con Tkinter.

    Funcionalidades:
    - Añadir nuevas tareas mediante el campo de entrada o presionando Enter.
    - Marcar tareas como completadas (doble clic o botón).
    - Eliminar tareas seleccionadas.
    - Visualización de todas las tareas en un Listbox con scroll vertical.
    """

    def __init__(self, root):
        """
        Inicializa la ventana principal, los widgets y la lista interna de tareas.
        """
        self.root = root
        self.root.title("Lista de Tareas")  # Título de la ventana
        self.root.geometry("420x500")  # Tamaño inicial de la ventana
        self.root.resizable(False, False)  # Evita que se pueda redimensionar

        # -------------------- TÍTULO PRINCIPAL --------------------
        # Etiqueta de encabezado con fuente grande y negrita
        tk.Label(root, text="Mi Lista de Tareas", font=("Helvetica", 18, "bold")).pack(pady=10)

        # -------------------- ETIQUETA DE ENTRADA --------------------
        # Texto informativo para indicar dónde escribir la nueva tarea
        tk.Label(root, text="Nueva Tarea:", font=("Helvetica", 12)).pack(anchor="w", padx=20)

        # -------------------- CAMPO DE ENTRADA --------------------
        # Campo donde el usuario escribe la nueva tarea
        self.task_entry = tk.Entry(root, font=("Helvetica", 12))
        self.task_entry.pack(padx=20, pady=5, fill=tk.X)  # Se ajusta al ancho de la ventana
        self.task_entry.bind("<Return>", self.agregar_tarea)  # Presionar Enter añade la tarea

        # -------------------- BOTONES PROPORCIONADOS --------------------
        # Frame contenedor para los botones, alineados horizontalmente
        btn_frame = tk.Frame(root)
        btn_frame.pack(padx=20, pady=10, fill=tk.X)

        # Botón: Añadir Tarea
        self.add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=self.agregar_tarea)
        self.add_btn.grid(row=0, column=0, padx=5, sticky="ew")  # sticky="ew" para expandir horizontalmente

        # Botón: Marcar como Completada
        self.complete_btn = tk.Button(btn_frame, text="Marcar como Completada", command=self.marcar_completada)
        self.complete_btn.grid(row=0, column=1, padx=5, sticky="ew")

        # Botón: Eliminar Tarea
        self.delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.delete_btn.grid(row=0, column=2, padx=5, sticky="ew")

        # Configurar las columnas para que tengan el mismo peso y se distribuyan uniformemente
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(1, weight=1)
        btn_frame.grid_columnconfigure(2, weight=1)

        # -------------------- LISTBOX CON SCROLL --------------------
        # Frame contenedor del Listbox y la scrollbar
        listbox_frame = tk.Frame(root)
        listbox_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)  # Se expande al tamaño del frame

        # Scrollbar vertical
        self.scrollbar = tk.Scrollbar(listbox_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Ubicada a la derecha del Listbox

        # Listbox que mostrará las tareas
        self.task_listbox = tk.Listbox(
            listbox_frame,
            font=("Helvetica", 12),
            yscrollcommand=self.scrollbar.set,  # Conecta el Listbox con la scrollbar
            selectbackground="#d9d9d9",  # Color de fondo al seleccionar
            selectforeground="black",  # Color de texto al seleccionar
            activestyle='none'  # Evita estilo extra al seleccionar
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Ocupa todo el espacio restante

        # Conectar la scrollbar con el listbox
        self.scrollbar.config(command=self.task_listbox.yview)

        # Doble clic sobre una tarea para marcarla como completada
        self.task_listbox.bind("<Double-Button-1>", self.marcar_completada)

        # Lista interna que almacena las tareas como diccionarios {'text': texto, 'done': estado}
        self.tasks = []

    # -------------------- FUNCIONES PRINCIPALES --------------------

    def agregar_tarea(self, event=None):
        """
        Agrega una nueva tarea a la lista.
        Se activa con el botón "Añadir Tarea" o presionando Enter.
        """
        tarea = self.task_entry.get().strip()  # Quita espacios al inicio y final
        if tarea:  # Solo si el campo no está vacío
            self.tasks.append({"text": tarea, "done": False})  # Añade la tarea con estado pendiente
            self.actualizar_lista()  # Refresca la lista visual
            self.task_entry.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea.")

    def marcar_completada(self, event=None):
        """
        Cambia el estado de la tarea seleccionada.
        Si estaba pendiente, se marca como completada y viceversa.
        """
        seleccion = self.task_listbox.curselection()  # Índice de la tarea seleccionada
        if seleccion:
            index = seleccion[0]
            self.tasks[index]["done"] = not self.tasks[index]["done"]  # Cambia estado
            self.actualizar_lista()
        else:
            messagebox.showinfo("Seleccionar tarea", "Selecciona una tarea para marcarla como completada.")

    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada de la lista.
        """
        seleccion = self.task_listbox.curselection()
        if seleccion:
            index = seleccion[0]
            del self.tasks[index]  # Elimina de la lista interna
            self.actualizar_lista()
        else:
            messagebox.showinfo("Seleccionar tarea", "Selecciona una tarea para eliminarla.")

    def actualizar_lista(self):
        """
        Refresca el Listbox mostrando todas las tareas actuales.
        Añade un "✔️" a las tareas completadas.
        """
        self.task_listbox.delete(0, tk.END)  # Limpia el Listbox
        for tarea in self.tasks:
            texto = tarea["text"]
            if tarea["done"]:
                texto += " ✔️"  # Indicador visual de completado
            self.task_listbox.insert(tk.END, texto)  # Inserta en el Listbox


# -------------------- EJECUCIÓN DE LA APLICACIÓN --------------------
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = ListaTareasApp(root)  # Crear la instancia de la aplicación
    root.mainloop()  # Ejecutar el bucle principal de Tkinter
