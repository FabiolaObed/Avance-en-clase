producto={"Nombre": "" , 
      "Marca":"",
      "Costo": 0,
      "Cantidad":0,
      
}

lista_productos =[]
flag=True
while flag:
    try:
        producto["Nombre"]=input("Ingrese el nombre del producto: ")
        producto["Marca"]=input("Ingrese la marca del producto: ")
        producto["Costo"]=int(input("Ingrese el costo : "))
        producto["Cantidad"]=int(input("Ingrese la cantida : "))
    except ValueError:
        print("Algo salio mal intentalo otra vez")
    else:
        producto["Nombre"]= producto

    
lista_productos.append(producto)
print(lista_productos)

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
