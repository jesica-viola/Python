#ejercicio1: eliminar duplicados de una lista
#escriba un programa donde tenga una lista y que a continuacion
#elimine los elementos repetidos por ultimo mostrar la lista

#creamos una lista
lista = [1, 2, 3,"Ariel", 7, 7, 3,"Alberto", 1, "Ariel", 2, "Alberto"]
#conjunto = set(lista) #convertimos la lista a un conjunto tipo set
#lista = list(conjunto) # convertimos el conjunto a una lista
#print(lista)
#sino para un codigo eficiente en una sola linea
lista = list(set(lista))
print(lista)
