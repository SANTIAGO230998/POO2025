# Importar librerías necesarias
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Para seleccionar fechas

# Clase principal de la agenda
class AgendaPersonal:
    def __init__(self, root):
        # Configuración de ventana
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("800x450")  # Tamaño fijo
        self.root.resizable(False, False)  # Para que no se redimensione la ventana

        # ---------- ESTILOS ----------
        style = ttk.Style(self.root)
        style.theme_use("clam")  # Tema personalizable

        # Encabezados del Treeview
        style.configure("Treeview.Heading",
                        font=("Helvetica", 10, "bold"),
                        foreground="white",
                        background="#2C3E50")
        # Mantener color al pasar el mouse
        style.map("Treeview.Heading",
                  background=[("active", "#2C3E50")])

        # Estilo general del Treeview
        style.configure("Treeview",
                        font=("Helvetica", 10),
                        rowheight=25,
                        background="#F5F5F5",
                        fieldbackground="#F5F5F5")

        # ---------- FRAME DE ENTRADA DE DATOS ----------
        input_frame = tk.Frame(self.root, padx=10, pady=10)
        input_frame.pack(fill="x")  # Se ajusta horizontalmente, pero widgets internos fijos

        # Configurar columnas internas
        for i in range(6):
            input_frame.columnconfigure(i, weight=1)

        # ----------- FECHA -----------
        tk.Label(input_frame, text="Fecha:", font=("Arial", 10)).grid(
            row=0, column=0, sticky="e", padx=5, pady=5)
        self.date_entry = DateEntry(input_frame, date_pattern='yyyy-mm-dd', width=12)
        self.date_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        # ----------- HORA -----------
        tk.Label(input_frame, text="Hora:", font=("Arial", 10)).grid(
            row=0, column=2, sticky="e", padx=(20, 2))
        time_frame = tk.Frame(input_frame)
        time_frame.grid(row=0, column=3, sticky="w")

        # ComboBox de hora
        self.hour_cb = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(24)],
                                    width=3, state="readonly")
        self.hour_cb.grid(row=0, column=0)
        self.hour_cb.set("08")

        # Separador ":"
        tk.Label(time_frame, text=":", font=("Arial", 10)).grid(row=0, column=1, padx=2)

        # ComboBox de minutos
        self.minute_cb = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(60)],
                                      width=3, state="readonly")
        self.minute_cb.grid(row=0, column=2)
        self.minute_cb.set("00")

        # ----------- DESCRIPCIÓN -----------
        tk.Label(input_frame, text="Descripción:", font=("Arial", 10)).grid(
            row=1, column=0, sticky="e", padx=5, pady=5)
        self.desc_entry = tk.Entry(input_frame, width=70)  # Más ancho para llegar al scrollbar
        self.desc_entry.grid(row=1, column=1, columnspan=5, sticky="w", padx=5, pady=5)

        # ---------- BOTONES ----------
        button_frame = tk.Frame(self.root, pady=10)
        button_frame.pack()

        self.add_button = tk.Button(button_frame, text="Agregar Evento", bg="#4CAF50", fg="white",
                                    font=("Arial", 10), width=20, command=self.agregar_evento)
        self.add_button.grid(row=0, column=0, padx=10)

        self.delete_button = tk.Button(button_frame, text="Eliminar Evento Seleccionado", bg="#f44336", fg="white",
                                       font=("Arial", 10), width=25, command=self.eliminar_evento)
        self.delete_button.grid(row=0, column=1, padx=10)

        self.exit_button = tk.Button(button_frame, text="Salir", bg="#9E9E9E", fg="white",
                                     font=("Arial", 10), width=15, command=self.root.quit)
        self.exit_button.grid(row=0, column=2, padx=10)

        # ---------- TREEVIEW CON SCROLLBAR ----------
        list_frame = tk.Frame(self.root, padx=10)
        list_frame.pack(fill="both", expand=True)

        columns = ("Fecha", "Hora", "Descripción")

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Treeview con scrollbar
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings",
                                 yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tree.yview)

        # Encabezados
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        # Columnas con ancho fijo y NO redimensionables
        self.tree.column("Fecha", anchor="center", width=200, stretch=False)
        self.tree.column("Hora", anchor="center", width=100, stretch=False)
        self.tree.column("Descripción", anchor="center", width=480, stretch=False)  # Llegar hasta scrollbar

        # Mostrar tabla (solo verticalmente expandible)
        self.tree.pack(fill="y", expand=True, pady=10)

    # ---------- FUNCIONES ----------
    def agregar_evento(self):
        """Agregar evento al Treeview"""
        fecha = self.date_entry.get()
        hora = f"{self.hour_cb.get()}:{self.minute_cb.get()}"
        descripcion = self.desc_entry.get().strip()

        if not (fecha and self.hour_cb.get() and self.minute_cb.get() and descripcion):
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        """Eliminar evento seleccionado con confirmación"""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Sin selección", "Selecciona un evento para eliminar.")
            return

        confirmar = messagebox.askyesno("Eliminar", "¿Estás seguro de eliminar el evento seleccionado?")
        if confirmar:
            self.tree.delete(seleccion[0])

# ---------- EJECUCIÓN PRINCIPAL ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()



