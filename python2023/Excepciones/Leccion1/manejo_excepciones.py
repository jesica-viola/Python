resultado  = None
a = '10'
b = 0
try:
    resultado = a/b # modificamos
except Exception as e:
    print(f'Ocurrio un error: {e}') # cuando se divide por 0 da error

print(f'El resultado es: {resultado}')
print('Seguimos...')