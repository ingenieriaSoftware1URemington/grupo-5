from services.sistema_agencia import SistemaAgencia
from models.turista import Turista
from models.hotel import Hotel
from models.vuelo import Vuelo


def menu():

    sistema = SistemaAgencia()


    # =========================
    # HOTELES
    # =========================

    hotel1 = Hotel("H1", "Decameron", "Cartagena", 5, 10)
    hotel2 = Hotel("H2", "Hilton", "Bogotá", 5, 8)
    hotel3 = Hotel("H3", "Dann Carlton", "Medellín", 4, 12)

    sistema.registrar_hotel(hotel1)
    sistema.registrar_hotel(hotel2)
    sistema.registrar_hotel(hotel3)


    # =========================
    # VUELOS
    # =========================


    vuelo1 = Vuelo("V1", "Pereira", "Cartagena", 300000)
    vuelo2 = Vuelo("V2", "Bogotá", "Medellín", 200000)

    sistema.registrar_vuelo(vuelo1)
    sistema.registrar_vuelo(vuelo2)


    while True:

        print("\n===== MENÚ AGENCIA =====")
        print("1. Registrar turista")
        print("2. Ver turistas")
        print("3. Ver hoteles")
        print("4. Ver vuelos")
        print("5. Reservar hotel")
        print("6. Reservar vuelo")
        print("7. Salir")

        opcion = input("Seleccione: ")


        if opcion == "1":

            id = input("ID: ")
            nombre = input("Nombre: ")
            documento = input("Documento: ")
            email = input("Email: ")
            presupuesto = float(input("Presupuesto: "))

            turista = Turista(id, nombre, documento, email, presupuesto)

            sistema.registrar_turista(turista)


        elif opcion == "2":

            for t in sistema.obtener_turistas():
                print(t)


        elif opcion == "3":

            print("\nHoteles disponibles:")

            for h in sistema.obtener_hoteles():
                print(h)


        elif opcion == "4":

            print("\nVuelos disponibles:")

            for v in sistema.obtener_vuelos():
                print(v)


        elif opcion == "5":

            id_turista = input("ID turista: ")

            turista = sistema.obtener_turista(id_turista)

            for h in sistema.obtener_hoteles():
                print(h)

            id_hotel = input("Seleccione hotel: ")

            hotel = sistema._hoteles.get(id_hotel)

            sistema.crear_reserva_hotel("R1", turista, hotel)

            print("Reserva de hotel creada.")


        elif opcion == "6":

            id_turista = input("ID turista: ")

            turista = sistema.obtener_turista(id_turista)

            for v in sistema.obtener_vuelos():
                print(v)

            id_vuelo = input("Seleccione vuelo: ")

            vuelo = sistema._vuelos.get(id_vuelo)

            sistema.crear_reserva_vuelo("R2", turista, vuelo)

            print("Reserva de vuelo creada.")


        elif opcion == "7":

            break


if __name__ == "__main__":
    menu()