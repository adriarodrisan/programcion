s1 = {}
fin_del_programa= False
while fin_del_programa != True:
    u = str(input("quieres entrar: "))
    if u == "Si"or u=="si":
        n =str(input("¿Quires añadir al set? "))
        if n == "Si"or n=="si":
            nombreclave=int(input("añade el nombre de la clave: "))
            s1.add(nombreclave)
        else:
            m= str(input("¿Quires borrar del Diccionario? "))
            if m== "Si" or m=="si":
                print(s1)
                borrarclave=int(input("Dime el nombre de la clave que quieres borrar: "))
                s1.remove(borrarclave)
            else:
                print(s1)
    if u == "No"or u=="no":    
        fin_del_programa= True