#PRE:lleguir el text i comti la seva freqüencia
texto= str(input("Dime un texto que quieras aqui pero no te pases: "))
texto= texto.casefold()
contarpalabras=texto.split(" ")
for i in range(len(contarpalabras)):
    for j in range(len(contarpalabras)):
        if contarpalabras[i]== contarpalabras[j]:
            