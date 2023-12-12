#PRE: Recibimos 2 numeros enteros y un numero que indique la operacion
def calculadora():
    #constant
    TXT_INTRODUCIR_NUMEROS = "Itroducir un numero entero: "
    TXT_INTRODUCIR_OPERACION = "Introduce que operacion hace 1 para sumar, 2 para restar, 3 para multiplicar, 4 para dividir: "
    SUMA= 1
    RESTA= 2
    MULTIPLICAR= 3
    DIVIDIR= 4
    #endconstant

    #var
    a= None
    b= None
    operando= None
    resultado= None
    #endvar

    a=int(input(TXT_INTRODUCIR_NUMEROS))
    operando= int(input(TXT_INTRODUCIR_OPERACION))
    b=int(input(TXT_INTRODUCIR_NUMEROS))

    if operando == SUMA:
        resultado= a+b
    elif operando == RESTA:
        resultado= a-b
    elif operando == MULTIPLICAR:
        resultado= a*b
    elif operando == DIVIDIR and b!=0:
        resultado= a/b
    elif operando == DIVIDIR and b==0:
        resultado=" el resultado es 0"
    else:
        resultado= "operando no soportado por la aplicacion"

    print("el resultado és",resultado)
#POST: Devolvemos el resultado de la operación seleccionada si esta existe

calculadora() #Esto es importante, si no invocamos no se ejecuta