from models.reserva_hotel import ReservaHotel
from models.reserva_vuelo import ReservaVuelo


class SistemaAgencia:
    def __init__(self):
        self._turistas = {}
        self._hoteles = {}
        self._vuelos = {}
        self._reservas = {}

    def registrar_turista(self, turista):
        self._turistas[turista.get_id()] = turista

    def registrar_hotel(self, hotel):
        self._hoteles[hotel.get_id()] = hotel

    def registrar_vuelo(self, vuelo):
        self._vuelos[vuelo.get_id()] = vuelo

    def crear_reserva_hotel(self, id_reserva, turista, sucursal, fecha, hotel, entrada, salida):
        reserva = ReservaHotel(id_reserva, turista, sucursal, fecha, hotel, entrada, salida)
        self._reservas[id_reserva] = reserva
        sucursal.agregar_reserva(reserva)

    def crear_reserva_vuelo(self, id_reserva, turista, sucursal, fecha, vuelo):
        reserva = ReservaVuelo(id_reserva, turista, sucursal, fecha, vuelo)
        self._reservas[id_reserva] = reserva
        sucursal.agregar_reserva(reserva)

    def cancelar_reserva(self, id_reserva):
        if id_reserva in self._reservas:
            self._reservas[id_reserva].cancelar()