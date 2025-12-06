class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = str(id_producto).zfill(3)  # Siempre string con ceros
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ------ Getters ------
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # ------ Setters ------
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa.")

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            raise ValueError("El precio no puede ser negativo.")

    # ------ Representación legible ------
    def __str__(self):
        return f"{self.__id:<5} | {self.__nombre:<15} | {self.__cantidad:<8} | ${self.__precio:<10.2f}"

    # ------ Convertir a diccionario para JSON ------
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }
