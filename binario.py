#PRE: Demana un numero en binari
binario = int(input("número en binario: "))

decimal = 0
i = 0
while (binario>0):
    digito  = binario%10
    binario = int(binario//10)
    decimal = decimal+digito*(2**i)
    i = i+1
print("en decimal:",decimal)
#POST: Retorna el numero en decimal