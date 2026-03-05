class SistemaAgencia:

    def __init__(self):
        self._turistas = {}
        self._hoteles = {}
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

    def registrar_sucursal(self, sucursal):
        if sucursal.id in self._sucursales:
            return False
        self._sucursales[sucursal.id] = sucursal
        return True

    # =========================
    # RESERVAS
    # =========================

    def crear_reserva_hotel(self, id_reserva, turista, sucursal,
                            fecha_reserva, hotel,
                            fecha_entrada, fecha_salida):

        if id_reserva in self._reservas:
            print("La reserva ya existe.")
            return False

        if turista.id not in self._turistas:
            print("El turista no está registrado.")
            return False

        if hotel.id not in self._hoteles:
            print("El hotel no está registrado.")
            return False

        if sucursal.id not in self._sucursales:
            print("La sucursal no está registrada.")
            return False

        self._reservas[id_reserva] = {
            "turista": turista,
            "sucursal": sucursal,
            "hotel": hotel,
            "fecha_reserva": fecha_reserva,
            "fecha_entrada": fecha_entrada,
            "fecha_salida": fecha_salida
        }

        return True

    # =========================
    # CONSULTAS
    # =========================

    def obtener_turistas(self):
        return list(self._turistas.values())

    def obtener_turista(self, id_turista):
        return self._turistas.get(id_turista)

    def obtener_reservas(self):
        return self._reservas.values()