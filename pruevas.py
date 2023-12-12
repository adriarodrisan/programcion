rangofinal = int(input("Introduce un número para encontrar todos los primos hasta ese número: "))
rangoinicial= int(input("Introduce un número desde donde quieres enpezar: "))
numeros_primeros= []
numeros_encontrados= 0
for i in range(rangoinicial, rangofinal+1):
    # Si i es un numero primo entonces añadiremos a la lista numero_primers
    # Un numero primo es aquel que solo se puede dividir entre 1 y si mismo
    # Un numero primo es aquel que solo se puede dividir por dos numeros no mayores a el
    # Un numero primo es aquel que entre 2 y el mismo menos 1, no puede dividirse por ninguno
    i_es_primo= True
    j= 2
    while j < i and i_es_primo==True:
        if (i % j == 0):
            i_es_primo= False
        j=j+1
    # Si I es un primo lo introducuremos en una lista numeros
    if i_es_primo==True:
        # Tenemos que introducir el numero en la lista, Pero la lista tiene tamaño menor del que necesitamos
        # La lista tiene el tamaño fr numeros encontrados
        numeros_encontrados= numeros_encontrados+1
        # Hemos borrado todos los numeros encontrados hasta ahora para poder hacer el array más grande
        numero_primers_auxuliar= [None]* numeros_encontrados
        for k in range(0,numeros_encontrados-1):
            numero_primers_auxuliar[k]= numeros_primeros[k]
        numero_primers_auxuliar[numeros_encontrados-1]=i
        numeros_primeros= numero_primers_auxuliar
print(numeros_primeros)