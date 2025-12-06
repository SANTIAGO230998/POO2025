import json
from producto import Producto
import os

class Inventario:
    def __init__(self, archivo="productos.json"):
        self.archivo = archivo
        self.productos = {}  # ID como string -> Producto
        self.cargar_productos()

    # ---------- Cargar desde JSON ----------
    def cargar_productos(self):
        if not os.path.exists(self.archivo):
            self.productos = {}
            return
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.productos = {str(d["id"]): Producto(str(d["id"]), d["nombre"], d["cantidad"], d["precio"]) for d in datos}
        except (json.JSONDecodeError, KeyError):
            self.productos = {}

    # ---------- Guardar en JSON ----------
    def guardar_productos(self):
        datos = [p.to_dict() for p in self.productos.values()]
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    # ---------- Listar productos ----------
    def listar_productos(self):
        return list(self.productos.values())

    # ---------- Agregar producto ----------
    def agregar_producto(self, producto: Producto):
        pid = str(producto.get_id())
        if pid in self.productos:
            return False
        self.productos[pid] = producto
        self.guardar_productos()
        return True

    # ---------- Actualizar producto ----------
    def actualizar_producto(self, pid, nombre, cantidad, precio):
        pid = str(pid)
        if pid in self.productos:
            p = self.productos[pid]
            p.set_nombre(nombre)
            p.set_cantidad(cantidad)
            p.set_precio(precio)
            self.guardar_productos()
            return True
        return False

    # ---------- Eliminar producto ----------
    def eliminar_producto(self, pid):
        pid = str(pid)
        if pid in self.productos:
            del self.productos[pid]
            self.guardar_productos()
            return True
        return False
