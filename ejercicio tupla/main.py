#ejercicio tupla
import math

tupla=(13, 1, 8, 3, 2, 5, 8) #definimos la tupla
#crear una lista que solo incluya los numeros menores a 5
#e imprima por consola [1, 3, 2]

lista = []
#filtramos los elemenos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

#Ejercicio matematicas
#para sacar la raiz cuadrada de un nro +
numero = int(input('Digite un numero: '))
while numero < 0:
    print('Error -> Deberia ser un nro positivo')
    numero = int(input('Digite un nro+:'))
print(f'\nsu raiz cuadrada es {math.sqrt(numero):2f}')

