#Ejercicio4: sumar nros pares dentro de un rango
#hacer un programa para sumar nros pares entr de un rango
##por ej suma de pares 2-30/ suma= 240

a = int(input('Digite de donde comenzara la suma: '))
b= int(input('Digite el nro maximo que quiere sumar: '))
suma=0
for i in range(a,b+1):
    if i%2==0: #esto es para solo sumar los pares
        suma += i
print(f"\nLa suma de nros pares dentro del rango es: {suma}")