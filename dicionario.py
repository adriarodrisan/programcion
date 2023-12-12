d1 = {}
AÑADIR=1
ELIMINAR=2
MOSTRAR=3
fin_del_programa= False
while fin_del_programa != True:
    u = str(input("quieres entrar: "))
    if u == "Si"or u=="si":
        n =int(input("Añadir:1 Eliminar:2 Mostrar:3 = "))
        if n == AÑADIR:
            nombreclave=str(input("añade el nombre de la clave: "))
            nombrevalor=int (input("añade el nombre del valor de la clave: "))
            d1[nombreclave]= nombrevalor 
        else:
            if n== ELIMINAR:
                print(d1)
                existe= False
                borrarclave=str(input("Dime el nombre de la clave que quieres borrar: "))
                for borrar in d1.keys():
                    if borrar == borrarclave:
                       existe = True 
                if existe == True:
                    del(d1[borrarclave])
            else:
                if n == MOSTRAR:
                    print(d1)
    if u == "No"or u=="no": 
        print(d1)   
        fin_del_programa= True