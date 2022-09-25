#ejercicio 10: no repetir caracterees
#hacer un programa que pida una cadena por teclado, luego
#meter los caracteres en una lista sin repetir caracteres

cadena = input('Digite una cadena: ')
lista = []
for i in cadena:
    if i not in lista: #si el caracter no esta en la lista
        lista.append(i)# lo agregamos a la lista
print(f'\nlista de caracteres sin repetir ninguno: \n{lista}')
