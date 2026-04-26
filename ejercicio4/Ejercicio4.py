inventario = {
    "Laptop": {"precio": 2000, "cantidad": 3},
    "Mouse": {"precio": 50, "cantidad": 10},
    "Teclado": {"precio": 100, "cantidad": 5}
}

def valor_total(inv):
    total = 0
    for producto in inv:
        total += inv[producto]["precio"] * inv[producto]["cantidad"]
    return total

print("Valor total:", valor_total(inventario))