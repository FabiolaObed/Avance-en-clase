def opcion1():
 producto={}

 lista_productos =[]
 flag=True
 while flag:
    try:
        nomproducto =input("Ingrese el nombre del producto: ")
        marproducto  =input("Ingrese la marca del producto: ")
        cosproducto  =int(input("Ingrese el costo : "))
        cantproducto=int(input("Ingrese la cantida : "))
    except ValueError:
        print("intentalo otra vez")
    else:
        producto["Nombre"]= nomproducto
        producto["Marca"]= marproducto
        producto["Costo"]= cosproducto
        producto["Cantidad"]= cantproducto
        lista_productos.append(producto)
        producto={}
        pregunta = input("Desea agregar mas productos?")
        if str(pregunta) !="SI":
            flag=False 
        print(lista_productos)
        
    def opcion2():
                pregunta = input("Desea agregar mas productos?")
    if str(pregunta) !="SI" or "NO":
            flag=False 
    print(opcion1)

    while True:
         print(""" Supermercado
               Elija una de las opciones
        1.Listar los productos 
        2.Agregar mas Productos
        3.Hacer la venta.
        """)
         opcion = input("Elija la opcion del menu" )
         a =float(input())
         if opcion=="1":
          print("La lista de los prodcutos es",opcion1)
         elif opcion=="2":
          print("Agregar mas productos", opcion2)
         

opcion1()
#menu 
#print("""
#      Supermercado 
 #     elija la opcion 
 
#1.Listar los productos
#2. Agregar mas productos 
#3. hacer la venta 

#""")
#opcion = input("elijan la opcion del menu")
#auto["estado"]=False
# = auto.get("colores")
#lista_colores.append("azul")
#auto["colores"]= lista_colores
#auto["transmision"]="Automatico"
#print(auto)

#for llave , valor in auto.items():
#   print(llave,valor)

#keys() sonn las llaver
#values() valores 
#get() algo en espesifico de la lista
#items()


