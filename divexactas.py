 # se piden dos numeros uno que sea para una division
flag1=True
flag2=True
while flag1: 
    try:
         a = int(input("Valor 1 : "))
         flag1=False
    except ValueError:
         print("te quivocaste")
print(a)
         
while flag2:              
    try:
         b = int(input("Valor 2 : "))  
         flag2=False
    except ValueError:
         print("te quivocaste")        
print(b)

print(f"mi valor obtenidos son {a} y {b}")

def die (x,y):
    if (x%y)==0:
       r=f"{x} / {y} es una divicion exacta"
    else:
       (x%y)==2
       r=f"{x} / {y} es una divicion inexacta"
    return r

print(die(a,b))




productos = [1,2,3,4,5,6,7,8]
contador=[]
while True:
    print(productos[contador])
    if 7 == contador:
        break
    else:
        contador += 1
    
