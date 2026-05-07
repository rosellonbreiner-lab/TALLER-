"""
Sistema de Gestión de Notas
Aplicación de consola para gestionar estudiantes y sus notas.
"""

import json
import os

# Nombre del archivo JSON para persistencia
ARCHIVO_DATOS = "notas.json"


def cargar_datos():
    """
    Carga los datos desde el archivo JSON.
    Si el archivo no existe, retorna un diccionario vacío.
    """
    try:
        if os.path.exists(ARCHIVO_DATOS):
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        else:
            return {}
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error al cargar datos: {e}")
        return {}


def guardar_datos(estudiantes):
    """
    Guarda los datos de los estudiantes en un archivo JSON.
    """
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)
        print("Datos guardados exitosamente.")
    except IOError as e:
        print(f"Error al guardar datos: {e}")


def registrar_estudiante(estudiantes):
    """
    Registra un nuevo estudiante con nombre e ID.
    """
    id_estudiante = input("Ingrese el ID del estudiante: ").strip()
    
    # Validar que el ID no exista
    if id_estudiante in estudiantes:
        print("Error: Ya existe un estudiante con ese ID.")
        return
    
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    
    # Validar que el nombre no esté vacío
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return
    
    # Inicializar el estudiante sin notas
    estudiantes[id_estudiante] = {
        "nombre": nombre,
        "notas": []
    }
    print(f"Estudiante '{nombre}' registrado exitosamente con ID: {id_estudiante}")


def agregar_nota(estudiantes):
    """
    Agrega una nota a un estudiante existente.
    Valida que la nota esté entre 0 y 5.
    """
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    id_estudiante = input("Ingrese el ID del estudiante: ").strip()
    
    if id_estudiante not in estudiantes:
        print("Error: No existe un estudiante con ese ID.")
        return
    
    # Solicitar y validar la nota
    nota_str = input("Ingrese la nota (0 a 5): ").strip()
    
    try:
        nota = float(nota_str)
    except ValueError:
        print("Error: La nota debe ser un número.")
        return
    
    # Validar que la nota esté en el rango de 0 a 5
    if nota < 0 or nota > 5:
        print("Error: La nota debe estar entre 0 y 5.")
        return
    
    # Agregar la nota al estudiante
    estudiantes[id_estudiante]["notas"].append(nota)
    print(f"Nota {nota} agregada al estudiante {estudiantes[id_estudiante]['nombre']}.")


def calcular_promedio(estudiantes, id_estudiante):
    """
    Calcula el promedio de las notas de un estudiante.
    Si no tiene notas, retorna 0.
    """
    if id_estudiante not in estudiantes:
        return 0
    
    notas = estudiantes[id_estudiante]["notas"]
    
    if not notas:
        return 0
    
    return sum(notas) / len(notas)


def mostrar_reporte(estudiantes):
    """
    Muestra un reporte con el nombre, promedio y estado de cada estudiante.
    """
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    print("\n" + "=" * 50)
    print("         REPORTE DE ESTUDIANTES")
    print("=" * 50)
    print(f"{'ID':<10} {'Nombre':<20} {'Promedio':<10} {'Estado':<12}")
    print("-" * 50)
    
    for id_est, datos in estudiantes.items():
        nombre = datos["nombre"]
        promedio = calcular_promedio(estudiantes, id_est)
        
        # Redondear el promedio a 2 decimales
        promedio_redondeado = round(promedio, 2)
        
        # Determinar el estado (Aprobado si promedio >= 3.0)
        if promedio_redondeado >= 3.0:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        
        print(f"{id_est:<10} {nombre:<20} {promedio_redondeado:<10} {estado:<12}")
    
    print("=" * 50 + "\n")


def mostrar_menu():
    """
    Muestra el menú de opciones.
    """
    print("\n--- Sistema de Gestión de Notas ---")
    print("1. Registrar estudiante")
    print("2. Agregar nota")
    print("3. Mostrar reporte")
    print("4. Guardar datos")
    print("5. Salir")


def main():
    """
    Función principal que corre el programa.
    """
    # Cargar datos al iniciar
    estudiantes = cargar_datos()
    print("Bienvenido al Sistema de Gestión de Notas!")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            agregar_nota(estudiantes)
        elif opcion == "3":
            mostrar_reporte(estudiantes)
        elif opcion == "4":
            guardar_datos(estudiantes)
        elif opcion == "5":
            # Preguntar si desea guardar antes de salir
            guardar = input("¿Desea guardar los datos antes de salir? (s/n): ").strip().lower()
            if guardar == "s":
                guardar_datos(estudiantes)
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")


if __name__ == "__main__":
    main()
