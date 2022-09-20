#ejercicio3: insertar elementos y ordenarlos
#pedir numeros y meterlos en una lista, cuando el usuario
#introduzca un nro 0, el progrma deja de insertar.
#por ultimo, mostrar los numeros ordenados de menor a mayor

lista =[]
salir = False
while not salir:
    numero = int(input('Digite un numero:'))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() #la lista esta ordenada con esta funcion
print(f'lista ordenada: \n{lista}')
