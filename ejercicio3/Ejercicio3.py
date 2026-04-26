agenda = {}

def agregar(nombre, telefono):
    agenda[nombre] = telefono

def buscar(nombre):
    return agenda.get(nombre, "No encontrado")

def eliminar(nombre):
    if nombre in agenda:
        del agenda[nombre]
        return "Eliminado"
    return "No existe"


# Prueba
agregar("Juan", "123")
agregar("Ana", "456")

print(buscar("Juan"))
print(eliminar("Juan"))
print(buscar("Juan"))