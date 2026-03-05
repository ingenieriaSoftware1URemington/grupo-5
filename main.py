from services.sistema_agencia import SistemaAgencia
from models.turista import Turista
from models.hotel import Hotel
from models.sucursal import Sucursal


def menu():
    sistema = SistemaAgencia()

    while True:
        print("\n===== MENÚ SISTEMA AGENCIA =====")
        print("1. Registrar turista")
        print("2. Listar turistas")
        print("3. Crear reserva hotel")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_turista = input("ID: ")
            nombre = input("Nombre: ")
            documento = input("Documento: ")
            email = input("Email: ")
            presupuesto = float(input("Presupuesto: "))

            turista = Turista(id_turista, nombre, documento, email, presupuesto)
            sistema.registrar_turista(turista)

            print("Turista registrado correctamente.")

        elif opcion == "2":
            turistas = sistema._turistas.values()
            for t in turistas:
                print(t)

        elif opcion == "3":
            # Datos básicos de ejemplo
            id_turista = input("ID del turista: ")
            turista = sistema._turistas.get(id_turista)

            if not turista:
                print("Turista no encontrado.")
                continue

            hotel = Hotel("H1", "Decameron", "Cartagena", 5, 10)
            sucursal = Sucursal("S1", "Sucursal Centro", "Medellín", "Calle 10")

            sistema.registrar_hotel(hotel)

            sistema.crear_reserva_hotel(
                "R1",
                turista,
                sucursal,
                "2026-02-20",
                hotel,
                "2026-03-01",
                "2026-03-05"
            )

            print("Reserva creada correctamente.")

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()