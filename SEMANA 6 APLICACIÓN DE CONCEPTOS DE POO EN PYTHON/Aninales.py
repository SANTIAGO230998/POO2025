# A continuación, se presenta un programa que crea instancias de animales que muestran su descripción y sonido personalizado
# Se aplican los principios de la POO

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

# SubClase Perro hereda de Clase Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad) #Llamamos al constructor de la clase base
        self.__raza = raza  # atributo privado (encapsulado)

    def hablar(self):  # sobrescritura (polimorfismo)
        return "Guau guau"

    def obtener_raza(self):
        # Método público que permite acceder al atributo privado _raza
        return self.__raza

# SubClase Ave hereda de Clase Animal
class Ave(Animal):
    def __init__(self, nombre, edad, puede_volar):
        super().__init__(nombre, edad)
        self.__puede_volar = puede_volar  # encapsulado

    def hablar(self):  # polimorfismo
        return "Pío pío"

    def puede_volar_funcion(self):
        # Método público que devuelve que el ave puede volar
        return self.__puede_volar