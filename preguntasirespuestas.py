llista_preguntes=["¿Que dos pokemons no tenian devilidades asta llegar la sexta generacion?","¿Qué tipo de Pokémon es inmune a los movimientos de tipo Normal?"]
numeroalotorio=[0,1,2,3,4]
seed=
''' Com fer un número aleatòri: 
cearem una variable anomenada seed i farem que tingui el valor
que vulguis, llavors en el punt on vulguis fer servir un
número aleatòri farem el següent codi.'''
seed = (seed * 997) % 1000
random = (seed * 503) % 1000 / 100
numero_pregunta = int(random * (len(llista_preguntes)))