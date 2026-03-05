class Sucursal:

    def __init__(self, id, nombre, ciudad, direccion):
        self.id = id
        self.nombre = nombre
        self.ciudad = ciudad
        self.direccion = direccion

    def __str__(self):
        return f"Sucursal: {self.nombre} - {self.ciudad}"