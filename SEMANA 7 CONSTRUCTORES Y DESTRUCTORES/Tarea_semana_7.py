"""Sistema de Biblioteca usando constructores y destructores.
Este programa define tres clases principales: Libro, Usuario y Prestamo.
Cada clase incluye un constructor (__init__) y un destructor (__del__),
para demostrar cómo se crean y destruyen los objetos en Python."""

class Libro:
    def __init__(self, titulo, autor):
        """Constructor de la clase Libro.Se ejecuta automáticamente al crear un nuevo libro. Sirve para inicializar los atributos título y autor."""
        self.titulo = titulo
        self.autor = autor
        print(f"[SE HA CARGADO EL LIBRO] '{self.titulo}' por {self.autor}")

    def mostrar_info(self):
        """Muestra la información del libro."""
        print(f"Libro: {self.titulo} - Autor: {self.autor}")

    def __del__(self):
        """Destructor de la clase Libro. Se ejecuta automáticamente cuando el objeto deja de usarse. Ideal para liberar recursos si los hubiera (aquí solo imprimimos)."""
        print(f"[LIBRO ELIMINADO] '{self.titulo}' se ha retirado de la memoria.")


class Usuario:
    def __init__(self, nombre):
        """Constructor de la clase Usuario. Se llama al crear un nuevo usuario. Inicializa el atributo 'nombre'."""
        self.nombre = nombre
        print(f"[USUARIO HA SIDO REGISTRADO] {self.nombre}")

    def mostrar_info(self):
        """Muestra la información del usuario."""
        print(f"Usuario: {self.nombre}")

    def __del__(self):
        """Destructor de la clase Usuario. Se ejecuta cuando el objeto es eliminado o el programa termina. Aquí solo muestra un mensaje, pero podría cerrar archivos o conexiones."""
        print(f"[USUARIO ELIMINADO] {self.nombre} ha sido eliminado del sistema.")


class Prestamo:
    def __init__(self, usuario, libro):
        """Constructor de la clase Prestamo. Se llama cuando un usuario toma prestado un libro. Recibe objetos de tipo Usuario y Libro como parámetros."""
        self.usuario = usuario #composición
        self.libro = libro #composición
        print(f"[PRÉSTAMO INICIADO] {usuario.nombre} ha tomado prestado el libro '{libro.titulo}'.")

    def mostrar_info(self):
        """Muestra qué libro tiene prestado qué usuario."""
        print(f"{self.usuario.nombre} tiene prestado el libro '{self.libro.titulo}'.")

    def __del__(self):
        """Destructor de la clase Prestamo. Se ejecuta cuando el préstamo finaliza (el objeto deja de existir). Puede usarse para registrar la devolución o cerrar recursos."""
        print(f"[PRÉSTAMO FINALIZADO] Devolución del libro '{self.libro.titulo}' por {self.usuario.nombre}.")


# FUNCIÓN PRINCIPAL DEL PROGRAMA
def main ():
    # Se crean las instancias de las clases
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Marquez")
    usuario1 = Usuario("Santiago Lara")
    prestamo1 = Prestamo(usuario1,libro1)

    print("\n--- Información del préstamo ---")
    prestamo1.mostrar_info()

    # Cuando la función termina, los objetos se eliminan automáticamente y se ejecutan los destructores de cada clase

# Ejecutar el programa
if __name__ == "__main__":
    main()

