#comenzamos con FUNCIONES
#definimos una funcion
def mi_funcion():# para identificar la funcion utilizamos ()
    print('Saludos a los alumnos de la tecnicatura!')
#no se puede llamar la funcion antes de definirla
mi_funcion()# estamos llamando a la funcion
mi_funcion()# podemos ejecutarla las veces q querramos

#desempaquetado de listas o list unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1])# pasamos uno por uno los datos de la lista a la funcion
show(*person) # esto es lo mismo que lo anterior pero lo pasamos todo junto
person2 = ("osvaldo", "Giordanini")# desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n ==3: #cuando llega a 3 se termina por el break, no se ejecuta el resto
        break
else:
    print("esto se termino") # si la lista estaria vacia igual se ejecuta el else

#list de comprehension, lista de comprension
names= ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] # esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"}]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

#paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a traves del canal de YouTube")
    print(f"nombre: {name}, apellido: {lastName}")
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Jesica', 'viola')

#la palabra return en funciones
#creaamos una funcion para sumar
def sumar(a, b):
    return a + b
resultado = sumar(78, 22)
print(f'El resultado de la suma es {resultado}')# dos maneras de ejecurar la funcion
print(f'El resultado de la suma es: {sumar(55, 45)}') #esta es otra manera

def sumar2(a = 0, b = 0):# le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

#argumentos variables en funciones
def listarNombres(*nombres):# normalmente se utiliza: *args
    for nombre in nombres: #se convierte en una tupla
        print(nombre)
listarNombres('Lucas', 'Jesica', 'Fiorella', 'Leonardo', 'Phoebe', 'Leila')
listarNombres('Marcos', 'Matias', 'Sebastian', 'Franco')
