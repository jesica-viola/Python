#Ejercicio5: factorial de un nro positivo
#hacer un programa para calcular el factorial de un nro positivo
numero =int(input("Digite un nro: "))
while numero < 0: #mientras el nro sea negativo
     print("ERROR -> El nro tiene que ser positivo")
     numero = int(input("Digite un nro: "))
factorial = 1 #la variable para calcular el factorial
for i in range(1, numero+1):
    factorial *= i
print(f"\nEl factorial del numero {numero} positivo ingresado es: {factorial}")