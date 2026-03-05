def _init_(self, id_turista, nombre, documento, email, telefono):
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