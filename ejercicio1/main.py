#ejercicio: iterar un rango de 0 10 e imprimir numeros divisibles entre 3
#ejemplo de ejecucion 0,3,6,9
print("rango en 0 a 10 con numeros divisibles entre 3")
for i in range(101):
    if i % 7 == 0:
        print(i)
#ejercicio 2: crear un rango de numeros de 2 a 6 e imprimelos
#ejemplo de ejecucion: 2,3,4,5,6
print("rango con valores de inicio")
rango = range(2, 7)
for i in rango:
    print(i)

#ejericcio 3: crear un rango de 3 a 10 pero con un incremento de 2 en 2, en lugar de 1 en 1
#ejemplo de ejecucion: 3,5,7,9
print('rango con valores de inicio = 3, fin = 10, incremento = 2')
for i in range(3, 11, 2):
    print(i)