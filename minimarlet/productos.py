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
    print('Producto|Marca|Costo|Cantidad ')
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
        if producto.get("nombre","marca")== nombreproducto and marcaproducto:
            print("este producto ya esta registrado")
            producto["cantidad"]=producto.get("cantidad") + cantidadproducto
            flag = True
        return flag
    