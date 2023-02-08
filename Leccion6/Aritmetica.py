class Aritmetica:
    """
    el nombre de este tpipo de comentario es : DocString
    esto es documentacion de la clase en pytho 
    vamos a hacer en esta clase alguna operaciones de suma, resta, multipli, y mas
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    #metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB
    def resta(self):
        return self.operandoA - self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
aritmetica1 = Aritmetica(7, 9) #le pasamos los argumentos para los operandos
print(f'la suma de los nros: {aritmetica1.sumar()}')
print(f'la resta de los nros es: {aritmetica1.resta()}')
print(f'la multiplicacion de los nros es: {aritmetica1.multiplicar()}')
print('la division de los nros es: {aritmetica1.dividir():.2f}')
