class Turista:
    def __init__(self, id_turista, nombre, documento, email, telefono):
        self._id_turista = id_turista
        self._nombre = nombre
        self._documento = documento
        self._email = email
        self._telefono = telefono

    def get_id(self):
        return self._id_turista

    def get_nombre(self):
        return self._nombre

    def set_email(self, nuevo_email):
        self._email = nuevo_email

    def mostrar_info(self):
        return f"Turista: {self._nombre} - Email: {self._email}"
        # =========================================
# CLASE VUELO
# Representa un vuelo disponible en el sistema
# =========================================

class Vuelo:

    def __init__(self, id_vuelo, origen, destino, precio):

        # Identificador del vuelo
        self.id = id_vuelo

        # Ciudad de salida
        self.origen = origen

        # Ciudad de destino
        self.destino = destino

        # Precio del vuelo
        self.precio = precio


    # Método para mostrar información del vuelo
    def __str__(self):

        return f"Vuelo {self.id} | {self.origen} -> {self.destino} | Precio: ${self.precio}"