class Producto:
    def __init__(self,nombre,marca,costo,cantidad):
        self._nombre=nombre
        self._marca=marca
        self._costo=costo
        self._cantidad=cantidad
    
    def get_nombre(self):
        return self._nombre 