import json
import os

class GestionInventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo

    def guardar_productos(self, productos):
        # Guardar todos los productos como diccionario con ID como string
        data = {str(pid): prod.to_dict() for pid, prod in productos.items()}
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def cargar_productos(self, Producto):
        if not os.path.exists(self.archivo):
            return {}
        with open(self.archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
        productos = {}
        for pid, info in data.items():
            # ID forzado a string
            productos[str(pid)] = Producto(str(pid), info["nombre"], info["cantidad"], info["precio"])
        return productos
