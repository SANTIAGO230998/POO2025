from producto import Producto
from gestor_archivo import GestionInventario

class Inventario:
    """
    Clase que maneja la lógica de inventario usando un diccionario.
    Clave: ID del producto, Valor: objeto Producto.
    """

    def __init__(self):
        self.gestor = GestionInventario()
        self.productos = self.gestor.cargar_productos(Producto)

    # ------ Agregar producto ------
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            return False  # No se puede agregar ID repetido
        self.productos[producto.get_id()] = producto
        self.gestor.guardar_productos(self.productos)
        return True

    # ------ Eliminar producto ------
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.gestor.guardar_productos(self.productos)
            return True
        return False

    # ------ Actualizar producto ------
    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto not in self.productos:
            return False
        p = self.productos[id_producto]
        if nombre: p.set_nombre(nombre)
        if cantidad is not None: p.set_cantidad(cantidad)
        if precio is not None: p.set_precio(precio)
        self.gestor.guardar_productos(self.productos)
        return True

    # ------ Listar todos los productos ------
    def listar_productos(self):
        return list(self.productos.values())
