from producto import Producto,input_int

lista_productos = []
p = Producto("laptop","Asus",2000,5)
#lista_productos.append(p)
#print(lista_productos)
#producto = lista_productos[0]
#print(producto.info())

nombre = input("Nombre del producto: ")
marca = input("Marca del producto: ")
precio = input_int("Precio del producto: ", "No ingresaste bien el precio")
cantidad = input_int("Cantidad del producto: ", "No ingresaste una cantidad valida")

t = Producto(nombre,marca,precio,cantidad)
print(t.info())