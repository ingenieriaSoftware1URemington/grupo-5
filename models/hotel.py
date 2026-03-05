class Hotel:
    def __init__(self, id_hotel, nombre, ciudad, categoria, plazas_totales):
        self._id_hotel = id_hotel
        self._nombre = nombre
        self._ciudad = ciudad
        self._categoria = categoria
        self._plazas_totales = plazas_totales
        self._plazas_disponibles = plazas_totales

    def hay_disponibilidad(self):
        return self._plazas_disponibles > 0

    def reservar_plaza(self):
        if self.hay_disponibilidad():
            self._plazas_disponibles -= 1

    def liberar_plaza(self):
        if self._plazas_disponibles < self._plazas_totales:
            self._plazas_disponibles += 1

    def get_id(self):
        return self._id_hotel

    def mostrar_info(self):
        return f"Hotel: {self._nombre} - Disponibles: {self._habitaciones}"