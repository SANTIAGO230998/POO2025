Tarea: Sistema de Gestión de Inventarios Mejorado

Objetivo: Mejorar el sistema de gestión de inventarios desarrollado anteriormente para que utilice archivos para almacenar y recuperar la información del inventario y maneje excepciones durante la lectura y escritura de archivos.

Nuevos Requisitos:

Almacenamiento de Inventarios en Archivos:

Modificar la clase Inventario para que al añadir, actualizar, o eliminar productos, estas modificaciones se reflejen en un archivo de texto (por ejemplo, inventario.txt).
Recuperación de Inventarios desde Archivos:

Al iniciar el programa, cargar automáticamente los productos existentes en inventario.txt para reconstruir el inventario.
Manejo de Excepciones:

Implementar manejo de excepciones para capturar y tratar adecuadamente posibles errores durante la manipulación de archivos, como FileNotFoundError y PermissionError.
Asegurar que el programa maneje casos en los que el archivo de inventario no exista, creándolo si es necesario.
Modificaciones a la Interfaz de Usuario en la Consola:

Actualizar la interfaz de usuario para notificar al usuario sobre el éxito o fallo de operaciones de archivo (por ejemplo, notificar al usuario cuando un producto se añade exitosamente al archivo de inventario).
Instrucciones Adicionales:

Mantén la organización y claridad del código, asegurando que todas las modificaciones estén bien comentadas para explicar el funcionamiento del manejo de archivos y excepciones.
Realiza pruebas exhaustivas para asegurarte de que el programa puede manejar situaciones como archivos corruptos, falta de permisos de escritura, y más.
Evaluación:

La tarea será evaluada en base a la integración efectiva del almacenamiento en archivos y el robusto manejo de excepciones, además de los criterios previamente establecidos de funcionalidad, calidad y claridad del código, y organización y documentación del repositorio de GitHub.

Esta tarea avanzada permite a los estudiantes aplicar conceptos críticos de la programación en Python, como la manipulación de archivos y el manejo de excepciones, a un proyecto práctico, reforzando su comprensión y habilidad para desarrollar aplicaciones resilientes y mantenibles.