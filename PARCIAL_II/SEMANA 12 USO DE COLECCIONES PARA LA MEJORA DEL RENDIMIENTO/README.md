Tarea: Sistema de Gestión de Biblioteca Digital

Objetivo: Desarrollar un sistema para gestionar una biblioteca digital. El sistema permitirá administrar los libros disponibles, las categorías de libros, los usuarios registrados y el historial de préstamos.

Requisitos:

Clases Principales:

Libro: Representa un libro con atributos como título, autor, categoría y ISBN. Utiliza una tupla para almacenar el autor y el título, ya que estos no cambiarán una vez creados.

Usuario: Representa a un usuario de la biblioteca con atributos como nombre, ID de usuario (único) y una lista de libros actualmente prestados.

Biblioteca: Gestiona las colecciones de libros, usuarios y préstamos. Utiliza un diccionario para almacenar los libros disponibles, con el ISBN como clave y el objeto Libro como valor, para búsquedas eficientes. Usa un conjunto para manejar los IDs de usuarios únicos.

Funcionalidades:

Añadir/quitar libros: Permitir añadir o quitar libros de la biblioteca.

Registrar/dar de baja usuarios: Permitir el registro de nuevos usuarios y la baja de usuarios existentes.

Prestar/devolver libros: Facilitar el préstamo de libros a usuarios y la devolución de los mismos.

Buscar libros: Implementar búsquedas de libros por título, autor o categoría.

Listar libros prestados: Mostrar una lista de todos los libros actualmente prestados a un usuario.

Implementación:

Utiliza listas para gestionar los libros prestados a cada usuario.

Emplea tuplas para los atributos inmutables de los libros.

Usa diccionarios para almacenar y acceder eficientemente a los libros por ISBN.

Aplica conjuntos para asegurar IDs de usuario únicos y gestionar los usuarios registrados.

Instrucciones:

Diseña y desarrolla las clases necesarias para implementar el sistema de gestión de biblioteca digital siguiendo los requisitos especificados.

Asegúrate de incluir métodos para cada una de las funcionalidades requeridas.

Comenta tu código adecuadamente para explicar la lógica detrás de tus decisiones de implementación.

Prueba tu sistema creando objetos de cada clase y ejecutando varias operaciones del sistema de biblioteca, como registrar usuarios, añadir libros, prestar y devolver libros, y buscar en el catálogo.

Entrega:

Sube tu código fuente a tu repositorio en GitHub.
Asegúrate de que tu repositorio sea público para que pueda ser revisado.
Esta tarea no solo desafía a los estudiantes a aplicar los conceptos de colecciones en Python dentro de un contexto de POO, sino que también fomenta el pensamiento crítico y la solución de problemas al diseñar un sistema complejo y funcional.