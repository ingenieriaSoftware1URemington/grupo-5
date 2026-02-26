class Vuelo:
    def __init__(self, id_vuelo, origen, destino, fecha, aerolinea, plazas_totales):
        self._id_vuelo = id_vuelo
        self._origen = origen
        self._destino = destino
        self._fecha = fecha
        self._aerolinea = aerolinea
        self._plazas_totales = plazas_totales
        self._plazas_disponibles = plazas_totales
        self._turistas = []

    def hay_disponibilidad(self):
        return self._plazas_disponibles > 0

    def reservar_plaza(self, turista):
        if self.hay_disponibilidad():
            self._plazas_disponibles -= 1
            self._turistas.append(turista)

    def liberar_plaza(self, turista):
        if turista in self._turistas:
            self._plazas_disponibles += 1
            self._turistas.remove(turista)

    def get_id(self):
        return self._id_vuelo

    def get_turistas(self):
        return self._turistas