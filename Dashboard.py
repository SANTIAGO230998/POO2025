import os

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    print(f"\nIntentando abrir: {ruta_script_absoluta}")
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            print("\n--- Resultado de la ejecución ---\n")
            exec(codigo, globals())
    except FileNotFoundError:
        print(" El archivo no se encontró.")
    except Exception as e:
        print(f"⚠ Ocurrió un error al leer o ejecutar el archivo: {e}")

def mostrar_menu():
    # Subimos dos niveles hasta el directorio raíz del proyecto
    ruta_base = os.getcwd()

    opciones = {
        '1': [
            'PARCIAL I/SEMANA 3 PROGRAMACIÓN TRADICIONAL VS POO/1. Tarea Programación Tradicional.py',
            'PARCIAL I/SEMANA 3 PROGRAMACIÓN TRADICIONAL VS POO/2. Tarea POO.py',
        ],
        '2': 'PARCIAL I/SEMANA 4 CARACTERÍSTICAS DE LA POO/EjemplosMundoReal_POO.py',
        '3': 'PARCIAL I/SEMANA 5 TIPOS DE DATOS, IDENTIFICADORES/Tarea_semana_5.py',
        '4': 'PARCIAL I/SEMANA 6 APLICACIÓN DE CONCEPTOS DE POO EN PYTHON/Animales.py',
        '5': 'PARCIAL I/SEMANA 7 CONSTRUCTORES Y DESTRUCTORES/Tarea_semana_7.py',
    }

    while True:
        print("\n Menú Principal - Dashboard")
        for key, value in opciones.items():
            label = f"{len(value)} archivos" if isinstance(value, list) else value
            print(f"{key} - {label}")
        print("0 - Salir")

        eleccion = input("Elige una opción para ver su(s) script(s) o '0' para salir: ")
        if eleccion == '0':
            print("¡Hasta luego!")
            break
        elif eleccion in opciones:
            rutas = opciones[eleccion]
            if isinstance(rutas, list):
                for ruta_relativa in rutas:
                    ruta_script = os.path.join(ruta_base, ruta_relativa)
                    mostrar_codigo(ruta_script)
            else:
                ruta_script = os.path.join(ruta_base, rutas)
                mostrar_codigo(ruta_script)
        else:
            print(" Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()