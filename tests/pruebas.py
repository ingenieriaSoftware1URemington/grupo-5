def ejecutar_pruebas():
    print("=" * 65)
    print("  SISTEMA DE GESTIÓN - AGENCIA DE VIAJES")
    print("  Proyecto Ingeniería de Software I")
    print("=" * 65)

    sistema = SistemaAgencia()

    # ── Datos base ────────────────────────────────────────────────
    print("\n[SETUP] Registrando entidades base...")
    sistema.registrar_sucursal("S01", "Sucursal Centro", "Medellín", "Calle 10 #45-20")
    sistema.registrar_sucursal("S02", "Sucursal Norte",  "Bogotá",   "Av. 68 #120-30")

    sistema.registrar_turista("T01", "Ana Gómez",    "CC-10001", "ana@mail.com",   "311-1111")
    sistema.registrar_turista("T02", "Carlos Ruiz",  "CC-10002", "carlos@mail.com","322-2222")
    sistema.registrar_turista("T03", "Lucia Vargas", "CC-10003", "lucia@mail.com", "333-3333")

    sistema.registrar_hotel("H01", "Hotel Camino Real", "Cartagena", 4, 2)
    sistema.registrar_hotel("H02", "Hotel Montaña",     "Manizales", 3, 5)

    sistema.registrar_vuelo("V01", "Medellín", "Cartagena", "2025-08-10", "Avianca", 2)
    sistema.registrar_vuelo("V02", "Bogotá",   "San Andrés", "2025-09-01", "LATAM",  1)

    # ─────────────────────────────────────────────────────────────
    print("\n" + "─" * 65)
    print("  CASO DE PRUEBA 1: Reserva exitosa de hotel y vuelo")
    print("─" * 65)
    print("  Entrada : Turista T01, Sucursal S01, Hotel H01 (2 plazas), Vuelo V01 (2 plazas)")
    print("  Proceso : Verificar disponibilidad → reservar plaza → crear reserva → asociar sucursal")
    print("  Esperado: Reserva confirmada, plazas decrementadas")
    r1 = sistema.crear_reserva_hotel("T01", "S01", "H01", "2025-08-10", "2025-08-15")
    r2 = sistema.crear_reserva_vuelo("T01", "S01", "V01")
    print("  Resultado obtenido:")
    r1.mostrar_info()
    r2.mostrar_info()
    sistema.consultar_disponibilidad_hotel("H01")
    sistema.consultar_disponibilidad_vuelo("V01")

    # ─────────────────────────────────────────────────────────────
    print("\n" + "─" * 65)
    print("  CASO DE PRUEBA 2: Reserva sin disponibilidad")
    print("─" * 65)
    print("  Entrada : Turista T02 y T03 intentan reservar Vuelo V02 (sólo 1 plaza)")
    print("  Proceso : T02 reserva exitosamente → T03 intenta reservar → sin plazas")
    print("  Esperado: Primera reserva OK, segunda lanza error de disponibilidad")
    sistema.crear_reserva_vuelo("T02", "S01", "V02")
    try:
        sistema.crear_reserva_vuelo("T03", "S01", "V02")
    except ValueError as e:
        print(f"  ✔ Error capturado correctamente: {e}")
    sistema.consultar_disponibilidad_vuelo("V02")

    # ─────────────────────────────────────────────────────────────
    print("\n" + "─" * 65)
    print("  CASO DE PRUEBA 3: Cancelación de reserva")
    print("─" * 65)
    r3 = sistema.crear_reserva_hotel("T02", "S02", "H01", "2025-09-05", "2025-09-10")
    print(f"  Entrada : Reserva existente '{r3.get_id()}' en Hotel H01")
    print("  Proceso : Cancelar reserva → liberar plaza → cambiar estado")
    print("  Esperado: Estado = CANCELADA, plaza restaurada en hotel")
    sistema.cancelar_reserva(r3.get_id())
    print("  Resultado obtenido:")
    r3.mostrar_info()
    sistema.consultar_disponibilidad_hotel("H01")

    # ─────────────────────────────────────────────────────────────
    print("\n" + "─" * 65)
    print("  CASO DE PRUEBA 4: Asociación correcta a sucursal")
    print("─" * 65)
    print("  Entrada : Reservas creadas previamente en S01 y S02")
    print("  Proceso : Consultar reservas por sucursal")
    print("  Esperado: Cada sucursal muestra sólo sus propias reservas")
    sistema.mostrar_reservas_sucursal("S01")
    sistema.mostrar_reservas_sucursal("S02")

    print("\n" + "=" * 65)
    print("  Todas las pruebas completadas exitosamente.")
    print("=" * 65)


if __name__ == "__main__":
    ejecutar_pruebas()