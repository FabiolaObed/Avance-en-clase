def cant_vc(n):
    cantidad_vocales=0
    cantidad_consonantes=0
    n = n.lower()
    
    for letra in n:    
        if letra =="a" or letra =="e" or letra =="i" or letra =="o" or letra =="u":
           cantidad_vocales += 1 
        else:
             cantidad_consonantes += 1
    r = f""" Nombre: {n.capitalize}
            Numero de vocales:{cantidad_vocales}
            Numero de consonates:{cantidad_consonantes}
            Numero de letras {len(n)}"""
    return r     
lista_nombres =[]
flag=True
while flag:
    nombres = input("Ingrese un nombre o para terminar escriba x:")

    if nombres == "x":
      flag=False
    else:
        cnombre =nombres.capitalize() 
        if cnombre in lista_nombres:
            pass
        else:
           lista_nombres.append(cnombre)

lista_nombres.sort()
print(lista_nombres)
print(f"cantidad de nombres son {len(lista_nombres)}")

for i in lista_nombres:
    print(cant_vc(i))





#lista_num.append(9)
#print(lista_num)
#print(10 in lista_num)
#print(lista_num[6]) imprimira el puesto indicado 
#print(len(lista_num)) para ver cuantos elementos hay en la lista a