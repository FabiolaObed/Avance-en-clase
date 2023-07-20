from productos import crearproductos, listarproductos,ventaproductos

def menu():
    lista_de_productos = []
    omenu = """
    MINIMARKET
    ___________________
    1.Listar productos
    2.Agregar productos
    3.Venta
    4.Salir
    """
    flag = True
    while flag:
        try:
            print(omenu)
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            print('Has elegido una opcion que no esta en el menu')
        else:
            if opcion == 1:
                print("Listando productos")
                listarproductos(lista_de_productos)
            elif opcion == 2:
                print("Agregando productos")
                crearproductos(lista_de_productos)
            elif opcion == 3:
                print("Iniciando Venta")
                ventaproductos(lista_de_productos)
                
            elif opcion == 4:
                print("Saliendo")
                flag = False
menu()

         