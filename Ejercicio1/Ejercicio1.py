def calcular_promedio(notas):
    return sum(notas) / len(notas)

def nota_mas_alta(notas):
    return max(notas)

def nota_mas_baja(notas):
    return min(notas)


# Programa principal (prueba)
notas = [3.5, 4.2, 2.8, 5.0, 3.9]

print("Lista de notas:", notas)
print("Promedio:", calcular_promedio(notas))
print("Nota más alta:", nota_mas_alta(notas))
print("Nota más baja:", nota_mas_baja(notas))