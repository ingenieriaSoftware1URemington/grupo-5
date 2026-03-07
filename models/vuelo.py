# =========================================
# CLASE VUELO
# Representa un vuelo disponible
# =========================================

class Vuelo:

    def __init__(self, id, origen, destino, precio):

        self.id = id
        self.origen = origen
        self.destino = destino
        self.precio = precio


    # Muestra información del vuelo
    def __str__(self):

        return f"Vuelo {self.id} | {self.origen} -> {self.destino} | Precio: ${self.precio}"