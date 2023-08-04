def crearproductos(lista_productos):
    producto = {}
    flag=True
    while flag:
        try: 
            nombreproducto = input("Nombre del producto: ")
            marcaproducto = input("Marca del producto: ")
            costoproducto = entrada("Costo del producto: ")
            cantidadproducto = entrada("Cantidad del producto: ")
        except ValueError:
            print("ALGO SALIO MAL INTENTALO OTRA VEZ")
        else:
            producto["nombre"]= nombreproducto
            producto["marca"]= marcaproducto
            producto["costo"]= costoproducto
            producto["cantidad"]= cantidadproducto
            flag_repeti=coincidenaproducto(nombreproducto,cantidadproducto,lista_productos)
            if not flag_repeti:
               lista_productos.append(producto)
            producto = {}
            pregunta = input("Desea agrear mas Productos? SI/NO")
            if str(pregunta) != "SI":
                flag = False

    return lista_productos


def listarproductos(lista_productos):
    print('N° | Producto | Marca | Costo | Cantidad ')
    contador = 0
    for producto in lista_productos:
        contador +=1
        print(f"{contador} {producto.get('nombre')} | {producto.get('marca')} | {producto.get('costo')}| {producto.get('cantidad')}")




def entrada(mensaje):
    while True:
        try:  
            numero_ingreso=int(input(mensaje))
        except ValueError:
            print("Ingrese solo numeros")
        else:
            break
    return numero_ingreso

def coincidenaproducto(nombreproducto,marcaproducto,cantidadproducto,lista_productos):
   flag = False
   for producto in lista_productos:
        if producto.get("nombre")== nombreproducto and producto.get("marca")== marcaproducto and producto.get("cantidad")== cantidadproducto:
            print("este producto ya esta registrado")
            producto["cantidad"]=producto.get("cantidad") + cantidadproducto
            flag = True
        return flag
   
def ventaproductos(lista_de_productos):
    lista_venta=[]
    producto_venta={}
    listarproductos(lista_de_productos)
    flag=True
    while flag:
        try:
         seleccionproducto = int(input("Eliga el numero del producto: "))
         producto = (lista_de_productos[seleccionproducto-1])
         cantidadproducto= int(input(f"Escriba la cantidad de :{producto.get('nombre')}: "))
        except ValueError:
         print("Eliga una opcion")
        else:
        
         producto.get("cantidad")<=cantidadproducto


         producto["cantidad"]=producto.get("cantidad")- cantidadproducto
         producto_venta["producto"]=producto.get("nombre")
         producto_venta["cantidad"]=cantidadproducto
         producto_venta["subtotal"]=cantidadproducto * producto.get("costo")
         lista_venta.append(producto_venta)
         listarproductos(lista_de_productos)
         producto_venta = {}
         print(lista_venta)
         pregunta = str(input("Desea vender mas productos?Si/No: "))
        if (pregunta).upper=="NO":
         flag=False 
         print(lista_venta)
        
def coincidenventa(nombreproducto,cantidadproducto,costoproducto,producto_venta,marcaproducto):
   flag = False
   for producto in producto_venta:
        if producto.get("nombre")== nombreproducto and producto.get("marca")== marcaproducto and producto.get("cantidad")== cantidadproducto and producto.get("costo")==costoproducto:
            print("este producto ya esta registrado")
            flag_repeti=coincidenventa(nombreproducto,cantidadproducto,costoproducto,producto_venta)
        else:
            if not flag_repeti:
               producto_venta.append(producto)
            producto = {}
            pregunta = input("Desea agregar mas Productos? SI/NO")
            if str(pregunta) != "SI":
                flag = False
            producto["cantidad"]=producto.get("cantidad") + cantidadproducto and producto.get("costo")+costoproducto
            flag = True
        return flag
   
    

    
    