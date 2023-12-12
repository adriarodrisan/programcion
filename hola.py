#Heu de fer un codi en Python3 que ordeni el següent array de forma ascendent.

array = ["indigo", "groc", "verd", "vermell", "blau", "cian", "taronja"]

#L'ordenació la fem segons la seva longitud d'ona.
longitud_dones = {"indigo": 420,"groc": 570,"verd": 520,"vermell": 650,"blau": 475,"cian": 500,"taronja": 590}
n = len(array)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if longitud_dones(array[j]) < longitud_dones(array[min_index]):
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    print(array)