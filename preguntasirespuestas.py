llista_preguntes=["¿En qué año se llevó a cabo la Revolución Rusa?","¿En año se produjo la primera explosion nuclear","¿qual es el numero perfecto para Sheldon Cooper","¿Cuántos continentes hay en el mundo?","¿Cuántos elementos químicos hay en la tabla periódica?"]
llista_respuestas=[1923,1945,73,5,118]
numeroalotorio=[0,1,2,3,4]
nota=0
seed=int(input("seed= "))
''' Com fer un número aleatòri: 
cearem una variable anomenada seed i farem que tingui el valor
que vulguis, llavors en el punt on vulguis fer servir un
número aleatòri farem el següent codi.'''
seed = (seed * 997) % 1000
random = (seed * 503) % 1000 / 100
numero_pregunta = int(random * (len(llista_preguntes)))
#print(llista_preguntes[numero_pregunta])
print(seed)
respuesta =int(input("Respuesta"))
if llista_respuestas[i] == respuesta:
    print("Correcte!")
    nota= nota+10
else:
    print("Incorrecte")
