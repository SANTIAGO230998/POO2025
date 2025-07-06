# main.py
# Este archivo contiene el código principal del programa
# Se crean objetos de tipo Perro y Ave para demostrar los conceptos de POO

from Aninales import Perro, Ave #Importamos las clases desde Animales.py

def main():
    # Crear una instancia de Perro con nombre, edad y raza
    perro1 = Perro("Pelusin", 12, "Labrador")
    print("🐶 Información del Perro:")
    print(perro1.descripcion()) #Método heredado de la clase Animal
    print("Sonido:", perro1.hablar()) #Método sobreescrito
    print("Raza:", perro1.obtener_raza()) #Acceso al atributo encapsulado

    print("\n-------------------------------\n")

    # Crear una instancia de Ave con nombre, edad y si puede volar
    ave1 = Ave("Malia", 2, True)
    print("🐦 Información del Ave:")
    print(ave1.descripcion()) #Método heredado de la clase Animal
    print("Sonido:", ave1.hablar()) #Método sobreescrito
    print("¿Puede volar?", "Sí" if ave1.puede_volar_funcion() else "No")

# Este bloque asegura que el código solo se ejecute cuando el archivo se corre directamente
if __name__ == "__main__":
    main()
