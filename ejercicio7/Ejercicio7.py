rangos = [
    (4.5, 5.0, "A"),
    (4.0, 4.4, "B"),
    (3.0, 3.9, "C"),
    (2.0, 2.9, "D"),
    (0.0, 1.9, "F")
]

def convertir(nota):
    for min_, max_, letra in rangos:
        if min_ <= nota <= max_:
            return letra

estudiantes = {
    "Juan": 4.6,
    "Ana": 3.8,
    "Luis": 2.5
}

for nombre, nota in estudiantes.items():
    print(nombre, "->", convertir(nota))