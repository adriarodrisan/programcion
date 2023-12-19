#PRE:introdueix un llista de tuples amb la informació requerida
estudiante1=[]
estudiante2=[]
llista1=[]
llista2=[]
#Afegir elements a la llista d'estudisantes(Nom, Cognom, Edat, Nota1, Nota2, Nota3).
nombre1=str(input("introduce el nombre del alumno: " ))
apellido=str(input("Introduzca los apellidos del estudiante: ") )
edad=int(input("Introduzca la edad del estudiante: "))
nota1_1= float(input("Introduzca la nota del primer examen del estudiante: "))
nota2_1= float(input("Introduzca la nota del segundo examen del estudiante: "))
nota3_1= float(input("Introduzca la nota del tercer examen del estudiante: "))
mediaponderada1=nota1_1*0.3+nota2_1*0.4+nota3_1*0.3
tupla1=(nombre1,apellido,edad,nota1_1,nota2_1,nota3_1, mediaponderada1)
estudiante1.append(tupla1)
nombre2=str(input("introduce el nombre del alumno: " ))
apellido=str(input("Introduzca los apellidos del estudiante: ") )
edad=int(input("Introduzca la edad del estudiante: "))
nota1_2= float(input("Introduzca la nota del primer examen del estudiante: "))
nota2_2= float(input("Introduzca la nota del segundo examen del estudiante: "))
nota3_2= float(input("Introduzca la nota del tercer examen del estudiante: "))
mediaponderada2=nota1_2*0.3+nota2_2*0.4+nota3_2*0.3
tupla2=(nombre2,apellido,edad,nota1_2,nota2_2,nota3_2, mediaponderada2)
estudiante2.append(tupla2)

if mediaponderada1 >=7:
    llista1.append(tupla1)
else:
    if mediaponderada2 >=7:
        llista1.append(tupla2)
if nota1_1>=8 or nota2_1>=8 or nota3_1>=8:
   llista2.append(tupla1)
    
else:
    if nota1_2>=8 or nota2_2>=8 or nota3_2>=8:
        llista2.append(tupla2)
print(llista1[0], llista1[6])
print(llista2) 
#POST: devuelve el nombre i la media de sus examenes