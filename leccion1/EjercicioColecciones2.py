#Ejercicio2 Operaciones de conjuntos con listas
#Escriba un programa que tenga 2 listas y que a continuacion
#cree las siguientes listas (en las que no deben haber repeticiones)
#1 lista de palabras que aparecen en las listas
#2 lista de palabras que aparecen en la primera lista pero no en la segunda
#3 lista de palabras que aparecen en la segunda lista pero no en la 1ra
#4 lista de palabras que aparecen en ambas listas

lista1 = [1, 2, 4, 5, 6, 7, 2, 4, 1, 6, 9]
lista2 = [4, 5, 6, 7, 8, 1, 2, 3]

#eliminar elementos repetidos de ambas listas con conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) #union de los 2 conjuntos
solo1 = list(conjunto1 - conjunto2) #solo muestra conjunto1
solo2 = list(conjunto2 - conjunto1) #solo muestra el conjunto2
interseccion = list(conjunto1 & conjunto2) #mostramos ambas listas

print(f"lista de palabras que aparecen en las listas: {union}")
print(f"lista de palabras que aparecen en la 1ra lista pero no en la 2da: {solo1}")
print(f"lista de palabras que aparecen en la 2da lista pero no en la 1ra: {solo2}")
print(f"lista de palabras que aparecen en ambas listas: {interseccion}")

