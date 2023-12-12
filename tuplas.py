servidores= []
AFEGUIR= 1
ELIMINAR= 2
MOSTRAR= 3
SALIR= 4
fin_del_programa= False 
while fin_del_programa == False:
    opcion= int(input("Que quieres hacer 1- Afeguir servidor, 2- eliminar servidor, 3- Mostrar Servidor, 4 Salir del programa: "))
    if opcion== AFEGUIR:
        nombre= input("Introduce el nombre del servidor: ")
        ip= input("Introduce la IP del servidor: ")
        estado= input("Introduce el estado del servidor[activo/inactivo]: ")
        tupla=(nombre, ip, estado)
        servidores.append(tupla)
    else:
        if opcion == ELIMINAR:
            servidor_a_borrar= input("introduce el nombre del servidor a borrar: ")
        else:
            if opcion== MOSTRAR:
                for i in range(0,len(servidores)) servidores:
                    print ("Nombre del servidor:", servidores[i][0])
                    print ("IP del servidor:", servidores[i][1])
                    print ("Estado del servidor:", servidores[i][2])
            else:
                if opcion == SALIR:
                    fin_del_programa= True