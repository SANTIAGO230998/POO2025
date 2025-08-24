from producto import Producto  # Importamos la clase Producto
from prettytable import PrettyTable  # Para mostrar los productos en tabla bonita
from archivo import GestionInventario  # Clase que gestiona lectura/escritura en archivo TXT


class Inventario:
    def __init__(self):
        """
        Inicializa un inventario vacío.
        Carga automáticamente los productos existentes desde el archivo TXT.
        """
        self.gestor = GestionInventario()  # Instancia del gestor de archivos
        self.productos = self.gestor.cargar_productos(Producto)  # Lista de productos cargada desde archivo

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario si el ID no existe.
        Luego guarda el inventario actualizado en el archivo.
        """
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("❌ El ID ya existe.")
        else:
            self.productos.append(producto)
            print("✅ Producto agregado.")
            self.gestor.guardar_productos(self.productos)  # Guardar cambios en archivo

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID.
        Guarda los cambios en el archivo.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("✅ Producto eliminado.")
                self.gestor.guardar_productos(self.productos)
                return
        print("❌ No se encontró el producto.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto por su ID.
        Guarda los cambios en el archivo después de modificar.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("✅ Producto actualizado.")
                print(p)
                self.gestor.guardar_productos(self.productos)
                return
        print("❌ No se encontró el producto.")

    def buscar_por_nombre(self, nombre):
        """
        Devuelve una lista de productos cuyo nombre contenga el texto buscado.
        Búsqueda no sensible a mayúsculas/minúsculas.
        """
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        """
        Muestra todos los productos en una tabla usando PrettyTable.
        Si el inventario está vacío, muestra un mensaje.
        """
        if not self.productos:
            print("📦 Inventario vacío.")
            return

        # Crear tabla con encabezados
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Cantidad", "Precio"]

        # Agregar cada producto como fila en la tabla
        for p in self.productos:
            tabla.add_row([p.get_id(), p.get_nombre(), p.get_cantidad(), f"${p.get_precio():.2f}"])

        # Mostrar tabla en consola
        print(tabla)
