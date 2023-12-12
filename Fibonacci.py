#Pre: Demana un numero positiu
n= int(input("Dame un numero positivo: "))
a = 1
b = 1
if n== 1:
    print("1")
elif n == 2:
    print("1", "1")
else:
    print(a)
    print(b)
    for i in range(n - 3):
        total = a + b
        b = a
        a = total
        print(total)
#Post: retorna els primers n numeros de fibonacci