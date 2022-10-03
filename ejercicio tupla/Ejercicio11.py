#ejercicio 11: agenda telefonica
#hacer un progrma que simule una agenda de contactos. Crear un diccionario donde la clave
#sea el nombre del usuario y el valor sea el telefono, el programa tendra el siguinte menu
#       1. nuevo contacto
#        2. Borrar contacto
#           3 ver contactos existentes
#               4.Salir

agenda = {}
while True:
    print('\t.:MENU:.')
    print('1. nuevo contacto')
    print('2. borrar contacto')
    print('3. ver contactos existentes')
    print('4. Salir')
    opcion = int(input('digite una opción de menu: '))
    if opcion == 1:
        nombre = input('ingrese el nombre del contacto: ')
        telefono = input('ingrese el nro de telefono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('contacto guardado')
        else:
            print('ese contacto ya existe en agenda!')
    elif opcion==2:
        nombre = input('cual es el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha eliminado el contacto')
        else:
            print('este contacto no existe en la agenda')
    elif opcion==3:
        print('agenda de contactos')
        for clave, valor in agenda.items():
            print(f'nombre: {clave}, telefono: {valor}')
    elif opcion == 4:
        print('gracias por utlizar su agenda de contactos')
        break
    else:
        print('se equivoco de opcion de menu!')
    print()

