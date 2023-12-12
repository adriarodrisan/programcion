'''
Primera tarea, LEER el enunciado
Si no entiendo las reglas, busco en google!
Tenemos que repartir a cada jugador 13 cartas
cuantas cartas hay? Cuantos jugadores hay? 52 cartas y 4 jugadores
Primero tenemos que crear la mano (una lista de 52 cartas aleatorias)
'''
cartas=["7H","5S","9C","4C","6H","8S","2C","AH","3S","KS","JD","10S","QC","AC","8H","6D","3H","5D","4D","10D",
        "JC","QS","9S","KH","2S","7C","8C","3C","4S","2H","AD","7S","10H","JS","KD","5H","9D","QH","6C","QD",
        "6S","8D","2D","AS","JH","5C","KC","3D","9H","10C","7D","4H"]

# Ya tenemos las cartas, tenemos que repartir las manos, 13 cartas a cada jugador
jugadores=[[],[],[],[]]
for i in range(0,13):
    for j in range(0,4):
        jugadores[j].append(cartas.pop())

index= 0 
for jugador in jugadores:
    print("jugador", index, ": ",", ".join(jugador))
    print("Cartas repatidas al jugador:", len(jugador))
    print()
    index= index+1

mesa= []
for jugador in jugadores:
    mesa.append(jugador.pop(0))
for carta in mesa:
    print(carta)
carta= mesa.pop(0)
carta_mas_alta= {"numero": carta[:-1], "palo": carta[-1]}
for carta in mesa:
    carta_a_comparar= {"numero": carta[:-1], "palo": carta[-1]}
    if carta_mas_alta["palo"] == carta_a_comparar["palo"]:
        if carta_mas_alta["numero"] < carta_a_comparar["numero"]:
            carta_mas_alta= carta_a_comparar
    print(f"ganador con un {carta_mas_alta}")