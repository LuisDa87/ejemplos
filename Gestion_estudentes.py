from funciones_students import *

# Umbral por defecto para listar estudiantes con notas bajas
NOTA_BAJA = 3.0


def main():
    """
    Función principal para ejecutar el sistema de gestión de estudiantes.
    """
    estudiantes = [
        {"nombre": "Alice Smith", "edad": 20, "id": "S1001", "nota": 4.2},
        {"nombre": "Bob Johnson", "edad": 22, "id": "S1002", "nota": 3.5},
        {"nombre": "Charlie Brown", "edad": 19, "id": "S1003", "nota": 2.8},
        {"nombre": "Diana Garcia", "edad": 21, "id": "S1004", "nota": 4.8},
        {"nombre": "Eve Williams", "edad": 23, "id": "S1005", "nota": 3.9}
    ]

    while True:
        print("\nSistema de Gestión de Estudiantes")
        print("1. Agregar Estudiante")
        print("2. Buscar Estudiante por ID")
        print("3. Buscar Estudiantes por Nombre")
        print("4. Actualizar Información del Estudiante")
        print("5. Eliminar Estudiante")
        print("6. Calcular Promedio de Notas")
        print("7. Listar Estudiantes por Debajo del Umbral")
        print("8. Salir")

        opcion = obtener_entrada("Ingrese su elección: ", int)

        if opcion is None:
            print("Opción inválida. Por favor, ingrese un número.")
            continue # Regresa al inicio del bucle

        if opcion == 1:
            agregar_estudiante(estudiantes)

        elif opcion == 2:
            id_estudiante = obtener_entrada("Ingrese el ID del estudiante a buscar: ", str)
            if id_estudiante is not None:
                estudiante = buscar_estudiante_por_id(estudiantes, id_estudiante)
                mostrar_informacion_estudiante(estudiante)

        elif opcion == 3:
            nombre = obtener_entrada("Ingrese el nombre del estudiante (o parte de él) a buscar: ", str)
            if nombre is not None:
                resultados = buscar_estudiantes_por_nombre(estudiantes, nombre)
                mostrar_lista_estudiantes(resultados)

        elif opcion == 4:
            id_estudiante = obtener_entrada("Ingrese el ID del estudiante a actualizar: ", str)
            if id_estudiante is not None:
                actualizar_informacion_estudiante(estudiantes, id_estudiante)

        elif opcion == 5:
            id_estudiante = obtener_entrada("Ingrese el ID del estudiante a eliminar: ", str)
            if id_estudiante is not None:
                eliminar_estudiante(estudiantes, id_estudiante)

        elif opcion == 6:
            promedio_notas = calcular_promedio_notas(estudiantes)
            if promedio_notas is not None:
                print(f"Promedio de notas de todos los estudiantes: {promedio_notas}")
            else:
                print("No hay estudiantes registrados para calcular el promedio de notas.")

        elif opcion == 7:
            umbral_str = obtener_entrada(f"Ingrese el umbral para las notas (por defecto: {NOTA_BAJA}): ", float)
            umbral = NOTA_BAJA if umbral_str is None else umbral_str
            estudiantes_debajo_umbral = listar_estudiantes_por_debajo_del_umbral(estudiantes, umbral)
            print(f"\nEstudiantes con notas por debajo de {umbral}:")
            mostrar_lista_estudiantes(estudiantes_debajo_umbral)

        elif opcion == 8:
            print("Saliendo del Sistema de Gestión de Estudiantes. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
