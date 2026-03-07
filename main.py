# =========================================
# IMPORTACIÓN DE CLASES
# =========================================

from services.sistema_agencia import SistemaAgencia
from models.turista import Turista
from models.hotel import Hotel
from models.sucursal import Sucursal


def menu():

    # Se crea el sistema principal de la agencia
    sistema = SistemaAgencia()

    # =========================================
    # CREACIÓN DE HOTEL Y SUCURSAL
    # =========================================

    # Creamos un hotel que estará disponible en el sistema
    hotel = Hotel("H1", "Decameron", "Cartagena", 5, 10)

    # Creamos una sucursal de la agencia
    sucursal = Sucursal("S1", "Sucursal Centro", "Medellín", "Calle 10")

    # Registramos hotel y sucursal en el sistema
    sistema.registrar_hotel(hotel)
    sistema.registrar_sucursal(sucursal)

    # =========================================
    # MOSTRAR HOTEL AL INICIAR EL PROGRAMA
    # =========================================

    print("\n===== SISTEMA DE AGENCIA DE VIAJES =====")
    print(f"Hotel disponible: {hotel.nombre}")
    print(f"Ciudad: {hotel.ciudad}")
    print("========================================")


    while True:

        print("\n===== MENÚ SISTEMA AGENCIA =====")
        print("1. Registrar turista")
        print("2. Listar turistas")
        print("3. Crear reserva hotel")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")


        # =========================
        # REGISTRAR TURISTA
        # =========================
        if opcion == "1":

            id_turista = input("ID: ")
            nombre = input("Nombre: ")
            documento = input("Documento: ")
            email = input("Email: ")
            presupuesto = float(input("Presupuesto: "))

            turista = Turista(id_turista, nombre, documento, email, presupuesto)

            sistema.registrar_turista(turista)

            print("Turista registrado correctamente.")


        # =========================
        # LISTAR TURISTAS
        # =========================
        elif opcion == "2":

            for t in sistema.obtener_turistas():
                print(t)


        # =========================
        # CREAR RESERVA
        # =========================
        elif opcion == "3":

            id_turista = input("ID del turista: ")
            turista = sistema.obtener_turista(id_turista)

            if not turista:
                print("Turista no encontrado.")
                continue

            id_reserva = input("ID de la reserva: ")

            sistema.crear_reserva_hotel(
                id_reserva,
                turista,
                sucursal,
                "2026-02-20",
                hotel,
                "2026-03-01",
                "2026-03-05"
            )

            print(f"Reserva creada en el hotel {hotel.nombre} correctamente.")


        # =========================
        # SALIR
        # =========================
        elif opcion == "4":

            print("Saliendo del sistema...")
            break


        else:
            print("Opción inválida.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()