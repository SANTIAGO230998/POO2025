# Definición de clases para animales y código principal unificados

# Clase base que define atributos y comportamientos comunes para todos los animales
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre      # atributo protegido
        self._edad = edad          # atributo protegido

    def descripcion(self):
        # Método común que devuelve una descripción general del animal
        return f"{self._nombre}, {self._edad} años"

    def hablar(self):
        # Método genérico, se espera que sea sobrescrito en las subclases
        return "Hace un sonido desconocido"

# Subclase Perro hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad) #Llamamos al constructor de la clase base
        self.__raza = raza  # atributo privado (encapsulado)

    def hablar(self):  # sobrescritura (polimorfismo)
        return "Guau guau"

    def obtener_raza(self):
        # Método público que permite acceder al atributo privado __raza
        return self.__raza

# Subclase Ave hereda de Animal
class Ave(Animal):
    def __init__(self, nombre, edad, puede_volar):
        super().__init__(nombre, edad)
        self.__puede_volar = puede_volar  # encapsulado

    def hablar(self):  # polimorfismo
        return "Pío pío"

    def puede_volar_funcion(self):
        # Método público que devuelve si el ave puede volar
        return self.__puede_volar

# Código principal
def main():
    # Crear una instancia de Perro con nombre, edad y raza
    perro1 = Perro("Pelusin", 12, "Labrador")
    print("🐶 Información del Perro:")
    print(perro1.descripcion())  # Método heredado de Animal
    print("Sonido:", perro1.hablar())  # Método sobrescrito
    print("Raza:", perro1.obtener_raza())  # Acceso a atributo encapsulado

    print("\n-------------------------------\n")

    # Crear una instancia de Ave con nombre, edad y si puede volar
    ave1 = Ave("Malia", 2, True)
    print("🐦 Información del Ave:")
    print(ave1.descripcion())  # Método heredado de Animal
    print("Sonido:", ave1.hablar())  # Método sobrescrito
    print("¿Puede volar?", "Sí" if ave1.puede_volar_funcion() else "No")

if __name__ == "__main__":
    main()
