class Persona:
    def __init__(self,nombre,genero,edad,altura):
        self._nombre = nombre
        self._genero = genero
        self._edad = edad
        self._altura = altura
  
    def correr(self,punto_llegada):
        print(f"{self._nombre} tienes q avanzar al {punto_llegada}")
        print("si llegaste detente ahi")

    def dormir(self,tiempo_dormido ):
        print(f"{self._nombre} empieza a dormir {tiempo_dormido}")
    
    def comer(self,eat_food):
        print(f"{self._nombre} empieza comer{eat_food}")
    
    
Juancarlos = Persona("Juancarlos","hombre","50","1,50")
Juancarlos.correr("a la mesa")

Ivan = Persona("Ivan","varon","20","1.60")
Ivan.dormir("30 minutos")

Juancarlos=Persona("Juancarlos","hombre","50","1,50")
Juancarlos.comer("Juancarlos come verduras")

   







#def entrada(mensaje):
#    while True:
#        try:  
#            numero_ingreso=int
#        except ValueError:
#            print("Ingrese solo numeros")
#        else:
#            break
#    return numero_ingreso

        