# Este ejemplo representa un sistema de gestión de productos electrónicos en un almacén
class Producto:
    # Constructor (Clase Padre)
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.precio_original = precio  # Guardamos el precio original antes de aplicar descuento

    def aplicar_descuento(self, porcentaje):
        # Calcula el monto de descuento según el porcentaje dado
        descuento_monto = self.precio * (porcentaje / 100)
        # Resta el descuento al precio actual
        self.precio -= descuento_monto
        # Retorna el monto descontado para llevar el control
        return descuento_monto

    def mostrar_info(self):
        # Devuelve una cadena con el nombre y precio formateado del producto
        return f"{self.nombre} - ${self.precio:.2f}"


class Electronico(Producto):
    def __init__(self, nombre, precio, garantia_meses):
        # Llamamos al constructor de la clase padre para nombre y precio
        super().__init__(nombre, precio)
        # Agregamos atributo específico para electrónicos: garantía en meses
        self.garantia_meses = garantia_meses

    def mostrar_info(self):
        # Extiende la info del producto añadiendo garantía
        return f"{super().mostrar_info()} | Garantía: {self.garantia_meses} meses"


# Definimos el IVA fijo del 15%
IVA = 0.15

# Pedimos al usuario la cantidad de productos electrónicos que desea ingresar
while True:
    try:
        cantidad = int(input("¿Cuántos productos electrónicos desea ingresar? "))
        if cantidad > 0:
            break
        else:
            print("Ingrese un número mayor a 0.")
    except ValueError:
        print("❌ Error: Ingrese un número entero válido.")

# Variables acumuladoras para sumar totales de todos los productos
total_subtotal = 0      # Suma de todos los precios antes de descuento
total_descuento = 0     # Suma total de descuentos aplicados
total_iva = 0           # Suma total de IVA calculado
total_final = 0         # Suma total final a pagar (precio con descuento + IVA)

# Variable para guardar toda la información detallada de los productos
detalle_productos = ""

# Bucle para ingresar datos de cada producto uno a uno
for i in range(cantidad):
    print(f"\nProducto electrónico #{i + 1}")

    # Captura del nombre (sin validación especial)
    nombre = input("Ingrese el nombre: ")

    # Validación del precio
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio >= 0:
                break
            else:
                print("El precio no puede ser negativo.")
        except ValueError:
            print("❌ Error: Ingrese un número válido para el precio.")

    # Validación de garantía
    while True:
        try:
            garantia = int(input("Ingrese la garantía en meses: "))
            if garantia >= 0:
                break
            else:
                print("La garantía no puede ser negativa.")
        except ValueError:
            print("❌ Error: Ingrese un número entero para la garantía.")

    # Creamos la instancia del producto electrónico
    producto = Electronico(nombre, precio, garantia)

    descuento_aplicado = 0  # Inicializamos variable para guardar el descuento aplicado

    # Preguntar si desea aplicar descuento
    aplicar_desc = input("¿Desea aplicar un descuento a este producto? (s/n): ").lower()
    if aplicar_desc == 's':
        while True:
            try:
                porcentaje_desc = float(input("Ingrese el porcentaje de descuento: "))
                if 0 <= porcentaje_desc <= 100:
                    descuento_aplicado = producto.aplicar_descuento(porcentaje_desc)
                    break
                else:
                    print("Ingrese un porcentaje entre 0 y 100.")
            except ValueError:
                print("❌ Error: Ingrese un número válido para el porcentaje de descuento.")

    # Calcular valores para el producto actual
    subtotal = producto.precio_original            # Precio antes de descuento
    descuento = descuento_aplicado                 # Monto descontado
    iva = producto.precio * IVA                    # IVA calculado sobre el precio descontado
    total = producto.precio + iva                  # Precio final + IVA

    # Acumulamos los valores para el resumen total
    total_subtotal += subtotal
    total_descuento += descuento
    total_iva += iva
    total_final += total

    # Guardamos detalle del producto actual
    detalle_productos += f"\nProducto #{i + 1}:\n"
    detalle_productos += f"  Nombre: {producto.nombre}\n"
    detalle_productos += f"  Garantía: {producto.garantia_meses} meses\n"
    detalle_productos += f"  Subtotal: ${subtotal:.2f}\n"
    detalle_productos += f"  Descuento aplicado: -${descuento:.2f}\n"
    detalle_productos += f"  IVA (15%): +${iva:.2f}\n"
    detalle_productos += f"  Total a pagar: ${total:.2f}\n"

# Mostrar información final de todos los productos
print("\n--- Detalles de todos los productos ---")
print(detalle_productos)

# Mostrar resumen final
print("--- Resumen total ---")
print(f"Subtotal total: ${total_subtotal:.2f}")
print(f"Descuento total: -${total_descuento:.2f}")
print(f"IVA total (15%): +${total_iva:.2f}")
print(f"Total final a pagar: ${total_final:.2f}")