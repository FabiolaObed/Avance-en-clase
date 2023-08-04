#una lista sirve para coleccionar datos , agrupar datos
#[]  esto es una lista
#productos = []
#productos.append("laptop")
#productos.append("tablet")
#print(producto)
#{}  esto es un diccionario
#productos = {}

#productos["nombre"]="laptop"
#productos["precio"]=1200

#print(productos.get("nombre"))


#for 
#productos = [1,2,3,4,5,6,7,8]
#suma_elemetos=[]
#for producto in productos:
#    suma_elemetos.append(producto+1)
#print(suma_elemetos)
#print(productos)


#lo q esta dentro del parentesis se llaman parametro
#n1=12
#n2=2
#def multipliacacion(valor1,valor2):
#    resultado=valor1*valor2
#    return resultado
#print(multipliacacion(n1,n2))

#import math
#def circunferencia(radio):
#    resultado=2*math.pi*radio*radio
#    return resultado
#print(circunferencia(15))

def suma (a, b):
    return a+b
def resta (a, b):
    return a-b
def multiplicacion (a, b):
    return a*b
def divicion (a, b):
    return a/b

def input_int(mensaje,mensaje_error):
    while True:
        try:
            v=int(input(mensaje))
        except ValueError:
              print(mensaje_error)
        else:
            return v





menu="""
    CALCULADORA
opcines:
1. Sumar
2. Restar
3. Multiplicar 
4. Dividir  
5. Salir
"""
flag=True 
while flag:
     print(menu)
     opcion=input_int("Elije una opcion: ","Es la opcion incorrecta")

     if opcion in [1,2,3,4]:
        a=input_int("Ingrese el primer valor: ","no es un numero")
        b=input_int("Ingrese el segundo valor: ","no es un numero")
        if opcion == 1:
            print(f"El resultado es {suma(a,b)}")
        elif opcion == 2:
            print(f"El resultado es {resta(a,b)}")
        elif opcion == 3:
             print(f"El resultado es {multiplicacion(a,b)}")
        elif opcion == 4:
             print(f"El resultado es {divicion(a,b)}")

     elif opcion == 5:
         print("Saliendo")
         break
     

     else:
         print("No existe esta opcion")