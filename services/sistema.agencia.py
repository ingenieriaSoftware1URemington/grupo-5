from services.sistema_agencia import SistemaAgencia
from models.turista import Turista
from models.hotel import Hotel
from models.sucursal import Sucursal

def main():
    sistema = SistemaAgencia()

    turista = Turista("T1", "Ana", "123", "ana@email.com", "300000")
    hotel = Hotel("H1", "Decameron", "Cartagena", 5, 10)
    sucursal = Sucursal("S1", "Sucursal Centro", "Medellín", "Calle 10")

    sistema.registrar_turista(turista)
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

    print("Proyecto funcionando correctamente ✅")

if __name__ == "__main__":
    main()