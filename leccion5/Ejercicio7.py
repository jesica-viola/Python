#ejercicio7: juego adivina el nro
#Se debe generar un nro aleatorio entre 1-100 y luego pedir nros indicando
#si es mayor o menor respecto a N. Se termina cuando el usuario acierta. Se debe mostrar el nro de intentos

import random
print("\t .:Juego ADIVINA EL NUMERO:.")
aleatorio = random.randint(0, 100)#le damos el rango donde se generara el nro aleatorio
contador = 0
while True:
    numero = int(input("Digite un nro: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el nro, digite un nro MENOR: ")
    elif numero < aleatorio:
        print("\tNo es el nro, digite un nro MAYOR: ")
    else:
        print(f"FELICIDADES, acabas de adivinar el nro {aleatorio}")
        break #rompe el ciclo y bucle
print(f"numero de intentos: {contador}")

