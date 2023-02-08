class Persona: # creamos una clase
    #pass // no se procesa nada mas (no tiene contenido)
    def __init__(self, nombre, apellido, edad): #se lo llama metodo init dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
persona1 = Persona('Ariel', 'Betancud', 40) #necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)