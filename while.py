flag=True
while flag:
    try:
         numero = int(input("Ingrese solo numeros: "))
         print(numero)
         flag=False
    except ValueError as e:
         print("Usted escribio una letra: ")
          