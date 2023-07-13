auto={"marca": " Toyota" , 
      "Modelo":"Hilux",
      "NumeroAccidentes": 1,
      "estado": True,
      "colores":["negro","gris"]
      }

#auto["estado"]=False
lista_colores = auto.get("colores")
lista_colores.append("azul")
auto["colores"]= lista_colores
auto["transmision"]="Automatico"
print(auto)

#for llave , valor in auto.items():
#   print(llave,valor)

#keys() sonn las llaver
#values() valores 
#get() algo en espesifico de la lista
#items()
