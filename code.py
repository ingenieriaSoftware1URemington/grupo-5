class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True


class Usuario:
    def __init__(self, id_user, nombre):
        self.id = id_user
        self.nombre = nombre


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, titulo, autor, isbn):
        self.libros.append(Libro(titulo, autor, isbn))
        print("Libro agregado")

    def agregar_usuario(self, id_user, nombre):
        self.usuarios.append(Usuario(id_user, nombre))
        print("Usuario agregado")

    def prestar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn and libro.disponible:
                libro.disponible = False
                return "Préstamo exitoso"
        return "No se pudo prestar el libro"

    def devolver_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                libro.disponible = True
                return "Libro devuelto"
        return "Libro no encontrado"

    def mostrar_libros(self):
        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            print(f"{libro.titulo} - {estado}")


# ---- PRUEBA ----
biblio = Biblioteca()
biblio.agregar_libro("1984", "Orwell", "123")
biblio.agregar_usuario(1, "Juan")

print(biblio.prestar_libro("123"))
biblio.mostrar_libros()

print(biblio.devolver_libro("123"))
biblio.mostrar_libros()



