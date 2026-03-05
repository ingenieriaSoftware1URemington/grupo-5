# SOLO importa modelos si los necesitas
from models.turista import Turista
from models.hotel import Hotel
from models.sucursal import Sucursal


class SistemaAgencia:

    def __init__(self):
        self._turistas = {}
        self._hoteles = {}
        self._sucursales = {}
        self._reservas = {}

    def registrar_turista(self, turista):
        self._turistas[turista.id] = turista

    def registrar_hotel(self, hotel):
        self._hoteles[hotel.id] = hotel

    def registrar_sucursal(self, sucursal):
        self._sucursales[sucursal.id] = sucursal

    def crear_reserva_hotel(self, id_reserva, turista, sucursal, fecha_reserva, hotel, fecha_entrada, fecha_salida):
        self._reservas[id_reserva] = {
            "turista": turista,
            "sucursal": sucursal,
            "hotel": hotel,
            "fecha_reserva": fecha_reserva,
            "fecha_entrada": fecha_entrada,
            "fecha_salida": fecha_salida
        }