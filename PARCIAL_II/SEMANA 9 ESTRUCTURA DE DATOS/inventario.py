# Clase que gestiona la lista de productos

from producto import Producto
from prettytable import PrettyTable

class Inventario:
    def __init__(self):
        """Crea un inventario vacío."""
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto si el ID no existe."""
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("❌ El ID ya existe.")
        else:
            self.productos.append(producto)
            print("✅ Producto agregado.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por ID."""
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("✅ Producto eliminado.")
                return
        print("❌ No se encontró el producto.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza cantidad y/o precio por ID."""
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("✅ Producto actualizado.")
                print(p)
                return
        print("❌ No se encontró el producto.")

    def buscar_por_nombre(self, nombre):
        """Busca productos que contengan el texto en el nombre."""
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        """Muestra todos los productos en tabla usando PrettyTable."""
        if not self.productos:
            print("📦 Inventario vacío.")
            return
# Presenta los datos en una tabla para que se vea mejor visualmente
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Cantidad", "Precio"]

        for p in self.productos:
            tabla.add_row([p.get_id(), p.get_nombre(), p.get_cantidad(), f"${p.get_precio():.2f}"])

        print(tabla)