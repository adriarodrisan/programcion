# Pre: Demana dos numeros al usuari
num1 = int(input("Introduce el primer numero: "))

num2 = int(input("Introduce el segundo numero: "))
def mcd(num1, num2):

	residu = 0

	while(num2 > 0):

		residu = num2

		num2 = num1 % num2

		num1 = residu
	return num1
print("El maxim comu divisor de",num1,"y",num2,"es",mcd(num1, num2))
#Post: retorna el maxim comu divisor dels dos numeros