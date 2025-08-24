# archivo.py
import os  # Para verificar si el archivo existe y manejar rutas de archivos
from producto import Producto  # Importamos la clase Producto para crear objetos


class GestionInventario:
    def __init__(self, nombre_archivo="inventario.txt"):
        """
        Inicializa la clase con el nombre del archivo donde se guardará el inventario.
        Por defecto se usará 'inventario.txt'.
        """
        self.nombre_archivo = nombre_archivo

    def guardar_productos(self, productos):
        """
        Guarda la lista de productos en un archivo de texto en formato tipo tabla.
        Sobrescribe el archivo completo con los productos actuales.
        """
        try:
            # Abrimos el archivo en modo escritura ('w') con encoding UTF-8
            with open(self.nombre_archivo, "w", encoding="utf-8") as f:
                # Escribimos el encabezado de la tabla
                f.write(f"{'ID':<5} | {'Nombre':<15} | {'Cantidad':<8} | {'Precio':<10}\n")
                # Línea separadora
                f.write("-" * 50 + "\n")

                # Escribimos cada producto en una línea usando su método __str__()
                for p in productos:
                    f.write(str(p) + "\n")

            # Mensaje de éxito al guardar
            print(f"✅ Inventario guardado en {self.nombre_archivo}")

        except PermissionError:
            # Error si no se puede escribir en el archivo (archivo abierto o sin permisos)
            print("❌ Error: No se puede escribir en el archivo (archivo abierto o sin permisos).")

        except Exception as e:
            # Captura cualquier otro error inesperado al guardar
            print(f"❌ Error al guardar inventario: {e}")

    def cargar_productos(self, Producto):
        """
        Carga los productos desde el archivo de texto y devuelve una lista de objetos Producto.
        Si el archivo no existe, se crea vacío con encabezado y se devuelve una lista vacía.
        """
        productos = []  # Lista donde se almacenarán los objetos Producto

        # Verificamos si el archivo existe
        if not os.path.exists(self.nombre_archivo):
            # Si no existe, lo creamos con encabezado vacío
            with open(self.nombre_archivo, "w", encoding="utf-8") as f:
                f.write(f"{'ID':<5} | {'Nombre':<15} | {'Cantidad':<8} | {'Precio':<10}\n")
                f.write("-" * 50 + "\n")
            # Retornamos lista vacía porque no hay productos todavía
            return productos

        # Si el archivo existe, intentamos leerlo
        try:
            with open(self.nombre_archivo, "r", encoding="utf-8") as f:
                # Leemos todas las líneas, saltando las dos primeras (encabezado)
                lines = f.readlines()[2:]

                # Procesamos cada línea para crear objetos Producto
                for line in lines:
                    parts = line.strip().split("|")  # Separamos cada campo por '|'
                    if len(parts) != 4:
                        continue  # Saltamos líneas mal formateadas

                    # Limpiamos espacios y convertimos a tipos correctos
                    id_producto = parts[0].strip()
                    nombre = parts[1].strip()
                    cantidad = int(parts[2].strip())
                    precio = float(parts[3].strip().replace("$", ""))

                    # Creamos el objeto Producto y lo agregamos a la lista
                    productos.append(Producto(id_producto, nombre, cantidad, precio))

        except PermissionError:
            # Error si no hay permisos para leer el archivo
            print("❌ No tienes permisos para leer el archivo.")

        except Exception as e:
            # Captura cualquier otro error inesperado
            print(f"❌ Error al leer inventario: {e}")

        # Retornamos la lista de productos cargados
        return productos

