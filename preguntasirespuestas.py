llista_preguntes=["¿En qué año se llevó a cabo la Revolución Rusa?","¿En año se produjo la primera explosion nuclear","¿qual es el numero perfecto para Sheldon Cooper","¿Cuántos continentes hay en el mundo?","¿Cuántos elementos químicos hay en la tabla periódica?"]
llista_respuestas=[1923,1945,73,5,118]
seed=int(input("introduce un numero: "))
parar=0
puntos=0
while parar is 0:
    seed = (seed * 997) % 1000
    random = (seed * 503) % 1000 / 100
    numero_pregunta = int(random * (len(llista_preguntes)))
    respuesta= input(llista_preguntes[numero_pregunta])
    puntos +=1 if respuesta== llista_respuestas[numero_pregunta]else 0
    parar= int(input("Si no quieres seguir jugando?[0 para seguir,1 para parar]"))
print("Tus puntos han sido:", puntos)
'''
nota=0
Com fer un número aleatòri: 
cearem una variable anomenada seed i farem que tingui el valor
que vulguis, llavors en el punt on vulguis fer servir un
número aleatòri farem el següent codi.  
print(seed)
respuesta =int(input("Respuesta"))
if llista_respuestas[i] == respuesta:
    print("Correcte!")
    nota= nota+10
else:
    print("Incorrecte")'''
