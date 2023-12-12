#Pedir una frase
TXT_INTRODUCIR_TEXT= "Itroducir un text separados por espacios: "
contadordepalabras= 1
palabras= str(input(TXT_INTRODUCIR_TEXT))
fin_texto=False
i=0
aux=[]
while fin_texto != True:
    aux[i]=palabras[i]
    fin_texto = aux==palabras
    i+=1
contadordepalabras= i
print(contadordepalabras)
#devolver quantas palabras has escrito
