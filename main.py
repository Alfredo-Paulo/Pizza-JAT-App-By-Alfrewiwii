from datos import menu, T_SALSA, T_MASA, AG_INGREDIENTE, QT_INGREDIENTE
from add import agregar_ingrediente
from masa import tipo_masa
from remove import quitar_ingrediente
from salsa import tipo_salsa
from show import mostrar_ingredientes
from tiempo import estimar_tiempo

# Datos iniciales de la pizza
ingredientes_orden = {
    'masa': 'Masa Tradicional',
    'salsa': 'Salsa de Tomate',
    'ingredientes': ['Queso']
}

while True:
    print(menu)
    opcion = input().strip()

    if opcion == '1':
        print(T_MASA)
        eleccion = input().strip().upper()
        ingredientes_orden = tipo_masa(ingredientes_orden, eleccion)
    elif opcion == '2':
        print(T_SALSA)
        eleccion = input().strip().upper()
        ingredientes_orden = tipo_salsa(ingredientes_orden, eleccion)
    elif opcion == '3':
        print(AG_INGREDIENTE)
        eleccion = int(input().strip())
        ingredientes_orden = agregar_ingrediente(ingredientes_orden, eleccion)
    elif opcion == '4':
        print(QT_INGREDIENTE)
        eleccion = int(input().strip())
        ingredientes_orden = quitar_ingrediente(ingredientes_orden, eleccion)
    elif opcion == '5':
        tiempo = estimar_tiempo(ingredientes_orden)
        print(f'Su Pizza estará lista en {tiempo} minutos')
        ordenar = input('Desea ordenar ahora S/N: ').strip().upper()
        if ordenar == 'S':
            print('Gracias por ordenar en Pizza JAT')
            print('Disfrute su Pizza')
            exit()
    elif opcion == '0':
        mostrar_ingredientes(ingredientes_orden)
    else:
        print('Su pedido ha sido cancelado. Gracias por contactarse a Pizza JAT')
        exit()
