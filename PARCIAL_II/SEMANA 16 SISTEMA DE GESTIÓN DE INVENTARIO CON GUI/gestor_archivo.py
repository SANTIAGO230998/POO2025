import json
import os

class GestionInventario:
    """
    Clase encargada de guardar y cargar productos usando JSON.
    """

    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo

    def guardar_productos(self, productos):
        """
        Guarda un diccionario de productos en JSON.
        Cada clave es el ID y el valor es un diccionario con los datos del producto.
        """
        data = {pid: prod.to_dict() for pid, prod in productos.items()}
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def cargar_productos(self, Producto):
        """
        Carga productos desde el archivo JSON.
        Retorna un diccionario: ID -> objeto Producto.
        """
        if not os.path.exists(self.archivo):
            return {}
        with open(self.archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
        productos = {}
        for pid, info in data.items():
            productos[pid] = Producto(pid, info["nombre"], info["cantidad"], info["precio"])
        return productos
