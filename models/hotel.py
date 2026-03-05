class Hotel:

    def __init__(self, id, nombre, ciudad, estrellas, habitaciones):
        self.id = id
        self.nombre = nombre
        self.ciudad = ciudad
        self.estrellas = estrellas
        self.habitaciones = habitaciones

    def __str__(self):
        return f"Hotel: {self.nombre} - Disponibles: {self.habitaciones}"