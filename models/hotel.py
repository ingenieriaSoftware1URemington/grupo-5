# =========================================
# CLASE HOTEL
# Representa un hotel disponible en el sistema
# =========================================

class Hotel:

    def __init__(self, id, nombre, ciudad, estrellas, habitaciones):

        self.id = id
        self.nombre = nombre
        self.ciudad = ciudad
        self.estrellas = estrellas
        self.habitaciones = habitaciones


    # Muestra información del hotel
    def __str__(self):

        return f"Hotel: {self.nombre} - {self.ciudad} | ⭐ {self.estrellas} | Habitaciones: {self.habitaciones}"