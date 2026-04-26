carrito = []

def agregar(nombre, precio):
    carrito.append({"nombre": nombre, "precio": precio})

def total():
    return sum(p["precio"] for p in carrito)

def aplicar_descuento(porcentaje):
    return total() * (1 - porcentaje/100)


# Prueba
agregar("Laptop", 2000)
agregar("Mouse", 50)

print("Total:", total())
print("Con descuento:", aplicar_descuento(10))