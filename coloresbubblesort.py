array = ["indigo", "groc", "verd", "vermell", "blau", "cian", "taronja"]
longitud_dones = {
    "indigo": 420,
    "groc": 570,
    "verd": 520,
    "vermell": 650,
    "blau": 475,
    "cian": 500,
    "taronja": 590
}
n = len(array)
for i in range(0, len(array)):
    for j in range(0, n-i-1 ):
        if longitud_dones[array[j]] > longitud_dones[array[j + 1]]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)