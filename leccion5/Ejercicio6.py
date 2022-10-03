#ejercicio6: tabla de multiplicar
#hacer un programa que pida un nro por teclado y guarde en una lista
#de multiplicar hasta el 10. Por ej: si digita el 5 la listaa tendra:
#5, 10, 15, 20, 25, 30, 35, 40, 45, 50

numero =int(input("Digite un nro: "))
lista = []# creamos una lista vacia
for i in range(1, 11):
    lista.append(i*numero)

print(f'\nTabla de multipliar de {numero}:\n {lista}')
for indice, i in enumerate(lista):
    print(f'{numero} x {i} = {lista[indice]}') #este ciclo es para ver la multiplicacion como una tabla
