import tkinter as tk
from tkinter import messagebox  # Para mostrar cuadros de mensaje (alertas, confirmaciones)

# -------------------------------
# Crear ventana principal
# -------------------------------
ventana = tk.Tk()
ventana.title("Gestión de Datos")       # Título de la ventana
ventana.geometry("450x350")             # Tamaño de la ventana
ventana.configure(bg="#f2f2f2")         # Color de fondo claro y moderno

# -------------------------------
# Función para agregar un dato
# -------------------------------
def agregar_dato():
    """
    Toma el texto del campo de entrada y lo agrega al Listbox si no está vacío.
    Luego limpia el campo de entrada.
    """
    dato = entrada.get()
    if dato:
        lista_datos.insert(tk.END, dato)   # Inserta el dato al final del Listbox
        entrada.delete(0, tk.END)          # Borra el contenido del campo de entrada
    else:
        # Si el campo está vacío, muestra una advertencia
        messagebox.showwarning("Campo vacío", "Por favor ingrese un dato.")

# -------------------------------
# Función para limpiar o eliminar datos
# -------------------------------
def limpiar_datos():
    """
    Elimina el ítem seleccionado del Listbox.
    Si no hay selección, pregunta si desea eliminar todos los datos.
    """
    seleccion = lista_datos.curselection()  # Obtener el índice del ítem seleccionado
    if seleccion:
        lista_datos.delete(seleccion[0])    # Elimina solo el ítem seleccionado
    else:
        if lista_datos.size() > 0:  # Si la lista tiene elementos
            # Confirmar con el usuario si quiere borrar todo
            confirmar = messagebox.askyesno("Confirmar", "¿Desea borrar todos los datos?")
            if confirmar:
                lista_datos.delete(0, tk.END)  # Elimina todos los ítems
        else:
            # Si no hay nada en la lista
            messagebox.showinfo("Lista vacía", "No hay datos para borrar.")

# -------------------------------
# Función para deseleccionar con clic
# -------------------------------
def seleccionar_o_deseleccionar(event):
    """
    Permite deseleccionar un ítem si el usuario hace clic en uno ya seleccionado.
    También permite seleccionar un nuevo ítem al hacer clic en otro.
    """
    index = lista_datos.nearest(event.y)  # Detecta el índice más cercano al clic del mouse
    if index >= 0:
        if index in lista_datos.curselection():
            lista_datos.selection_clear(index)  # Si ya estaba seleccionado, lo deselecciona
        else:
            lista_datos.selection_clear(0, tk.END)  # Deselecciona todo lo demás
            lista_datos.selection_set(index)        # Selecciona el nuevo ítem

# -------------------------------
# Estilo visual
# -------------------------------
fuente_general = ("Helvetica", 12)  # Fuente general para los widgets

# -------------------------------
# Crear widgets de la interfaz
# -------------------------------

# Etiqueta con instrucción
etiqueta = tk.Label(
    ventana,
    text="Ingrese un dato:",
    bg="#f2f2f2",
    font=("Helvetica", 14)
)
etiqueta.pack(pady=(20, 5))  # Espaciado arriba y abajo

# Campo de entrada de texto
entrada = tk.Entry(
    ventana,
    font=fuente_general,
    width=35,
    relief="solid",  # Borde visible
    bd=1             # Grosor del borde
)
entrada.pack(pady=(0, 10))

# Marco para contener botones horizontalmente
frame_botones = tk.Frame(ventana, bg="#f2f2f2")
frame_botones.pack(pady=5)

# Botón "Agregar"
boton_agregar = tk.Button(
    frame_botones,
    text="Agregar",
    font=fuente_general,
    bg="#4CAF50",          # Verde
    fg="white",            # Texto blanco
    activebackground="#45a049",  # Verde más oscuro al presionar
    relief="flat",         # Sin borde 3D
    padx=15,
    pady=5,
    command=agregar_dato   # Ejecuta la función al hacer clic
)
boton_agregar.pack(side=tk.LEFT, padx=10)

# Botón "Limpiar"
boton_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    font=fuente_general,
    bg="#e74c3c",           # Rojo
    fg="white",
    activebackground="#c0392b",  # Rojo más oscuro al presionar
    relief="flat",
    padx=15,
    pady=5,
    command=limpiar_datos   # Ejecuta la función al hacer clic
)
boton_limpiar.pack(side=tk.LEFT, padx=10)

# Listbox donde se mostrarán los datos ingresados
lista_datos = tk.Listbox(
    ventana,
    width=50,
    height=10,
    font=fuente_general,
    bd=1,
    relief="solid",
    selectbackground="#2c3e50",  # Fondo de ítem seleccionado (oscuro)
    selectforeground="white"     # Texto del ítem seleccionado (blanco)
)
lista_datos.pack(pady=20)

# Vincular clic izquierdo para seleccionar/deseleccionar ítems
lista_datos.bind("<Button-1>", seleccionar_o_deseleccionar)

# -------------------------------
# Ejecutar el ciclo principal de la app
# -------------------------------
ventana.mainloop()
