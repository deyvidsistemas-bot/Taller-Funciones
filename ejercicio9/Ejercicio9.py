productos = [
    ("Manzana", "Fruta"),
    ("Banano", "Fruta"),
    ("Zanahoria", "Verdura"),
    ("Lechuga", "Verdura")
]

def agrupar(lista):
    resultado = {}
    for producto, categoria in lista:
        if categoria not in resultado:
            resultado[categoria] = []
        resultado[categoria].append(producto)
    return resultado

print(agrupar(productos))