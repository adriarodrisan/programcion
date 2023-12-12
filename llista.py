#PRE: Demana al usuari el seu nom i un numero
llistausuari=["Pedro","Marc","Hugo","Martín","Lucas","Mateo","Leo","Daniel" ,"Alejandro","Pablo", "Manuel","Álvaro"]
n =str(input("si quires borrar de la lista: "))
if n == "No"or n=="no":
    nombreusuari=str(input("añade el nombre en la lista: "))
    llistausuari.append(nombreusuari)
    print(llistausuari)
if n== "Si" or n=="si":
    borrarusuari=int(input("Dime un numero para borrar el nombre selecionado: "))
    llistausuari.pop(borrarusuari)
    print(llistausuari)
#POST: retorna las listas canviadas
#Correcion
AFEGUIR= 1
ELIMINAR= 2
LLISTAR= 3
SALIR =4
lista= []
nombre= ""
fin_del_programa= False
while fin_del_programa== False:
#el unusuario puede escoger una opción de 3 opciones(afeguir, eliminar, llistar)
#tedremos un input con la opcion escogida por el  usuario
opcion= int(input("Que quieres hacer 1- Afeguir, 2- eliminar, 3- Llistar, 4- Salir: ")
# si la opcion 1 añadiremos, sino si la opcion es 2 eliminaremos, sino si la opcion es 3 listaremos.
if opcion== AFEGUIR:
    #Aqui añadimos
    #Para añadir necesitamos que el usuario introduzca un nombre
    nombre= input("Introduce el nombre del usuario: ")
    lista.append(nombre)
else:
    if opcion== ELIMINAR:
        nombre= input("Introduce el nombre del usuario a eliminar: ")
        if lista.count(nombre)> 0:
        lista.remove(nombre)
        else:
        if opcion== LLISTAR:
            print("Opcion A")
            for i in range (0,len(lista)):
                print (lista[i])
            print("Opcion B")
            