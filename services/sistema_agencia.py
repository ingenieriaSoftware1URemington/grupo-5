# =========================================
# SISTEMA AGENCIA
# Controla turistas, hoteles, vuelos y reservas
# =========================================

class SistemaAgencia:

    def __init__(self):

        self._turistas = {}
        self._hoteles = {}
        self._vuelos = {}
        self._sucursales = {}
        self._reservas = {}


    # =========================
    # REGISTROS
    # =========================

    def registrar_turista(self, turista):

        if turista.id in self._turistas:
            print("El turista ya está registrado.")
            return False

        self._turistas[turista.id] = turista
        return True


    def registrar_hotel(self, hotel):

        if hotel.id in self._hoteles:
            return False

        self._hoteles[hotel.id] = hotel
        return True


    def registrar_vuelo(self, vuelo):

        if vuelo.id in self._vuelos:
            return False

        self._vuelos[vuelo.id] = vuelo
        return True


    def registrar_sucursal(self, sucursal):

        if sucursal.id in self._sucursales:
            return False

        self._sucursales[sucursal.id] = sucursal
        return True


    # =========================
    # CONSULTAS
    # =========================

    def obtener_turistas(self):

        return list(self._turistas.values())


    def obtener_hoteles(self):

        return list(self._hoteles.values())


    def obtener_vuelos(self):

        return list(self._vuelos.values())


    def obtener_turista(self, id_turista):

        return self._turistas.get(id_turista)


    # =========================
    # RESERVAS
    # =========================

    def crear_reserva_hotel(self, id_reserva, turista, hotel):

        self._reservas[id_reserva] = {
            "turista": turista,
            "hotel": hotel
        }

        return True


    def crear_reserva_vuelo(self, id_reserva, turista, vuelo):

        self._reservas[id_reserva] = {
            "turista": turista,
            "vuelo": vuelo
        }

        return True