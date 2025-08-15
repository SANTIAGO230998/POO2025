# Menú en consola para el sistema de inventario

from inventario import Inventario
from producto import Producto

def menu():
    """Muestra el menú principal."""
    print("\n****** Sistema de Inventario ******")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID único: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad (Ingrese número entero): "))
            precio = float(input("Precio (Use punto para decimales): "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (enter si no cambia): ")
            precio = input("Nuevo precio (enter si no cambia): ")
            inventario.actualizar_producto(
                id_producto,
                nueva_cantidad=int(cantidad) if cantidad else None,
                nuevo_precio=float(precio) if precio else None
            )

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

if __name__ == "__main__":
    main()
