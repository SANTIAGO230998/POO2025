from inventario import Inventario
from producto import Producto

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
    Función principal que ejecuta el menú y controla el flujo del sistema.
    """
    inventario = Inventario()  # Se cargan los productos desde el archivo al iniciar

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID único: ")
            nombre = input("Nombre: ")

            # Validar cantidad
            while True:
                try:
                    cantidad = int(input("Cantidad: "))
                    if cantidad < 0:
                        print("❌ La cantidad no puede ser negativa.")
                        continue
                    break
                except ValueError:
                    print("❌ Ingresa un número entero válido.")

            # Validar precio
            while True:
                try:
                    precio = float(input("Precio: "))
                    if precio < 0:
                        print("❌ El precio no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print("❌ Ingresa un número válido.")

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")

            # Validar cantidad nueva (opcional)
            while True:
                cantidad = input("Nueva cantidad (enter si no cambia): ")
                if cantidad == "":
                    nueva_cantidad = None
                    break
                try:
                    nueva_cantidad = int(cantidad)
                    if nueva_cantidad < 0:
                        print("❌ La cantidad no puede ser negativa.")
                        continue
                    break
                except ValueError:
                    print("❌ Ingresa un número entero válido.")

            # Validar precio nuevo (opcional)
            while True:
                precio = input("Nuevo precio (enter si no cambia): ")
                if precio == "":
                    nuevo_precio = None
                    break
                try:
                    nuevo_precio = float(precio)
                    if nuevo_precio < 0:
                        print("❌ El precio no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print("❌ Ingresa un número válido.")

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Texto a buscar en nombre: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("❌ No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("👋 Saliendo...")
            break

        else:
            print("❌ Opción inválida.")

# Ejecuta el programa
if __name__ == "__main__":
    main()
