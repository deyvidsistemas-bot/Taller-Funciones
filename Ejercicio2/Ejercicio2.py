# Lista de tuplas (nombre, nota)
estudiantes = [
    ("Juan", 3.5),
    ("Ana", 4.5),
    ("Luis", 2.9),
    ("Sofia", 3.0),
    ("Carlos", 2.5)
]

def obtener_aprobados(lista):
    aprobados = []
    for nombre, nota in lista:
        if nota >= 3.0:
            aprobados.append((nombre, nota))
    return aprobados


# Programa principal (prueba)
resultado = obtener_aprobados(estudiantes)

print("Estudiantes aprobados:")
for estudiante in resultado:
    print(estudiante)