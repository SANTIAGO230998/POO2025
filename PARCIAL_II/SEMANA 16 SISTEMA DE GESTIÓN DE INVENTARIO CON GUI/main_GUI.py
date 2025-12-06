import tkinter as tk
from tkinter import ttk, messagebox
from inventario import Inventario
from producto import Producto
from PIL import Image, ImageTk

class SistemaInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE INVENTARIO")
        self.root.geometry("900x600")
        self.inventario = Inventario()
        self.ventana_productos_abierta = False
        self.selected_id = None  # ID seleccionado para eliminar

        # Atajo Escape para cerrar la app
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # Menú superior
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        opciones_menu = tk.Menu(self.menu, tearoff=0)
        opciones_menu.add_command(label="Productos", command=self.abrir_ventana_productos)
        opciones_menu.add_separator()
        opciones_menu.add_command(label="Salir", command=self.root.destroy)
        self.menu.add_cascade(label="Opciones", menu=opciones_menu)

        # --- Fondo dinámico ---
        self.original_image = Image.open("Fondo.jpeg")
        self.fondo_img = ImageTk.PhotoImage(self.original_image)
        self.fondo_label = tk.Label(self.root, image=self.fondo_img)
        self.fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.fondo_label.lower()  # fondo siempre debajo de los widgets

        # --- Frames portada ---
        self.frame_top = tk.Frame(self.root, bg=None)
        self.frame_top.place(relx=0.5, rely=0.20, anchor="n")
        self.frame_center = tk.Frame(self.root, bg=None)
        self.frame_center.place(relx=0.5, rely=0.52, anchor="center")
        self.frame_bottom = tk.Frame(self.root, bg=None)
        self.frame_bottom.place(relx=0.5, rely=0.85, anchor="s")

        # ----- Etiquetas portada -----
        self.lbl_uni = tk.Label(self.frame_top, text="UNIVERSIDAD ESTATAL AMAZÓNICA",
                                font=("Arial", 28, "bold"))
        self.lbl_uni.pack(pady=(0,20))

        self.lbl_est1 = tk.Label(self.frame_center, text="Estudiantes:", font=("Arial", 18))
        self.lbl_est1.pack(pady=(10,2))
        self.lbl_est2 = tk.Label(self.frame_center, text="Cristhian Chacha", font=("Arial", 18))
        self.lbl_est2.pack()
        self.lbl_est3 = tk.Label(self.frame_center, text="Cinthia Carrion", font=("Arial", 18))
        self.lbl_est3.pack()
        self.lbl_est4 = tk.Label(self.frame_center, text="Santiago Lara", font=("Arial", 18))
        self.lbl_est4.pack()

        self.lbl_carrera = tk.Label(self.frame_bottom, text="INGENIERÍA EN TECNOLOGÍAS DE LA INFORMACIÓN",
                                    font=("Arial", 20))
        self.lbl_carrera.pack()
        self.lbl_materia = tk.Label(self.frame_bottom, text="PROGRAMACIÓN ORIENTADA A OBJETOS",
                                    font=("Arial", 18))
        self.lbl_materia.pack(pady=(5,0))

        # --- Redimensionamiento ---
        self.redim_delay = None
        self.root.bind("<Configure>", self.redimensionar_portada_lento, add="+")

        # --- Forzar redimensionamiento inicial ---
        self.root.update_idletasks()
        class EventFake:
            def __init__(self, width, height):
                self.width = width
                self.height = height
        self.redimensionar_portada(EventFake(self.root.winfo_width(), self.root.winfo_height()))

    def redimensionar_portada_lento(self, event):
        if self.redim_delay:
            self.root.after_cancel(self.redim_delay)
        self.redim_delay = self.root.after(100, lambda: self.redimensionar_portada(event))

    def redimensionar_portada(self, event):
        if event.width < 100 or event.height < 100:
            return
        resized = self.original_image.resize((event.width, event.height), Image.LANCZOS)
        self.fondo_img = ImageTk.PhotoImage(resized)
        self.fondo_label.config(image=self.fondo_img)
        self.fondo_label.lower()
        ancho = event.width
        self.lbl_uni.config(font=("Arial", max(24, ancho // 25), "bold"))
        self.lbl_est1.config(font=("Arial", max(16, ancho // 45)))
        self.lbl_est2.config(font=("Arial", max(16, ancho // 45)))
        self.lbl_est3.config(font=("Arial", max(16, ancho // 45)))
        self.lbl_est4.config(font=("Arial", max(16, ancho // 45)))
        self.lbl_carrera.config(font=("Arial", max(18, ancho // 40)))
        self.lbl_materia.config(font=("Arial", max(16, ancho // 45)))

    # ---------- Ventana de productos ----------
    def abrir_ventana_productos(self):
        if self.ventana_productos_abierta:
            return
        self.ventana_productos_abierta = True
        self.ventana_productos = tk.Toplevel(self.root)
        self.ventana_productos.title("GESTIÓN DE PRODUCTOS")
        self.ventana_productos.geometry("850x500")
        self.ventana_productos.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_productos)
        self.ventana_productos.bind("<Escape>", lambda e: self.ventana_productos.destroy())

        # Variables
        self.var_id = tk.StringVar()
        self.var_nombre = tk.StringVar()
        self.var_cantidad = tk.StringVar()
        self.var_precio = tk.StringVar()
        self.var_buscar = tk.StringVar()
        self.selected_id = None

        # Frame superior
        frame_top = tk.Frame(self.ventana_productos)
        frame_top.pack(fill="x", padx=10, pady=10)

        # Entradas
        tk.Label(frame_top, text="ID:").grid(row=0, column=0, sticky="w")
        self.entry_id = tk.Entry(frame_top, textvariable=self.var_id, width=25)
        self.entry_id.grid(row=0, column=1)
        tk.Label(frame_top, text="Nombre:").grid(row=1, column=0, sticky="w")
        self.entry_nombre = tk.Entry(frame_top, textvariable=self.var_nombre, width=25)
        self.entry_nombre.grid(row=1, column=1)
        tk.Label(frame_top, text="Cantidad:").grid(row=2, column=0, sticky="w")
        self.entry_cantidad = tk.Entry(frame_top, textvariable=self.var_cantidad, width=25)
        self.entry_cantidad.grid(row=2, column=1)
        tk.Label(frame_top, text="Precio:").grid(row=3, column=0, sticky="w")
        self.entry_precio = tk.Entry(frame_top, textvariable=self.var_precio, width=25)
        self.entry_precio.grid(row=3, column=1)

        # Botones
        tk.Button(frame_top, text="Agregar", bg="#4CAF50", fg="white", width=12,
                  command=self.agregar_producto).grid(row=0, column=2, padx=20)
        tk.Button(frame_top, text="Modificar", bg="#2196F3", fg="white", width=12,
                  command=self.modificar_producto).grid(row=1, column=2, padx=20)
        tk.Button(frame_top, text="Eliminar", bg="#f44336", fg="white", width=12,
                  command=self.eliminar_producto).grid(row=2, column=2, padx=20)
        tk.Button(frame_top, text="Cerrar", bg="#9E9E9E", fg="white", width=12,
                  command=self.cerrar_ventana_productos).grid(row=3, column=2, padx=20)

        # Buscar
        tk.Label(frame_top, text="Buscar:").grid(row=0, column=3, sticky="w")
        self.entry_buscar = tk.Entry(frame_top, textvariable=self.var_buscar, width=20)
        self.entry_buscar.grid(row=0, column=4)
        tk.Button(frame_top, text="Buscar", bg="#FF9800", fg="white", width=12,
                  command=self.buscar_producto).grid(row=1, column=4)

        # Treeview
        self.tree_frame = tk.Frame(self.ventana_productos)
        self.tree_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree_scroll = tk.Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side="right", fill="y")

        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings",
                                 yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.config(command=self.tree.yview)
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="both", expand=True)

        # Doble clic para cargar
        self.tree.bind("<Double-1>", self.cargar_producto_seleccionado)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_para_eliminar)

        self.cargar_tabla()

    # ---------- Seleccionar ----------
    def seleccionar_para_eliminar(self, event):
        selected = self.tree.selection()
        if selected:
            self.selected_id = str(self.tree.item(selected[0])["values"][0])
        else:
            self.selected_id = None

    # ---------- Eliminar ----------
    def eliminar_producto(self):
        pid = self.selected_id
        if not pid:
            messagebox.showerror("Error", "Seleccione un producto para eliminar", parent=self.ventana_productos)
            return
        if messagebox.askyesno("Confirmar", f"¿Eliminar producto {pid}?", parent=self.ventana_productos):
            if self.inventario.eliminar_producto(pid):
                messagebox.showinfo("✅", "Producto eliminado", parent=self.ventana_productos)
                self.selected_id = None
                self.cargar_tabla()
            else:
                messagebox.showerror("❌", "No se pudo eliminar el producto", parent=self.ventana_productos)

    # ---------- Cargar producto seleccionado ----------
    def cargar_producto_seleccionado(self, event):
        item = self.tree.selection()
        if not item:
            return
        pid, nombre, cantidad, precio = self.tree.item(item)["values"]
        self.selected_id = str(pid)
        self.var_id.set(str(pid))
        self.entry_id.config(state="disabled")
        self.var_nombre.set(nombre)
        self.var_cantidad.set(cantidad)
        if isinstance(precio, str) and precio.startswith("$"):
            precio = precio.replace("$","")
        self.var_precio.set(precio)

    # ---------- Cerrar ventana ----------
    def cerrar_ventana_productos(self):
        self.ventana_productos_abierta = False
        self.ventana_productos.destroy()

    # ---------- Cargar tabla ----------
    def cargar_tabla(self, productos=None):
        for i in self.tree.get_children():
            self.tree.delete(i)
        if productos is None:
            productos = self.inventario.listar_productos()
        for p in productos:
            self.tree.insert("", "end", values=(str(p.get_id()), p.get_nombre(), p.get_cantidad(), f"${p.get_precio():.2f}"))

    # ---------- Agregar ----------
    def agregar_producto(self):
        pid = self.var_id.get().strip()
        nombre = self.var_nombre.get().strip()
        cantidad = self.var_cantidad.get().strip()
        precio = self.var_precio.get().strip()
        if not pid or not nombre or not cantidad or not precio:
            messagebox.showerror("Error", "Todos los campos son obligatorios", parent=self.ventana_productos)
            return
        try:
            cantidad = int(cantidad)
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser entero y Precio decimal", parent=self.ventana_productos)
            return
        p = Producto(pid, nombre, cantidad, precio)
        if self.inventario.agregar_producto(p):
            messagebox.showinfo("✅", "Producto agregado", parent=self.ventana_productos)
            self.limpiar_campos()
            self.cargar_tabla()
        else:
            messagebox.showerror("❌", "ID ya existe", parent=self.ventana_productos)

    # ---------- Modificar ----------
    def modificar_producto(self):
        pid = self.var_id.get().strip()
        nombre = self.var_nombre.get().strip()
        cantidad = self.var_cantidad.get().strip()
        precio = self.var_precio.get().strip()
        if not pid:
            messagebox.showerror("Error", "Seleccione un producto para modificar", parent=self.ventana_productos)
            return
        try:
            cantidad = int(cantidad)
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser entero y Precio decimal", parent=self.ventana_productos)
            return
        self.inventario.actualizar_producto(pid, nombre, cantidad, precio)
        messagebox.showinfo("✅", "Producto modificado", parent=self.ventana_productos)
        self.limpiar_campos()
        self.entry_id.config(state="normal")
        self.cargar_tabla()

    # ---------- Buscar ----------
    def buscar_producto(self):
        nombre = self.var_buscar.get().strip().lower()
        if not nombre:
            self.cargar_tabla()
            return
        resultados = [p for p in self.inventario.listar_productos() if nombre in p.get_nombre().lower()]
        self.cargar_tabla(resultados)

    # ---------- Limpiar campos ----------
    def limpiar_campos(self):
        self.var_id.set("")
        self.var_nombre.set("")
        self.var_cantidad.set("")
        self.var_precio.set("")
        self.entry_id.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaInventario(root)
    root.mainloop()

