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
for i in range(n-1):
    for j in range(0,i+1, -1):
        if longitud_dones(array[j]) < longitud_dones(array[min_index]):
            min_index = j
            array[i], array[min_index] = array[min_index], array[i]
    print(array)