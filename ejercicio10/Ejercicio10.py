votos = ["Ana", "Luis", "Ana", "Pedro", "Luis", "Ana", "X"]

candidatos = ["Ana", "Luis", "Pedro"]

def contar_votos(votos, candidatos):
    conteo = {c: 0 for c in candidatos}
    invalidos = 0

    for voto in votos:
        if voto in conteo:
            conteo[voto] += 1
        else:
            invalidos += 1

    total_validos = sum(conteo.values())
    ganador = max(conteo, key=conteo.get)
    porcentaje = (conteo[ganador] / total_validos) * 100

    return conteo, invalidos, ganador, porcentaje


resultado = contar_votos(votos, candidatos)

print("Conteo:", resultado[0])
print("Inválidos:", resultado[1])
print("Ganador:", resultado[2])
print("Porcentaje:", resultado[3])