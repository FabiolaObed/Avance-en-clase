from producto import Producto,input_int
prueba2=
prueba=["laptop","sus",1200,20]
lista_productos = []
lista_productos.append(prueba)

def compara_porductos(nom,mar,lista_productos):
    existe = False 
    for p in lista_productos:
        if nom.upper() == p.get_nombre().upper() and mar.upper() == p.get_marca().upper() :
            print("El producto ya existe")
            existe=True
        else:
            print("Agregando producto")
    return existe



def crear_producto(lista_producto):
    nombre = input("Nombre del producto: ")
    marca = input("Marca del producto: ")
    precio = input_int("Precio del producto: ", "No ingresaste bien el precio")
    cantidad = input_int("Cantidad del producto: ", "No ingresaste una cantidad valida")

    existencia = compara_porductos(nombre,marca,lista_productos)
    if not existencia:
        nuevo_producto = Producto(nombre,marca,precio,cantidad)
        lista_producto.append(nuevo_producto)

crear_producto(lista_productos)
print(lista_productos)

def lista_producto(lista_productos):
     c=0
     for p in lista_productos:
         c+=1
         print(f"{c}.{p.get_info_completa()}")
lista_producto(lista_productos)



    