Sistema de Control de Calificaciones

Programa desarrollado en Python para administrar alumnos y sus notas desde la consola.

Descripción

Esta aplicación académica permite realizar diferentes operaciones relacionadas con estudiantes y evaluaciones, tales como:

Registrar alumnos con código e identificación
Ingresar calificaciones numéricas entre 0.0 y 5.0
Obtener el promedio general de cada alumno
Generar informes con el resultado académico
Almacenar la información en un archivo JSON
Requisitos

Para ejecutar el sistema se necesita:

Python 3 o superior
No requiere instalar módulos externos
Utiliza únicamente librerías incluidas en Python
Ejecución del programa

Para iniciar la aplicación se debe ejecutar:

python main.py
Funciones principales
1. Registrar alumno

Permite agregar nuevos estudiantes al sistema solicitando:

Código o ID único
Nombre completo del estudiante

El sistema valida que el identificador no exista previamente.

2. Ingresar calificación

Permite añadir notas a un estudiante ya registrado.

Características:

Solo acepta valores entre 0 y 5
Un alumno puede tener varias notas almacenadas
3. Consultar reporte

Genera un listado con la información académica de cada estudiante:

Código del estudiante
Nombre completo
Promedio final
Estado académico

El estado se determina así:

Aprobado: promedio mayor o igual a 3.0
Reprobado: promedio menor a 3.0
4. Guardar información

Todos los registros pueden almacenarse en el archivo:

datos_notas.json

Esto permite conservar la información incluso después de cerrar el programa.

5. Cerrar sistema

Antes de finalizar, la aplicación pregunta si desea guardar los cambios realizados.

Organización del código

El programa está dividido en varias funciones:

leer_datos(): carga la información desde el archivo JSON
guardar_informacion(): almacena los datos en el archivo
crear_estudiante(): registra nuevos alumnos
registrar_nota(): añade calificaciones
obtener_promedio(): calcula el promedio del estudiante
generar_reporte(): muestra el informe completo
menu_principal(): enseña las opciones del sistema
main(): controla la ejecución principal
Formato del archivo JSON

La información se guarda de la siguiente manera:

{
    "EST001": {
        "nombre": "Carlos Ramirez",
        "notas": [4.0, 3.5, 4.8]
    }
}
Uso del proyecto

Este sistema puede utilizarse con fines educativos, académicos o de práctica en programación con Python.
