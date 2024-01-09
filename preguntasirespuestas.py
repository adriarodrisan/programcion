llista_preguntes=["¿Que dos pokemons no tenian devilidades asta llegar la sexta generacion?","¿Qué tipo de Pokémon es inmune a los movimientos de tipo Normal?","¿Cuál es el proceso mediante el cual las plantas producen su propio alimento utilizando la luz solar?",""]
numeroalotorio=[0,1,2,3,4]
seed=int(input("seed= "))
''' Com fer un número aleatòri: 
cearem una variable anomenada seed i farem que tingui el valor
que vulguis, llavors en el punt on vulguis fer servir un
número aleatòri farem el següent codi.'''
seed = (seed * 997) % 1000
random = (seed * 503) % 1000 / 100
numero_pregunta = int(random * (len(llista_preguntes)))
print(numero_pregunta)