class Turista:

    def __init__(self, id, nombre, documento, email, presupuesto):
        self.id = id
        self.nombre = nombre
        self.documento = documento
        self.email = email
        self.presupuesto = presupuesto

    def get_id(self):
        return self.id

    def __str__(self):
        return f"{self.id} - {self.nombre} - ${self.presupuesto}"