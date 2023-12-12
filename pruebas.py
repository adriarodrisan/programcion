array = ["indigo", "groc", "verd", "vermell", "blau", "cian", "taronja"]

# Diccionari amb longituds d'ona associades als colors
longitud_dones = {
    "indigo": 420,
    "groc": 570,
    "verd": 520,
    "vermell": 650,
    "blau": 475,
    "cian": 500,
    "taronja": 590
}

# Implementació del bubble sort per ordenar segons la longitud d'ona
n = len(array)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if longitud_dones[array[j]] > longitud_dones[array[j + 1]]:
            # Intercanviem els elements si estan fora d'ordre
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)