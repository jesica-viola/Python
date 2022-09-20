nombres = ["naty", "osvaldo", "lily", "ariel"] #lista de nombres
print(nombres)
print(nombres[0:2])#solo muestra el indice 0, 1 pero no el indice 2
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3])#indices a mostrar 0,1,2
print(nombres[1: ])
#modificamos un valor ponemos posicion y asignamos el dato
nombres[2] = "Liliana"
print(nombres)

#iterar una lista
for nombre in nombres:#nombre es singular, la lista plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista")

#preguntamos cuantos elementos tiene
print(len(nombres))#le pasamos como parametro la lista

#agregamos un elemento
nombres.append("marcelo")
print(nombres)

#insertar un elemento en un indice especifico
nombres.insert(1, "alberto")
print(nombres)
nombres.insert(3, "debora")
print(nombres)

#eliminar el ultimo elemento
nombres.remove("alberto")
print(nombres)

#eliminar el ultimo elemento
nombres.pop()
print(nombres)

#eliminar un indice especifico
del nombres[2]#del significa delete
print(nombres)
#eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#eliminar la lista
del nombres#si ponemos print muestra error

#DEFINIMOS UNA TUPLA
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)
print(len(cocina))

#como acceder a un elemento, para esto usamos corchetes no parentesis
print(cocina[0])
#mostrar de manera inversa (el ultimo elemento)
print(cocina[-1])

#acceder a un rango
print(cocina[0:1])
#ejemplo
verduras = ('papa',)#importante ponerle la coma sino es tipo string

#recorrer los elementos de una tupla
for cocinar in cocina:
    print(cocinar)# print usa \n para saltos de lineas
    #se usa end= para eliminar los saltos d lineas por ej
    #print(cocinar, end=' ')
#cocina[o]= plato #marca error xq no se puede agregar elementos o eliminarlos
#print(cocina)

#en tuplas no se puede utilizar las funciones append, remove, insert. Sus elementos se escirben en parentesis

#para modificar los elementos de tupla se debe pasar a lista sino no se puee
cocinaLista = list(cocina)
cocinaLista[0]= 'plato'
cocina = tuple(cocinaLista)
print(cocina)

#tipo set: no tiene orden, no permite almacenar elementos duplicados, no se puede
#modificar pero se puede agregar o modificar. No mantiene ningun indice (el orden es aleatorio)
#sin orden y sin indices sus elementos se escriben en corchetes. Cada vez que se ejecuta el print cambia el orden

planetas = {'marte', 'jupiter', 'venus'}
print(planetas)
print(len(planetas))
#verficar si un elemento existe dentro del set
print('marte' in planetas)#devuelve un tipo booleano
#preguntar si marte no esta en planetas ej->
print('marte' not in planetas)
#agregar un elemento
planetas.add('tierra')#add es una funcion, solo se agregara una vez el elemnto
print(planetas)
#eliminar elementos, puede arrojar un error si el elemento no xiste
planetas.remove('jupiter')
print(planetas)
planetas.discard('tierra')#discar no da error por acentos, mayusculas etc o inexistencia
print(planetas)
#limpiar el set
planetas.clear()
print(planetas)
#eliminar set o conjunto
#del planetas

#diccionario es coleccion pero ordenompuesto por dos elementos
#una llave y un valor
#dict(key, value)
diccionario = {
    'IDE': 'Integrates Development Environment',
    'POO': 'Programacio orientada a objetos',
    'SABD': 'Sistema de Administracion de base de datos'

}
print(diccionario)
print(len(diccionario))#cantidad de elementos del diccionario
#acceder a un diccionario on la llave (key)
print(diccionario['IDE'])
#otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))
#modificamos los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#como recorrer los elementos
for termino in diccionario:
    print(termino)

#for termino, valor in diccionario: #recorremos mostrando solo las llaves
#  print(termino, valor)
for termino, valor in diccionario.items():
    print(termino, valor)

#otras maneras de acceder a un diccionario
for termino in diccionario.keys():#estamos usando una funcion
    print(termino)#muestra solo las llaves
for valor in diccionario.values():#usamos una funcion para acceder al valor
    print(valor)
#comprobar la existencia de algun elemento
print('IDE' in diccionario)#devuelve boolean
#agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)
#eliminar un elemento
diccionario.pop('SABD')
print(diccionario)
#vaciar un diccionario
diccionario.clear()
print(diccionario)
#eliminar diccionario
del diccionario

# concatenamos listas
lista1 = [1, 2, 3, 1, 1]
lista2 = [4, 5, 6]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9]) # funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # funcion para ubicar en que indice esta el valor ingresado
print(lista3.index(2)) #si el elemento no esta da error
#como saber cuantos valores son repetidos en una lista
print(lista3.count(1))
#poner al reves una lista
lista3.reverse()
print(lista3)

#para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2 #repite 2 veces los numeros [1, 2, 3, 1, 2, 3]
lista3 = lista3 *2 #exactamente lo mismo

print(lista)
print(lista3)

#metodos de ordenamiento (es una funcion)
lista3.sort()
print(lista3)
lista3.sort(reverse=True)
print(lista3)

tupla = (4, 'Hola', 6.78, [1, 3, 78], 4, 'Hola')
print(tupla)

print(4 in tupla) #accion booleana, su respuesta es de tipo booleana
#lo que podemos usar dentro de tuplas son: index, count, len,
#en tuplas se puede convertir de tupla a lista y de lista a tupla

#repaso de set o conjunto para definir un conjunto
conjunto = set()
conjunto1 = {'bye'}
conjunto.add(7)
conjunto.add('Hola')
print(conjunto)
conjunto.add('Hola')
print(conjunto1)
print(3 not in conjunto1)#preguntamos si un valor NO esta en el conjunto

#como hacr la igualdad de dos conjuntos
print(conjunto1 == conjunto)#nos devuelve como resp un boolean
#operaciones en conjuntos
conjunto3 = conjunto1 | conjunto#la linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 - conjunto#asigna el valor que esta en el conjunto1 y no en el conjunto
print(conjunto3)
conjunto3 = conjunto - conjunto1
print(conjunto3)

conjunto3 = conjunto1 & conjunto#que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 ^conjunto#elementos que no comparten o que son diferentes
print(conjunto3)

conjunto3 = conjunto1 | conjunto
print(conjunto.issubset(conjunto3))#aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto))

print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto))
print(conjunto.issuperset(conjunto3))

#como saber si ambos conjuntos son disconexos (si no comparten elemntos en comun
print(conjunto1.isdisjoint(conjunto)) #no hay cosas en comun

#convertir un conjunto totalmente en inmutable
conjunto1 = frozenset #esto hace que el conjunto sea totalmente inmutable
#no se puede agregar, modificar ni eliminar elementos

#repaso diccionarios
diccionarioNuevo = {'azul': 'blue', 'rojo': 'red', 'verde': 'green', 'amarillo': 'yellow'}
print(diccionarioNuevo)
del (diccionarioNuevo['azul'])
print(diccionarioNuevo)

#los diccioarios pueden almacenar diferentes tipos de datos
diccionario2 = {'ariel': {'edad': 40, 'altura': 1.83}, 'osvaldo': [45, 1.85], 'natalia': [35, 1.67]}
print(diccionario2)

#ejercicio
seleccionArgentina = {
    10: {'nombre': 'lionel messi', 'edad': 35, 'altura': 1.70},
    11: {'nombre': 'angel di maria', 'edad': 34, 'altura': 1.80},
    24: {'nombre': 'paulo dybala', 'edad': 28, 'altura': 1.77},
    19: {'nombre': 'nicolas otamendi', 'edad': 34, 'altura': 1.83},
    1: {'nombre': 'franco armani', 'edad': 35, 'altura': 1.89}
    }
print(seleccionArgentina)
print(seleccionArgentina[10])

for valor in seleccionArgentina:
    print(valor)
print('tenemos cargados en el diccionario la cantidad de:', end=' ')
print(len(seleccionArgentina))


# pilas usando listas
pila = [1, 2, 3]

#agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#sacamos elementos desde el final
pila.pop()
print(pila)

#sacamos elementos desde el final
elementoBorrado = pila.pop()#quita el ultimo elemento y lo guarda en una variable
print(f'sacamos el elemento {elementoBorrado}')
print(f'la pila ahora quedo asi:{pila}')

#colas con listas
#estructura de datos de tipo fifo (first input / first output)
#el primero que se agrega es el primero que se elimina
cola = ['ariel', 'osvaldo', 'liliana', 'pilar']
#agregamos elementos al final de la cola
cola.append('natalia')
cola.append('jose')
print(cola)
#sacamos elemento de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
