class Producto:
    def __init__(self,nombre,marca,precio,cantidad):
        self.nombre =nombre 
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad
    def info(self):
        return f"{self.nombre},{self.marca},{self.precio},{self.cantidad}"
    
    def actualizar_cantidad(self,cantidad_vendida):
        self.cantidad = self.cantidad - cantidad_vendida

    def __str__(self):
        return{self.nombre},{self.marca}
    

    
def input_int(mensaje,mensaje_error):
    while True:
        try:
            v=int(input(mensaje))
        except ValueError:
              print(mensaje_error)
        else:
            return v
        

