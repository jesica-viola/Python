#DEclaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding='utf8') #la w es de write significa escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Con esto terminamos.')
except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close() # con esto se debe cerrar el archivo
#archivo.write('todo quedo perfecto') no se puede poner nada despues de cerrar el archivo
