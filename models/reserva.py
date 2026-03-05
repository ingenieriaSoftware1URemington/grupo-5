class Reserva:
    def __init__(self, id_reserva, turista, sucursal, fecha_reserva):
        self._id_reserva = id_reserva
        self._turista = turista
        self._sucursal = sucursal
        self._fecha_reserva = fecha_reserva
        self._estado = "Activa"

    def cancelar(self):
        self._estado = "Cancelada"

    def get_estado(self):
        return self._estado

    def get_turista(self):
        return self._turista

    def get_sucursal(self):
        return self._sucursal

    def mostrar_info(self):
        return f"Reserva {self._id_reserva} - Estado: {self._estado}"