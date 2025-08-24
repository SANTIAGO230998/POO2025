from inventario import Inventario  # Importamos la clase Inventario
from producto import Producto  # Importamos la clase Producto

def menu():
    """
    Muestra el menú principal del sistema de inventario.
    """
    print("\n****** Sistema de Inventario ******")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    """
    Función principal que ejecuta el bucle del programa.
    """
    inventario = Inventario()  # Creamos un objeto Inventario y cargamos los productos desde archivo

    while True:
        menu()  # Mostrar opciones al usuario
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Añadir un producto
            id_producto = input("ID único: ")
            nombre = input("Nombre: ")

            # Validar cantidad (debe ser entero y no negativo)
            while True:
                try:
                    cantidad = int(input("Cantidad: "))
                    if cantidad < 0:
                        print("❌ La cantidad no puede ser negativa.")
                        continue
                    break
                except ValueError:
                    print("❌ Ingresa un número entero válido.")

            # Validar precio (debe ser float y no negativo)
            while True:
                try:
                    precio = float(input("Precio: "))
                    if precio < 0:
                        print("❌ El precio no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print("❌ Ingresa un número válido.")

            # Crear objeto Producto y agregarlo al inventario
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            # Eliminar un producto por su ID
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Actualizar producto existente
            id_producto = input("ID del producto a actualizar: ")

            # Nueva cantidad con validación
            while True:
                cantidad = input("Nueva cantidad (enter si no cambia): ")
                if cantidad == "":
                    nueva_cantidad = None  # No cambia
                    break
                try:
                    nueva_cantidad = int(cantidad)
                    if nueva_cantidad < 0:
                        print("❌ La cantidad no puede ser negativa.")
                        continue
                    break
                except ValueError:
                    print("❌ Ingresa un número entero válido.")

            # Nuevo precio con validación
            while True:
                precio = input("Nuevo precio (enter si no cambia): ")
                if precio == "":
                    nuevo_precio = None  # No cambia
                    break
                try:
                    nuevo_precio = float(precio)
                    if nuevo_precio < 0:
                        print("❌ El precio no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print("❌ Ingresa un número válido.")

            # Actualizar el producto en el inventario
            inventario.actualizar_producto(
                id_producto,
                nueva_cantidad=nueva_cantidad,
                nuevo_precio=nuevo_precio
            )

        elif opcion == "4":
            # Buscar productos por nombre
            nombre = input("Texto a buscar en nombre: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("❌ No se encontraron productos.")

        elif opcion == "5":
            # Mostrar todos los productos en tabla
            inventario.mostrar_todos()

        elif opcion == "6":
            # Salir del programa
            print("👋 Saliendo...")
            break

        else:
            # Opción inválida
            print("❌ Opción inválida.")

# Ejecuta la función principal si este archivo se corre directamente
if __name__ == "__main__":
    main()
