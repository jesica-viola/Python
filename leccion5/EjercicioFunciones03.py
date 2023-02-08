#ejercicio3: funcion recursiva
#imprimir nros de 5-1 de manera descendente usando funciones recursivas
#puede ser cualquier valor positivo, por ej si pasamos el 5 debe imprimir
#5
#4
#3
#2
#1

def imprimir_nros_recursivos(numero):
    if numero >= 1: #caso base
        print(numero)
        imprimir_nros_recursivos(numero-1) # caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto!')
imprimir_nros_recursivos(5)

#tarea: que el nro lo ingrese el usuario
numeroEscalon = int(input('Ingrese un nro: '))
print(f'El nro que ira bajando su valor en 1 es: {numeroEscalon}')
numero = imprimir_nros_recursivos(numeroEscalon)

