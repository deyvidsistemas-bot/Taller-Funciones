palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]

def contar_frecuencia(lista):
    frecuencia = {}
    for palabra in lista:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

print(contar_frecuencia(palabras))