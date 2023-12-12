constant
    TXT_INTRODUCIR_NUMEROS = "Itroducir un numero entero: "
endconstant

result=None
a= None
a=int(input(TXT_INTRODUCIR_NUMEROS))
primo= a/a or a/1
for a in range (2,a) :
    if a/a == 0:
        print("és primo")
    elif a/a==1:
        print("No es primo")
