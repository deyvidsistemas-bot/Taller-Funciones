temperaturas = {
    "Bogotá": [18, 20, 17, 19],
    "Cali": [30, 32, 31, 29],
    "Medellín": [25, 27, 26, 24]
}

def analizar_temp(data):
    todas = []
    for ciudad in data:
        todas.extend(data[ciudad])
    return max(todas), min(todas)

maxima, minima = analizar_temp(temperaturas)

print("Más caliente:", maxima)
print("Más fría:", minima)