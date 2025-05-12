NOTA_BAJA = 3.0
# Función para obtener la entrada del usuario de forma segura
# Umbral por defecto
UMBRAL_DEFAULT = 3.0

def obtener_entrada(mensaje, tipo=str):
    """Obtiene entrada del usuario."""
    entrada = input(mensaje)
    if not entrada:
        return None
    if tipo == int and entrada.isdigit():
        return int(entrada)
    if tipo == float:
        try:
            return float(entrada)
        except ValueError:
            return None
    return entrada if tipo == str else None

def agregar_estudiante(estudiantes):
    """Agrega un estudiante."""
    nombre = obtener_entrada("Nombre: ")
    edad = obtener_entrada("Edad: ", int)
    id_estudiante = obtener_entrada("ID: ")
    nota = obtener_entrada("Nota (0.0 - 5.0): ", float)
    if nombre and edad and id_estudiante and nota and 0 < edad and 0 <= nota <= 5:
        for estudiante in estudiantes:
            if estudiante['id'] == id_estudiante:
                print(f"Error: ID {id_estudiante} existe.")
                return
        estudiantes.append({'nombre': nombre, 'edad': edad, 'id': id_estudiante, 'nota': nota})
        print("Estudiante agregado.")
    else:
        print("Entrada inválida.")

def buscar_estudiante_por_id(estudiantes, id_estudiante):
    """Busca estudiante por ID."""
    for estudiante in estudiantes:
        if estudiante['id'] == id_estudiante:
            return estudiante
    return None

def buscar_estudiantes_por_nombre(estudiantes, nombre):
    """Busca estudiantes por nombre."""
    nombre_lower = nombre.lower()
    return [est for est in estudiantes if nombre_lower in est['nombre'].lower()]

def actualizar_informacion_estudiante(estudiantes, id_estudiante):
    """Actualiza estudiante."""
    for estudiante in estudiantes:
        if estudiante['id'] == id_estudiante:
            print("1. Edad\n2. Nota\n3. Ambas")
            opcion = obtener_entrada("Opción: ", int)
            if opcion in [1, 2, 3]:
                if opcion in [1, 3]:
                    edad = obtener_entrada("Nueva edad: ", int)
                    if edad and edad > 0:
                        estudiante['edad'] = edad
                if opcion in [2, 3]:
                    nota = obtener_entrada("Nueva nota (0.0 - 5.0): ", float)
                    if nota and 0 <= nota <= 5:
                        estudiante['nota'] = nota
                print("Estudiante actualizado.")
                return
            else:
                print("Opción inválida.")
                return
    print(f"Error: Estudiante con ID {id_estudiante} no encontrado.")

def eliminar_estudiante(estudiantes, id_estudiante):
    """Elimina estudiante."""
    for estudiante in estudiantes:
        if estudiante['id'] == id_estudiante:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado.")
            return
    print(f"Error: Estudiante con ID {id_estudiante} no encontrado.")

def calcular_promedio_notas(estudiantes):
    """Calcula promedio de notas."""
    if not estudiantes:
        return None
    total_notas = sum(estudiante['nota'] for estudiante in estudiantes)
    return round(total_notas / len(estudiantes), 2)

def listar_estudiantes_por_debajo_del_umbral(estudiantes, umbral=UMBRAL_DEFAULT):
    """Lista estudiantes por debajo del umbral."""
    return [estudiante for estudiante in estudiantes if estudiante['nota'] < umbral]

def mostrar_informacion_estudiante(estudiante):
    """Muestra información de un estudiante."""
    if estudiante:
        print(f"  Nombre: {estudiante['nombre']}")
        print(f"  Edad: {estudiante['edad']}")
        print(f"  ID: {estudiante['id']}")
        print(f"  Nota: {estudiante['nota']}")
    else:
        print("Estudiante no encontrado.")

def mostrar_lista_estudiantes(lista_estudiantes):
    """Muestra una lista de estudiantes."""
    if lista_estudiantes:
        for estudiante in lista_estudiantes:
            mostrar_informacion_estudiante(estudiante)
            print("-" * 20)
    else:
        print("No se encontraron estudiantes.")



