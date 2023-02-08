#ejercicio 5: convertidor de temperaturas
#realizar 2 funciones para convertir de grados celsius a fahrenheit y viseversa
#investigar las formulas

#funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 #la presedencia: *, / y +
#funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # respetar la presedencia utilizano parentesis

celsius = float(input('Digite el valor de celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius}, C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')
