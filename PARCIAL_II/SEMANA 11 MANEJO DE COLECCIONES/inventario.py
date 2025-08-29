from producto import Producto
from prettytable import PrettyTable
from archivo import GestionInventario

class Inventario:
    def __init__(self):
        """
        Inicializa un inventario como diccionario.
        Carga automáticamente los productos existentes desde el archivo TXT.
        """
        self.gestor = GestionInventario()
        self.productos = self.gestor.cargar_productos(Producto)  # Diccionario: ID -> Producto

    def agregar_producto(self, producto):
        """
        Agrega un producto si su ID no existe aún.
        """
        if producto.get_id() in self.productos:
            print("❌ El ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto agregado.")
            self.gestor.guardar_productos(self.productos)

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID, si existe.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("✅ Producto eliminado.")
            self.gestor.guardar_productos(self.productos)
        else:
            print("❌ No se encontró el producto.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza cantidad y/o precio de un producto si el ID existe.
        """
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print("✅ Producto actualizado.")
            print(producto)
            self.gestor.guardar_productos(self.productos)
        else:
            print("❌ No se encontró el producto.")

    def buscar_por_nombre(self, nombre):
        """
        Devuelve una lista de productos que contienen el texto en su nombre (sin importar mayúsculas).
        """
        return [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        """
        Muestra todos los productos en una tabla bonita con PrettyTable.
        """
        if not self.productos:
            print("📦 Inventario vacío.")
            return

        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Cantidad", "Precio"]

        for p in self.productos.values():
            tabla.add_row([p.get_id(), p.get_nombre(), p.get_cantidad(), f"${p.get_precio():.2f}"])

        print(tabla)
