from models.reserva import Reserva

class ReservaVuelo(Reserva):
    def __init__(self, id_reserva, turista, sucursal, fecha_reserva, vuelo):
        super().__init__(id_reserva, turista, sucursal, fecha_reserva)
        self._vuelo = vuelo
        vuelo.reservar_plaza(turista)

    def cancelar(self):
        super().cancelar()
        self._vuelo.liberar_plaza(self._turista)

    def get_vuelo(self):
        return self._vuelo