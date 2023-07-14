def coincidenaproducto(nombreproducto,cantidadproducto,lista_productos):
   flag = False
   for producto in lista_productos:
        if producto.get("nombre")== nombreproducto:
            print("este producto ya esta registrado")
            producto["cantidad"]=producto.get("cantidad") + cantidadproducto
            flag = True
        return flag
    







#def entrada(mensaje):
#    while True:
#        try:  
#            numero_ingreso=int
#        except ValueError:
#            print("Ingrese solo numeros")
#        else:
#            break
#    return numero_ingreso

        