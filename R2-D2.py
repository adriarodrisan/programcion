#Pre: Demana dos numeros
def encontrar_primos(rangofinal):
    numeros = [True] * (rangofinal + 1)
    numeros[0] = numeros[1] = False  
    
    for i in range(rangoinicial, int(rangofinal**0.5) + 1):
        if numeros[i]:
            # Marcar los múltiplos como no primos
            for j in range(i * i, rangofinal + 1, i):
                numeros[j] = False
    primos = [i for i, es_primo in enumerate(numeros) if es_primo]
    return primos
rangofinal = int(input("Introduce un número para encontrar todos los primos hasta ese número: "))
rangoinicial= int(input("Introduce un número desde donde quieres enpezar: "))
lista_primos = encontrar_primos(rangofinal)
print("Números primos desde", rangoinicial,"hasta",rangofinal, ":", lista_primos)
#post: retorna el rango  de nombres primers desde un numero fins altre