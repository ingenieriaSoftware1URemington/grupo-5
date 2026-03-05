class Sucursal:
    def __init__(self, id_sucursal, nombre, ciudad, direccion):
        self._id_sucursal = id_sucursal
        self._nombre = nombre
        self._ciudad = ciudad
        self._direccion = direccion
        self._reservas = []

    def agregar_reserva(self, reserva):
        self._reservas.append(reserva)

    def get_reservas(self):
        return self._reservas

    def mostrar_info(self):
        return f"Sucursal: {self._nombre} - Ciudad: {self._ciudad}"